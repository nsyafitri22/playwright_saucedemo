from locator.cart import Loc
from playwright.sync_api import expect

import allure

class Cart:
    def __init__(self, setup):
        self.setup = setup
    def remove_product(self):
        with allure.step('Click Button Remove'):
            self.setup.locator(Loc.remove_product).click()
    def recheck_page(self):
        with allure.step('Validate Page Cart After Remove Product'):
            assert self.setup.locator(Loc.recheck_page).inner_text() == 'Your Cart'
    def checkout_product(self):
        with allure.step('Checkout Product'):
            self.setup.locator(Loc.checkout_product).click()