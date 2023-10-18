import time
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.specialist_select_page import SelectSpecialistPage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class ExpertlistPage(BasePage):

    SELECT_PERFORMERS: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)")
    SELECT_EXTERNAL_EXPERTS: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)>.sidenav-collapse.show > .sidenav-item:nth-child(2)")
    SELECT_MARKET: Tuple[str, str] = (By.CSS_SELECTOR, ".sidenav-menu > .sidenav-item:nth-child(4)>.sidenav-collapse.show > .sidenav-item:nth-child(2) > .sidenav-collapse.sidenav-level-2.show >  .sidenav-item:nth-child(3)")

    "market search button"
    MARKET_SEARCH_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content .sidebar button.btn-primary")
    FEMALE_BTN: Tuple[str, str] = (By.CSS_SELECTOR, ".sidebar.shadow-3.mb-5 > .section:nth-child(1) .mb-3:nth-child(4) .form-check.mb-0:nth-child(3) .form-check-input")
    SELECT_DROPDOWN_LIST_PROFILE: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div:nth-child(2) > div > div.sidebar.shadow-3.mb-5 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div > div")
    SELECT_DROPDOWN_LIST_COUNTRY: Tuple[str, str] = (By.CSS_SELECTOR, "#main-content > div > div:nth-child(2) > div > div.sidebar.shadow-3.mb-5 > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Create new position")
    def select_menu_market(self) -> str:
        time.sleep(3)
        self.click(self.SELECT_PERFORMERS)
        self.click(self.SELECT_EXTERNAL_EXPERTS)
        self.click(self.SELECT_MARKET)

    @allure.step("Search button")
    def search_btn(self) -> None:
        self.scroll_to_bottom()
        self.click(self.MARKET_SEARCH_BTN)
        time.sleep(3)

    @allure.step("Search profile type on market")
    def search_profile(self) -> None:
        self.click(self.SELECT_DROPDOWN_LIST_PROFILE)

    @allure.step("Search country of specialist on market")
    def search_country(self) -> None:
        self.click(self.SELECT_DROPDOWN_LIST_COUNTRY)

    @allure.step("mail/femail btn")
    def femail_btn(self) -> None:
        self.click(self.FEMALE_BTN)
