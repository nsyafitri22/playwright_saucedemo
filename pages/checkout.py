from locator.checkout import Loc
from playwright.sync_api import expect

import allure

class Checkout:
    def __init__(self, setup):
        self.setup = setup
    def form_information(self,URL):
        with allure.step('Success Checkout and Direct to Page Fill Form to Sending'):
            expect(self.setup).to_have_url(URL)
    def first_name(self,firstname):
        with allure.step('Fill Form First Name'):
            self.setup.locator(Loc.first_name).fill(firstname)
    def last_name(self,lastname):
        with allure.step('Fill Form Last Name'):
            self.setup.locator(Loc.last_name).fill(lastname)
    def postal_code(self,postal_code):
        with allure.step('Fill Form Postal Code'):
            self.setup.locator(Loc.postal_code).fill(postal_code)
    def button_checkout(self):
        with allure.step('Click Button Continue'):
            self.setup.locator(Loc.button_checkout).click()
    def success_checkout(self,URL):
        with allure.step('Success Login and Direct to Homepage'):
            expect(self.setup).to_have_url(URL)