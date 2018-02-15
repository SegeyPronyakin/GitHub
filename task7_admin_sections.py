from selenium import webdriver
import time
driver = webdriver.Firefox()


URL = 'http://localhost/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'

def close_wd(wd):
    wd.close()


def authorization():
    """Функция авторизации"""

    driver.get(URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()


def click_menu():
    """Функция перебора всех пунктов меню (включая подпункты)"""

    x = 0                       #Счетчик для элементов меню
    sub_menu_element_count = 0  #Счетчик элементов подменю

    #Проходим по элементам меню
    for element_menu in driver.find_elements_by_css_selector("ul[id='box-apps-menu'] li[id='app-']"):
        driver.find_elements_by_css_selector("ul[id='box-apps-menu'] li[id='app-']")[x].click()
        x+=1

        #Если есть список элементов подменю, то проходимся по нему (len(sub_menu)>0)
        sub_menu = driver.find_elements_by_css_selector("ul[class='docs'] li")
        if len(sub_menu)>0:
            for sub_menu_element in sub_menu:
                driver.find_elements_by_css_selector("ul[class='docs'] li")[sub_menu_element_count].click()
                sub_menu_element_count+=1
            sub_menu_element_count = 0   #Обнуляется счетчик элементов подменю для следующего пункта меню


def  main():
    authorization()
    click_menu()
    close_wd(driver)


if __name__ == '__main__':
    main()
