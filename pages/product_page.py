from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def basket_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text

    def added_product_name_in_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text

    def add_product_to_basket(self):
        WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BTN)).click()

    def should_be_added_product_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "No message about product added to basket"
        assert self.product_name() == self.added_product_name_in_message(),\
            f"Name of added product '{self.product_name()}' is not found in message"

    def should_be_basket_info_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE_FORM), \
            "No message about basket info"
        assert self.product_price() in self.basket_message(),\
            "Incorrect price in basket info message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is not disappeared but should be"


