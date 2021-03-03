import requests
import json
import pytest
from ke7.a import login

@pytest.fixture(scope="function")
def login_fix():
    s = requests.session()
    login(s)
    return s


def test_1(login_fix):
    s = login_fix
    url1 = "http://192.168.1.232:9999/api/v2/member/user/getUserPageList"
    data1 = {
        "realName": "",
        "loginName": "",
        "phone": "",
        "deptCodes": None,
        "isValid": "",
        "appLoginFlag": "",
        "pcLoginFlag": "",
        "orgCode": "330782000000_11330782097919258G",
        "length": 10,
        "pageNum": 1,
        "orderField": "",
        "orderMethod": "",
        "isPass": "1"
    }
    r1 = s.post(url=url1, json=data1)
    print(r1.text, r1.headers)
    assert r1.json()["code"] == 200


def test_2():
    url1 = "http://192.168.1.232:9999/api/v2/member/user/getUserPageList"
    data1 = {
        "realName": "",
        "loginName": "",
        "phone": "",
        "deptCodes": None,
        "isValid": "",
        "appLoginFlag": "",
        "pcLoginFlag": "",
        "orgCode": "330782000000_11330782097919258G",
        "length": 10,
        "pageNum": 1,
        "orderField": "",
        "orderMethod": "",
        "isPass": "1"
    }
    r1 = requests.post(url=url1, json=data1)
    assert r1.json()["code"] == 500

