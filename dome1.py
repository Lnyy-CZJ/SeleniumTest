from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#八大方法
# driver.find_element(By.XPATH, '//*[@id="kw"]')    # 根据xpath选择元素(万金油)
# driver.find_element(By.CSS_SELECTOR, '#kw')       # 根据css选择器选择元素
# driver.find_element(By.NAME, 'wd')                # 根据name属性值选择元素
# driver.find_element(By.CLASS_NAME, 's_ipt')       # 根据类名选择元素
# driver.find_element(By.LINK_TEXT, 'hao123')       # 根据链接文本选择元素
# driver.find_element(By.PARTIAL_LINK_TEXT, 'hao')  # 根据包含文本选择
# driver.find_element(By.TAG_NAME, 'title')         # 根据标签名选择 # 目标元素在当前html中是唯一标签或众多标签第一个时候使用
# driver.find_element(By.ID, 'su')                  # 根据id选择

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        sleep(1)

    def test1_id(self):
        #id元麦是唯一的
        self.driver.find_element(by=By.ID, value="kw").send_keys("selenium")
        sleep(1)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(1)
        self.driver.quit()

    def test2_name(self):
        #name 方法会返回多个元素，默认返回第一个
        elementname= self.driver.find_element(by=By.NAME, value="wd")
        elementname.send_keys("selenium")
        sleep(2)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(3)
        self.driver.quit()

    def test3_Linktext(self):
        #id元麦是唯一的
        self.driver.find_element(by=By.ID, value="kw").send_keys("selenium")
        sleep(1)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(1)
        self.driver.find_element(by=By.LINK_TEXT, value="百度首页").click()
        sleep(2)
        self.driver.quit()

    def test4_PartialLinktext(self):
        #id元麦是唯一的
        self.driver.find_element(by=By.ID, value="kw").send_keys("selenium")
        sleep(1)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(1)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="首页").click()
        sleep(2)
        self.driver.quit()

    def test5_xpath(self):
        #id元麦是唯一的
        self.driver.find_element(by=By.XPATH, value='//*[@id="kw"]').send_keys("selenium")
        sleep(1)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(1)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="首页").click()
        sleep(2)
        self.driver.quit()

    def test6_tagname(self):
        pass

    def test7_sss_selector(self):
        #id元麦是唯一的
        self.driver.find_element(by=By.CSS_SELECTOR, value='#kw').send_keys("selenium")
        sleep(1)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(1)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="首页").click()
        sleep(2)
        self.driver.quit()

    def test8_classname(self):
        #id元麦是唯一的
        self.driver.find_element(by=By.CLASS_NAME, value='s_ipt').send_keys("selenium")
        sleep(1)
        self.driver.find_element(by=By.ID, value="su").click()
        sleep(1)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="首页").click()
        sleep(2)
        self.driver.quit()


case = TestCase()
case.test8_classname()