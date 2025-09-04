from playwright.sync_api import sync_playwright

import pytest
import allure

@pytest.fixture()
def setup():
    with sync_playwright() as n:
        with allure.step('Buka Browser'):
            browser = n.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
        # page.wait_for_timeout(10000) #timeout 10 detik (tergantung websitenya)
        with allure.step('Open URL'):
            page.goto('https://saucedemo.com')
        yield page
        with allure.step('Close Browser'):
            context.close()
            browser.close()