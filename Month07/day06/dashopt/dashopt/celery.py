import os
from celery import Celery
from django.conf import settings


# 1.设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashopt.settings')
# 2.初始化celery应用
app = Celery("dashopt", broker="redis://127.0.0.1:6379/15")
# 3.设置自动发现异步任务
app.autodiscover_tasks(settings.INSTALLED_APPS)














