import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     print(link)
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    # print(link)
    browser.get(link)
    browser.implicitly_wait(10)
    # time.sleep(3)
    # print(answer)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector(".textarea.ember-text-area.ember-view").send_keys(answer)
    # time.sleep(3)
    browser.find_element_by_css_selector(".submit-submission ").click()
    time.sleep(10)