import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.conftest import base_url
from playwright.sync_api import Page,sync_playwright


class TestLogin:
    def test_login(self, login_page: LoginPage,inventory_page: InventoryPage,base_url)-> None:
        login_page.navigate(base_url)
        login_page.login('standard_user','secret_sauce')
        assert inventory_page.page_url() == "https://www.saucedemo.com/inventory.html"
        print('loggimg..')