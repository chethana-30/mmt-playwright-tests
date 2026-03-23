# from playwright.sync_api import BrowserContext
# from pages.base_page import BasePage


# class BusPage(BasePage):
#     """Page Object for the Bus tab on MakeMyTrip homepage."""

#     def __init__(self, context: BrowserContext):
#         super().__init__(context)

#     # -------------------------------------------------------------------------
#     # LOCATORS
#     # -------------------------------------------------------------------------

#     def get_bus_tab(self):
#         return self.page.locator('//li[@data-cy="menu_Buses"]')

#     def get_bus_tab_active_anchor(self):
#         return self.page.locator('//li[@data-cy="menu_Buses"]//a[contains(@class,"active")]')

#     def get_bus_tab_active_icon(self):
#         return self.page.locator('//span[contains(@class,"chBuses") and contains(@class,"active")]')

#     def get_bus_search_form(self):
#         return self.page.locator('//input[@class="react-autosuggest__input react-autosuggest__input--open"]')

#     # -------------------------------------------------------------------------
#     # ACTIONS
#     # -------------------------------------------------------------------------

#     def navigate_to_home(self) -> None:
#         self.navigate()

#     def click_bus_tab(self) -> None:
#         self.get_bus_tab().click()
#         self.page.wait_for_timeout(1000)

#     # -------------------------------------------------------------------------
#     # STATE CHECKS
#     # -------------------------------------------------------------------------

#     def is_bus_tab_visible(self) -> bool:
#         return self.get_bus_tab().is_visible()

#     def is_bus_tab_active_by_anchor_class(self) -> bool:
#         return self.get_bus_tab_active_anchor().count() > 0

#     def is_bus_tab_active_by_icon_class(self) -> bool:
#         return self.get_bus_tab_active_icon().count() > 0

#     def is_bus_search_form_visible(self) -> bool:
#         return self.get_bus_search_form().is_visible()


from playwright.sync_api import BrowserContext
from pages.base_page import BasePage


class BusPage(BasePage):
    """Page Object for the Bus tab on MakeMyTrip homepage."""

    TAB_CY = "menu_Buses"
    URL_KEYWORD = "bus-tickets"

    def __init__(self, context: BrowserContext):
        super().__init__(context)

   
    # LOCATORS


    def get_tab(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]')

    def get_tab_active_anchor(self):
        return self.page.locator(f'//li[@data-cy="{self.TAB_CY}"]//a[contains(@class,"active")]')

    def get_tab_active_icon(self):
        return self.page.locator('//span[contains(@class,"chBuses") and contains(@class,"active")]')

    def get_search_form(self):
        return self.page.locator('//label[@for="fromCity"]//span[@class="appendBottom5 textStyle"]')
    def get_autosuggest_container(self):
        return self.page.locator('//div[@class="react-autosuggest__container react-autosuggest__container--open"]')

    # ACTIONS


    def open(self) -> None:
        """Navigate to homepage and click the Bus tab."""
        self._navigate_to_home()
        self.get_tab().click()
        self.page.wait_for_timeout(1000)

    # Keep old methods for backward compatibility with existing TestBusTab tests
    def navigate_to_home(self) -> None:
        self._navigate_to_home()

    def click_bus_tab(self) -> None:
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
    

    # Keep old methods for backward compatibility with existing TestBusTab tests
    def is_bus_tab_visible(self) -> bool:
        return self.get_tab().is_visible()

    def is_bus_tab_active_by_anchor_class(self) -> bool:
        return self.get_tab_active_anchor().count() > 0

    def is_bus_tab_active_by_icon_class(self) -> bool:
        return self.get_tab_active_icon().count() > 0

    def is_bus_search_form_visible(self) -> bool:
        return self.get_search_form().is_visible()