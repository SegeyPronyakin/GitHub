from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 5)

QUANTITY_XPATH = '//div[@id="cart"]//a[2]/span[@class="quantity"]'
FIRST_ELEMENT = '//*[@id="box-most-popular"]//a[1]/div[2]'

def add_to_cart():
    """Функция добавления товара в корзину с последующим удалением"""

    driver.get('http://localhost/litecart/en/')
    count_product = driver.find_element_by_xpath(QUANTITY_XPATH)
    #Пока в корзине меньше N товаров, добавлять товары
    while int(count_product.get_attribute('textContent')) < 3:
        driver.find_element_by_xpath(QUANTITY_XPATH)
        driver.find_element_by_xpath(FIRST_ELEMENT).click() #кликаем первый
        # Присваиваем Х значение на 1 больше, чем ранее
        x = int(driver.find_element_by_xpath(QUANTITY_XPATH).get_attribute('textContent')) + 1
        if len(driver.find_elements_by_name('options[Size]')) > 0: #если на странице есть этот блок, то работаем с ним
            driver.find_element_by_name('options[Size]').click()
            driver.find_element_by_css_selector('select[name="options[Size]"] option[value="Small"]').click()
            driver.find_element_by_name('add_cart_product').click()
            #Пока счетчик не станет равным X (то есть на 1 больше, чем до клика для добавления товара),ожидаем появления
            #счетчика равным X (ожидаение появления нужного текста элемента)
            if int(driver.find_element_by_xpath(QUANTITY_XPATH).get_attribute(
                'textContent')) < x:
                wait.until(EC.text_to_be_present_in_element((By.XPATH, QUANTITY_XPATH), str(x)))
            driver.get('http://localhost/litecart/en/') #возвращаемся на главную после добавления товара
        else:
            driver.find_element_by_name('add_cart_product').click()
            if int(driver.find_element_by_xpath(QUANTITY_XPATH).get_attribute(
                    'textContent')) < x:
                wait.until(EC.text_to_be_present_in_element((By.XPATH, QUANTITY_XPATH), str(x)))
            driver.get('http://localhost/litecart/en/')
        count_product = driver.find_element_by_xpath(QUANTITY_XPATH) #поиск элемента после каждого цикла

    driver.find_element_by_xpath('//div[@id="cart"]//a[3]').click() #переход в корзину по завершению цикла

    #Удаление элементов с ожиданием обновления таблицы
    remove_button_list = driver.find_elements_by_css_selector('li[class="item"] button[name="remove_cart_item"]')
    for button in remove_button_list:
        button_remove = driver.find_element_by_css_selector('div[class="viewport"] button[name="remove_cart_item"]')
        button_remove.click()
        table = driver.find_element_by_id('box-checkout-summary')
        wait.until(EC.staleness_of(table)) #таблица была, но исчезла


def main():
    add_to_cart()
    driver.close()


if __name__ == '__main__':
    main()

