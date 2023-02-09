from ronglian_sms_sdk import SmsSDK

accId = '8a216da87b52cabc017b58abc72701cd'
accToken = '5e8e05d59b81465abbd26cf16c7a2374'
appId = '8a216da87b52cabc017b58abc81601d3'


def send_message(tid, mobile, datas):
    sdk = SmsSDK(accId, accToken, appId)
    resp = sdk.sendMessage(tid, mobile, datas)

    return resp

