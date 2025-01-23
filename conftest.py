import pytest
from playwright.async_api import async_playwright, Page
from config import BASE_URL, BROWSER_HEADLESS

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from playwright.async_api import async_playwright, Page
from contextlib import asynccontextmanager



@pytest.fixture(scope="session")
async def base_url():
    return BASE_URL

@asynccontextmanager
@pytest.fixture(scope='function')
async def chromium_page():
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await page.close()
        await context.close()
        await browser.close()
        await playwright.stop()


# @pytest.fixture(scope="function")
# async def chromium_page() -> Page:
#     async with get_chromium_page() as page:
#         yield page


@pytest.fixture(scope="function")
async def login_page(chromium_page: Page) -> LoginPage:
    print(f"DEBUG: chromium_page type: {type(chromium_page)}")
    return LoginPage(chromium_page)


@pytest.fixture(scope="function")
async def inventory_page(chromium_page: Page) -> InventoryPage:
    return InventoryPage(chromium_page)
