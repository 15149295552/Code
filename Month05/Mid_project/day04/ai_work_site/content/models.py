from django.db import models
from user.models import UserProfile

# Create your models here.
class Topic(models.Model):
    id = models.AutoField('ID',primary_key=True)
    title = models.CharField(max_length=50,verbose_name="文章标题")
    # 5类 ： 教学心得 teach  学习感悟 learn  知识整理knowledge   首页后台  团队风采 team  行业信息 news
    category = models.CharField(max_length=20,verbose_name="内容分类")
    content = models.TextField(verbose_name='文章内容')
    introduce = models.CharField(max_length=128,verbose_name="内容简介",default="进来看看吧")
    # public  & private
    limit = models.CharField(max_length=20,verbose_name="查看权限")
    click_count = models.IntegerField(verbose_name="点击量",default=0)
    recommend = models.FloatField(verbose_name='推荐值',default=0.0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,default=None)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        db_table = 'topic'
        ordering = ['-recommend','-created_time']

    def __str__(self):
        return self.title

class Message(models.Model):
    pass
