import time

from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}

desired_caps['platformName'] = 'Android'  # 设备系统

desired_caps['platformVersion'] = '6.0.1'  # 设备系统版本

desired_caps['deviceName'] = '127.0.0.1:7555'  # 设备名称

desired_caps['appPackage'] = 'com.alibaba.android.rimet'

desired_caps['appActivity'] = '.biz.LaunchHomeActivity'

desired_caps['noReset'] = 'true'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id("com.alibaba.android.rimet:id/img_shortcut").click()
metohd = driver.find_element_by_accessibility_id("掌上执法")
ele = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable())
print(ele)
time.sleep(10)
driver.quit()
