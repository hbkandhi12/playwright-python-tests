from pages.base_page import BasePage
from playwright.async_api import Page, async_playwright


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.items_name_list = self.page.locator('.inventory_item_name ')
        self.add_items_cart_list = self.page.locator("[id *= 'add-to-cart']")
        self.shopping_cart_link = self.page.locator('.shopping_cart_link')
        self.shopping_cart_badge = self.page.locator('.shopping_cart_badge')
        self.remove_items_cart = self.page.locator("[id*='remove']")

    async def page_url(self):
        return self.page.url

    async def click_item(self, item_name: str):
        count = 0;
        items_count = await self.items_name_list.count()
        for i in range(items_count):
            item = self.items_name_list.nth(i)
            text = await item.inner_text()
            if item_name in text:
                add_to_cart_button = self.add_items_cart_list.nth(i)
                if add_to_cart_button.is_visible():
                    await add_to_cart_button.click()
                    count += 1
                    break
                else:
                    print(f"Item '{item_name}' found but button is not clickable.")
                    return
        # Assert that the cart now has one item
        cart_badge_text = await self.shopping_cart_badge.text_content()
        assert cart_badge_text == count, f"Expected cart to have {count} item/items, but found {cart_badge_text}."

    async def click_shopping_cart(self):
        await self.shopping_cart_link.click()