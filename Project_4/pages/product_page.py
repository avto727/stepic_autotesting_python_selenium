from .base_page import BasePage
from .locators import ProductPageLocators


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
