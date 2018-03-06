from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

#config
LOGIN = 'admin'
PASSWORD = 'admin'
ADMIN_URL = 'http://localhost/litecart/admin/'
CATEGORY_URL = 'http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1'


def login_admin_panel():
    driver.get(ADMIN_URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()

def check_log():
    driver.get(CATEGORY_URL)
    product_rows = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')
    x = 0
    for i in product_rows:
        element = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')[x].click()
        curent_url = driver.current_url
        after_click = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')
        if len(product_rows)< len(after_click):
            y = x
            for i in product_rows:
                driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')[y].click()
                if len(driver.get_log('browser')) > 0:
                    print('Есть сообщения об ошибках при открытии страницы ' + str(driver.current_url))
                else:
                    print('На странице ' + str(driver.current_url) + ' сообщений об ошибках нет')
                y += 1
                driver.get(curent_url)
        driver.get(CATEGORY_URL)
        x += 1
        break


def main():
    login_admin_panel()
    check_log()

if __name__ == '__main__':
    main()

# def check_log():
#     driver.get(CATEGORY_URL)
#     product_rows = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')
#     x = 0
#     for i in product_rows:
#         element = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')[x].click()
#         sub_elements = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')
#         if len(sub_elements)>0:
#             y = 0
#             for a in sub_elements:
#                 curent_url = driver.current_url
#                 driver.find_elements_by_xpath('//tr[@class="row"]//td[3]/a')[y].click()
#                 y+=1
#                 time.sleep(2)
#                 driver.get(curent_url)
#         time.sleep(2)
#         driver.get(CATEGORY_URL)
#         x+=1