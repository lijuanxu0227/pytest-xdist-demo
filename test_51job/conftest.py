import pytest


@pytest.fixture(scope="module")
def open_51(login):
    token = login
    print(f"###用户 {token} 打开51job网站###")