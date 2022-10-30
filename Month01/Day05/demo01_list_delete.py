# 列表中元素删除的‘坑’

# 需求：删除列表所有的6
lists = [5, 6, 4, 6, 6, 7]

# lists.remove(6)
# lists.remove(6)
# lists.remove(6)
#
# print(lists)

# for x in lists:
#     if x == 6:
#         lists.remove(6)
#
# print(lists)

# for x in range(len(lists)):
#     if lists[x] == 6:
#         lists.remove(6)
#
# print(lists)


for x in range(len(lists)-1, -1, -1):
    if lists[x] == 6:
        # lists.remove(6)
        del lists[x]      # 推荐

print(lists)

'''
    前2个方法：列表删除元素后，后续的元素会前移，产生元素跳过现象
    结论：删除列表中的多个元素，推荐使用倒序删除+del的方法
'''