# import pytest
# from playwright.sync_api import BrowserType
# from pages.bus_page import BusPage
# from pages.flights_page import FlightsPage
# from pages.hotels_page import HotelsPage
# from pages.holidays_page import HolidaysPage
# from pages.trains_page import TrainsPage
# from pages.cabs_page import CabsPage
# from pages.forex_page import ForexPage
# from pages.homestays_page import HomeStayPage

# @pytest.fixture(scope="session")
# def mmt_context(playwright):
#     browser = playwright.chromium.launch(
#         headless=False,  # headed mode helps bypass bot detection
#         args=[
#             "--disable-blink-features=AutomationControlled",
#             "--no-sandbox",
#         ]
#     )
#     context = browser.new_context(
#         user_agent=(
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
#             "AppleWebKit/537.36 (KHTML, like Gecko) "
#             "Chrome/124.0.0.0 Safari/537.36"
#         ),
#         viewport={"width": 1280, "height": 800},
#         locale="en-IN",
#     )
#     yield context
#     context.close()
#     browser.close()

# @pytest.fixture
# def flights_page(mmt_context):
#     return FlightsPage(mmt_context)

# @pytest.fixture
# def hotels_page(mmt_context):
#     return HotelsPage(mmt_context)

# @pytest.fixture
# def holidays_page(mmt_context):
#     return HolidaysPage(mmt_context)

# @pytest.fixture
# def trains_page(mmt_context):
#     return TrainsPage(mmt_context)

# @pytest.fixture
# def bus_page(mmt_context):
#     return BusPage(mmt_context)

# @pytest.fixture
# def cabs_page(mmt_context):
#     return CabsPage(mmt_context)

# @pytest.fixture
# def forex_page(mmt_context):
#     return ForexPage(mmt_context)

# @pytest.fixture
# def homestays_page(mmt_context):
#     return HomeStayPage(mmt_context)


import pytest

from pages.bus_page import BusPage
from pages.flights_page import FlightsPage
from pages.hotels_page import HotelsPage
from pages.holidays_page import HolidaysPage
from pages.trains_page import TrainsPage
from pages.cabs_page import CabsPage
from pages.forex_page import ForexPage
from pages.homestays_page import HomeStayPage



@pytest.fixture(scope="session")
def mmt_context(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars",
            "--disable-dev-shm-usage",
        ]
    )
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
        locale="en-IN",
    )
    # Suppress navigator.webdriver without any extra package
    context.add_init_script(
        "Object.defineProperty(navigator, 'webdriver', { get: () => undefined });"
    )
    yield context
    context.close()
    browser.close()


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

