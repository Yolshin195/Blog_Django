"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from . import views

urlpatterns = [
        url(r'^1/', views.basic_one),
        url(r'^2/', views.template_two),
        url(r'^3/', views.template_three_simple),

        url(r'^articles/all/$', views.articles),

        url(r'^articles/addcoment/(?P<article_id>\d+)/$',
            views.addcomment
        ),
        url(r'^articles/addlike/(?P<article_id>\d+)/$',
            views.addlike, name="addlike"
        ),
        url(r'^articles/get/(?P<article_id>\d+)/$',
            views.article, name='article'
        ),

        url(r'^page/(\d+)/$', views.articles),

        url(r'^', views.articles, name='main'),
]

