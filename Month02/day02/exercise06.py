"""
    画出下列代码内存图,说出终端显示结果
"""
bridegroom_name = "武大郎"
bride_name = "潘金莲"
temp = bridegroom_name
bridegroom_name = bride_name
bride_name = temp
print("交换后的新郎：" + bridegroom_name)  #
print("交换后的新娘：" + bride_name)  #
