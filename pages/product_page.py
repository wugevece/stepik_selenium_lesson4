from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def basket_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text

    def added_product_message_text(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE).text

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_added_product_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_MESSAGE),\
            "No message about product added to basket"
        assert self.product_name() in self.added_product_message_text(),\
            f"Name of added product '{self.product_name()}' is not found in message"

    def should_be_basket_info_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE_FORM), \
            "No message about basket info"
        assert self.product_price() in self.basket_message(),\
            "Incorrect price in basket info message"
