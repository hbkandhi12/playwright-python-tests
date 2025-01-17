import pytest
from playwright.sync_api import Page, sync_playwright
from config import BASE_URL,BROWSER_HEADLESS

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=BROWSER_HEADLESS)
        context = chromium.new_context()
        page = context.new_page()
        yield page
        page.close()


@pytest.fixture(scope='function')
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)


@pytest.fixture(scope='function')
def inventory_page(chromium_page: Page) -> InventoryPage:
    return InventoryPage(chromium_page)
