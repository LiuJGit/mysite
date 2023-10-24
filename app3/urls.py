'''
app 新建 urls.py 文件
'''

from django.urls import re_path as url
import app3.views as views

app_name = 'app3' # 设置 app namespace
urlpatterns = [
    url(r'set_session/$',views.SetSession.as_view(), name='set_session'),
    url(r'get_session/$',views.GetSession.as_view(), name='get_session'),
    url(r'login/$',views.LoginView.as_view(), name='login'),
    url(r'rece/$',views.ReceiveView.as_view(), name='rece'),
]