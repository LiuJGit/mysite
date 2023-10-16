from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
import json
from django.views import View

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


def B(request):
    '''
    能正常发起转账的页面
    '''
    response = render(request,'app2/B.html')
    # 通过正常途径访问时设置一个cookie
    # 若开启 django csrf 中间件，django 还会保证存在一个名为 csrftoken 的 cookie（不存在就新设置一个）
    response.set_cookie('password','123')
    return response


def check_request(request):
    '''
    检查发送的请求的情况
    '''
    # print(f'----请求头----')
    # print(request.headers)
    # print(request.headers.get('Origin',None))

    print('----请求携带的cookie----')
    print(request.COOKIES)

    print('----请求携带的数据----')
    print('POST 携带的数据：', request.POST)

    password = request.COOKIES.get('password', None)
    if password:
        # 关闭 django 的 csrf 中间件，
        # 只要存在 password cookie 就能转账成功。
        # 打开 django 的 csrf 的中间件，对于跨站点提交的请求，根本不允许访问；
        # 但是，人为地在攻击网页 C 的表单中添加合法的 csrfmiddlewaretoken 
        # (比如在浏览器中查看B页面的源码，就可以看到合法的 csrfmiddlewaretoken)，
        # 再发起请求就可以通过 django 自带 csrf 中间件的检测了。
        return HttpResponse('转账成功')

        # # 若提交的表单带有 csrf token，并通过 cookie 中的 csrf token 的检验
        # # 比如，二者相等，或其他的合法性校验（类似于公钥(cookie中的csrf token)和私钥(表单中的csrf token)是否匹配，
        # # 则转账成功，否则是黑客攻击。
        # # 这里为了方便，我们假设只要表单带有 csrf token 就通过了检验，因为正常情况下，黑客是拿不到表单中的 csrf token 的。
        # # 这里相当于实现了一个简单的防止 csrf 的逻辑。
        # if request.POST.get('csrfmiddlewaretoken'):
        #     return HttpResponse('转账成功')
        # else:
        #     return HttpResponse('黑客攻击')
    else:
        return HttpResponse('请先登录')
    

class TestView(View):

    def get(self, request):
        print('接收到get请求')
        return render(request, 'app2/view.html')
    
    def post(self, request):
        print('接收到post请求')
        return HttpResponse('类视图：post 方法')