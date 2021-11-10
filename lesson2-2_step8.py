from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fields = browser.find_elements(By.CSS_SELECTOR,"input[type='text']")
    for field in fields:
      field.send_keys('answer')
    
    filed = browser.find_element(By.CSS_SELECTOR,"input[type=file]")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'lesson2-2_step8.txt')           # добавляем к этому пути имя файла 
    filed.send_keys(file_path)
      # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице 
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()