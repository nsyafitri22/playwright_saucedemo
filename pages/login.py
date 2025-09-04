from locator.login import Loc
from playwright.sync_api import expect

import allure

class Login:
    def __init__(self, setup):
        self.setup = setup
    def input_username(self,username):
        with allure.step('Input Username'):
            self.setup.locator(Loc.input_username).fill(username)
    def input_password(self,password):
        with allure.step('Input Password'):
            self.setup.locator(Loc.input_password).fill(password)
    def click_button_login(self):
        with allure.step('Click Button Login'):
            self.setup.locator(Loc.button_login).click()
    def error_message(self,error_message):
        with allure.step('Check Expected Error Message'):
            not_fill = self.setup.locator(Loc.error_message)
            expect(not_fill).to_have_text(error_message)