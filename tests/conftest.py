import pytest
from playwright.sync_api import Page, sync_playwright

from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        context = chromium.new_context()
        page = context.new_page()
        yield page
        page.close()

@pytest.fixture(scope='function')
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)




