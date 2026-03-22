# conftest.py

import pytest

from pages.bus_page import BusPage
from pages.flights_page import FlightsPage
from pages.hotels_page import HotelsPage
from pages.holidays_page import HolidaysPage
from pages.trains_page import TrainsPage
from pages.cabs_page import CabsPage
from pages.forex_page import ForexPage
from pages.homestays_page import HomeStayPage  # class lives in homestays_page.py


# ============================================================================
#  SESSION FIXTURE
#  One browser context shared across all tests.
#  pytest-playwright provides the `browser` fixture automatically —
#  no need to call sync_playwright() manually anywhere.
# ============================================================================

@pytest.fixture(scope="session")
def mmt_context(browser):
    context = browser.new_context()
    yield context
    context.close()


# ============================================================================
#  PAGE OBJECT FIXTURES
#  Function-scoped (default) — each test gets a fresh page object
#  but reuses the same browser context, so no repeated browser launches.
# ============================================================================

@pytest.fixture
def flights_page(mmt_context):
    return FlightsPage(mmt_context)


@pytest.fixture
def hotels_page(mmt_context):
    return HotelsPage(mmt_context)


@pytest.fixture
def holidays_page(mmt_context):
    return HolidaysPage(mmt_context)


@pytest.fixture
def trains_page(mmt_context):
    return TrainsPage(mmt_context)


@pytest.fixture
def bus_page(mmt_context):
    return BusPage(mmt_context)


@pytest.fixture
def cabs_page(mmt_context):
    return CabsPage(mmt_context)


@pytest.fixture
def forex_page(mmt_context):
    return ForexPage(mmt_context)


@pytest.fixture
def homestays_page(mmt_context):
    return HomeStayPage(mmt_context)