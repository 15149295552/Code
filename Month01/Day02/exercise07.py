'''
练习1：商场推出了商品优惠活动，活动内容如下：
    1、如果是VIP客户，消费小于500元，则享受85折，否则享受8折。
    2、若不是VIP客户，消费大于800元，则享受9折，否则原价。
    根据用户输入的账户类型及消费金额，打印折扣信息及折扣后的应付金额。

分析：
   1、获取账户类型（是/非VIP）与消费金额（float）
   2、判断账户类型（是/否） 与 消费金额 大于0
      正常情况：
         if vip == '是':
            if money < 500:
                print('享受85折', money * 0.85)
            else:
                print('享受8折', money * 0.8)
         else:
            if money > 800:
                print('享受9折', money * 0.9)
            else:
                print('不打折', money)
      错误情况：
         '输入错误'
'''

vip = input('请输入是否为VIP（是/否）：')
money = float(input('请输入消费金额：'))

if (vip == '是' or vip == '否') and money > 0:  # 输入正确情况
    if vip == '是':
        if money < 500:
            print('享受85折', '应付金额：', money * 0.85)
        else:
            print('享受8折', '应付金额：', money * 0.8)
    else:
        if money > 800:
            print('享受9折', '应付金额：', money * 0.9)
        else:
            print('不打折', '应付金额：', money)
else:
    print('输入错误')