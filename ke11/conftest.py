import requests
import pytest
from ke7.a import login

@pytest.fixture(scope="function")
def login_fix():
    s = requests.session()
    login(s)
    return s