import requests
import json

def login(s):

    url = "http://192.168.1.232:9999/api/v2/auth/users/login?_allow_anonymous=true"
    data = {
      "loginName": "chenkai1",
      "password": "XXfeIY885g3ffwm39QY8OWfr4SV45OVFEa/tE/iWiBzq4dHB2lZFeGKorBEFdyuhXvKvrYlQDRVETfSFTUvqZrmpx7TZ40LXkPayOj7nWYoNdRBSDS2I1d339M4ja4Ep23ub/9IKCn5lau3LjML2BZG4EoB/YA0ypPisl1sd0n56L1R22Uvy4/WMxtSq9DDDZUM9027yrCwmS9dAosEr4n5GRVd9DrCZCeFssCqgTqahkXr013vJDkj/rZAatV8GYdL0DL+I6PqKO4lWRaH8pTCCwHsz5Gjk/srPHcGuT1X9tN+TWvUX6FhlNH1MhLiWueSKrSXmDSWkON3/HMLKGg==",
      "type": 2,
      "checkCode": "1"
    }
    r = s.post(url=url, json=data)
    # print(r.json())

    # token
    token = r.json()["data"]["token"]
    print(token)

    header = {
            'Authorization': "Bearer %s" % token
               }
    s.headers.update(header)
    return token
if __name__ == '__main__':
    s = requests.session()
    login(s)
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

