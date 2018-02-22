from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


driver = webdriver.Chrome()
ADMIN_URL = 'http://localhost/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'
PRODUCT_PATH = os.path.abspath("img.jpg")
NAME_PRODUCT = 'BatDuck'


def login_admin_panel():
    """Функция авторизации"""

    driver.maximize_window()
    driver.get(ADMIN_URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()


def add_product():
    """Функция добавления товара"""

    driver.find_element_by_xpath('//ul[@id="box-apps-menu"]//li[2]').click()
    driver.find_element_by_xpath("//*[@id='content']/div[1]/a[2]").click()
    driver.find_element_by_css_selector('input[name="name[en]"]').send_keys(NAME_PRODUCT)
    driver.find_element_by_css_selector('input[name="code"]').send_keys('001')
    driver.find_element_by_css_selector('input[name="product_groups[]"]').click()
    driver.find_element_by_css_selector('input[name="quantity"]').clear()
    driver.find_element_by_css_selector('input[name="quantity"]').send_keys('3')
    driver.find_element_by_css_selector('input[name="date_valid_from"]').send_keys(Keys.HOME + '29032017')
    driver.find_element_by_css_selector('input[name="date_valid_to"]').send_keys(Keys.HOME + '29032019')
    driver.find_element_by_css_selector('input[name="new_images[]"]').send_keys(PRODUCT_PATH)
    time.sleep(2)

    driver.find_element_by_xpath('//form//ul/li[2]').click()
    driver.find_element_by_css_selector('select[name="manufacturer_id"]').click()
    driver.find_element_by_css_selector('select[name="manufacturer_id"] option[value="1"]').click()
    driver.find_element_by_css_selector('input[name="keywords"]').send_keys('Any KEYS')
    driver.find_element_by_css_selector('input[name="short_description[en]"]').send_keys('Short description')
    driver.find_element_by_css_selector('div[class="trumbowyg-editor"]').send_keys('description description description')
    driver.find_element_by_css_selector('input[name="head_title[en]"]').send_keys('BatDuck')
    driver.find_element_by_css_selector('input[name="meta_description[en]"]').send_keys('BatDuck meta')
    time.sleep(2)

    driver.find_element_by_xpath('//form//ul/li[4]').click()
    driver.find_element_by_css_selector('input[name="purchase_price"]').clear()
    driver.find_element_by_css_selector('input[name="purchase_price"]').send_keys(Keys.HOME + '100')
    driver.find_element_by_css_selector('select[name="purchase_price_currency_code"]').click()
    driver.find_element_by_css_selector('select[name="purchase_price_currency_code"] option[value="USD"]').click()
    driver.find_element_by_css_selector('input[name="prices[USD]"]').send_keys('150')
    driver.find_element_by_css_selector('button[name="save"]').click()
    time.sleep(2)

    names = driver.find_elements_by_xpath('//table[@class="dataTable"]//tr//a')
    names_list = []
    for name in names:
        names_list.append(name.get_attribute('textContent'))
    if NAME_PRODUCT in names_list:
        print("TEST OK")
    else:
        print("TEST FAIL")



def main():
    login_admin_panel()
    add_product()
    driver.close()



if __name__ == '__main__':
    main()