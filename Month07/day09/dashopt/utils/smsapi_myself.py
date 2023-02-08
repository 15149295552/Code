import time
import base64
import hashlib
import requests


class SmsSDK:
    def __init__(self, accId, accToken, appId):
        self.accId = accId
        self.accToken = accToken
        self.appId = appId
        self.now_time = time.strftime("%Y%m%d%H%M%S")

    def get_url(self):
        string = self.accId + self.accToken + self.now_time
        m = hashlib.md5()
        m.update(string.encode())
        sig = m.hexdigest().upper()

        return f"https://app.cloopen.com:8883/2013-12-26/Accounts/{self.accId}/SMS/TemplateSMS?sig={sig}"

    def get_data(self, mobile, tid, datas):
        data = {
            "to": mobile,
            "appId": self.appId,
            "templateId": tid,
            "datas": datas
        }

        return data

    def get_headers(self):
        string = self.accId + ":" + self.now_time
        auth = base64.b64encode(string.encode()).decode()

        headers = {
            "Accept": "application/json;",
            "Content-Type": "application/json;charset=utf-8;",
            # Content-Length:256;
            "Authorization": auth,
        }

        return headers

    def sendMessage(self, tid, mobile, datas):
        url = self.get_url()
        data = self.get_data(mobile, tid, datas)
        headers = self.get_headers()

        html = requests.post(url=url, json=data, headers=headers).json()

        return html


if __name__ == '__main__':
    accId = '8a216da87b52cabc017b58abc72701cd'
    accToken = '5e8e05d59b81465abbd26cf16c7a2374'
    appId = '8a216da87b52cabc017b58abc81601d3'

    sdk = SmsSDK(accId, accToken, appId)
    html = sdk.sendMessage("1", "13603263409", (871016, 5))
    print(html)








