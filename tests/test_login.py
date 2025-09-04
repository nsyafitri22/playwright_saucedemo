from pages.login import Login
from pages.inventory import Inventory

import pytest
import allure

@allure.title('Login dengan username dan password benar / valid')
@allure.description('Test Login dengan data valid')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_positive(setup):
     login = Login(setup)
     inventory = Inventory(setup)
     login.input_username('standard_user')
     login.input_password('secret_sauce')
     login.click_button_login()
     inventory.check_url('https://www.saucedemo.com/inventory.html')
     inventory.check_label()

negative_case = [
    ('','','Epic sadface: Username is required'),
    ('', 'secret_sauce','Epic sadface: Username is required'),
    ('standard_user', '','Epic sadface: Password is required'),
    ('standard_use', 'secret_sauce','Epic sadface: Username and password do not match any user in this service'),
    ('standard_user','secret_sauc','Epic sadface: Username and password do not match any user in this service'),
    ('locked_out_user', 'secret_sauce','Epic sadface: Sorry, this user has been locked out.')
]

@allure.title('Login dengan username dan password salah')
@allure.description('Test Login dengan data tidak valid')
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.parametrize('username,password, error_message',negative_case)
def test_login_negative(setup,username,password, error_message):
    login = Login(setup)
    login.input_username(username)
    login.input_password(password)
    login.click_button_login()
    login.error_message(error_message)