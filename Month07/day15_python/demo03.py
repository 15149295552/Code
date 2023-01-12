"""
    定制化数据处理
        列
"""
import pandas as pd

df_data = pd.read_excel("01餐饮数据.xlsx")

# 1. 修改
df_data["城市"] = "长春"
df_data["人均"] += 10

# 2. 追加
df_data["测评"] = "完成"
# df_data["总分"] = df_data["口味"] + df_data["环境"] + df_data["服务"]
# df_data["总分"] = df_data[["口味","环境","服务"]].sum() # 计算列
# df_data["总分"] = df_data[["口味", "环境", "服务"]].sum(axis=1)  # 计算列
# df_data["平均"] = df_data[["口味", "环境", "服务"]].mean(axis=1)

# 3. 插入
df_data.insert(3,"平均",df_data[["口味", "环境", "服务"]].mean(axis=1))

# 4. 删除
# df_data.drop("点评")
df_data.drop(["点评","环境"],axis=1,inplace=True)

df_data.to_excel("测试.xlsx", index=False)
