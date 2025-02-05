from playwright.async_api import Page, Locator
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.inv_item_name: Locator = self.page.locator('.inventory_item_name')
        self.inv_item_price: Locator = self.page.locator('.inventory_item_price')
        self.inv_item_description: Locator = self.page.locator('.inventory_item_desc')
        self.remove_item_cart_btn: Locator = self.page.locator('.cart_button')
        self.checkout_btn: Locator = self.page.locator('.checkout_button')


    async def page_url(self):
         return self.page.url

