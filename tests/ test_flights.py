class TestFlightsTab:
    """
    Given I am on the MakeMyTrip homepage
    When I click on the Flights tab
    Then the Flights tab should be active/selected
    And the Flights search form should be visible
    And no other tab's form should be visible
    """

    def test_tab_url_is_correct(self, flights_page):
        """Clicking the tab navigates to the correct URL."""
        flights_page.open()
        assert flights_page.is_url_correct(), \
            f"Expected 'flights' in URL, got: {flights_page.get_current_url()}"

    def test_tab_is_active(self, flights_page):
        """The correct tab is highlighted/active."""
        flights_page.open()
        assert flights_page.is_active(), \
            "Flights tab anchor does not have the active CSS class"

    def test_search_form_is_visible(self, flights_page):
        """The correct search form for this tab is displayed."""
        flights_page.open()
        assert flights_page.is_search_form_visible(), \
            "Flights search form is not visible after clicking the tab"

    def test_no_other_tab_form_is_visible(self, flights_page, hotels_page):
        """No other tab's content is shown at the same time."""
        flights_page.open()
        # Hotels form should NOT be visible when Flights tab is active
        assert not hotels_page.is_search_form_visible(), \
            "Hotels search form is visible while Flights tab is active — unexpected overlap"