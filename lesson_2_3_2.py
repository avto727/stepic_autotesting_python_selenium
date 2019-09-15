from selenium import webdriver
import time, math
import os

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_id("button")
    browser.find_element_by_css_selector('button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    first_window = browser.window_handles[0]

    x = int(browser.find_element_by_css_selector('#input_value').text)
    y = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element_by_css_selector('#answer').send_keys(y)


    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла