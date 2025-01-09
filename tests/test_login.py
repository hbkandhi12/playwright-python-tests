import pytest

from pages.login_page import LoginPage
from tests.conftest import base_url


class TestLogin:
    def test_login(self, login_page: LoginPage, base_url)-> None:
        login_page.navigate(base_url)
        login_page.login('standard_user','secret_sauce')