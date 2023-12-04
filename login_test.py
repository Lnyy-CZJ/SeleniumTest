import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 使用 fixture 来初始化浏览器驱动
@pytest.fixture
def browser():
    # 初始化 Chrome 浏览器
    driver = webdriver.Firefox()
    yield driver
    # 测试结束后退出浏览器
    driver.quit()

# 测试用例
def test_search_on_google(browser):
    # 打开谷歌主页
    browser.get('https://www.google.com')
    # 找到搜索框并输入关键词
    search_box = browser.find_element_by_name('q')
    search_box.send_keys('Selenium testing')
    search_box.send_keys(Keys.RETURN)
    # 等待搜索结果加载
    browser.implicitly_wait(5)
    # 断言页面标题是否包含关键词
    assert 'Selenium testing' in browser.title

# 运行测试
if __name__ == "__main__":
    pytest.main([__file__])