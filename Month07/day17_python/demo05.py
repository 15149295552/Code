"""
    简体转换为繁体
"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

option = ChromeOptions()
option.add_argument("--headless")
with Chrome(options=option) as driver:
    driver.get("http://www.aies.cn/")
    input_txt = driver.find_element(By.XPATH,'//textarea[@id="txt"]')
    button_convert = driver.find_element(By.XPATH,'//input[@value="简体转繁体"]')

    while True:
        input_txt.send_keys(input("请输入简体："))
        button_convert.click()
        # 如果网速慢,需要强制等待,
        time.sleep(0.5)
        print(input_txt.get_attribute("value"))
        input_txt.clear()


