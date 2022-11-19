from django.db import models
from user.models import UserProfile


# Create your models here.
class Topic(models.Model):
    id = models.AutoField("ID",primary_key=True)
    title = models.CharField(max_length=50, verbose_name="文章标题")
    # 5类  前台 教学心得teach  学习感悟learn  知识整理knowledge   后台  团队风采 team  最新咨询 news
    category = models.CharField(max_length=20, verbose_name="文章分类")
    #public & private
    limit = models.CharField(max_length=20, verbose_name="文章权限")
    introduce = models.CharField(max_length=90, verbose_name="文章简介",default="进来看看吧")
    content = models.TextField(verbose_name="文章内容")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    click_count = models.IntegerField(verbose_name="点击量",default=0)
    recommend = models.SmallIntegerField(verbose_name='推荐值',default=0)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True,default=None)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        db_table = 'topic'
        ordering = ['-recommend','-created_time']

    def __str__(self):
        return self.title

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    parent_message = models.IntegerField(verbose_name='回复的留言id')
    publisher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "留言"
        verbose_name_plural = "留言"
        db_table = 'message'
        ordering = ['-created_time']
