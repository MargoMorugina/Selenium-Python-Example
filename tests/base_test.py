from typing import Union

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage

class BaseTest:
    driver: Union[Chrome, Firefox, Edge]
    wait: WebDriverWait
    login_page: LoginPage

