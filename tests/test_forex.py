class TestForexTab:
    def test_tab_url_is_correct(self, forex_page):
        forex_page.open()
        assert forex_page.is_url_correct(), \
            f"Expected 'forex' in URL, got: {forex_page.get_current_url()}"

    def test_tab_is_active(self, forex_page):
        forex_page.open()
        assert forex_page.is_active(), \
            "Forex tab is not marked as active"

    def test_search_form_is_visible(self, forex_page):
        forex_page.open()
        assert forex_page.is_search_form_visible(), \
            "Forex search form is not visible"

    def test_no_other_tab_form_is_visible(self, forex_page, flights_page):
        forex_page.open()
        assert not flights_page.is_search_form_visible(), \
            "Flights form visible while Forex tab is active"