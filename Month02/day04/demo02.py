"""
    小结 - 流程控制语句
        选择语句：让代码根据条件有选择性的执行
            if 条件1:
                语句1
            elif 条件2:
                语句2
            else:
                语句3
        循环语句：让代码重复性的执行
            -- 根条件重复,例如:纸张对折到珠穆朗玛峰
            while 条件:
                语句
           -- 根次数重复,例如:纸张对折20次
            for 变量 in 可迭代对象:
                语句
        跳转语句：在循环中使用
            break 跳出(结束循环)
            continue 跳过(本次循环体后续代码不执行,继续执行后续循环)
"""
total_score = 0  # 总成绩
for count in range(1,6):  # 0~4
    total_score += int(input("请输入成绩:"))
print("平均成绩：" + str(total_score / count))
