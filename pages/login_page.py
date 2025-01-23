from playwright.async_api import Page, Locator

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.username_input: Locator = self.page.locator('#user-name')
        self.password_input: Locator = self.page.locator('#password')
        self.login_btn: Locator = self.page.locator('#login-button')

    async def login(self, username: str, password: str) -> None:
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_btn.click()
