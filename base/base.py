from appium  import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化driver对象
    def __init__(self):
        # 定义空字典
        desired_caps = {}
        # 指定平台名称 必须写对
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        # 不能为空，可以随便写
        desired_caps['deviceName'] = 'emulator-5554'
        # 包名/
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        # 启动名
        desired_caps['appActivity'] = '.activity.LoginActivity t7'

        # 声明?机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(10)


    # 查找元素
    def base_find(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击方法
    def base_click(self,loc):
        # 调用查找元素
        self.base_find(loc).click()

    # 输入方法
    def base_input(self,loc,value):

        el = self.base_find(loc)
        # 清空输入框
        el.clear()
        # 输入值
        el.send_keys(value)