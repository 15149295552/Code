"""
    自定义缓存装饰器(可传参)
"""
from django.core.cache import caches


def cache_check(**cache_kwargs):
    def _cache_check(func):
        def wrapper(self, request, *args, **kwargs):
            """
            装饰逻辑|缓存装饰器逻辑
            :cache_kwargs 装饰器参数
            :func 被装饰的方法
            :self request args kwargs 方法参数
            """
            # cache_kwargs: {'expire': 30, 'cache': 'detail', 'key': 'gd'}
            # kwargs: {'sku_id': 1}

            # 1.确认缓存中是否存在数据(Redis-get())
            rcache = caches[cache_kwargs.get("cache", "default")]
            rkey = f"{cache_kwargs.get('key')}{kwargs.get('sku_id')}"
            rresp = rcache.get(rkey)
            #  1.1 存在:直接返回
            if rresp:
                print("\033[31mdata from redis\033[0m")
                return rresp

            #  1.2 不存在:先走视图,再缓存,最后返回
            mresp = func(self, request, *args, **kwargs)
            expire = cache_kwargs.get("expire", 60)
            rcache.set(rkey, mresp, expire)

            return mresp
        return wrapper
    return _cache_check










