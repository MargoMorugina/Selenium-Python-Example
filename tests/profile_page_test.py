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

class TestProfilePage(BaseTest):

    @allure.description("")
    @allure.title("")
    @pytest.mark.run(order=3)

    def test_simple_profile_page(self, json_data: dict):
        """fixed"""
        self.profile_page.profile_login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        page_title = json_data["profile"]["sp_page_title"]
        assert_that(page_title).is_equal_to(self.profile_page.get_profile_page_title())


    def test_change_profile_type(self, json_data: dict):
        """fixed, passed only then type simple"""
        self.profile_page.profile_login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        self.profile_page.change_type_profile()
        page_title = json_data["profile"]["dp_page_title"]
        assert_that(page_title).is_equal_to(self.profile_page.get_profile_page_title())



