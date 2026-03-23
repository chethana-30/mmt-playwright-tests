class TestHolidaysTab:
    def test_tab_url_is_correct(self, holidays_page):
        holidays_page.open()
        assert holidays_page.is_url_correct(), \
            f"Expected 'holidays' in URL, got: {holidays_page.get_current_url()}"

    def test_tab_is_active(self, holidays_page):
        holidays_page.open()
        assert holidays_page.is_active(), \
            "Holidays tab is not marked as active"

    def test_search_form_is_visible(self, holidays_page):
        holidays_page.open()
        assert holidays_page.is_search_form_visible(), \
            "Holidays search form is not visible"

    def test_no_other_tab_form_is_visible(self, holidays_page, flights_page):
        holidays_page.open()
        assert not flights_page.get_autosuggest_container().is_visible(), \
             "Flights form visible while Holidays tab is active"