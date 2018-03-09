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
        self.count_product = self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')
        # Пока в корзине меньше N товаров, добавлять товары
        while int(self.count_product.get_attribute('textContent')) < 3:
            self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')
            self.driver.find_element_by_xpath('//*[@id="box-most-popular"]//a[1]/div[2]').click()  # кликаем первый
            # Присваиваем Х значение на 1 больше, чем ранее
            x = int(self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute('textContent')) + 1

            if len(self.driver.find_elements_by_name(
                    'options[Size]')) > 0:  # если на странице есть этот блок, то работаем с ним
                self.driver.find_element_by_name('options[Size]').click()
                self.driver.find_element_by_css_selector('select[name="options[Size]"] option[value="Small"]').click()
                self.driver.find_element_by_name('add_cart_product').click()
                if int(self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute(
                        'textContent')) < x:
                    self.wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                                      '//div[@id="cart"]//a[2]/span[@class="quantity"]'), str(x)))
                self.driver.get('http://localhost/litecart/en/')  # возвращаемся на главную после добавления товара
            else:
                self.driver.find_element_by_name('add_cart_product').click()
                if int(self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute(
                        'textContent')) < x:
                    self.wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                                      '//div[@id="cart"]//a[2]/span[@class="quantity"]'), str(x)))
                self.driver.get('http://localhost/litecart/en/')
            self.count_product = self.driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')  # поиск элемента после каждого цикла

        self.driver.find_element_by_xpath('//div[@id="cart"]//a[3]').click()  # переход в корзину по завершению цикла