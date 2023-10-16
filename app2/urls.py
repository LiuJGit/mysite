'''
app 新建 urls.py 文件
'''

from django.conf.urls import url
import app2.views as views

app_name = 'app2' # 设置 app namespace
urlpatterns = [
    url('index/', views.index, name='index'),
    url('test_cookie/', views.test_cookie, name='test_cookie'),
    url('test_session/', views.test_session, name='test_session'),
    url('B/', views.B, name='B'),
    url('check_request/', views.check_request, name='check_request'),
    url('test_view/', views.TestView.as_view(), name='test_view'),
    url('test_tmp/', views.test_tmp, name='test_tmp'), # 测试模板继承
]