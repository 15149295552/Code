"""
    一个小球从100m高度落下,每次弹回原高度一半.
    计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)   13 次
    -- 全过程总共移动多少米?
    数据：高度       次数     距离
    处理：高度/=2   次数+=1  距离+=?
"""
height = 100
count = 0
distance = height
# height是下落高度
# while height > 0.01:
# height / 2 是弹起高度
while height / 2 > 0.01:
    # 弹起来一次
    height /= 2
    count += 1
    distance += height * 2  # 累加起落距离
    # 测试
    # print(f"第{count}次弹起来的高度是{height}")
print(f"总共弹起来{count}次")
print(f"移动距离{distance:.2f}米")
print(f"移动距离%.2f米" % distance)
