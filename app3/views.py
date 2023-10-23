from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

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