from base.base import Base

import page
class PageLogin(Base):
    # 同意协议
    def page_ok(self):
        self.base_click(page.login_ok)

    # 点击同意登录
    def page_click(self):
        self.base_click(page.login_btn)

    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_input_username,username)


    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.login_input_password,password)

    # 点击登录
    def page_click_btn(self):
        self.base_click(page.login_click_btn)

    # 业务组合
    def page_login(self,username,password):
        self.page_input_username(username)

        self.page_input_password(password)

        self.page_click_btn()