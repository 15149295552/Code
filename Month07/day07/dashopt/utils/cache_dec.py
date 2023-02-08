"""
    自定义缓存装饰器-可传参
"""


def cache_check(**cache_kwargs):
    def _cache_check(func):
        def wrapper(self, request, *args, **kwargs):

            return func(self, request, *args, **kwargs)
        return wrapper
    return _cache_check











