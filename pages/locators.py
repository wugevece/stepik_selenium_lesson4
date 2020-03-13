from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_MESSAGE_FORM = (By.CSS_SELECTOR, "#messages .alert:nth-child(3)")
    BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")