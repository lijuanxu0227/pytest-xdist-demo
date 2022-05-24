import pytest


@pytest.fixture(scope="function")
def open_weibo(login):
    token = login
    print(f"&&& 用户 {token} 返回微博首页 &&&")