'''
app 新建 urls.py 文件
'''

from django.conf.urls import url
import book.views as views

app_name = 'book' # 设置 app namespace
urlpatterns = [
    url(r'^index/$', views.index, name='index'), # url函数的name参数：设置 URL name

    # http://127.0.0.1:8000/book/分类id/书籍id/
    # http://127.0.0.1:8000/book/category_id/book_id/
    # 分组来获取正则中的数据
    # 1. 根据位置来获取 url中的参数
    url(r'^(\d+)/(\d+)/$', views.getid, name='getid'),
    # 2. 关键字参数--推荐大家使用关键字参数
    # url(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', views.getid, name='getid'),
]