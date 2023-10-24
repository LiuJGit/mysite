from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.


class SetSession(View):

    def get(self,request):

        # 增加数据
        request.session['name']='mike'
        request.session['photo']='http://www.baidu.com'
        request.session['id']='123'

        # 删除某一个数据
        # del request.session['name']

        # 删除session的所有数据,保留key
        # request.session.clear()

        # 把数据库/redis中的key都删除了
        # request.session.flush()

        # session是有时间的 默认是2周
        # 我们可以设置时间
        # request.session.set_expiry(sencods)
        # request.session.set_expiry(20)
        return HttpResponse('set session')


class GetSession(View):

    def get(self,request):

        # 获取数据
        print('----')
        for key, value in request.session.items():
            print(key,':',value)
            print('----')

        return HttpResponse('get session')
    

class LoginView(View):

    def get(self,request):

        return render(request,'app3/login.html')

    def post(self,request):
        pass



class ReceiveView(View):

    def get(self,request):

        data = request.GET
        username = data.get('username')
        password=data.get('password')

        return JsonResponse({'info':{'username':username}})


    def post(self,request):
        
        # request.POST只适用于以表单形式提交的数据，即Content-Type为application/x-www-form-urlencoded或multipart/form-data的请求。
        # 它无法解析application/json类型的请求体。在这种情况下，可以使用request.body获取请求体的原始字节数据，
        # 然后通过json.loads(request.body.decode())将其解码为Python对象。
        # data = request.POST # 获取到空的 QueryDict
        data=json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')

        return JsonResponse({'info':{'username':username}})