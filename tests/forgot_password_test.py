import os

import allure
import pytest
from assertpy import assert_that

from tests.base_test import BaseTest

@allure.epic("Security")
@allure.story("Forgot Password Feature's Functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.security
@allure.parent_suite("Custom parent suite")
@allure.suite("Custom suite")
@allure.sub_suite("Custom sub suite")
class TestForgotPassword(BaseTest):
    @allure.description("Forgot password with a valid email address")
    @allure.title("Forgot Password with valid email test")
    def test_valid_email(self, json_data: dict):
        """fixed"""
        self.login_page.click_forgot_password()
        self.forgot_password_page.send_password_reset_link(os.getenv("EMAIL"))
        expected_success_message = json_data["forgot_password"]["success_message"]
        assert_that(expected_success_message).described_as("success message").is_equal_to(
            self.forget_password_page.get_success_message())

    @allure.description("Forgot Password with invalid email address")
    @allure.title("Forgot Password with invalid email test")
    def test_invalid_email(self, json_data: dict):
        """fixed"""
        self.login_page.click_forgot_password()
        invalid_email = json_data["inv_creds"]["inv_email"]
        self.forgot_password_page.send_password_reset_link(invalid_email)
        expected_error_message = json_data["forgot_password"]["error_message"]
        assert_that(expected_error_message).described_as("error message").is_equal_to(
            self.forget_password_page.get_invalid_email_message())
'''
    @allure.description("Exception catching")
    @allure.title("Exception test")
   
   
    def test_expected_exception_on_page_title(self):
        self.about_page.click_login_link()
        self.login_page.click_forgot_password()
        with pytest.raises(AssertionError) as e:
            assert_that(self.forget_password_page.get_page_title()).described_as(
                "page title"
            ).is_equal_to("something else")
        assert "AssertionError" in str(e)'''
