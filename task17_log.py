from selenium import webdriver
driver = webdriver.Chrome()

LOGIN = 'admin'
PASSWORD = 'admin'
ADMIN_URL = 'http://localhost/litecart/admin/'
CATEGORY_URL = 'http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1'


def login_admin_panel():
    driver.get(ADMIN_URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()


def print_log():
    """Функция вывода на экран ошибок"""

    if len(driver.get_log('browser')) > 0:
        print('Есть сообщения об ошибках при открытии страницы ' + str(driver.current_url))
    else:
        print('На странице ' + str(driver.current_url) + ' сообщений об ошибках нет')


def check_log():
    """функия перебора товаров на странице категории"""

    driver.get(CATEGORY_URL)
    product_rows = driver.find_elements_by_xpath('//table[@class="dataTable"]//tr[@class="row"]//td[3]/a')
    x=0
    for row in product_rows:
        new_table = driver.find_elements_by_xpath('//table[@class="dataTable"]//tr[@class="row"]//td[3]/a')
        driver.find_elements_by_xpath('//table[@class="dataTable"]//tr[@class="row"]//td[3]/a')[x].click()
        print_log()
        x+=1
        driver.get(CATEGORY_URL)

def main():
    login_admin_panel()
    check_log()
    driver.quit()


if __name__ == '__main__':
    main()
