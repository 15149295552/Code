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
