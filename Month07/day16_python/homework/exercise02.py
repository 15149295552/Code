"""
    2.对"03字符串处理.xlsx"的"字符串处理练习"子表中数据处理
    按"："拆分,获取第二个元素作为"类型"列数据
    将"演员："替换为空(不用正则表达式)
"""
import pandas as pd

df_data = pd.read_excel("03字符串处理.xlsx", sheet_name="字符串处理练习")

# Linux修改源码时需要赋予写入权限，在终端中输入下列命令：
# sudo chmod -R 777 /usr/local/lib/python3.10/dist-packages/
df_data["类型"] = df_data["类型"].str.split("：", expand=True)[1]
df_data["演员"] = df_data["演员"].str.replace("演员：", "")
print(df_data)
