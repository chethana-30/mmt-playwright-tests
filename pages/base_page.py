# # from playwright.sync_api import BrowserContext, Page

# # BASE_URL = "https://www.makemytrip.com"


# # class BasePage:
# #     def __init__(self, context: BrowserContext, page: Page = None):
# #         self.context = context
# #         self.base_url = BASE_URL
# #         if page:
# #             self.page = page
# #         elif context.pages:
# #             self.page = context.pages[0]
# #         else:
# #             self.page = context.new_page()

# #     # SHARED NAVIGATION

# #     def _navigate_to_home(self) -> None:
# #         """Navigate to homepage and dismiss any popup."""
# #         self.page.goto(self.base_url, wait_until="domcontentloaded", timeout=60000)
# #         self.page.wait_for_timeout(2000)
# #         self._close_login_popup()

# #     def _close_login_popup(self) -> None:
# #         """Gracefully dismiss the login modal if it appears."""
# #         try:
# #             close_btn = self.page.locator(
# #                 '//div[contains(@class,"modalContainer")]//span[contains(@class,"close")]'
# #             )
# #             close_btn.wait_for(state="visible", timeout=5000)
# #             close_btn.click()
# #             self.page.wait_for_timeout(500)
# #         except Exception:
# #             pass

    
# #     # SHARED STATE


# #     def get_current_url(self) -> str:
# #         return self.page.url


# from playwright.sync_api import BrowserContext, Page
# from playwright_stealth import stealth_sync

# BASE_URL = "https://www.makemytrip.com"


# class BasePage:
#     def __init__(self, context: BrowserContext, page: Page = None):
#         self.context = context
#         self.base_url = BASE_URL
#         if page:
#             self.page = page
#         elif context.pages:
#             self.page = context.pages[0]
#         else:
#             self.page = context.new_page()

#         # Apply stealth on every page to suppress bot detection signals
#         stealth_sync(self.page)

#     def _navigate_to_home(self) -> None:
#         """Navigate to homepage and dismiss any popup."""
#         self.page.goto(self.base_url, wait_until="domcontentloaded", timeout=60000)
#         self.page.wait_for_timeout(3000)  # give JS time to render the modal
#         self._close_login_popup()

#     def _close_login_popup(self) -> None:
#         """Gracefully dismiss the login modal if it appears."""
#         # Try multiple known selectors for the close button
#         close_selectors = [
#             '//span[contains(@class,"commonModal__close")]',
#             '//div[contains(@class,"loginModal")]//span[contains(@class,"close")]',
#             '//div[contains(@class,"modalContainer")]//span[contains(@class,"close")]',
#             '[data-cy="closeModal"]',
#             '.modal-close',
#             'span.close',
#         ]
#         for selector in close_selectors:
#             try:
#                 btn = self.page.locator(selector).first
#                 if btn.is_visible(timeout=2000):
#                     btn.click()
#                     self.page.wait_for_timeout(500)
#                     return
#             except Exception:
#                 continue

#     def get_current_url(self) -> str:
#         return self.page.url

from playwright.sync_api import BrowserContext, Page

BASE_URL = "https://www.makemytrip.com"


class BasePage:
    def __init__(self, context: BrowserContext, page: Page = None):
        self.context = context
        self.base_url = BASE_URL
        if page:
            self.page = page
        elif context.pages:
            self.page = context.pages[0]
        else:
            self.page = context.new_page()

    def _navigate_to_home(self) -> None:
        self.page.goto(self.base_url, wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_timeout(3000)
        self._close_login_popup()

    def _close_login_popup(self) -> None:
        """Try multiple selectors to close the login modal."""
        close_selectors = [
            'span.commonModal__close',
            '[data-cy="closeModal"]',
            '//span[contains(@class,"commonModal__close")]',
            '//div[contains(@class,"loginModal")]//span[contains(@class,"close")]',
            '//div[contains(@class,"modalContainer")]//span[contains(@class,"close")]',
            'button[aria-label="close"]',
            '.modal-close',
        ]
        for selector in close_selectors:
            try:
                btn = self.page.locator(selector).first
                if btn.is_visible(timeout=2000):
                    btn.click()
                    self.page.wait_for_timeout(1000)
                    print(f"[INFO] Closed popup using: {selector}")
                    return
            except Exception:
                continue
        print("[INFO] No login popup found, continuing...")

    def get_current_url(self) -> str:
        return self.page.url