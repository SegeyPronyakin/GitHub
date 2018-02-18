"""
а) на главной странице и на странице товара совпадает текст названия товара
б) на главной странице и на странице товара совпадают цены (обычная и акционная)
в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
(цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
Необходимо убедиться, что тесты работают в разных браузерах, желательно проверить во всех трёх ключевых браузерах (Chrome, Firefox, IE).
"""


from selenium import webdriver

driver = webdriver.Chrome()
# driver_CHROME = webdriver.Chrome()
# driver_FIREFOX = webdriver.Firefox()
# driver_IE = webdriver.Ie()
def a():
    driver.get('http://localhost/litecart/en/')
    name_of_homepage_product = driver.find_element_by_css_selector('#box-campaigns div[class="name"]').get_attribute('textContent') #Имя на главной странице:
    cost_of_homepage = driver.find_element_by_css_selector("#box-campaigns [class='regular-price']").get_attribute('textContent').replace('$','')
    cost_color_homepage = driver.find_element_by_css_selector("[class='regular-price']").value_of_css_property('color').replace('rgba(', '').replace(')', '')
    text_decoration_cost_homepage = driver.find_element_by_css_selector('#box-campaigns [class="regular-price"]').value_of_css_property('text-decoration')
    #Проверка цены
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

    driver.find_element_by_css_selector('div[class="information"] [class="regular-price"]').value_of_css_property('text-decoration')




    #     print('OK: цвет совпадает')
    #     print(cost_color_homepage.split(',')[:-1],cost_color_cart)
    # else:
    #     print('FAIL: цвет не совпадает')
    #     print(cost_color_homepage.split(',')[:-1], cost_color_cart)
    # print(cost_color_cart)



    print('*********************')
    cost_of_homepage = driver.find_elements_by_css_selector("#box-most-popular [class='campaign-price']")
    for i in cost_of_homepage:
        print(i.get_attribute('textContent'))




    # name_of_cart_product =
    #

    # cost_of_cart =
    #
    # sale_cost_of_homepage =
    # sale_cost_of_cart =



def main():
    a()


if __name__ == '__main__':
    main()

# if cost_of_homepage != '':
#     print(driver.find_elements_by_css_selector("[class='price-wrapper']")[x].get_attribute('textContent').replace('$',
#                                                                                                                   ''))
#     x += 1