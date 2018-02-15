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


def check_sticker():
    driver.get("http://localhost/litecart/en/")
    driver.maximize_window()
    ducks = driver.find_elements_by_css_selector("li[class='product column shadow hover-light']")
    stiker_list = driver.find_elements_by_css_selector('.sticker')

    #Если кол-во стикеров совпадает с кол-вом товаров, то у каждого товара
    #по одному стикеру
    if len(ducks) == len(stiker_list):
        print('Кол-во карточек продуктов на странице: ', len(ducks))
        print('Кол-во стикеров на странице: ', len(stiker_list))
        print('Вывод: каждый продукт имеет по одному стикеру.')
    else:
        print('Кол-во карточек продуктов на странице: ', len(ducks))
        print('Кол-во стикеров на странице: ', len(stiker_list))
        print("Условия ТЗ нарушены. Кол-во стикеров у каждой карточки продукта отлично от единицы.")



def  main():
    authorization()
    click_menu()
    check_sticker()
    close_wd(driver)


if __name__ == '__main__':
    main()
