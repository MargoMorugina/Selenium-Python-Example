import time
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.specialist_select_page import SelectSpecialistPage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class ConsultantPage(BasePage):
    """Login Page."""

    USERNAME_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD: Tuple[str, str] = (By.CSS_SELECTOR, '#Password')
    CONTINUE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '.btn-primary')
    LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '#btnSubmit.btn-primary')

    SELECT_CONSULTANT_BTN: Tuple[str, str] = (By.CSS_SELECTOR, ".d-flex > .card.col-12.m-2.shadow-3-strong.d-flex:nth-child(4)")

    PAGE_CONSULTANT_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, "#navbar > div > div > span")

    """create position"""
    SELECT_PERFORMERS: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)")
    SELECT_EXTERNAL_EXPERTS: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)>.sidenav-collapse.show > .sidenav-item:nth-child(2)")
    SELECT_DB_EXPERTS: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)>.sidenav-collapse.show > .sidenav-item:nth-child(2) > .sidenav-collapse.sidenav-level-2.show >  .sidenav-item:nth-child(1)")

    ADD_POSITION: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div > div.saf-container > div > div > table > thead > tr:nth-child(2) > td:nth-child(1) > div > div > div > div > span")
    INPUT_NAME_POSITION: Tuple[str, str] = (By.CSS_SELECTOR, ".modal-content input.form-control.form-control-md.form-icon-trailing")
    SELECT_DIVISION: Tuple[str, str] = (By.CSS_SELECTOR, "body > div.modal.fade.show.modal-static > div > div > div.modal-body > div > div:nth-child(2) > div > div > div > div > div > div > div:nth-child(1) > div > div.ms-1 > div > span > span > button")
    SELECT_DIVISION_MODAL: Tuple[str, str] = (By.CSS_SELECTOR, "body > div.modal.fade.show.modal-static.exp-modal-on-front > div > div > div.modal-body > table > tbody > tr:nth-child(3) > td > span > div > div")

    SELECT_RESPONSIBLE: Tuple[str, str] = (By.CSS_SELECTOR, ".my-2 button.btn.btn-brand-dark.btn-sm.ripple-surface")
    SELECT_SPECIALIZATION: Tuple[str, str] = (By.CSS_SELECTOR, ".modal-body .row.mb-3:nth-child(6)")
    SELECT_OPTION: Tuple[str, str] = (By.CSS_SELECTOR, ".select-dropdown.open .select-option:nth-child(3)")
    INPUT_DATE: Tuple[str, str] = (By.CSS_SELECTOR, ".modal-body .row.mb-3:nth-child(8) .form-outline.datepicker input.form-control")
    SAVE_BTN: Tuple[str, str] = (By.CSS_SELECTOR, ".modal-footer button.btn-primary.ripple-surface")

    NEW_POSITION_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div > div:nth-child(2) > div.card > div > p > div > div:nth-child(2)")

    SELECT_MARKET: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)>.sidenav-collapse.show > .sidenav-item:nth-child(2) > .sidenav-collapse.sidenav-level-2.show >  .sidenav-item:nth-child(3)")

    """Approval position and send invites"""
    APPROVAL_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div > div:nth-child(2) > div.mt-3 > div.pb-1.border-bottom.border-primary-50.exp-no-print > div > div:nth-child(2) > button")
    SEND_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "body > div.modal.fade.show.modal - static > div > div > div.modal - footer > div > div > div > div: nth - child(1) > button")
    GO_TO_INVITES: Tuple[str, str] = (By.CSS_SELECTOR, "#tab-tab2")
    ADD_OPERATOR_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "#tab2 > div > div > div > table > thead > tr > th:nth-child(1) > div > div > span > span > button")
    MARKET_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "body > div.modal.fade.show.modal-static > div > div > div.modal-body > div > div:nth-child(2) > div > div")
    SELECT_DROPDOWN_LIST_PROFILE: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div:nth-child(2) > div > div.sidebar.shadow-3.mb-5 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div > div")
    SELECT_DROPDOWN_LIST_COUNTRY: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div:nth-child(2) > div > div.sidebar.shadow-3.mb-5 > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div")
    SEND_INVITE_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "# tab2 > div > div > div > table > tbody > tr > td:nth-child(5) > div > button")
    INPUT_COMMENT: Tuple[str, str] = (By.CSS_SELECTOR, "# MDBTextarea-109783")
    SUBMIT_BTN: Tuple[str, str] = (By.CSS_SELECTOR, " body > div.modal.fade.show.modal-static > div > div > div.modal-footer.py-1 > div > div > div > div:nth-child(1) > button")
    """accept invite"""
    MORE_DETAIL_BTN: Tuple[str, str] = (By.CSS_SELECTOR, ".ripple - surface - dark")
    ACCEPT_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "div.p - 2: nth - child(1) > button:nth - child(1)")
    SUBMIT_PERSONAL_DATA: Tuple[str, str] = (By.CSS_SELECTOR, ".btn - primary")
    STATUS_INVITE_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, "# tab2 > div > div > div > table > tbody > tr > td:nth-child(4) > div > span > span")
    "market search button"
    MARKET_SEARCH_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content .sidebar button.btn-primary")

    FEMALE_BTN: Tuple[str, str] = (By.CSS_SELECTOR, ".sidebar.shadow-3.mb-5 > .section:nth-child(1) .mb-3:nth-child(4) .form-check.mb-0:nth-child(3) .form-check-input")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Log in with username: {username} and password: {password}")
    def consultant_login(self, username: str, password: str) -> str:
        self.fill_text(self.USERNAME_FIELD, username)
        self.click(self.CONTINUE_BUTTON)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        self.click(self.SELECT_CONSULTANT_BTN)

    @allure.step("Get page title")
    def get_consultant_page_title(self) -> str:
        return self.get_text(self.PAGE_CONSULTANT_TITLE)

    @allure.step("Create new position")
    def create_new_position(self) -> str:
        time.sleep(3)
        self.click(self.SELECT_PERFORMERS)
        self.click(self.SELECT_EXTERNAL_EXPERTS)
        self.click(self.SELECT_DB_EXPERTS)
        self.click(self.ADD_POSITION)
        time.sleep(1)

    @allure.step("Create new position")
    def select_menu_market(self) -> str:
        time.sleep(3)
        self.click(self.SELECT_PERFORMERS)
        self.click(self.SELECT_EXTERNAL_EXPERTS)
        self.click(self.SELECT_MARKET)


    @allure.step("fill form")
    def fill_form_for_new_position(self, name_position: str, current_date: str) -> str:
        self.fill_text(self.INPUT_NAME_POSITION, name_position)
        self.click(self.SELECT_DIVISION)
        self.click(self.SELECT_DIVISION_MODAL)
        time.sleep(1)
        self.click(self.SELECT_SPECIALIZATION)
        self.click(self.SELECT_OPTION)
        self.click(self.SELECT_RESPONSIBLE)
        self.click(self.INPUT_DATE)
        self.fill_text(self.INPUT_DATE, current_date)
        self.click(self.SAVE_BTN)
        time.sleep(3)

    @allure.step("Get new position title")
    def get_new_position_title(self) -> str:
        return self.get_text(self.NEW_POSITION_TITLE)

    @allure.step("approval position and send invite")
    def approval_position(self) -> str:
        self.click(self.APPROVAL_BTN)
        self.click(self.SAVE_BTN)
        self.click(self.GO_TO_INVITES)
        self.click(self.ADD_OPERATOR_BTN)
        self.click(self.MARKET_BTN)
        time.sleep(5)

    @allure.step("accept invite")
    def accept_invite(self) -> None:
        self.click(self.MORE_DETAIL_BTN)
        self.click(self.ACCEPT_BTN)
        self.click(self.SUBMIT_PERSONAL_DATA)

    @allure.step("Get status of invites")
    def get_status_of_invite(self) -> str:
        return self.get_text(self.STATUS_INVITE_TITLE)

    @allure.step("Search button")
    def search_btn(self) -> None:
        self.scroll_to_bottom()
        self.click(self.MARKET_SEARCH_BTN)

    @allure.step("Search profile type on market")
    def search_profile(self) -> None:
        self.click(self.SELECT_DROPDOWN_LIST_PROFILE)

    @allure.step("Search country of specialist on market")
    def search_country(self) -> None:
        self.click(self.SELECT_DROPDOWN_LIST_COUNTRY)

    @allure.step("mail/femail btn")
    def femail_btn(self) -> None:
        self.click(self.FEMALE_BTN)

    @allure.step("go to externalposition page")
    def go_to_externalposition_page(self) -> None:
        time.sleep(3)
        self.click(self.SELECT_PERFORMERS)
        self.click(self.SELECT_EXTERNAL_EXPERTS)
        self.click(self.SELECT_DB_EXPERTS)
        time.sleep(1)























