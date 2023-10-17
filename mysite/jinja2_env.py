'''
新建文件，创建 env，自定义jinja2全局函数或过滤器
'''
from jinja2 import Environment
from django.template.defaultfilters import date, default

def environmnet(**option):

    #1.创建 Environment实例
    env=Environment(**option)

    # 2 jinja2的全局函数和过滤器本质上都是python函数，但二者传参的语法不同；
    # DTL过滤器本质上也是python函数，因此既可以注册为jinja2的全局函数，也可以注册为jinja2的过滤器。注意，jinja2过滤器的传参语法和DTL的不同。
    # jinja2本身也实现了一些全局函数和过滤器供用户直接使用，但有些过滤器是 DTL 独有的，或者我们想实现用户自定义的全局函数或过滤器，
    # 此时，我们就需要新建 env，自定义全局函数或过滤器。

    #2.1 注册全局函数
    env.globals.update({
        'date':date, # 将DTL的date过滤器注册为全局函数
        'default':default, # jinja2有default过滤器，但没有default全局函数，这里可以注册一个
        'udf1':udf1,
    })
    env.globals['add_numbers'] = udf2 # 注册为全局函数的另一种方式

    # 2.2 注册过滤器
    env.filters['date'] = date # 注册为过滤器
    env.filters['udf1'] = udf1
    env.filters['add_numbers'] = udf2
    
    #3.返回Environment实例
    return env

# 用户自定义函数
def udf1(s):
    return f'---{s}---'

# 用户自定义函数
def udf2(a, b):
    return a + b