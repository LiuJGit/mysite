from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
import json

# Create your views here.

def index(request):
    return JsonResponse({'app name': 'app2'})
    # return HttpResponse('这是app2')
    # return redirect('book:index')


def test_cookie(request):
    # 查看请求头中有没有cookie信息
    if not request.COOKIES:
        print('---不存在cookie，下面我们设置2个cookie---')
        # cookie 数据
        data = {'username':'liujian', 'password':'123'}
        # 创建一个response
        response = HttpResponse('没有cookie，但我们进行了设置，再次刷新查看所设置的所有cookies，以及当前cookies是否被删除了')
        # 设置cookie, key-value 键值对
        for key, value in data.items():
            # max_age: 从服务器接收到这个请求后 max_age 秒后这个cookie失效
            response.set_cookie(key,value,max_age=10)
        return response
    else:
        cookies = request.COOKIES # cookies 就是一个字典
        print('---请求头中的cookies为：',cookies,'---')
        # 创建response
        response = JsonResponse({})
        delete = True # 是否删除 cookies
        if delete:
            print('---但被我们删除了---')
            for key, value in cookies.items():
                # 删除cookie的两种方式：
                # response.delete_cookie(key)
                response.set_cookie(key,value,max_age=0)
        cookies['delete'] = delete
        response.content = json.dumps(cookies)
        return response
    

def test_session(request):

    print('---首先查看是否存在key为sessionid的cookie：', 'sessionid' in request.COOKIES)
    print('---session数据对象：',request.session, type(request.session))
    if not request.session.is_empty():
        print('---sessionid存在，能取到相应的session数据：')
        print(request.session.keys(), request.session.values())
        print(request.session.items())
        print('sessionid的值为:', request.COOKIES['sessionid'])
    else:
        print('---sessionid不存在，不能取到相应的session数据，或者说取到的session数据为空：')
        print(request.session.keys(), request.session.values())
        print(request.session.items())
    
    # 设置session数据
    print('---下面，我们设置了session数据---')
    request.session['username'] = 'liujian'
    request.session['password'] = '12345'

    # # 在数据库中删除整条session记录
    # print('---下面，我们删除了整条session记录---')
    # request.session.flush()

    # # 在数据库中只删除这条session数据的'password'字段及值
    # print('---下面，我们只删除session_data中保存的数据，不删除整条session记录---')
    # try:
    #     # del request.session['username']
    #     request.session.clear()
    # except:
    #     pass
    
    return HttpResponse('test_session')