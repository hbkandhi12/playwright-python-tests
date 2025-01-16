from playwright.sync_api import Page,sync_playwright

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.username_input: Locator = self.page.locator("#user-name")
        self.password_input: Locator = self.page.locator("#password")
        self.login_btn: Locator = self.page.locator("#login-button")

    def login(self, username: str, password: str)-> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()





