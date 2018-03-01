from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome(desired_capabilities={"unexpectedAlertBehaviour": "dismiss"}) #закрытие алерта
LOGIN = 'admin'
PASSWORD = 'admin'
ADMIN_URL = 'http://localhost/litecart/admin/'
COUNTRY_URL = 'http://localhost/litecart/admin/?app=countries&doc=countries'


def login_admin_panel():
    driver.maximize_window()
    driver.get(ADMIN_URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()


def function():
    """Функция проверки на открытие новых окон"""

    driver.get(COUNTRY_URL)
    driver.find_element_by_css_selector('#content div a').click()
    link_list = driver.find_elements_by_xpath('//*[@id="content"]//tbody//td/a')
    main_window = driver.current_window_handle #текущее окно
    print('Главное окно:', main_window)
    windows_list_OLD = []
    windows_list_NEW = []
    x = 0
    #по списку ссылок на странице
    for link in link_list:
        windows_list_OLD.append(driver.window_handles) #список старых окон
        #механизм повтора события при закрытии алерта
        try:
            driver.find_elements_by_xpath('//*[@id="content"]//tbody//td/a')[x].click()
        except UnexpectedAlertPresentException:
            driver.find_elements_by_xpath('//*[@id="content"]//tbody//td/a')[x].click()
        windows_list_NEW.append(driver.window_handles) #список новых окон после клика по ссылке
        result = list(set(windows_list_NEW[0])^set(windows_list_OLD[0]))#получение нового элемента из списка (новое окно)
        if result!=[]: #в момент возникновения алерта, в список ничего не добавляется и он пуст. Делаем проверку на []
            new_window = driver.switch_to.window(result[0]) #переключаемся в новое окно
            print('Новое окно:', result[0])
            driver.close()
        driver.switch_to.window(main_window) #переключаемся в главное окно
        #обнуляем списки для следующих итераций
        windows_list_NEW = []
        windows_list_OLD = []
        x += 1


def main():
    login_admin_panel()
    function()
    driver.quit()


if __name__ == '__main__':
    main()