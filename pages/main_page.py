from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/en/')
        return self

    def check_quantity_product(self):
        self.count_product = self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute('textContent')
        return int(self.count_product)

    def click_first_element(self):
        self.driver.find_element_by_xpath('//*[@id="box-most-popular"]//a[1]/div[2]').click()
        return self