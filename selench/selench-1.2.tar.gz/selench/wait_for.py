from typing import List

from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class WaitFor:
    def __init__(self, driver):
        self._driver = driver

    def element_visibility(self, path: str, timeout: int = None) -> WebElement:
        """
        An expectation for checking that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width
        that is greater than 0.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.visibility_of_element_located(locator),
                                                                       "Element is not visible")
        return element

    def elements_visibility(self, path: str, timeout: int = None) -> List[WebElement]:
        """
        An expectation for checking that all elements are present on the DOM of a page and visible.
        Visibility means that the elements are not only displayed but also has a height and width
        that is greater than 0.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        elements = WebDriverWait(self._driver.webdriver, timeout).until(ec.visibility_of_all_elements_located(locator),
                                                                        "Not all elements are visible")
        return elements

    def element_invisibility(self, path: str, timeout: int = None) -> WebElement:
        """
        An Expectation for checking that an element is either invisible or not present on the DOM.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.invisibility_of_element_located(locator),
                                                                       "Element is not invisible")
        return element

    def elements_invisibility(self, path: str, timeout: int = None) -> List[WebElement]:
        """
        An Expectation for checking that elements are either invisible or not present on the DOM.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        elements = WebDriverWait(self._driver.webdriver, timeout).until(
            self._visibility_of_all_elements_located(locator), "Elements are not invisible")
        return elements

    def element_staleness(self, element: WebElement, timeout: int = None) -> WebElement:
        """
        Wait until an element is no longer attached to the DOM. element is the element to wait for.
        returns False if the element is still attached to the DOM, true otherwise.
        """
        if not timeout: timeout = self._driver.wait
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.staleness_of(element),
                                                                       "Element did not go stale")
        return element

    def element_clickable(self, path: str, timeout: int = None) -> WebElement:
        """
        An Expectation for checking an element is visible and enabled such that you can click it.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.element_to_be_clickable(locator),
                                                                       "Element is not clickable")
        return element

    def element_text(self, path: str, timeout: int = None) -> bool:
        """
        An expectation for checking if text is present in the specified element.

        :Usage:
            driver.wait_for.element_text('//div[@id="msg"]')
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(lambda d: bool(d.find_element(*locator).text),
                                                                       "No text in element")
        return element

    def element_text_to_be(self, path: str, text: str, timeout: int = None) -> bool:
        """
        An expectation for checking if the given text is present in the specified element.

        :Usage:
            driver.wait_for.element_text_to_be('//div[@id="msg"]', 'welcome')
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.text_to_be_present_in_element(locator, text),
                                                                       f"Element text is not `{text}`")
        return element

    def element_selection_state(self, path: str, is_selected: bool, timeout: int = None) -> bool:
        """
        An expectation to locate an element and check if the selection state specified is in that state.
        is_selected is a boolean

        :Usage:
            driver.wait_for.element_selection_state('input[type="checkbox"]', False)
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(
            ec.element_located_selection_state_to_be(locator, is_selected),
            "Element is not selected" if is_selected else "Element is selected")
        return element

    def element_presence(self, path: str, timeout: int = None) -> WebElement:
        """
        An expectation for checking that an element is present on the DOM of a page.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.presence_of_element_located(locator),
                                                                       "Element is not present on the DOM")
        return element

    def elements_presence(self, path: str, timeout: int = None) -> List[WebElement]:
        """
        An expectation for checking that there is at least one element present on a web page.
        """
        if not timeout: timeout = self._driver.wait
        locator = self._driver._detect_locator_type(path)
        elements = WebDriverWait(self._driver.webdriver, timeout).until(ec.presence_of_element_located(locator),
                                                                        "Elements are not present on the DOM")
        return elements

    def url_to_be(self, url: str, timeout: int = None) -> bool:
        """
        An expectation for checking the current url. url is the expected url, which must be an exact match
        returns True if the url matches, false otherwise.
        """
        if not timeout: timeout = self._driver.wait
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.url_to_be(url),
                                                                       f"{url} != {self._driver.url}")
        return element

    def url_to_contain(self, url: str, timeout: int = None) -> bool:
        """
        An expectation for checking that the current url contains a case-sensitive substring.
        """
        if not timeout: timeout = self._driver.wait
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.url_contains(url),
                                                                       f"`{self._driver.url}` does not contain `{url}`")
        return element

    def title_to_be(self, title: str, timeout: int = None) -> bool:
        """
        An expectation for checking the title of a page. title is the expected title, which must be an exact
        match returns True if the title matches, false otherwise.
        """
        if not timeout: timeout = self._driver.wait
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.title_is(title),
                                                                       f"`{title} != {self._driver.title}")
        return element

    def title_to_contain(self, title: str, timeout: int = None) -> bool:
        """
        An expectation for checking that the title contains a case-sensitive substring.
        """
        if not timeout: timeout = self._driver.wait
        element = WebDriverWait(self._driver.webdriver, timeout).until(ec.title_contains(title),
                                                                       f"`{self._driver.title}` does not contain `{title}`")
        return element

    """
     * Custom "Expected Conditions" *
    """

    @staticmethod
    def _visibility_of_all_elements_located(locator):

        def _predicate(driver):
            try:
                elements = driver.find_elements(*locator)
                for element in elements:
                    if element.is_displayed():
                        return False
                return elements
            except StaleElementReferenceException:
                return False

        return _predicate
