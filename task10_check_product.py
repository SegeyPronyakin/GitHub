from selenium import webdriver


driver_CHROME = webdriver.Chrome()
driver_FIREFOX = webdriver.Firefox()


def check_product_property(driver):
    driver.get('http://localhost/litecart/en/')
    name_of_homepage_product = driver.find_element_by_css_selector('#box-campaigns div[class="name"]').get_attribute('textContent') #Имя на главной странице:
    cost_of_homepage = driver.find_element_by_css_selector("#box-campaigns [class='regular-price']").get_attribute('textContent').replace('$','')
    cost_color_homepage = driver.find_element_by_css_selector("[class='regular-price']").value_of_css_property('color').replace('rgba(', '').replace(')', '')
    text_decoration_cost_homepage = driver.find_element_by_css_selector('#box-campaigns [class="regular-price"]').value_of_css_property('text-decoration')

    #Проверка на размер цены на главной странице
    size_old_cost_homepage = driver.find_element_by_css_selector("#box-campaigns [class='regular-price']").size
    size_new_cost_homepage = driver.find_element_by_css_selector("#box-campaigns [class='campaign-price']").size
    if int(size_old_cost_homepage['width']) < int(size_new_cost_homepage['width']):
        print("OK: новая цена больше старой на главной странице")

    #Проверка цен на совпадение
    driver.find_element_by_css_selector('#box-campaigns div[class="name"]').click()
    cost_of_cart = driver.find_element_by_css_selector('div[class="information"] [class="regular-price"]').get_attribute('textContent').replace('$','')
    if int(cost_of_cart) == int(cost_of_homepage):
        print("OK: Цены совпадают")
        print(cost_of_homepage, cost_of_cart)
    else:
        print("Fail: цены не совпадают")
        print(cost_of_homepage, cost_of_cart)

    #Проверка имени
    name_of_catr_product = driver.find_element_by_css_selector('#box-product h1').get_attribute('textContent')
    if name_of_homepage_product == name_of_catr_product:
        print("OK: названия совпадают")
        print(name_of_homepage_product, name_of_catr_product)
    else:
        print("FAIL: названия не совпадают")
        print(name_of_homepage_product, name_of_catr_product)

    #Проверка на серый цвет старой цены
    cost_color_cart  = driver.find_element_by_css_selector('div[class="information"] [class="regular-price"]').value_of_css_property('color').replace('rgba(', '').replace(')', '').split(',')[:-1]
    for i in cost_color_homepage.split(',')[:-1]:
        a = 0
        if cost_color_homepage.split(',')[:-1][a] == cost_color_homepage.split(',')[:-1][0]:
            print("Цвет старой цены на главной странице серый")
        else:
            print('Цвет старой цены на главной странице НЕ серый')
        a+=1

    for i in cost_color_cart:
        a = 0
        if cost_color_cart[a] == cost_color_cart[0]:
            print('Цвет старой цены в карточке товара серый')
        else:
            print('Цвет старой цены в карточке товара НЕ сервый')
        a+=1

    #Проверка на перечеркнутую цену
    if 'line-through' in text_decoration_cost_homepage:
        print("ОК: старая цена на гланой странице перечеркнутая")
    else:
        print('FAIL: старя цена на главной странице не перечернутая')

    text_decoration_cost_cart = driver.find_element_by_css_selector('div[class="information"] [class="regular-price"]').value_of_css_property('text-decoration')
    if 'line-through' in text_decoration_cost_cart:
        print("ОК: старая цена на странице товара перечеркнутая")
    else:
        print('FAIL: старя цена на странице товара не перечернутая')

    #Проверка размера цены в карточке товара
    size_old_cost_cart = driver.find_element_by_css_selector('div[class="information"] [class="regular-price"]').size
    size_new_cost_cart = driver.find_element_by_css_selector("div[class='information'] [class='campaign-price']").size
    if int(size_old_cost_cart['width']) < int(size_new_cost_cart['width']):
        print("OK: новая цена больше старой на странице карточки товара")

    print("Проверка окончена")
    print('*********************')
    driver.close()


def main():
    check_product_property(driver_CHROME)
    check_product_property(driver_FIREFOX)


if __name__ == '__main__':
    main()

