import os

from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/login.feature")

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")


@given("the login page is open")
def open_login(page, state):
    page.goto(BASE_URL)
    state["page"] = page


@when(parsers.parse('I log in as "{username}" with password "{password}"'))
def do_login(state, username, password):
    page = state["page"]
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")


@then("I should see the products page")
def see_products(state):
    page = state["page"]
    assert page.inner_text(".title") == "Products"


@then(parsers.parse('I should see an error containing "{text}"'))
def see_error(state, text):
    page = state["page"]
    assert text.lower() in page.inner_text("[data-test='error']").lower()
