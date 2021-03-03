import pytest
import requests
import os

#设置一个环境变量
os.environ["xadmin_host"] = "http://192.168.1.232:9999"
host= os.environ["xadmin_host"]
@pytest.fixture(scope="function")
def demo_fix(request):
    print("测试用例执行：前置条件，数据准备")
    yield "howll"
    print("测试用例结束后：数据清理")
    s = requests.session()

    # def close_s():
    #     s.close()
    #
    # request.addfinalizer(close_s())  # 终结函数


def test_1(demo_fix):
    url1 = host+"/api/v2/member/user/getUserPageList"
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
    print(r1.text, r1.headers)
    assert r1.json()["code"] == 500


def test_2(demo_fix):
    print("测试用例2")


def test_3():
    print("测试用例3")
