import os
from typing import Tuple, Union

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Chrome, Edge, Firefox
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import (
    StaleElementReferenceException,
)
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: Union[Chrome, Firefox, Edge], wait: WebDriverWait):
        self.driver = driver
        self.default_driver = driver
        self.default_wait = wait
        self.wait = wait
        self.new_driver = None
        self.new_wait = None

    def edit_cookie(self, cookie_key: str, cookie_value: str):
        cookie = self.wait.until(
            lambda d: d.get_cookie(cookie_key),
            message=f"Cookie '{cookie_key}' does not exist within the given timeout",
        )
        self.driver.delete_cookie(cookie_key)
        self.driver.add_cookie(
            {
                "name": cookie["name"],
                "value": cookie_value,
                "domain": cookie["domain"],
                "path": cookie["path"],
                "secure": cookie["secure"],
                "expiry": (cookie["expiry"]),
            }
        )

    def create_new_tab(self):
        self.driver.execute_script("window.open('about:blank', '_blank');")

    def set_activ_new_window(self):
        if self.new_driver is None:
            chrome_options1 = webdriver.ChromeOptions()
            chrome_options1.add_argument("--user-data-dir=" + os.getcwd() + "\\tmp")
            self.new_driver = webdriver.Chrome(options=chrome_options1)
            self.new_wait = WebDriverWait(self.new_driver, 10)
        self.driver = self.new_driver
        self.wait = self.new_wait

    def set_active_default_window(self):
        self.driver = self.default_driver
        self.wait = self.default_wait

    def go_to_tab(self, index: int):
        self.driver.switch_to.window(self.driver.window_handles[index])

    """def go_to_alert(self):
        self.driver.switch_to.alert"""

    def go_to_url(self, url: str):
        self.driver.get(url)

    def click(self, locator: Tuple[str, str]) -> None:
        el: WebElement = self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        self._highlight_element(el, "green")
        el.click()

    def fill_text(self, locator: Tuple[str, str], txt: str) -> None:
        el: WebElement = self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        el.click()
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def clear_text(self, locator: Tuple[str, str]) -> None:
        el: WebElement = self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        el.clear()

    def scroll_to_bottom(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def submit(self, webelement: WebElement) -> None:
        self._highlight_element(webelement, "green")
        webelement.submit()

    def get_text(self, locator: Tuple[str, str]) -> str:
        el: WebElement = self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )
        self._highlight_element(el, "green")
        return el.text

    def move_to_element(self, webelement: WebElement) -> None:
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()

    def is_elem_displayed(self, webelement: WebElement) -> bool:
        try:
            return webelement.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def _highlight_element(self, webelement: WebElement, color: str) -> None:
        original_style = webelement.get_attribute("style")
        new_style = f"background-color:yellow;border: 1px solid {color}{original_style}"
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style
            + "');},0);",
            webelement,
        )
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style
            + "');},400);",
            webelement,
        )










