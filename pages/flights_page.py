from playwright.sync_api import BrowserContext
from pages.base_page import BasePage


class FlightsPage(BasePage):
    """Page Object for the Flights tab on MakeMyTrip homepage."""

    TAB_CY = "menu_Flights"
    URL_KEYWORD = "flights"

    def __init__(self, context: BrowserContext):
        super().__init__(context)


    # LOCATORS
   

    def get_tab(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]')

    def get_tab_active_anchor(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]//a[contains(@class,"active")]')

    def get_search_form(self):
        return self.page.locator('//label[@for="fromCity"]//span[@class="lbl_input appendBottom10"]')

    def get_autosuggest_container(self):
        return self.page.locator('//div[@class="react-autosuggest__container react-autosuggest__container--open"]')


    # ACTIONS


    def open(self) -> None:
        """Navigate to homepage and click the Flights tab."""
        self._navigate_to_home()
        self.get_tab().click()
        self.page.wait_for_timeout(1000)

    def dismiss_overlays(self):
        """Close GST tooltip and chatbot widget if they appear."""
    
    # Close the GST tooltip if visible
        gst_close = self.page.locator('//div[contains(@class,"gstToolTip")]//button')
        if gst_close.is_visible():
            gst_close.click()
            self.page.wait_for_timeout(300)

   
    # STATE CHECKS
    

    def is_url_correct(self) -> bool:
        return self.URL_KEYWORD in self.page.url

    def is_active(self) -> bool:
        return self.get_tab_active_anchor().count() > 0

    # def is_search_form_visible(self) -> bool:
    #     """Click the fromCity field and check if the autosuggest dropdown opens."""
    #     self.get_search_form().click()
    #     self.page.wait_for_timeout(500)
    #     return self.get_autosuggest_container().is_visible()

    def is_search_form_visible(self) -> bool:
        self.dismiss_overlays()
        self.get_search_form().click()
        self.page.wait_for_timeout(500)
        return self.get_autosuggest_container().is_visible()