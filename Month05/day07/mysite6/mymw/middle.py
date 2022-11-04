from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("中间件:process_request()执行~~~")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件:process_view()执行~~~")

    def process_response(self, request, response):
        print("中间件:process_response()执行~~")

        return response


class VisitLimit(MiddlewareMixin):
    dic = {}

    def process_request(self, request):
        ip_addr = request.META.get("REMOTE_ADDR")
        path_url = request.path_info
        if path_url != "/test":
            return None

        # dic: {}
        times = self.dic.get(ip_addr, 0)
        # 创建新的键值对或对现有的键值对+1
        self.dic[ip_addr] = times + 1

        if times < 5:
            return None

        return HttpResponse(f"超过5次,已经{times}次")








