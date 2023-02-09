from django.db import models


class UserProfile(models.Model):
    """用户表"""
    # 用户名、密码、邮箱、手机号、是否激活、创建时间、更新时间
    username = models.CharField(max_length=11, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    is_active = models.BooleanField(default=False, verbose_name="是否激活")

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    # 修改表名
    class Meta:
        # 表名: 应用名_类名非驼峰
        db_table = "users_user_profile"


class Address(models.Model):
    """
        收货地址表
        用户表:地址表 ---> 1:n
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # 收件人 地址 邮编 手机号
    receiver = models.CharField(verbose_name="收件人", max_length=10)
    address = models.CharField(verbose_name="收件地址", max_length=100)
    postcode = models.CharField(verbose_name="邮编", max_length=6)
    receiver_mobile = models.CharField(verbose_name="手机号", max_length=11)
    # 标签 默认地址
    tag = models.CharField(verbose_name="标签", max_length=10)
    is_default = models.BooleanField(verbose_name="默认地址", default=False)
    # 伪删除
    is_delete = models.BooleanField(verbose_name="伪删除", default=False)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    # 修改表名
    class Meta:
        # 表名: 应用名_类名非驼峰
        db_table = "users_address"


class WeiBoProfile(models.Model):
    """
    微博表,和用户表是1..1的关系
    """
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    wuid = models.CharField(max_length=10, unique=True, db_index=True)
    access_token = models.CharField(max_length=32)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users_weibo_profile"


