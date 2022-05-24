import pytest
from filelock import FileLock
import json


# 方法一：锁定文件
# @pytest.fixture(scope="session")
# def login():
#     print("====登录功能，返回账号，token===")
#     with FileLock("session.lock"):
#         name = "testyy"
#         token = "npoi213bn4"
#
#     yield name, token
#     print("====退出登录！！！====")

# 方法二：使用文件锁+自动判断
@pytest.fixture(scope="session")
def login(tmp_path_factory, worker_id):
    # 如果是单机运行 则运行这里的代码块【不可删除、修改】
    if worker_id == "master":
        """
        【自定义代码块】
        这里就写你要本身应该要做的操作，比如：登录请求、新增数据、清空数据库历史数据等等
        """
        name = "testyy"
        token = "npoi213bn4"
        # 如果测试用例有需要，可以返回对应的数据，比如 token
        print(f"master首次执行，数据是{name}，{token} ")
        return name, token
    # 如果是分布式运行
    # 获取所有子节点共享的临时目录，无需修改【不可删除、修改】
    root_tmp_dir = tmp_path_factory.getbasetemp().parent
    # 【不可删除、修改】
    fn = root_tmp_dir / "data.json"
    # 【不可删除、修改】
    with FileLock(str(fn) + ".lock"):
        # 【不可删除、修改】
        if fn.is_file():
            # 缓存文件中读取数据，像登录操作的话就是token 【不可删除、修改】
            token = json.loads(fn.read_text())
            print(f"worker读取缓存文件，数据是{token} ")
        else:
            """
            【自定义代码块】
            这里就写你要本身应该要做的操作，比如：登录请求、新增数据、清空数据库历史数据等等
            """
            token = "npoi213bn45"
            # 【不可删除、修改】
            fn.write_text(json.dumps(token))
            print(f"worker首次执行，数据是{token} ")
            # 如果测试用例有需要，可以返回对应的数据，比如 token
    return token
