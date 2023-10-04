'''
app 新建 urls.py 文件
'''

from django.conf.urls import url
import book.views as views

urlpatterns = [
    url(r'^index/$',views.index),
]