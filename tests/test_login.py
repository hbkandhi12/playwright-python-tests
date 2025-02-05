from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from conftest import base_url
from config import INVENTORY_PAGE_URL, CART_PAGE_URL, CHECKOUT_PAGE_URL
from playwright.async_api import async_playwright
import allure
import pytest


class TestLogin:
    @allure.feature("Login and add item to cart")
    @pytest.mark.asyncio
    async def test_login(self, login_page, inventory_page, cart_page, base_url) -> None:
        await login_page.navigate(base_url)
        await login_page.login('standard_user', 'secret_sauce')
        print(f" inventory_page: {inventory_page}")
        print(f" inventory_page URL: {await inventory_page.page_url()}")
        assert await inventory_page.page_url() == INVENTORY_PAGE_URL , f"URL Mismatch: Expected url was {INVENTORY_PAGE_URL} but instaed found {inventory_page.page_url()}"
        await inventory_page.click_item('Sauce Labs Bike Light')
        # navigate to cart page
        await click_shopping_cart()
        assert await cart_page.page_url() == CART_PAGE_URL,f"URL Mismatch: Expected url was {CART_PAGE_URL} but instead found {cart_page.page_url()}"
