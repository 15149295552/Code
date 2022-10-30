"""
     练习3：
     在终端中输入课程阶段数,显示课程名称
     输入：        输出：
      1          	Python语言核心编程
      2          	Python高级软件技术
      3          	Web 全栈
      4             人工智能
"""
number = input("请输入数字：")
if number == "1":
    print("Python语言核心编程")
elif number == "2":
    print("Python高级软件技术")
elif number == "3":
    print("Web 全栈")
elif number == "4":
    print("人工智能")




# 缺点：即使前面条件满足,后面条件也要判断
#   　　浪费cpu性能
# number = int(input("请输入数字："))
# if number == 1:
#     print("Python语言核心编程")
# if number == 2:
#     print("Python高级软件技术")
# if number == 3:
#     print("Web 全栈")
# if number == 4:
#     print("人工智能")
