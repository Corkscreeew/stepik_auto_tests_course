from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Явное ожидание Explicit Waits
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    # button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

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



    # Неявное ожидание Implicit wait
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    #
    # browser = webdriver.Chrome()
    # # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)
    #
    # browser.get("http://suninjuly.github.io/wait1.html")
    #
    # button = browser.find_element(By.ID, "verify")
    # button.click()
    # message = browser.find_element(By.ID, "verify_message")
    #
    # assert "successful" in message.text