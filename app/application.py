from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import Cart


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.main_page = MainPage(self.driver).open()
        self.product_page = ProductPage.add_to_cart(self)
        self.cart = Cart.go_to_cart(self)
        self.cart = Cart.remove_product(self)

    def wd_quit(self):
        self.driver.quit()
        print('Тест окончен.')




