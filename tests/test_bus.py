class TestBusTab:
    def test_tab_url_is_correct(self, bus_page):
        bus_page.open()
        assert bus_page.is_url_correct(), \
            f"Expected 'bus-tickets' in URL, got: {bus_page.get_current_url()}"

    def test_tab_is_active(self, bus_page):
        bus_page.open()
        assert bus_page.is_active(), \
            "Bus tab is not marked as active"

    def test_search_form_is_visible(self, bus_page):
        bus_page.open()
        assert bus_page.is_search_form_visible(), \
            "Bus search form is not visible"

    def test_no_other_tab_form_is_visible(self, bus_page, flights_page):
        bus_page.open()
        assert not flights_page.is_search_form_visible(), \
            "Flights form visible while Bus tab is active"