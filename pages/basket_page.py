from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_ITEMS), \
            "Items are found in basket but should bot be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "No text about empty basket"
