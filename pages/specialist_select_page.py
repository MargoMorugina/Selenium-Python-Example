import os
import time
from lib2to3.pgen2 import driver

from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from typing import Tuple, Union
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage

class SelectSpecialistPage(BasePage):

    SPECIALISTS_LIST = "#main-content > div > div:nth-child(2) > div > div.content.flex-fill > div > div.row.row-cols-1.row-cols-lg-2.row-cols-xl-3.g-4.mb-4.mt-1"
    PROFILE_LIST = ".select-dropdown.open"
    COUNTRY_LIST = ".select-options-list"

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def get_list_from_market(self, name: str):
        specialist_list = self.driver.find_element(By.CSS_SELECTOR, self.SPECIALISTS_LIST)
        child_list = specialist_list.find_elements(By.CSS_SELECTOR, "*")
        for child in child_list:
            name_element = child.find_elements(By.CSS_SELECTOR, ".name")
            if len(name_element) == 0:
                continue
            name_element = name_element[0]
            if name_element.text == name:
                child.find_element(By.CSS_SELECTOR, '.icon-buttons > span:nth-child(2)').click()
                break

    def select_profile_type_list(self, profile_type: str):
        profile_type_list = self.driver.find_element(By.CSS_SELECTOR, self.PROFILE_LIST)
        child_profile_list = profile_type_list.find_elements(By.CSS_SELECTOR, "*")
        for child in child_profile_list:
            name_element = child.find_elements(By.CSS_SELECTOR, ".select-option-text")
            if len(name_element) == 0:
                continue
            name_element = name_element[0]
            if name_element.text == profile_type:
                child.click()
                break


    def select_operator_from_market(self, operator_name: str):
        specialist_list = self.driver.find_element(By.CSS_SELECTOR, self.SPECIALISTS_LIST)
        child_list = specialist_list.find_elements(By.CSS_SELECTOR, "*")
        for child in child_list:
            name_element = child.find_elements(By.CSS_SELECTOR, ".name")
            if len(name_element) == 0:
                continue
            name_element = name_element[0]
            if name_element.text == operator_name:
                child.click()
                break

    def select_specialist_country(self, specialist_country: str):
        specialist_country_list = self.driver.find_element(By.CSS_SELECTOR, self.COUNTRY_LIST)
        child_specialist_country_list = specialist_country_list.find_elements(By.CSS_SELECTOR, "*")
        for child in child_specialist_country_list:
            name_element = child.find_elements(By.CSS_SELECTOR, ".select-option-text")
            if len(name_element) == 0:
                continue
            name_element = name_element[0]
            if name_element.text == specialist_country:
                child.click()
                break