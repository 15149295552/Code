from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=30, verbose_name='昵称', null=True)
    phone = models.CharField(max_length=11,default='')
    avatar = models.ImageField(upload_to='avatar', null=True)
    sign = models.CharField(max_length=50, verbose_name='个人签名', default="撸起袖子加油干！")
    info = models.CharField(max_length=150, verbose_name='个人简介', default=' ',null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        db_table = 'user_profile'

    def __str__(self):
        return self.username
