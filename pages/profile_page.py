import time
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    """Profile Page"""

    USERNAME_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, '#Password')
    CONTINUE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '.btn-primary')
    LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#btnSubmit.btn-primary')

    PROFILE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#navbar > div > ul > li:nth-child(4) > a')
    CHANGE_PROFILE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#main-content > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div:nth-child(2) > div > small > button')
    SELECT_DOCTOR_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#main-content > div > div:nth-child(2) > div > section > div > div > div:nth-child(2) > div.row > div:nth-child(1) > div > div:nth-child(1) > div > div')

    SAVE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#main-content > div > div:nth-child(2) > div > section > div > div > div:nth-child(2) > div.d-flex.justify-content-end.my-2 > div > div > div > div:nth-child(1) > button')

    SIMLEPROF_PAGE_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div:nth-child(2) > div > small")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Log in with username: {username} and password: {password}")
    def profile_login(self, username: str, password: str) -> None:
        self.fill_text(self.USERNAME_FIELD, username)
        self.click(self.CONTINUE_BUTTON)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(5)
        self.click(self.PROFILE_BUTTON)

    @allure.step("Get page title")
    def get_profile_page_title(self) -> str:
        return self.get_text(self.SIMLEPROF_PAGE_TITLE)


    @allure.step("change profile type")
    def change_type_profile(self) -> None:
        self.click(self.CHANGE_PROFILE_BUTTON)
        self.click(self.SELECT_DOCTOR_BUTTON)
        time.sleep(5)
        self.click(self.SAVE_BUTTON)
        time.sleep(5)

