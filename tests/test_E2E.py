from pages.login import Login
from pages.inventory import Inventory
from pages.cart import Cart
from pages.checkout import Checkout

import allure

@allure.title('Menambahkan Produk ke dalam Keranjang')
@allure.description('Menambahkan produk ke dalam keranjang')
@allure.severity(allure.severity_level.MINOR)
def test_add_cart(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_button_login()
    inventory.add_product()
    inventory.check_product()
    

@allure.title('Menambahkan > 1 Produk ke dalam Keranjang')
@allure.description('Menambahkan lebih dari 1 produk ke dalam keranjang')
@allure.severity(allure.severity_level.MINOR)
def test_add2_cart(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_button_login()
    inventory.add_product()
    inventory.add_product2()
    inventory.check_product2()

@allure.title('Menghapus produk di dalam keranjang')
@allure.description('Hapus produk di dalam keranjang')
@allure.severity(allure.severity_level.NORMAL)
def test_remove_cart(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    cart = Cart(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_button_login()
    inventory.add_product()
    inventory.check_product()
    inventory.cart_page()
    cart.remove_product()
    cart.recheck_page()

@allure.title('Melakukan Checkout Produk')
@allure.description('Melanjutkan proses checkout barang')
@allure.severity(allure.severity_level.MINOR)
def test_checkout(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_button_login()
    inventory.add_product()
    inventory.check_product()
    inventory.cart_page()
    cart.checkout_product()
    checkout.form_information('https://www.saucedemo.com/checkout-step-one.html')

@allure.title('Mengisi Form Data Pengiriman')
@allure.description('Mengisi Data Pengiriman')
@allure.severity(allure.severity_level.MINOR)
def test_fill_form(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_button_login()
    inventory.add_product()
    inventory.check_product()
    inventory.cart_page()
    cart.checkout_product()
    checkout.first_name('Acils')
    checkout.last_name('KC')
    checkout.postal_code('14045')
    checkout.button_checkout()
    checkout.success_checkout('https://www.saucedemo.com/checkout-step-two.html')