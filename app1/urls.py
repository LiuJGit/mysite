'''
app 新建 urls.py 文件
'''

from django.conf.urls import url
import app1.views as views

app_name = 'app1' # 设置 app namespace
urlpatterns = [
    url('detail/', views.detail, name='detail'), # 设置 URL name
]