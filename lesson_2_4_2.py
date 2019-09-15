from selenium import webdriver
import time, math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
    browser.find_element_by_id("book").click()

    x = int(browser.find_element_by_css_selector('#input_value').text)
    y = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element_by_css_selector('#answer').send_keys(y)


    browser.find_element_by_css_selector("button#solve").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла