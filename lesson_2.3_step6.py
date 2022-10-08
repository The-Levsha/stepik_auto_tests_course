from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

# Ваш код, который заполняет обязательные поля
button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# Ваш код, который заполняет обязательные поля
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

time.sleep(1)

#Вставляем полученный результат в поле
input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
input_field.send_keys(y)

button2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button2.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(15)
# закрываем браузер после всех манипуляций
browser.quit()