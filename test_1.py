import pytest


@pytest.mark.parametrize("n", list(range(5)))
def test_get_info(login, n):
    token = login
    print("***基础用例：获取用户个人信息***", n)
    print(f"token:{token}")


if __name__ == '__main__':
   pytest.main()
