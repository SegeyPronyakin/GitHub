from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_cart(self):
        self.driver.find_element_by_xpath('//div[@id="cart"]//a[3]').click()
        return self

    def remove_product(self):
        self.remove_button_list = self.driver.find_elements_by_css_selector('li[class="item"] button[name="remove_cart_item"]')
        for button in self.remove_button_list:
            button_remove = self.driver.find_element_by_css_selector('div[class="viewport"] button[name="remove_cart_item"]')
            button_remove.click()
            table = self.driver.find_element_by_id('box-checkout-summary')
            self.wait.until(EC.staleness_of(table))  # таблица была, но исчезла
        return self