class TestCabsTab:
    def test_tab_url_is_correct(self, cabs_page):
        cabs_page.open()
        assert cabs_page.is_url_correct(), \
            f"Expected 'cab' in URL, got: {cabs_page.get_current_url()}"

    def test_tab_is_active(self, cabs_page):
        cabs_page.open()
        assert cabs_page.is_active(), \
            "Cabs tab is not marked as active"

    def test_search_form_is_visible(self, cabs_page):
        cabs_page.open()
        assert cabs_page.is_search_form_visible(), \
            "Cabs search form is not visible"

    def test_no_other_tab_form_is_visible(self, cabs_page, flights_page):
        cabs_page.open()
        assert not flights_page.is_search_form_visible(), \
            "Flights form visible while Cabs tab is active"