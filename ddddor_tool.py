#自动化登录识别验证码
import time
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr

def get_code(URL,Xpath):
    # 创建一个dddocr的实例：
    ocr = ddddocr.DdddOcr()
    # URL = "http://jtest.cube.ganrobot.com:11882/login?redirect=%2Findex"
    # 使用selenium打开页面
    driver = webdriver.Edge()
    driver.get(URL)
    driver.maximize_window()

    # 去到验证码界面并截图整个界面
    st = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    png_name1 = str(st) + ".png"
    path = os.path.abspath("Image")
    file_path = path + "/" + png_name1
    driver.get_screenshot_as_file(file_path) # 截图

    # 找到验证码区域并抠图出来
    #Xpath= '//*[@id="app"]/div/form/div[3]/div/div[2]'
    ce = driver.find_element(By.XPATH, Xpath)
    # print(ce.location)
    left = ce.location["x"]
    top = ce.location["y"]
    right = ce.size["width"] + left
    height = ce.size["height"] + top
    # 抠图
    im = Image.open(file_path)
    img = im.crop((left, top, right, height))

    st2 = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    png_name2 = "--验证码截图--" + str(st2) + ".png"
    path = os.path.abspath("Image")
    file_path2 = path + "/" + png_name2
    img.save(file_path2)
    driver.close()

    # 使用dddocr识别验证码：
    with open(file_path2,"rb") as f:
        image_bytes = f.read()
        # print (img)
    result = ocr.classification(image_bytes)
    print("验证码为:",result)
    return result

URL = "http://jtest.cube.ganrobot.com:11882/login?redirect=%2Findex"
Xpath= '//*[@id="app"]/div/form/div[3]/div/div[2]'
get_code(URL,Xpath)
