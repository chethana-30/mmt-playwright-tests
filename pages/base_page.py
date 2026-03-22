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

    # SHARED NAVIGATION

    def _navigate_to_home(self) -> None:
        """Navigate to homepage and dismiss any popup."""
        self.page.goto(self.base_url, wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_timeout(2000)
        self._close_login_popup()

    def _close_login_popup(self) -> None:
        """Gracefully dismiss the login modal if it appears."""
        try:
            close_btn = self.page.locator(
                '//div[contains(@class,"modalContainer")]//span[contains(@class,"close")]'
            )
            close_btn.wait_for(state="visible", timeout=5000)
            close_btn.click()
            self.page.wait_for_timeout(500)
        except Exception:
            pass

    
    # SHARED STATE


    def get_current_url(self) -> str:
        return self.page.url