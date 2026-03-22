from playwright.sync_api import BrowserContext
from pages.base_page import BasePage


class CabsPage(BasePage):
    """Page Object for the Cabs tab on MakeMyTrip homepage."""

    TAB_CY = "menu_Cabs"
    URL_KEYWORD = "cab"

    def __init__(self, context: BrowserContext):
        super().__init__(context)

   
    # LOCATORS
 

    def get_tab(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]')

    def get_tab_active_anchor(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]//a[contains(@class,"active")]')

    def get_search_form(self):
        return self.page.locator('//input[@class="react-autosuggest__input react-autosuggest__input--open"]')


    # ACTIONS
 

    def open(self) -> None:
        """Navigate to homepage and click the Cabs tab."""
        self._navigate_to_home()
        self.get_tab().click()
        self.page.wait_for_timeout(1000)

   
    # STATE CHECKS


    def is_url_correct(self) -> bool:
        return self.URL_KEYWORD in self.page.url

    def is_active(self) -> bool:
        return self.get_tab_active_anchor().count() > 0

    def is_search_form_visible(self) -> bool:
        return self.get_search_form().is_visible()