from .pages.base_page import MainPage
from .pages.base_page import ProductPage
import pytest


@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{number}"
    page = MainPage(browser, link)
    page.open()
    # page.go_to_product_page()  # выполняем метод страницы - переходим на страницу товара
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_url()
    product_text = product_page.should_be_product_text()
    product_page.add_product_basket()
    product_page.solve_quiz_and_get_code()
    basket_text = product_page.should_be_add_to_basket()
    product_page.should_be_amount_basket()
    product_page.should_be_equality_text(product_text, basket_text)

