from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(desired_capabilities={"unexpectedAlertBehaviour": "dismiss"}) #закрытие алерта
wait = WebDriverWait(driver, 10)
LOGIN = 'admin'
PASSWORD = 'admin'
ADMIN_URL = 'http://localhost/litecart/admin/'
COUNTRY_URL = 'http://localhost/litecart/admin/?app=countries&doc=countries'


def login_admin_panel():
    """Функция авторизации"""

    driver.maximize_window()
    driver.get(ADMIN_URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()


def function():
    """Функция проверки на открытие новых окон"""

    driver.get(COUNTRY_URL)
    driver.find_element_by_css_selector('#content div a').click()
    link_list = driver.find_elements_by_xpath('//*[@id="content"]//td/a/i')
    main_window = driver.current_window_handle #текущее окно
    print('Главное окно:', main_window)
    windows_list_OLD = []
    windows_list_NEW = []
    error_list = []
    x = 0
    y = 0 #Счетчик открывшихся окон
    #По списку ссылок на странице
    for link in link_list:
        windows_list_OLD.append(driver.window_handles) #Список старых окон
        #Механизм повтора события при закрытии алерта
        try:
            driver.find_elements_by_xpath('//*[@id="content"]//td/a/i')[x].click()
            wait.until(EC.number_of_windows_to_be(2))
            windows_list_NEW.append(driver.window_handles)  # Список новых окон после клика по ссылке
        except UnexpectedAlertPresentException:
            driver.find_elements_by_xpath('//*[@id="content"]//td/a/i')[x].click()
            wait.until(EC.number_of_windows_to_be(2))
            windows_list_NEW.append(driver.window_handles)  # Список новых окон после клика по ссылке
        result = list(set(windows_list_NEW[0])^set(windows_list_OLD[0]))#Получение нового элемента из списка (новое окно)
        if len(result) >= 1: #В момент возникновения алерта, в список ничего не добавляется и он пуст. Делаем проверку на []
            new_window = driver.switch_to.window(result[0]) #Переключаемся в новое окно
            print('Новое окно:', result[0])
            driver.close()
            y += 1
        else:
            print('Ошибка: Алерт или ссылка открылась не в главном окне')
            error_list.append(driver.window_handles)
        driver.switch_to.window(main_window) #переключаемся в главное окно
        #Обнуляем списки для следующих итераций
        windows_list_NEW = []
        windows_list_OLD = []
        x += 1
    if len(link_list) == y:
        print('ТЕСТ ОК. КОЛ-ВО ССЫЛОК НА СТРАНИЦЕ И ОТКРЫТЫХ ОКОН СОВПАДАЮТ')
        print("Кол-во открытых окон: ", y, " ," " Кол-во ссылок:", len(link_list))
    else:
        print('Опять что-то не так')
        print("Кол-во открытых окон: ", y, "," " кол-во ссылок:", len(link_list))


def main():
    login_admin_panel()
    function()
    driver.quit()


if __name__ == '__main__':
    main()