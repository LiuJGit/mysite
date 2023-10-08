from django.shortcuts import render
from book.models import BookInfo
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):

    print('---反向解析URL---')
    print(reverse('book:index')) # 使用 app_namespace:name 的方式

    # 1.到数据库中查询书籍
    books= BookInfo.objects.all()
    for book in books:
        print(book)

    # 2.组织数据
    context = {
        'books':books
    }

    #3.传递给模板
    return render(request,'book/index.html', context)


def getid(request, category_id, book_id):
    """
    url 位置参数与关键字参数测试
    """
    s = f"category_id:{category_id}; book_id:{book_id}"
    print('---反向解析URL---')
    print(reverse('book:getid',args=(category_id,book_id))) # 这里的反向解析需要传参
    return HttpResponse(s)