import os

import requests
from pytest_bdd import scenarios, when, then, parsers

scenarios("../features/users_api.feature")

API_BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@when("I request the list of users")
def request_users(state):
    state["response"] = requests.get(f"{API_BASE}/users", timeout=15)


@when(parsers.parse('I request user "{user_id:d}"'))
def request_user(state, user_id):
    state["response"] = requests.get(f"{API_BASE}/users/{user_id}", timeout=15)


@then(parsers.parse("the response status should be {status:d}"))
def check_status(state, status):
    assert state["response"].status_code == status


@then(parsers.parse("the response should contain {count:d} users"))
def check_count(state, count):
    assert len(state["response"].json()) == count


@then(parsers.parse('the returned user id should be "{user_id:d}"'))
def check_user_id(state, user_id):
    assert state["response"].json()["id"] == user_id
