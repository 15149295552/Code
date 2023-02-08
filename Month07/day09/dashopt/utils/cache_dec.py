"""
    自定义缓存装饰器-可传参
"""
from django.core.cache import caches


def cache_check(**cache_kwargs):
    def _cache_check(func):
        def wrapper(self, request, *args, **kwargs):
            """
            :cache_kwargs 装饰器参数
            :func 被装饰的方法
            :self request args kwargs 方法参数
            """
            # cache_kwargs: {'expire': 60, 'cache': 'detail', 'key_prefix': 'gd'}
            # kwargs: {'sku_id': 1}
            """
            1.确认缓存中是否存在数据
            2.缓存中存在:则直接返回,结束!
            3.缓存中不存在:走视图,并把响应存入缓存中,再返回响应!
            """
            redis = caches[cache_kwargs.get("cache", "default")]
            key = cache_kwargs["key_prefix"] + str(kwargs["sku_id"])
            response = redis.get(key)

            if response:
                # 缓存中存在,直接返回!
                print("\033[31mdata from redis~\033[0m")
                return response

            # 缓存中不存在
            view_resp = func(self, request, *args, **kwargs)
            redis.set(key, view_resp, cache_kwargs["expire"])

            return view_resp
        return wrapper
    return _cache_check











