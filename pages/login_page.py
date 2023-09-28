import time
from typing import Tuple

import allure
from selenium.webdriver.common.by import By

from pages.top_bars.top_menu_bar import TopMenuBar


class LoginPage(TopMenuBar):
    """Login Page."""

    USERNAME_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, '#Password')
    CONTINUE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '.btn-primary')
    LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#btnSubmit.btn-primary')

    LOGIN_ERROR_MESSAGE: Tuple[str, str] = (By.CSS_SELECTOR, "#frmLogin #divPassword .invalid-feedback")
    PAGE_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, ".card-body .mb-3.me-4.flex-grow-1")

    PROFILE_DROP_DOWN_MENU = (By.CSS_SELECTOR, ".dropdown .rounded-circle.bg-secondary.p-1")
    PROFILE_LOGOUT = (By.CSS_SELECTOR, "ul.dropdown-menu > li:nth-child(9)")
    PAGE_LOGOUT_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, ".card-body > h4")

    FORGOT_PASSWORD_LINK: Tuple[str, str] = (
        By.CSS_SELECTOR,
        "[href='https://app.involve.me/password/reset']",
    )

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Log in with username: {username} and password: {password}")
    def login(self, username: str, password: str) -> None:
        self.fill_text(self.USERNAME_FIELD, username)
        self.click(self.CONTINUE_BUTTON)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    @allure.step("Get page title")
    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self) -> None:
        self.click(self.FORGOT_PASSWORD_LINK)

    @allure.step("Logout from system")
    def logout(self):
        # Click account drop down menu
        self.click(self.PROFILE_DROP_DOWN_MENU)
        # Click logout button
        self.click(self.PROFILE_LOGOUT)

    @allure.step("Get logout title")
    def get_page_logout_title(self) -> str:
        return self.get_text(self.PAGE_LOGOUT_TITLE)
