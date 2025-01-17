from pages.base_page import BasePage
from playwright.sync_api import Page,sync_playwright


class InventoryPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.items_name_list = self.page.locator('.inventory_item_name ')
        self.add_items_cart_list = self.page.locator("[id *= 'add-to-cart']")
        self.shopping_cart = self.page.locator('.shopping_cart_link')
        self.shopping_cart_badge = self.page.locator('.shopping_cart_badge')
        self.remove_items_cart = self.page.locator("[id*='remove']")


    def page_url(self,):
        return self.page.url

    def click_item(self, item_name : str):
        items_count = self.items_name_list.count()
        for i in range(items_count):
            item = self.items_name_list.nth(i)
            text = item.inner_text()
            if item_name in text:
                self.add_items_cart_list.nth(i).click()
                break
        assert self.shopping_cart_badge.text_content() == '1'
