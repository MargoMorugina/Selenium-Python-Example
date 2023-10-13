from typing import Union

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.consultant_page import ConsultantPage
from pages.specialist_select_page import SelectSpecialistPage


class BaseTest:
    driver: Union[Chrome, Firefox, Edge]
    wait: WebDriverWait
    login_page: LoginPage
    profile_page: ProfilePage
    consultant_page: ConsultantPage
    specialist_select_page: SelectSpecialistPage

