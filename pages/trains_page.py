from playwright.sync_api import BrowserContext
from pages.base_page import BasePage


class TrainsPage(BasePage):
    """Page Object for the Trains tab on MakeMyTrip homepage."""

    TAB_CY = "menu_Trains"
    URL_KEYWORD = "trains"

    def __init__(self, context: BrowserContext):
        super().__init__(context)

   
    # LOCATORS
  

    def get_tab(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]')

    def get_tab_active_anchor(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]//a[contains(@class,"active")]')

    def get_search_form(self):
        return self.page.locator('//label[@for="fromCity"]//span[@class="appendBottom2"]')
    
    def get_autosuggest_container(self):
        return self.page.locator('//div[@class="react-autosuggest__container react-autosuggest__container--open"]')

  
    # ACTIONS
   

    def open(self) -> None:
        """Navigate to homepage and click the Trains tab."""
        self._navigate_to_home()
        self.get_tab().click()
        self.page.wait_for_timeout(1000)

   
    # STATE CHECKS
  

    def is_url_correct(self) -> bool:
        return self.URL_KEYWORD in self.page.url

    def is_active(self) -> bool:
        return self.get_tab_active_anchor().count() > 0

    def is_search_form_visible(self) -> bool:
        """Click the fromCity field and check if the autosuggest dropdown opens."""
        self.get_search_form().click()
        self.page.wait_for_timeout(500)
        return self.get_autosuggest_container().is_visible()