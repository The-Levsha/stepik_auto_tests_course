from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)



wait = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

btn = browser.find_element(By.ID, "book")
btn.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

#Вставляем полученный результат в поле
input_field = browser.find_element(By.CSS_SELECTOR, "input.form-control")
input_field.send_keys(y)

#Скролл страницы вниз

browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)

button1 = browser.find_element(By.CSS_SELECTOR, "#solve")
button1.click()

time.sleep(10)
browser.quit()



