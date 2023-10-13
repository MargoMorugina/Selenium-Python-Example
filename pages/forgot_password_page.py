from typing import Tuple

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    RECOVERY_BY_EMAIL: Tuple[str, str] = (By.CSS_SELECTOR, "#ulPills > li:nth-child(2)")
    EMAIL_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, "#Email")
    SEND_PASSWORD_RESET_LINK_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR,"#btnSubmit")
    ERROR_MSG: Tuple[str, str] = (By.CSS_SELECTOR, ".card-body >  h4")
    SUCCESS_MSG: Tuple[str, str] = (By.CSS_SELECTOR, ".card-body >  h4")
    PAGE_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, ".e-form-heading")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Send password reset link to email address: {email}")
    def send_password_reset_link(self, email: str) -> None:
        self.click(self.RECOVERY_BY_EMAIL)
        self.fill_text(self.EMAIL_FIELD, email)
        self.click(self.SEND_PASSWORD_RESET_LINK_BUTTON)

    @allure.step("Get invalid email message")
    def get_invalid_email_message(self) -> str:
        return self.get_text(self.ERROR_MSG)

    @allure.step("Get success message")
    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_MSG)

    @allure.step("Get Forgot password page title")
    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)
