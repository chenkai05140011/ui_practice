import pytest
import requests
#笛卡尔积(参数化)


# @pytest.mark.skip("阻塞BUG")
#
# #标注可以按照标记去执行测试用例
# @pytest.mark.webtest

@pytest.mark.parametrize("x",["chenkai1", "", 10])
@pytest.mark.parametrize("y",["chenkai1", "", 10])
def test_demo1(x, y):
    url = "http://192.168.1.232:9999/api/v2/auth/users/login?_allow_anonymous=true"
    data = {
        "loginName": x,
        "password": y,
        "type": 2,
        "checkCode": "1"
    }
    r = requests.post(url=url, json=data)
    # print(r.json())
    assert r.json()["code"] == 200
#执行标签
if __name__ == '__main__':
    pytest.main(["-s", "test_b.py", "-m=webtest"])