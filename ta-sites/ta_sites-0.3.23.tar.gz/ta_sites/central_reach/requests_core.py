import datetime
import json
import time
import requests
from retry import retry
from .exceptions import BadRequestError, ScheduledMaintenanceError
from .core import CentralReachCore


def retry_if_bad_request(func):
    attempt = 1
    tries = 3

    @retry(exceptions=BadRequestError, tries=tries, delay=1, backoff=2)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as ex:
            nonlocal attempt
            print(f"Bad request Attempt {attempt}...", "WARN")
            attempt = attempt + 1 if attempt < tries else 1
            raise ex

    return wrapper


class CentralReachRequestsCore:
    def __init__(self, login: str, password: str):
        """
        CentralReachRequestsCore object. Please Inheritance it.

        :param login: login for CentralReach site.
        :param password: password for CentralReach site.
        """
        self.__login = login
        self.__password = password
        self.session = requests.session()
        self._login_to_central_reach(self.__login, self.__password)

    @staticmethod
    def _get_headers(is_json=True, add_headers: dict = None) -> dict:
        headers = {}
        if is_json:
            headers["content-type"] = "application/json; charset=UTF-8"
        if add_headers:
            for key, value in add_headers.items():
                headers[key] = value
        return headers

    @staticmethod
    def __is_scheduled_maintenance(response) -> bool:
        if response.status_code == 200 and "scheduled maintenance" in response.text.lower():
            return True
        return False

    @staticmethod
    def _is_json_response(response) -> bool:
        try:
            response.json()
            return True
        except json.decoder.JSONDecodeError:
            return False

    def check_response(
        self, response, mandatory_json: bool = False, exc_message: str = "", re_authorize: bool = True
    ) -> None:
        """
        This method check response and raise exception 'BadRequestError'
           or 'ScheduledMaintenanceError' with exc_message,
        If status code is 401 (unauthorized) then it will try login again
        :param response: response from request
        :param mandatory_json: bool, if True - it will check is response contain json data
        :param exc_message: text message which will be raise if response wrong
        :param re_authorize: bool, if True then it will try login again if status code is 401
        """
        if self.__is_scheduled_maintenance(response):
            print(exc_message, "Error")
            print("'Central Reach' site is currently unavailable due to scheduled maintenance", "Error")
            raise ScheduledMaintenanceError

        elif re_authorize and response.status_code == 401:
            self._login_to_central_reach(self.__login, self.__password)
            raise BadRequestError(
                f"{exc_message}Status Code: {response.status_code} (Unauthorized request), "
                f"Json content: {response.json()}, Headers: {response.headers}"
            )

        if response.status_code != 200 or (mandatory_json and not self._is_json_response(response)):
            exc_message = exc_message + "\n" if exc_message else ""
            if self._is_json_response(response):
                raise BadRequestError(
                    f"{exc_message}Status Code: {response.status_code}, "
                    f"Json content: {response.json()}, Headers: {response.headers}"
                )
            else:
                raise BadRequestError(
                    f"{exc_message}Status Code: {response.status_code}, " f"Headers: {response.headers}"
                )

    @retry_if_bad_request
    def _login_to_central_reach(self, login: str, password: str) -> None:
        central_reach_core = CentralReachCore(login, password, headless=True)
        central_reach_core.login_to_site()

        # Check authorisation
        timeout_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
        while datetime.datetime.now() < timeout_time:
            try:
                # Set cookies
                for name, value in central_reach_core.browser.get_cookies(as_dict=True).items():
                    self.session.cookies.set(name, value)
                # Check authorization
                self.__insurance_eligibility_status()
                break
            except BadRequestError:
                time.sleep(1)
                continue
        else:
            raise BadRequestError("Session is unauthorized after login to Central Reach")
        central_reach_core.browser.close_browser()

    def __insurance_eligibility_status(self) -> None:
        header = {"referer": "https://members.centralreach.com/"}
        url = "https://members.centralreach.com/crxapi/system/dictionary/InsuranceEligibilityStatus"
        response = self.session.get(url, headers=self._get_headers(is_json=True, add_headers=header))

        exception_message = "Problems with insurance eligibility request."
        self.check_response(response, mandatory_json=True, exc_message=exception_message, re_authorize=False)

    @retry_if_bad_request
    def _get_filters(self):
        payload = {
            "applicationSection": "billingmanager.billing",
        }
        url = "https://members.centralreach.com/api/?shared.loadFilters"
        response = self.session.post(url, json=payload, headers=self._get_headers(is_json=True))

        exception_message = "Problems with getting billings."
        self.check_response(response, mandatory_json=True, exc_message=exception_message)
        return response.json()["filters"]

    def get_filter_by_name(self, filter_name):
        filters = self._get_filters()
        for filter_data in filters:
            if str(filter_data["Name"]).strip() == filter_name:
                return json.loads(filter_data["filters"])
        else:
            raise Exception("Filter '{filter_name}' doesn't exist")

    @retry_if_bad_request
    def get_era_list(self, start_date: datetime = None, end_date: datetime = None):
        _start_date = start_date.strftime("%Y-%m-%d") if start_date else ""
        _end_date = end_date.strftime("%Y-%m-%d") if start_date else ""

        load_era_list_url = "https://members.centralreach.com/api/?claims.loadERAList"
        data = {
            "startDate": _start_date,
            "endDate": _end_date,
            "page": "1",
            "claimLabelId": "",
            "pageSize": "2000",
        }
        response = self.session.get(load_era_list_url, json=data)
        if response.status_code != 200:
            response = self.session.get(load_era_list_url, json=data)

        if "application/json" in response.headers.get("content-type"):
            if response.status_code == 200 and response.json().get("success", False) is True:
                return response.json()
            elif "message" in response.json():
                raise Exception(
                    f"Problems with getting 'Era List' from 'Central Reach' site. {response.json()['message']}"
                )
        raise Exception("Problems with getting 'Era List' from 'Central Reach' site.")

    def get_zero_pay_filter(self, start_date: datetime = None, end_date: datetime = None) -> dict:
        response = self.get_era_list(start_date, end_date)
        era_list_data = response["items"]

        # Zero Pay filter
        zero_pay_data: dict = {}
        for item in era_list_data:
            if item["PaymentAmount"] == 0.0:
                zero_pay_data[str(item["Id"])] = item
        return zero_pay_data

    def get_pr_filter(self, start_date: datetime = None, end_date: datetime = None) -> dict:
        response = self.get_era_list(start_date, end_date)
        era_list_data = response["items"]

        # PR filter
        pr_data: dict = {}
        for item in era_list_data:
            if (
                item["PaymentAmount"] == 0.0
                and item["PrAdjustmentTotal"] > 0
                and item["PiAdjustmentTotal"] == 0.0
                and item["Reconciled"] == "None"
            ):
                pr_data[str(item["Id"])] = item
        return pr_data

    def get_denial_filter(self, start_date: datetime = None, end_date: datetime = None) -> dict:
        response = self.get_era_list(start_date, end_date)
        era_list_data = response["items"]

        # Denial filter
        denial_data: dict = {}
        for item in era_list_data:
            if item["PaymentAmount"] == 0.0 and item["Reconciled"] == "None":
                denial_data[str(item["Id"])] = item
        return denial_data
