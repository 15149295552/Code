import time
from celery import Celery


app = Celery("dashop", broker="redis://127.0.0.1:6379/15")


@app.task
def send_email():
    print("Start sending...")
    time.sleep(5)
    print("End!!!!!!!!!!!!!")















