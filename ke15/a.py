import requests
import re
from requests_toolbelt import multipart#form表单数据格式

def login(s, name="chenkai1",
          password="XXfeIY885g3ffwm39QY8OWfr4SV45OVFEa/tE/iWiBzq4dHB2lZFeGKorBEFdyuhXvKvrYlQDRVETfSFTUvqZrmpx7TZ40LXkPayOj7nWYoNdRBSDS2I1d339M4ja4Ep23ub/9IKCn5lau3LjML2BZG4EoB/YA0ypPisl1sd0n56L1R22Uvy4/WMxtSq9DDDZUM9027yrCwmS9dAosEr4n5GRVd9DrCZCeFssCqgTqahkXr013vJDkj/rZAatV8GYdL0DL+I6PqKO4lWRaH8pTCCwHsz5Gjk/srPHcGuT1X9tN+TWvUX6FhlNH1MhLiWueSKrSXmDSWkON3/HMLKGg=="):
    url = "http://192.168.1.232:9999/api/v2/auth/users/login?_allow_anonymous=true"
    data = {
        "loginName": name,
        "password": password,
        "type": 2,
        "checkCode": "1"
    }
    r = s.post(url=url, json=data)

    # token
    token = r.json()["data"]["token"]
    #print(token)

    header = {
        'Authorization': "Bearer %s" % token
    }

    print(r.text)
    uid = re.findall('"message":"(.+?)"', r.text)
    return uid
s = requests.session()
re = login(s)
print(re)