import time
from celery import Celery


app = Celery("dashop", broker="redis://127.0.0.1:6379/15", backend="redis://127.0.0.1:6379/14")


@app.task
def async_send_sms(s1, s2):
    print("正在发送短信...")
    time.sleep(5)
    print("短信发送完成...")

    return s1 + s2













