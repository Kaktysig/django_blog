"""django_site_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import list_view, create_new_article, delete_view, article_view, create_new_comment, update_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', list_view, name='home'),
    url(r'^(?P<page>\d+)/$', list_view, name='homepage'),
    url(r'^create/$', create_new_article, name='create_new_article'),
    url(r'^delete/(?P<article_id>\d+)/$', delete_view, name='delete_article'),
    url(r'^article/(?P<article_id>\d+)/$', article_view, name='article'),
    url(r'^createcomment/(?P<article_id>\d+)/$', create_new_comment, name='create_new_comment'),
    url(r'^update/(?P<article_id>\d+)/$', update_view, name="update_article"),

]
