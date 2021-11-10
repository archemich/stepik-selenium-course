from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
nameInput = browser.find_element_by_css_selector(".first_class [placeholder='Input your first name']")
nameInput.send_keys("Мария")

# Заполнение поля "Фамилия"
lastnameInput = browser.find_element_by_css_selector(".second_class [placeholder='Input your last name']")
lastnameInput.send_keys("Марьина")

# Заполнение поля "Email"
emailInput = browser.find_element_by_css_selector(".third_class [placeholder='Input your email']")
emailInput.send_keys("maria@testmail.com")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()