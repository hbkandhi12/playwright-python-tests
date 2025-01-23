from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from conftest import base_url
from config import LANDING_URL
from playwright.async_api import async_playwright
import allure
import pytest


class TestLogin:
    @allure.feature("Login and add item to cart")
    @pytest.mark.asyncio
    async def test_login(self, login_page, inventory_page, base_url) -> None:
        await login_page.navigate(base_url)
        await login_page.login('standard_user', 'secret_sauce')
        print(f" inventory_page: {inventory_page}")
        print(f" inventory_page URL: {await inventory_page.page_url()}")
        assert await inventory_page.page_url() == LANDING_URL
        await inventory_page.click_item('Sauce Labs Bike Light')
