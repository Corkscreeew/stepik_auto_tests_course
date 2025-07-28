# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = "https://fake-shop.com/book1.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # link = browser.find_element(By.LINK_TEXT, "224592")
#     # link.click()
#     #
#     # input1 = browser.find_element(By.TAG_NAME, "input")
#     # input1.send_keys("Ivan")
#     # input2 = browser.find_element(By.NAME, "last_name")
#     # input2.send_keys("Petrov")
#     # input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     # input3.send_keys("Smolensk")
#     # input4 = browser.find_element(By.ID, "country")
#     # input4.send_keys("Russia")
#     # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     # button.click()
#
#     # подготовка для теста
#     # открываем страницу первого товара
#     # данный сайт не существует, этот код приведен только для примера
#     browser.get("https://fake-shop.com/book1.html")
#
#     # добавляем товар в корзину
#     add_button = browser.find_element(By.CSS_SELECTOR, ".add")
#     add_button.click()
#
#     # открываем страницу второго товара
#     browser.get("https://fake-shop.com/book2.html")
#
#     # добавляем товар в корзину
#     add_button = browser.find_element(By.CSS_SELECTOR, ".add")
#     add_button.click()
#
#     # тестовый сценарий
#     # открываем корзину
#     browser.get("https://fake-shop.com/basket.html")
#
#     # ищем все добавленные товары
#     goods = browser.find_elements(By.CSS_SELECTOR, ".good")
#
#     # проверяем, что количество товаров равно 2
#     assert len(goods) == 2
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()









# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.XPATH, '//div/button[text()="Submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# import math
#
# try:
#     link = "https://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     x_element = browser.find_element(By.ID, 'treasure')
#     x = x_element.get_attribute('valuex')
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     y = calc(x)
#
#     input = browser.find_element(By.ID, "answer")
#     input.send_keys(y)
#
#     checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
#     checkbox.click()
#
#     radiobutton = browser.find_element(By.ID, "robotsRule")
#     radiobutton.click()
#
#     time.sleep(1)
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(5)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# def send_keys_to_element(lokator, text):
#     x = browser.find_element(*lokator)
#     x.send_keys(text)
#
# send_keys_to_element((By.CSS_SELECTOR, '[type="submit"]'), 'Text')



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# import math
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     x = browser.find_element(By.ID, "num1")
#     num1 = int(x.text)
#
#     y = browser.find_element(By.ID, "num2")
#     num2 = int(y.text)
#
#     answer = num1 + num2
#
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(answer))
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(5)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()