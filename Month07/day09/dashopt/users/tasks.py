from django.conf import settings
from django.core import mail
from dashopt.celery import app
from utils.smsapi import send_message


@app.task
def async_send_active_email(email, username, verify_url):
    """
    功能函数: 发送邮件
    """
    subject = "达达商城激活邮件"
    message = f"""
    欢迎您:{username},请点击激活链接进行激活:<a href="{verify_url}" target="_blank">点击此处</a>"""

    mail.send_mail(
        subject=subject,
        # message: 发送文本内容邮件
        message="",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        # html_message: 发送html格式邮件
        html_message=message
    )


@app.task
def async_send_message(phone, datas):
    send_message("1", phone, datas)