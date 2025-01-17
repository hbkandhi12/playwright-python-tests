from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from conftest import base_url
from config import LANDING_URL


class TestLogin:
    def test_login(self, login_page: LoginPage,inventory_page: InventoryPage,base_url)-> None:
        login_page.navigate(base_url)
        login_page.login('standard_user','secret_sauce')
        assert inventory_page.page_url() == LANDING_URL
        inventory_page.click_item('Sauce Labs Bike Light')