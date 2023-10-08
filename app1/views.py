from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def detail(request):

    print('---反向路由解析---')
    print(reverse('app1_author:detail'))
    print(reverse('app1_publisher:detail'))
    print('---当前的instance namespace---')
    print(request.resolver_match.namespace)
    print('---指定instance namespace---')
    # 注意，存在or不存在与app namespace同名的instance namespace时，'app1:detail'会有不同的默认值
    print(reverse('app1:detail'))
    # 可以强行指定 instance namespace
    print(reverse('app1:detail', current_app='app1_author'))
    print('------')

    if request.resolver_match.namespace == 'app1_author':
        return HttpResponse('这里是作者的页面')
    elif request.resolver_match.namespace == 'app1_publisher':
        return HttpResponse('这里是出版商的页面')
    else:
        return HttpResponse('Django学习')