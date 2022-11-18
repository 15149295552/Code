import random
from ronglian_sms_sdk import SmsSDK


accId = '8a216da87b52cabc017b58abc72701cd'
accToken = '5e8e05d59b81465abbd26cf16c7a2374'
appId = '8a216da87b52cabc017b58abc81601d3'


def send_message(tid, mobile, datas):
    sdk = SmsSDK(accId, accToken, appId)
    resp = sdk.sendMessage(tid, mobile, datas)

    return resp


if __name__ == '__main__':
    tid = "1"
    mobile = "13603263409"
    datas = (random.randint(100000, 999999), 5)
    resp = send_message(tid, mobile, datas)
    print(resp)