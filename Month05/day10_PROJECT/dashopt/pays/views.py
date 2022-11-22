from alipay import AliPay
from django.conf import settings
from django.http import HttpResponse
from django.views import View

from orders.models import OrderInfo


class MyAlipay(View):
    """
    基类,用于初始化alipay对象并提供常用方法
    """
    def __init__(self, **kwargs):
        # 1.不能影响父类(View)的初始化
        super().__init__(**kwargs)
        # 2.初始化alipay对象
        self.alipay = AliPay(
            # 应用ID:控制台获取
            appid=settings.ALIPAY_APPID,
            # 异步通知地址[POST请求]:必须为公网IP
            app_notify_url=None,
            # 应用私钥:用于签名
            app_private_key_string=open(settings.ALIPAY_KEYS_DIR + "app_private_key.pem").read(),
            # 支付宝公钥:用于验签
            alipay_public_key_string=open(settings.ALIPAY_KEYS_DIR + "alipay_public_key.pem").read(),
            # 签名使用算法
            sign_type="RSA2",
            # True:请求发至沙箱,False:生产环境
            debug=True
        )


class ReturnView(MyAlipay):
    def get(self, request):
        """
        主动查询视图逻辑
        同步通知GET:只有支付信息,没有支付结果
        1.获取查询字符串(支付信息)
        2.不需要验签
        3.主动查询支付结果
        """
        data = request.GET
        out_trade_no = data.get("out_trade_no")
        trade_no = data.get("trade_no")

        result = self.alipay.api_alipay_trade_query(
            out_trade_no=out_trade_no,
            trade_no=trade_no
        )

        status = result.get("trade_status")
        if status == "TRADE_SUCCESS":
            # 支付成功,修改订单状态
            order = OrderInfo.objects.get(order_id=out_trade_no)
            order.status = 2
            order.save()
            return HttpResponse("----GET:主动查询,交易成功----")
        else:
            return HttpResponse("----GET:主动查询,交易失败----")


class NotifyView(MyAlipay):
    def post(self, request):
        """
        异步通知视图逻辑
        异步通知POST:有支付结果,但是必须为公网IP
        1.获取请求体数据
        2.验签[确认消息由支付宝发出]
        3.获取支付结果,根据支付结果修改订单状态
        """
        data = request.POST
        # 验签方法verify():True|False
        sign = data.get("sign")
        result = self.alipay.verify(
            data=data,
            signature=sign
        )
        if result:
            # 验签通过,此请求确认为支付宝发出
            status = data.get("trade_status")
            if status == "TRADE_SUCCESS":
                # 支付成功,修改订单状态(一查二改三保存)
                out_trade_no = data.get("out_trade_no")
                order = OrderInfo.objects.get(order_id=out_trade_no)
                order.status = 2
                order.save()
                print("----POST----")
                return HttpResponse("success")
        else:
            # 验签未通过,非支付宝发出
            return HttpResponse("违法请求~")

















