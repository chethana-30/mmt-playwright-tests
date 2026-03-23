class TestHotelsTab:
    """
    Given I am on the MakeMyTrip homepage
    When I click on the Hotels tab
    Then the Hotels tab should be active/selected
    And the Hotels search form should be visible
    And no other tab's form should be visible
    """

    def test_tab_url_is_correct(self, hotels_page):
        hotels_page.open()
        assert hotels_page.is_url_correct(), \
            f"Expected 'hotels' in URL, got: {hotels_page.get_current_url()}"

    def test_tab_is_active(self, hotels_page):
        hotels_page.open()
        assert hotels_page.is_active(), \
            "Hotels tab anchor does not have the active CSS class"

    def test_search_form_is_visible(self, hotels_page):
        hotels_page.open()
        assert hotels_page.is_search_form_visible(), \
            "Hotels search form is not visible after clicking the tab"

    def test_no_other_tab_form_is_visible(self, hotels_page, flights_page):
        hotels_page.open()
        assert not flights_page.get_autosuggest_container().is_visible(), \
            "Flights form visible while Hotels tab is active"