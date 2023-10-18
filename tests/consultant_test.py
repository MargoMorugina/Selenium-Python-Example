import json
import os
from datetime import datetime
import time
from pathlib import Path
import allure
import pytest
from assertpy import assert_that
from tests.base_test import BaseTest

# @allure.severity(allure.severity_level.BLOCKER)
# @allure.epic("Consultant Page")
# @allure.feature("Login")
@pytest.mark.security
class TestConsultant(BaseTest):
    def test_consultant_login(self, json_data: dict):
        """fixed"""
        self.consultant_page.consultant_login(os.getenv("EMAIL_CONS"), os.getenv("PASSWORD_CONS"))
        expected_page_title = json_data["profile"]["lk_page_title"]
        assert_that(expected_page_title).is_equal_to(self.consultant_page.get_consultant_page_title())

    def test_create_new_position(self, json_data: dict):
        """необходимо добавить еще 2 кейса: заполнение всех полей и заполнение только необязательных полей"""
        self.consultant_page.consultant_login(os.getenv("EMAIL_CONS"), os.getenv("PASSWORD_CONS"))
        self.consultant_page.create_new_position()
        name_position = json_data["new_position_for_operator"]["name_position"]
        current_date = datetime.now().strftime("%d.%m.%Y")
        self.consultant_page.fill_form_for_new_position(name_position, current_date)
        expected_new_position_title = json_data["new_position_for_operator"]["position_title"]
        assert_that(expected_new_position_title).is_equal_to(self.consultant_page.get_new_position_title())

    def test_add_operator_for_new_position(self, json_data: dict):
        position_number = json_data["position_number"]["position_number_1"]
        self.consultant_page.consultant_login(os.getenv("EMAIL_CONS"), os.getenv("PASSWORD_CONS"))
        self.consultant_page.go_to_externalposition_page()
        self.consultant_page.go_to_the_page()
        time.sleep(5)
        self.consultant_page.select_new_position()
        time.sleep(5)
        #self.specialist_select_page.select_empty_position(position_number)

        #self.consultant_page.approval_position()
        #self.specialist_select_page.select_operator_from_market(operator_name)







    """def test_registration_operator_and_autocreate_position(self, json_data: dict):
         OPERATOR_TAB = 1
         self.consultant_page.consultant_login(os.getenv("EMAIL_LKCONS"), os.getenv("PASSWORD_LKCONS"))
         self.consultant_page.create_new_tab()
         self.consultant_page.go_to_tab(OPERATOR_TAB)
         self.consultant_page.go_to_url('https://sts-q.in.top/Account/Registration?profileType=1')
         time.sleep(3)



    def test_passing_operator(self, json_data: dict):
         
         name_position = json_data["new_position_for_operator"]["name_position"]
         current_date = datetime.now().strftime("%d.%m.%Y")
         comment_for_invite = json_data["comments"]["invite_comment"]
         operator_name = json_data["operators_name"]["operator_2"]
         profile_type = json_data["profile_types"]["profile_type_operator"]
         self.consultant_page.consultant_login(os.getenv("EMAIL_CONS"), os.getenv("PASSWORD_CONS"))
         time.sleep(2)
         self.consultant_page.create_new_position()
         self.consultant_page.fill_form_for_new_position(name_position, current_date)
         time.sleep(5)
         self.consultant_page.approval_position()
         #self.specialist_select_page.select_profile_type_list(profile_type)
         #self.consultant_page.search_profile()
         self.specialist_select_page.select_operator_from_market(operator_name)"""

