"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'book/', include('book.urls')), # book 子应用

    # 子应用 app1，两个实例：author, publisher，测试 instance namespace
    # url(r'author/', include('app1.urls', namespace='app1')), # instance namespace 与 app namespace 同名，相当于设置了 app namespace 的默认值
    url(r'author/', include('app1.urls', namespace='app1_author')), # 这里设置的是 instance namespace
    url(r'publisher/', include('app1.urls', namespace='app1_publisher')), # 若不存在 instance 与 app 同名的情况，则 app namespce 默认值为最后一个
]
