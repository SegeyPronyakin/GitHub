from selenium import webdriver
from pages.main_page import MainPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver).open().check_quantity_product()

