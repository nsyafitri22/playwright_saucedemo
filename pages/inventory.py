from locator.inventory import Loc
from playwright.sync_api import expect

import allure

class Inventory:
    def __init__(self, setup):
        self.setup = setup
    def check_url(self,URL):
        with allure.step('Success Login and Direct to Homepage'):
            expect(self.setup).to_have_url(URL)
    def check_label(self):
        with allure.step('Check Label Title'):
            assert self.setup.locator(Loc.check_label).inner_text() == 'Swag Labs'
            self.setup.screenshot(type = 'png', path='ss/screenshot.png')
            allure.attach.file("ss/screenshot.png", name="Screenshot Login", attachment_type=allure.attachment_type.PNG)
    def add_product(self):
        with allure.step('Add Product'):
            self.setup.locator(Loc.add_product).click()
    def check_product(self):
        with allure.step('Check Jumlah Product After Add 1 Product'):
            assert self.setup.locator(Loc.check_product).inner_text() == '1'
    def add_product2(self):
        with allure.step('Add Product Kedua'):
            self.setup.locator(Loc.add_product2).click()
    def check_product2(self):
        with allure.step('Check Jumlah Product After Add 2 Product'):
            assert self.setup.locator(Loc.check_product2).inner_text() == '2'
    def cart_page(self):
        with allure.step('Go to Cart Page'):
            self.setup.locator(Loc.cart_page).click()
    