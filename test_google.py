import pytest
from selene import browser, be, have


@pytest.fixture
def settings():
    browser.driver.set_window_size(500, 500)


def test_selene(settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))