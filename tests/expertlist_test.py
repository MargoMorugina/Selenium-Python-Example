import json
import os
from datetime import datetime
import time
from pathlib import Path
import allure
import pytest
from assertpy import assert_that
from tests.base_test import BaseTest

@pytest.mark.security
class TestExpertlist(BaseTest):
    def test_search_by_profile_type(self, json_data: dict):
         profile_type = json_data["profile_types"]["profile_type_operator"]
         self.consultant_page.consultant_login(os.getenv("EMAIL_CONS"), os.getenv("PASSWORD_CONS"))
         self.expertlist_page.select_menu_market()
         time.sleep(3)
         self.expertlist_page.search_profile()
         self.specialist_select_page.select_profile_type_list(profile_type)
         time.sleep(3)
         self.expertlist_page.search_btn()

    def test_search_by_gender(self, json_data: dict):
         self.consultant_page.consultant_login(os.getenv("EMAIL_CONS"), os.getenv("PASSWORD_CONS"))
         self.expertlist_page.select_menu_market()
         time.sleep(5)
         self.expertlist_page.femail_btn()
         time.sleep(3)
         self.expertlist_page.search_btn()

