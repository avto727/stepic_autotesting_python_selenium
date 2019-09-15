from selenium import webdriver
import time
import math

def calc(x):
  print(x)
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)

    x_element = browser.find_element_by_css_selector('span#input_value')
    x = x_element.text
    y = calc(x)
    button = browser.find_element_by_css_selector("input#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element_by_css_selector('input#answer').send_keys(y)
    browser.find_element_by_css_selector('input#robotCheckbox').click()
    browser.find_element_by_css_selector('input#robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла