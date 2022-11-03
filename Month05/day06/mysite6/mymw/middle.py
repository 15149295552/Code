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
    def process_request(self, request):
        pass









