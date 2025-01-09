from playwright.sync_api import Page
from requests import Response


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page;


    def navigate(self, url: str) -> Response:
        return self.page.goto(url, wait_until="networkidle")