from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest



# 在启动浏览器时加入配置
driver = webdriver.Chrome()
driver.maximize_window()
# 打开
driver.get('http://ales.fat6.icinfo.co/?server=pre#/supervise/subsidiary/engineering')
#隐试等待
driver.implicitly_wait(3)
def test_1():
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]').send_keys("15868385402")
    # 显示等待
    WebDriverWait(driver, 10).until()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]').send_keys("aa112233.")
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys("1")
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, '.sidebar-nav__item-text[title="监管智库"]').click()
    driver.find_element(By.CSS_SELECTOR, '.sidebar-nav__item-text[title="监管标签"]').click()
    WebDriverWait(driver, 10).until(By.CSS_SELECTOR, '.sidebar-nav__item.is-leaf.sidebar-nav__selected.sidebar-nav__open')
    driver.find_element(By.CSS_SELECTOR, '.sidebar-nav__item.is-leaf.sidebar-nav__selected.sidebar-nav__open').click()
    driver.find_element(By.CSS_SELECTOR, '.ng-tns-c21-54.ng-tns-c21-46.ng-star-inserted').click()
    driver.find_element(By.CSS_SELECTOR, '.ant-btn.ng-star-inserted.ant-btn-primary').click()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入"]').send_keys("zdh_标签1")
    driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
    driver.find_element(By.CSS_SELECTOR, 'nz-select[nzplaceholder="请选择"]').click()
    driver.find_element(By.CSS_SELECTOR, '.ant-select-dropdown-menu-item.ng-star-inserted').click()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入"]').send_keys("zdh_标签1责任处室")
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入备注"]').send_keys("zdh_标签1说明")
    driver.find_element(By.CSS_SELECTOR, 'button[nztype="primary"]').click()
    time.sleep(5)
    driver.quit()



