from django.db import models


class Address(models.Model):
    # 收件人 收件地址 联系方式
    receiver = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)


class Book(models.Model):
    title = models.CharField(max_length=30)
    pub = models.CharField(max_length=50)


class OrderInfo(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class MemberInfo(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    is_member = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    member_id = models.IntegerField()
    email = models.EmailField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class ProductInfo(models.Model):
    # 商品名称 商品价格 商品库存
    # users_product_tab
    title = models.CharField("商品名称", max_length=100)
    price = models.DecimalField("价格", max_digits=10, decimal_places=2)
    stock = models.IntegerField("库存")
    sales = models.IntegerField("销量", default=0)

    class Meta:
        db_table = "users_product_tab"


class UserProfile(models.Model):
    username = models.CharField("用户名", max_length=20)
    password = models.CharField("密码", max_length=32)
    email = models.EmailField("邮箱")
    mobile = models.CharField("手机号", max_length=11)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_profile"




