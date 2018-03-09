from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.x = MainPage.check_quantity_product(self)
        while int(self.x) < 3:
            self.click_first_element = MainPage.click_first_element(self)
            self.x = int(self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute('textContent')) + 1
            self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')
            if len(self.driver.find_elements_by_name(
                    'options[Size]')) > 0:  # если на странице есть этот блок, то работаем с ним
                self.driver.find_element_by_name('options[Size]').click()
                self.driver.find_element_by_css_selector('select[name="options[Size]"] option[value="Small"]').click()
                self.driver.find_element_by_name('add_cart_product').click()
                self.wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                             '//div[@id="cart"]//a[2]/span[@class="quantity"]'), str(self.x)))
                #self.driver.get('http://localhost/litecart/en/')
                self.open = MainPage.open(self)

            else:
                self.driver.find_element_by_name('add_cart_product').click()
                if int(self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute(
                        'textContent')) < self.x:
                    self.wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                                      '//div[@id="cart"]//a[2]/span[@class="quantity"]'), str(self.x)))
                #self.driver.get('http://localhost/litecart/en/')  # возвращаемся на главную после добавления товара
                self.open = MainPage.open(self)

