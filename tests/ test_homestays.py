class TestHomestaysTab:
    def test_tab_url_is_correct(self, corporate_page):
        corporate_page.open()
        assert corporate_page.is_url_correct(), \
            f"Expected 'homestays' in URL, got: {corporate_page.get_current_url()}"

    def test_tab_is_active(self, corporate_page):
        corporate_page.open()
        assert corporate_page.is_active(), \
            "Homestays tab is not marked as active"

    def test_search_form_is_visible(self, corporate_page):
        corporate_page.open()
        assert corporate_page.is_search_form_visible(), \
            "Homestays search form is not visible"

    def test_no_other_tab_form_is_visible(self, corporate_page, flights_page):
        corporate_page.open()
        assert not flights_page.is_search_form_visible(), \
            "Flights form visible while Homestays tab is active"