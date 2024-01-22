import pytest
import requests
from http import HTTPStatus
from pytest_metadata.plugin import metadata_key

from param import API_TOKEN



def pytest_configure(config):
    config._metadata['URL'] = os.environ['url']


def test_main():
    assert True


@pytest.mark.parametrize("city", [["Poitiers",True], ["Paris",True],["Blargoug",False]])
def test_main_2(city):
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q="+city[0]+",fr&appid="
        + API_TOKEN
    )
    if city[1]:
        assert response.status_code == HTTPStatus.OK, "Return should be OK"
    else:
        assert response.status_code == HTTPStatus.NOT_FOUND, "Return should be not found"
