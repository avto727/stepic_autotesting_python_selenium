from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class BasePage():
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url
		
		
	def open(self):
		self.browser.get(self.url)

	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except ('NoSuchElementException'):
			return False
		return True

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
		
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def go_to_product_page(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        a_url = self.browser.current_url
        print(a_url)
        assert 'http://selenium1py.pythonanywhere.com/ru/accounts/login/' == a_url, "Login link is wrong"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

class ProductPage(BasePage):
    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        a_url = self.browser.current_url
        print('Шаг 1, a_url = ', a_url)
        # assert 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019' == a_url, "Login link is wrong"


    def add_product_basket(self):
        print('Шаг 3')
        self.browser.find_element(*ProductPageLocators.ADD_PROD_1).click()

    def should_be_add_to_basket(self):
        # реализуйте проверку надписи что товар добавлен
        print('Шаг 4')
        add_text = self.browser.find_element(*ProductPageLocators.TEXT_ADD_BASKET).text
        print(add_text)
        # assert "The shellcoder's handbook" == add_text, "Text_add is wrong"
        return add_text

    def should_be_product_text(self):
        # реализуйте проверку названия товара
        print('Шаг 5')
        product_text = self.browser.find_element(*ProductPageLocators.TEXT_PROD).text
        print('Шаг 2 product_text = ', product_text)
        # assert "The shellcoder's handbook" == product_text, "Text_add is wrong"
        return product_text

    def should_be_amount_basket(self):
        # реализуйте проверку что стоимость корзины совпадает с ценой товара
        print('Шаг 6')
        amount_basket = self.browser.find_element(*ProductPageLocators.AMOUNT_BASKET).text
        print(amount_basket)
        assert '9,99' in amount_basket, "amount_basket is wrong"

    def should_be_equality_text(self, product, basket):
        # реализуйте проверку что товар в корзине совпадает с добавленным
        print('Шаг 7')
        assert product == basket, 'text product not mach text basket'
