from selenium import webdriver
import time
import math

def calc(x):
  print(x)
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)

    x = browser.find_element_by_css_selector('span#num1').text
    y = browser.find_element_by_css_selector('span#num2').text
    z = int(x) + int(y)
    print(z)
    # browser.find_element_by_css_selector('input#answer').send_keys(y)
    browser.find_element_by_css_selector('select#dropdown').click()
    ttt = 'option[value="' + str(z) + '"]'
    print(ttt)
    browser.find_element_by_css_selector(ttt).click()
    browser.find_element_by_css_selector('button.btn').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла