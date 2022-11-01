import pytest


@pytest.fixture()
def set_up():
    print(" LAUNCH")
    yield
    print(" FINISH")

@pytest.fixture(scope="session")
def set_group():
    print("ENTER SYSTEM")
    yield
    print("EXIT SYSTEM")