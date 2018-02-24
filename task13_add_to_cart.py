"""
1) открыть главную страницу
2) открыть первый товар из списка
2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
3) подождать, пока счётчик товаров в корзине обновится
4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза,
чтобы в общей сложности в корзине было 3 единицы товара
5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
"""
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 5)

def add_to_cart():
    driver.get('http://localhost/litecart/en/')
    count_product = driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')

    while int(count_product.get_attribute('textContent')) < 5:
        count_product = driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')
        first_product = driver.find_element_by_xpath('//*[@id="box-most-popular"]//a[1]/div[2]').click()
        x = int(driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute(
            'textContent')) + 1

        if len(driver.find_elements_by_name('options[Size]')) > 0:
            driver.find_element_by_name('options[Size]').click()
            driver.find_element_by_css_selector('select[name="options[Size]"] option[value="Small"]').click()
            driver.find_element_by_name('add_cart_product').click()
            while int(driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute('textContent')) < x:
                #wait.until(EC.text_to_be_present_in_element(By.XPATH, '//div[@id="cart"]//a[2]/span[@class="quantity"]'))
                pass
            driver.get('http://localhost/litecart/en/')
        else:
            driver.find_element_by_name('add_cart_product').click()
            while int(driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]').get_attribute(
                    'textContent')) < x:
                #wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="cart"]//a[2]/span[@class="quantity"]')))
                pass
            driver.get('http://localhost/litecart/en/')
        print(x)

        count_product = driver.find_element_by_xpath('//div[@id="cart"]//a[2]/span[@class="quantity"]')

    driver.find_element_by_xpath('//div[@id="cart"]//a[3]').click() #в корзину


    remove_button_list = driver.find_elements_by_css_selector('li[class="item"] button[name="remove_cart_item"]')
    for button in remove_button_list:
        product = driver.find_element_by_css_selector('div[class="viewport"] button[name="remove_cart_item"]')
        product.click()
        table = driver.find_element_by_id('box-checkout-summary')
        wait.until(EC.staleness_of(table))














def main():
    add_to_cart()
    #driver.close()


if __name__ == '__main__':
    main()

# product = driver.find_element_by_css_selector('div[class="viewport"] button[name="remove_cart_item"]')
# product.click()
# time.sleep(2)

#
# for button in remove_button_list:
#     wait_element = wait.until(EC.visibility_of_element_located
#                               ((By.CSS_SELECTOR, 'div[class="viewport"] button[name="remove_cart_item"]')))
#     wait_element.click()

#
# wait_element = wait.until(
#     lambda d: d.find_element_by_css_selector('div[class="viewport"] button[name="remove_cart_item"]'))