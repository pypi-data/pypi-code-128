import braintree
import warnings
from braintree.error_result import ErrorResult
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult
from braintree.transaction import Transaction
from braintree.exceptions.not_found_error import NotFoundError
from braintree.exceptions.request_timeout_error import RequestTimeoutError


class TransactionGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def adjust_authorization(self, transaction_id, amount):
        transaction_params = {"amount": amount}
        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/adjust_authorization", {"transaction": transaction_params})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def clone_transaction(self, transaction_id, params):
        Resource.verify_keys(params, Transaction.clone_signature())
        return self._post("/transactions/" + transaction_id + "/clone", {"transaction-clone": params})

    def cancel_release(self, transaction_id):
        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/cancel_release", {})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def create(self, params):
        Resource.verify_keys(params, Transaction.create_signature())
        self.__check_for_deprecated_attributes(params)
        return self._post("/transactions", {"transaction": params})

    def credit(self, params):
        if params is None:
            params = {}
        params["type"] = Transaction.Type.Credit
        return self.create(params)

    def find(self, transaction_id):
        try:
            if transaction_id is None or transaction_id.strip() == "":
                raise NotFoundError()
            response = self.config.http().get(self.config.base_merchant_path() + "/transactions/" + transaction_id)
            return Transaction(self.gateway, response["transaction"])
        except NotFoundError:
            raise NotFoundError("transaction with id " + repr(transaction_id) + " not found")

    def hold_in_escrow(self, transaction_id):
        """
        Holds an existing submerchant transaction for escrow. It expects a transaction_id. ::

            result = braintree.Transaction.hold_in_escrow("my_transaction_id")
        """

        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/hold_in_escrow", {})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def refund(self, transaction_id, amount_or_options=None):
        """
        Refunds an existing transaction. It expects a transaction_id. ::

            result = braintree.Transaction.refund("my_transaction_id")
        """
        if isinstance(amount_or_options, dict):
            options = amount_or_options
        else:
            options = {
                "amount": amount_or_options
            }
        Resource.verify_keys(options, Transaction.refund_signature())
        response = self.config.http().post(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/refund", {"transaction": options})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def sale(self, params):
        if "recurring" in params.keys():
            warnings.warn("Use transaction_source parameter instead", DeprecationWarning)
        params.update({"type": "sale"})
        return self.create(params)

    def search(self, *query):
        if isinstance(query[0], list):
            query = query[0]

        response = self.config.http().post(self.config.base_merchant_path() + "/transactions/advanced_search_ids", {"search": self.__criteria(query)})
        if "search_results" in response:
            return ResourceCollection(query, response, self.__fetch)
        else:
            raise RequestTimeoutError("search timeout")

    def release_from_escrow(self, transaction_id):
        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/release_from_escrow", {})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def submit_for_settlement(self, transaction_id, amount=None, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, Transaction.submit_for_settlement_signature())
        transaction_params = {"amount": amount}
        transaction_params.update(params)
        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/submit_for_settlement",
                {"transaction": transaction_params})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def update_details(self, transaction_id, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, Transaction.update_details_signature())
        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/update_details",
                {"transaction": params})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def submit_for_partial_settlement(self, transaction_id, amount, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, Transaction.submit_for_settlement_signature())
        transaction_params = {"amount": amount}
        transaction_params.update(params)
        response = self.config.http().post(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/submit_for_partial_settlement",
                {"transaction": transaction_params})
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def void(self, transaction_id):
        response = self.config.http().put(self.config.base_merchant_path() + "/transactions/" + transaction_id + "/void")
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def __fetch(self, query, ids):
        criteria = self.__criteria(query)
        criteria["ids"] = braintree.transaction_search.TransactionSearch.ids.in_list(ids).to_param()
        response = self.config.http().post(self.config.base_merchant_path() + "/transactions/advanced_search", {"search": criteria})
        if "credit_card_transactions" in response:
            return [Transaction(self.gateway, item) for item in ResourceCollection._extract_as_array(response["credit_card_transactions"], "transaction")]
        else:
            raise RequestTimeoutError("search timeout")

    def __criteria(self, query):
        criteria = {}
        for term in query:
            if criteria.get(term.name):
                criteria[term.name] = dict(list(criteria[term.name].items()) + list(term.to_param().items()))
            else:
                criteria[term.name] = term.to_param()
        return criteria

    def _post(self, url, params=None):
        if params is None:
            params = {}
        response = self.config.http().post(self.config.base_merchant_path() + url, params)
        if "transaction" in response:
            return SuccessfulResult({"transaction": Transaction(self.gateway, response["transaction"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def __check_for_deprecated_attributes(self, params):
        if "device_session_id" in params.keys():
            warnings.warn("device_session_id is deprecated, use device_data parameter instead", DeprecationWarning)
        if "fraud_merchant_id" in params.keys():
            warnings.warn("fraud_merchant_id is deprecated, use device_data parameter instead", DeprecationWarning)
