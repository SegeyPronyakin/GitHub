from selenium import webdriver
driver = webdriver.Chrome()

#config
LOGIN = 'admin'
PASSWORD = 'admin'
ADMIN_URL = 'http://localhost/litecart/admin/'
COUNTRY_URL = 'http://localhost/litecart/admin/?app=countries&doc=countries'


def wd_close(wd):
    wd.close()


def login_admin_panel():
    driver.get(ADMIN_URL)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('login').click()


def country_sorting():
    """фУНКИЦИЯ ПРОВЕРКИ ОТСОРТОВАННОСТИ СПИСКА СТРАН"""

    country_list = []
    driver.get(COUNTRY_URL)
    country_element_list = driver.find_elements_by_css_selector('tr[class="row"] a')
    for country in country_element_list:
        #Проверка на наличие атрибута "text" и дальнейшее добавление значения атрибута в список.
        #Принято решение обойтись без xpath и проверить тег на наличие атрибута,
        #т.к. применялась бы привязка к порядковому номеру тега <a>
        if country.get_attribute('text') != "":
            country_list.append(country.get_attribute('text'))
    #Сортируется полученный список и сравнивается с исходным.
    if country_list == sorted(country_list):
        print('ОК: Список стран отсортирован')
    else:
        print('FAIL: Список стран неотсортрован')


def check_country_zone():
        """Функция проверки сортировки зон страны"""

        country_zone_list = driver.find_elements_by_xpath('//tr[@class="row"]/td[6]')
        y = -1  #Счетчик строк стран (-1 -- хедер таблицы)
        zones_list = []
        for zone in country_zone_list:
            y+=1
            #Если кол-во  зон больше 0, то переходим в эту страну и делаем проверку на сортировку
            quantity_zones = driver.find_elements_by_xpath('//tr[@class="row"]/td[6]')[y]\
            .get_attribute('textContent') #Элемент кол-ва зон в стране
            if int(quantity_zones) > 0:
                driver.find_elements_by_xpath('//tr[@class="row"]/td[7]')[y].click()
                #Проверка сортировки зон страны
                names_list = driver.find_elements_by_xpath('//table[@id="table-zones"]//td[3]')
                for name in names_list:
                    if name.get_attribute('textContent') != '':
                        zones_list.append(name.get_attribute('textContent'))
                if zones_list == sorted(zones_list):
                    print('OK: Список зон на странице страны отсортирован')
                else:
                    print("FAIL: Список зон на странице страны не отсортрован")
                zones_list = [] #Обнуляем список для следующих циклов
                driver.find_element_by_name('cancel').click()  #Возвращаемся на страницу стран


def geo_zone():
    """ФУНКЦИЯ ПРОВЕРКИ ОТСОРТИРОВАННОСТИ ВЫБРАННЫХ ЗОН В ВЫПАДАЮЩИХ СПИСКАХ
    НА СТРАНИЦЕ /?app=geo_zones&doc=geo_zones"""

    driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
    country = driver.find_elements_by_xpath('//tr[@class="row"]//td[3]') #список стран
    x=0
    zone_list = []
    #Переходим в каждую странцу и ищем среди выпадающих списков элемент
    #с тегом <options> и атрибутом selected
    for i in country:
        driver.find_elements_by_xpath('//tr[@class="row"]//td[5]')[x].click()
        zone_list_el = driver.find_elements_by_xpath('//table[@id="table-zones"]//tr//td[3]//option[@selected="selected"]') #[2] // td[3]
        for a in zone_list_el:
            zone_list.append(a.get_attribute('textContent'))
        if zone_list == sorted(zone_list): #сравниваем отсортированный и неотсортированный список
            print("OK: список зон на странице зон отсортирован")
        else:
            print("Fail: список зон на странице зон неотсортирован")
        zone_list = [] #обнуляю список для следующих стран
        x+=1
        driver.find_element_by_name('cancel').click()


def main():
    login_admin_panel()
    country_sorting()
    check_country_zone()
    geo_zone()
    wd_close(driver)


if __name__ == '__main__':
    main()

