from django.db import models


class UserProfile(models.Model):
    # 用户名username，要求字符类型，最大长度20，不能重复，不能为空，建立索引；
    username = models.CharField("用户名", max_length=20, unique=True, null=False, db_index=True)
    # 密码password，要求字符类型，最大长度32；
    password = models.CharField("密码", max_length=32)
    # 邮箱email：要求EmailField()
    email = models.EmailField("邮箱")
    # 手机号phone：要求字符类型，最大长度11；
    phone = models.CharField("手机号", max_length=11)
    # 创建时间created_time：要求增加数据时自动创建时间；
    created_time = models.DateTimeField(auto_now_add=True)
    # 更新时间updated_time：要求修改数据保存时自动更新时间；
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        # 表名：orders_user_profile
        db_table = "orders_user_profile"

    def __str__(self):
        return self.username


class OrderInfo(models.Model):
    # 用户表外键；
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # 订单总金额total_amount：要求浮点型，总位数10位，小数位2位；
    total_amount = models.DecimalField("总金额", max_digits=10, decimal_places=2)
    # 运费freight：要求浮点型，总数为10位，小数位2位；
    freight = models.DecimalField("运费", max_digits=10, decimal_places=2)
    # 订单状态status：要求整型；
    status = models.IntegerField("订单状态")
    # 订单创建时间created_time：同用户表要求；
    created_time = models.DateTimeField(auto_now_add=True)
    # 订单更新时间updated_time：同用户表要求；
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        # 表名：orders_order_info
        db_table = "orders_order_info"

    def __str__(self):
        return f"{self.user_profile.id}, {self.total_amount}"


class OrderGoods(models.Model):
    # 订单表外键；
    order_info = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    # 商品名称sku_name：要求字符类型，最大长度50；
    sku_name = models.CharField("商品名称", max_length=50)
    # 商品单价price：要求浮点型，总位数10位，小数位2位；
    price = models.DecimalField("单价", max_digits=10, decimal_places=2)
    # 商品数量count：要求整型
    count = models.IntegerField("数量")

    class Meta:
        # 表名：orders_order_goods
        db_table = "orders_order_goods"

    def __str__(self):
        return f"{self.sku_name},{self.count}"


# 请查询id为1的用户成交的订单都有哪些？
# user = UserProfile.objects.get(id=1)
# orders = OrderInfo.objects.filter(user_profile=user)

# 请查询id为1的订单都有哪些商品信息？
# order = OrderInfo.objects.get(id=1)
# skus = OrderGoods.objects.filter(order_info=order)