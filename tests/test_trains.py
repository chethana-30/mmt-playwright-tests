class TestTrainsTab:
    def test_tab_url_is_correct(self, trains_page):
        trains_page.open()
        assert trains_page.is_url_correct(), \
            f"Expected 'trains' in URL, got: {trains_page.get_current_url()}"

    def test_tab_is_active(self, trains_page):
        trains_page.open()
        assert trains_page.is_active(), \
            "Trains tab is not marked as active"

    def test_search_form_is_visible(self, trains_page):
        trains_page.open()
        assert trains_page.is_search_form_visible(), \
            "Trains search form is not visible"

    def test_no_other_tab_form_is_visible(self, trains_page, flights_page):
        trains_page.open()
        assert not flights_page.get_autosuggest_container().is_visible(), \
            "Flights form visible while Trains tab is active"