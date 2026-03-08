import logging
import pytest
from utils.client_api import APIClient

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)

@pytest.fixture()
def client():
    return APIClient()