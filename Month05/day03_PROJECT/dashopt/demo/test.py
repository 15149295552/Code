def logging_check(func):
    def wrapper(request, *args, **kwargs):
        print("也许时间是一种解药")
        print("也是我现在正服下的毒药")
        request = 871016
        return func(request, *args, **kwargs)
    return wrapper

@logging_check
def get(request):
    print("看不见你的笑我怎么睡的着")
    print(request)

get(666)


