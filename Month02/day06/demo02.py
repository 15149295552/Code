"""
    小结
        字典与列表基础操作
            创建
                列表名 = [元素1,元素2]
                字典名 = {键1:值,键2:值}
                列表名 = list(可迭代对象)
                字典名 = dict(可迭代对象)
            添加
                列表名.append(元素)
                列表名.insert(索引,元素)
                字典名[键] = 值
            定位
                列表名[整数]
                列表名[整数:整数:整数]
                字典名[键]
            删除
                del 列表名[索引或者切片]
                列表名.remove(元素)
                del 字典名[键]
            遍历
                for item in 列表名:
                for i in range(len(列表名)):
                for key in 字典名:
                for value in 字典名.values():
                for key,value in 字典名.items():
"""
