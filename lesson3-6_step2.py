import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope='session')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', [
  "https://stepik.org/lesson/236895/step/1",
  "https://stepik.org/lesson/236896/step/1",
  "https://stepik.org/lesson/236897/step/1",
  "https://stepik.org/lesson/236898/step/1",
  "https://stepik.org/lesson/236899/step/1",
  "https://stepik.org/lesson/236903/step/1",
  "https://stepik.org/lesson/236904/step/1",
  "https://stepik.org/lesson/236905/step/1",
  ])
def test_links(browser, link):
  browser.implicitly_wait(10)
  browser.get(link)
  answer = math.log(int(time.time()))
  browser.find_element(By.CSS_SELECTOR, '.string-quiz__textarea').send_keys(str(answer))
  button = WebDriverWait(browser, 1). until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
  button.click()
  hint_text = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.smart-hints__hint'))).text
  if hint_text != 'Correct!':
    print(hint_text)