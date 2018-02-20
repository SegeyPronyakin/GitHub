from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uuid


driver = webdriver.Chrome()
USERMAIL = "Pronyakin_" + str(uuid.uuid1())[0:7] + "@p33.org"
PASSWORD = "Pronyakin_"


def registration():
    """Функция регистрации нового пользователя с последующей авторизацией"""

    #Регистрация
    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_link_text("New customers click here").click()
    driver.find_element_by_name("firstname").send_keys("Serg")
    driver.find_element_by_name("lastname").send_keys("Pronyakin")
    driver.find_element_by_name("address1").send_keys("Broadway 9")
    driver.find_element_by_name("postcode").send_keys("12345")
    driver.find_element_by_name("city").send_keys("New York")
    driver.find_element_by_class_name("select2-selection__arrow").click()
    driver.find_element_by_css_selector("[class='select2-search__field']").send_keys('United States' + Keys.ENTER)
    driver.find_element_by_name("email").send_keys(USERMAIL)
    driver.find_element_by_name("phone").send_keys("7550055")
    driver.find_element_by_name("password").send_keys(PASSWORD)
    driver.find_element_by_name("confirmed_password").send_keys(PASSWORD)
    driver.find_element_by_name("create_account").click()
    driver.find_element_by_link_text("Logout").click()
    #Авторизация
    driver.find_element_by_name("email").send_keys(USERMAIL)
    driver.find_element_by_name("password").send_keys(PASSWORD)
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Logout").click()
    print("Test OK")


def main():
   registration()
   driver.close()


if __name__ == '__main__':
    main()