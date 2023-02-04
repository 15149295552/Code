import time
from celery import Celery

app = Celery("aid2210", broker="redis://127.0.0.1:6379/8")


@app.task
def send_email():
    print("Email is sending...")
    time.sleep(5)
    print("Email end!")




