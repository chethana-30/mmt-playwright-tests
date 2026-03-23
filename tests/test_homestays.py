class TestHomestaysTab:
    def test_tab_url_is_correct(self, homestays_page):
        homestays_page.open()
        assert homestays_page.is_url_correct(), \
            f"Expected 'homestays' in URL, got: {homestays_page.get_current_url()}"

    def test_tab_is_active(self, homestays_page):
        homestays_page.open()
        assert homestays_page.is_active(), \
            "Homestays tab is not marked as active"

    def test_search_form_is_visible(self, homestays_page):
        homestays_page.open()
        assert homestays_page.is_search_form_visible(), \
            "Homestays search form is not visible"

    def test_no_other_tab_form_is_visible(self, homestays_page, flights_page):
        homestays_page.open()
        assert not flights_page.get_autosuggest_container().is_visible(), \
             "Flights form visible while Homestays tab is active"