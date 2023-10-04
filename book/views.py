from django.shortcuts import render
from book.models import BookInfo

# Create your views here.

def index(request):

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