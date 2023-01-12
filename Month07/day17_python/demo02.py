"""
    采集百度新闻热搜标题
"""
from pandas import Series
# 1. 导入浏览器驱动工具
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# 2. 使用驱动打开浏览器
with Chrome() as driver:
    # 3. 访问web页面
    driver.get("https://top.baidu.com/board?tab=realtime&sa=fyb_realtime_31065")
    # 4. 获取html标签
    list_result = []
    for item in driver.find_elements(By.XPATH,'//div[@class="c-single-text-ellipsis"]'):
        # 5. 获取标签内的数据
        list_result.append(item.text)
    # 6. 保存数据
    series_title = Series(list_result, name="新闻标题")
    series_title.to_excel("百度新闻热搜标题.xlsx",index=False)