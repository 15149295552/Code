from django.conf import settings
from django.core import mail
from dashopt.celery import app
from utils.smsapi import send_message


@app.task
def async_send_active_email(email, verify_url):
    """
    功能函数:发送激活邮件
    """
    subject = "达达商城激活邮件"
    message = f"欢迎注册达达商城,请点击激活链接进行激活:{verify_url}"

    mail.send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


@app.task
def async_send_message(phone, datas):
    send_message("1", phone, datas)





