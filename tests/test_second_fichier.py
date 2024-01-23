import pytest
import requests
from http import HTTPStatus

from param import API_TOKEN





@pytest.mark.parametrize("city", [["Poitiers",True], ["Paris",True],["Blargoug",False]])
def test_report_essai(city):
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q="+city[0]+",fr&appid="
        + API_TOKEN
    )
    if city[1]:
        assert response.status_code == HTTPStatus.OK, "Return should be OK"
    else:
        assert False