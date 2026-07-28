import pytest


@pytest.fixture
def state() -> dict:
    """A per-scenario bag for sharing state between BDD steps."""
    return {}
