import base64
import hmac
import json
import time


class Jwt:
    def __init__(self):
        pass

    def make_token(self, payload, key):
        """生成token"""
        # 1.header
        header = {"alg": "HS256", "typ": "JWT"}
        header_str = json.dumps(header)
        header_bs64 = self.func(header_str)

        # 2.payload
        payload_str = json.dumps(payload)
        payload_bs64 = self.func(payload_str)

        # 3.sign
        part12 = header_bs64 + b"." + payload_bs64
        sign = hmac.new(key.encode(), part12, digestmod="SHA256").hexdigest()
        sign_bs64 = self.func(sign)

        return part12 + b"." + sign_bs64

    def check_token(self, token, key):
        """
        校验token
        1.校验合法性
        2.校验有效期
        """
        # token: b"xxx.yyy.zzz"
        part1, part2, part3 = token.split(b".")
        server3 = hmac.new(key.encode(), part1 + b"." + part2, digestmod="SHA256").hexdigest()
        server3 = self.func(server3)

        if server3 != part3:
            return False

        # 2.有效期
        # {"exp": xxx, ...}
        payload = json.loads(base64.b64decode(part2))
        exp = payload.get("exp")
        now = time.time()

        # exp: 6666
        # now: 6668
        if now > exp:
            return False

        return payload

    def func(self, string):
        """功能函数"""

        return base64.b64encode(string.encode())


if __name__ == '__main__':
    jwt = Jwt()
    payload = {
        "exp": time.time() + 5,
        "username": "zhaoliying"
    }
    key = "123456"

    token = jwt.make_token(payload, key)
    print(token)

    # 校验
    time.sleep(6)
    payload = jwt.check_token(token, key)
    print(payload)













