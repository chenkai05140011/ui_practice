import requests
import json
import pytest

@pytest.fixture(scope="function")
def login():
    print("先登入")

def setup_module():
    print("整个用例只调用一次")

def setup_function():
    # 函数级别的前置条件
    print("每个用例执行一遍")


def test_1(login):
    print("测试用例1")


def test_2(login):
    print("测试用例2")
