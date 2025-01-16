from pages.base_page import BasePage
from playwright.sync_api import Page,sync_playwright


class InventoryPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

    def page_url(self,):
        return self.page.url
