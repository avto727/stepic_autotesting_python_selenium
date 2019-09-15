from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PRODUCT_LINK = (By.CSS_SELECTOR, "#browse > li > ul > li:nth-child(1) > a")

class LoginPageLocators():
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration - email")
    EMAIL_SIGNIN = (By.CSS_SELECTOR, "#id_login-username")

class ProductPageLocators():
    ADD_PROD_1 = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    TEXT_ADD_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    TEXT_PROD = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')

    AMOUNT_BASKET = (By.CSS_SELECTOR, '.alert-info.fade.in > div > p:nth-child(1) > strong')