from django.conf import settings
from django.http import HttpResponse
from django.views import View
from alipay import AliPay
from orders.models import OrderInfo


class MyAlipay(View):
    """
    基类,用于初始化alipay对象并提供常用的方法
    """
    def __init__(self, **kwargs):
        # supder():不能影响父类初始化
        super().__init__(**kwargs)
        # 初始化alipay对象
        self.alipay = AliPay(
            # 应用ID:控制台获取
            appid=settings.APPID,
            # 异步通知地址: 必须为公网IP
            app_notify_url=None,
            # 应用私钥[用于签名]
            app_private_key_string=open(settings.KEYS_DIR + "app_private_key.pem").read(),
            # 支付宝公钥[用于验签]
            alipay_public_key_string=open(settings.KEYS_DIR + "alipay_public_key.pem").read(),
            # 签名使用算法
            sign_type="RSA2",
            # False:请求到生产环境,True:请求发至沙箱环境
            debug=True
        )


class ReturnUrlView(MyAlipay):
    def get(self, request):
        """
        同步通知:没有支付结果,只有支付信息
        主动查询视图逻辑
        1.获取查询字符串(支付信息)
        2.调用主动查询接口(alipay接口)
        """
        data = request.GET
        order_id = data.get("out_trade_no")
        trade_no = data.get("trade_no")

        result = self.alipay.api_alipay_trade_query(
            out_trade_no=order_id,
            trade_no=trade_no
        )
        status = result.get("trade_status")
        if status == "TRADE_SUCCESS":
            # 支付成功,修改订单状态 1 -> 2
            order = OrderInfo.objects.get(order_id=order_id)
            order.status = 2
            order.save()
            return HttpResponse("GET:主动查询,成功!")
        else:
            return HttpResponse("支付失败")


class NotifyUrlView(MyAlipay):
    def post(self, request):
        """
        异步通知视图逻辑,存在支付结果
        此地址必须为公网IP，不能是127.0.0.1
        1.获取请求体数据(支付结果、签名......)
        2.验签:确认消息来源
        3.获取支付结果,调整订单状态
        4.返回响应:suc
        """
        data = request.POST
        # 验签方法verify(),返回值: True|Fasle
        result = self.alipay.verify(
            data=data,
            signature=data.get("sign")
        )
        if result:
            # 请求由支付宝发出,获取支付结果
            status = data.get("trade_status")
            if status == "TRADE_SUCCESS":
                # 支付成功,修改订单状态 1 -> 2
                order_id = data.get("out_trade_no")
                order = OrderInfo.objects.get(order_id=order_id)
                order.status = 2
                order.save()

                return HttpResponse("success")
        else:
            # 伪造请求
            return HttpResponse("违法请求!")













