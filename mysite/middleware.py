
"""
新建文件，中间件
"""

# 类似于给 get_response 函数加了一个装饰器
def my_middleware1(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。

    print('----中间件1：init 时被调用----')

    def middleware(request):

        # 此处编写的代码会在每个请求处理视图前运行。
        print('中间件1：before request')

        response=get_response(request)

        # 此处编写的代码会在每个请求处理视图之后运行。
        print('中间件1：after request')

        return response

    print('####中间件1：init 时被调用####')

    return middleware


def my_middleware2(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。

    print('----中间件2：init 时被调用----')

    def middleware(request):

        # 此处编写的代码会在每个请求处理视图前运行。
        print('中间件2：before request')

        response=get_response(request)

        # 此处编写的代码会在每个请求处理视图之后运行。
        print('中间件2：after request')

        return response

    print('####中间件2：init 时被调用####')

    return middleware