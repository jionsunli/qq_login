import sys
import os
import time

sys.path.append(os.getcwd())

from page.page_login import PageLogin
import pytest


def get_data():
    return [("724314130","li..75183180")]
class TestLogin():
    # 初始化
    def setup_class(self):
        #获取pagelogin对象
        self.login = PageLogin()
        self.login.page_ok()
        self.login.page_click()

    # 结束
    def teardown_class(self):
        time.sleep(20)
        self.login.driver.quit()

    # 测试方法

    @pytest.mark.parametrize("username,password",get_data())
    def test_login(self,username,password):

        self.login.page_login(username,password)