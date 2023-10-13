import json
import os
import time
from pathlib import Path
import allure
import pytest
from assertpy import assert_that
from tests.base_test import BaseTest


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Security")
@allure.feature("Login")
@pytest.mark.security
class TestLogin(BaseTest):
    @allure.description("invalid login")
    @allure.title("Login with invalid credentials test")
    @pytest.mark.run(order=3)

    def test_invalid_login(self, json_data: dict):
        """fixed"""
        invalid_email = json_data["inv_creds"]["inv_email"]
        invalid_password = json_data["inv_creds"]["inv_password"]
        self.login_page.login(invalid_email, invalid_password)
        expected_error_message = json_data["login"]["error_message"]
        assert_that(expected_error_message).is_equal_to(self.login_page.get_error_message())

    @allure.description("valid login")
    @allure.title("Login with valid credentials test")
    @allure.tag("Tagged test")
    @pytest.mark.run(order=1)

    def test_valid_login(self, json_data: dict):
        """fixed"""
        self.login_page.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        expected_page_title = json_data["login"]["ws_page_title"]
        assert_that(expected_page_title).is_equal_to(self.login_page.get_page_title())

    @allure.description("Log out from app")
    @allure.title("Logout of system test")
    @allure.story("As a user i want to be able to logout after a successful login.")
    @pytest.mark.run(order=2)
    def test_logout(self, json_data: dict):
        """fixed"""
        self.login_page.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        time.sleep(5)
        self.login_page.logout()
        expected_page_title = json_data["login"]["lg_page_title"]
        assert_that(expected_page_title).is_equal_to(self.login_page.get_page_logout_title())


