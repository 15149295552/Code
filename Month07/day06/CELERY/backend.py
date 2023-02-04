import time
from celery import Celery

app = Celery("AID2210",
             broker="redis://127.0.0.1:6379/6",
             backend="redis://127.0.0.1:6379/7")


@app.task
def send_msg(mobile, code):
    print("正在发送中......")
    time.sleep(5)
    print("发送成功......")

    return f"{mobile}_{code}"

