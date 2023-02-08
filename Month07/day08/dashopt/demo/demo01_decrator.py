def log_check(func):
    def wrapper(request, *args, **kwargs):
        print("也许时间是一种解药")
        print("也是我现在正服下的毒药")
        return func(request, *args, **kwargs)
    return wrapper

@log_check
def get(request):
    print("看不见你的笑我怎么睡的着")

get(666)