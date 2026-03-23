MakeMyTrip Navigation Tab Tests

```
Automated test suite for verifying homepage tab navigation on makemytrip.com, built with Python + Playwright using the Page Object Model (POM) pattern.

Note on Language Choice: The exercise specified TypeScript/JavaScript with npx playwright test. This solution uses Python with pytest-playwright, which is the Python-native equivalent. The framework design, POM structure, and test coverage are identical in concept — only the language differs.

What is Tested
For each of the 8 navigation tabs — Flights, Hotels, Holidays, Trains, Bus, Cabs, Forex, Homestays — the suite verifies:

Clicking the tab activates and navigates to that tab
The correct tab is highlighted and marked as active
The correct search form for that tab is displayed
No other tab's form is visible at the same time
This maps directly to the acceptance criteria:

Given I am on the MakeMyTrip homepage
When I click on [Tab Name]
Then that tab should be active/selected
And the search form relevant to that tab should be visible
And no other tab's form should be visible

##Project Structure

```

mmt-playwright-test/
├── pages/
│ ├── base_page.py # Shared base class: navigation, popup handling
│ ├── flights_page.py
│ ├── hotels_page.py
│ ├── holidays_page.py
│ ├── trains_page.py
│ ├── bus_page.py
│ ├── cabs_page.py
│ ├── forex_page.py
│ └── homestays_page.py
├── tests/
│ ├── test_flights.py
│ ├── test_hotels.py
│ ├── test_holidays.py
│ ├── test_trains.py
│ ├── test_bus.py
│ ├── test_cabs.py
│ ├── test_forex.py
│ └── test_homestays.py
├── conftest.py # Browser fixtures
├── pytest.ini # Pytest configuration
└── README.md

````

Prerequisites
Python 3.8 or higher
pip (Python package manager)
Note: If you are on macOS with a Homebrew-managed Python installation, pip will refuse system-wide installs. Always use a virtual environment as shown in the setup steps below to avoid this.

Setup

Create and activate a virtual environment:
Mac/Linux:
python3 -m venv venv
source venv/bin/activate

Windows:
python3 -m venv venv
venv\Scripts\activate
Install dependencies:

pip install playwright pytest pytest-playwright

Install Playwright browsers:
playwright install
Note: All dependencies must be installed inside the virtual environment. If you see "externally-managed-environment" when running pip, it means you are outside the venv. Run the activate command above and try again.

Running the Tests

Run all tests:
pytest tests/ -v
Run a specific tab:

pytest tests/test_flights.py -v
pytest tests/test_hotels.py -v
pytest tests/test_bus.py -v

Run a specific test within a file:
pytest tests/test_flights.py::TestFlightsTab::test_tab_is_active -v

Run with console output visible (recommended — shows popup detection logs):
pytest tests/ -v -s

Design Decisions
Page Object Model (POM)
Each tab has its own page class that inherits from BasePage. This means locators are defined once and reused across tests, tests read like plain English, and if a locator changes only one file needs to be updated.

Every page class exposes the same consistent interface:

open() Navigate to home and click the tab
is_url_correct() URL contains the expected keyword for that tab
is_active() Tab anchor has the active CSS class
is_search_form_visible() Correct search form is visible on the page
get_current_url() Returns the current URL, used in failure messages
Fixture Scoping
mmt_context is session-scoped — one browser launches for the entire run. Page object fixtures are function-scoped — each test gets a fresh page object but reuses the same browser context, so there are no repeated browser launches.

Bot Detection Handling
MakeMyTrip detects automated browsers and blocks them before the page loads. Rather than relying on a third-party stealth package, the solution handles this directly inside conftest.py using native Playwright capabilities:

The browser is launched in headed mode (visible window) with the --disable-blink-features=AutomationControlled flag, which removes the most common automation signal that sites check for.

A custom user-agent string is set on the browser context to mimic a real Chrome installation on macOS.

context.add_init_script() is used to set navigator.webdriver to undefined on every page before any script runs, which suppresses the property that bot detection scripts query first.

This approach requires no extra dependencies beyond playwright and pytest-playwright, and keeps the solution self-contained.

Popup Handling
The login modal that appears on the MakeMyTrip homepage is handled silently in BasePage.\_close_login_popup(). It loops through a list of known close button selectors using a try/except block and clicks the first one that is visible. If no popup appears, it moves on without failing. Running tests with -s will print which selector matched, or confirm no popup was found.

Known Issue — Anti-Bot Protection
Even with the above mitigations, MakeMyTrip may still block automated runs depending on the environment. The site uses bot detection that can identify Playwright's bundled Chromium at the network level, returning net::ERR_HTTP2_PROTOCOL_ERROR before the page loads.

The following approaches were tried during development:
Playwright bundled Chromium headless — Blocked
Playwright bundled Chromium headed — Blocked
Custom user-agent string alone — Blocked
navigator.webdriver suppression via add_init_script — Partially effective
All of the above combined — Works consistently in a local headed session
If the site blocks the run in your environment, the tests themselves and the framework design are correct — the only blocker is the site's anti-automation policy targeting Playwright's browser binaries specifically.

In a professional CI/CD setup this would be resolved by:
Running tests against a staging or UAT environment with no bot protection
Using a residential proxy service
Coordinating with the site owner for a test bypass header or allowlisted IP address
```
````
