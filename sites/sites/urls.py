# -*- coding: utf-8 -*-
"""sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/blog/', permanent=True)),
    url(r'^blog/$',login),
    url(r'^blog/logout/$',logout),
    url(r'^index/$',index),
    url(r'^blog/(?P<username>[-\w]+)/$', blog_detail, name='blog_detail'),
    url(r'^blog/(?P<username>[-\w]+)/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^post/update/(?P<username>[-\w]+)/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    url(r'^post/create/$', create_post, name='create_post'),
    url(r'^post/delete/(?P<username>[-\w]+)/(?P<pk>\d+)/$', delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
