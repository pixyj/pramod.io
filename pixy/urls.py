"""pixy URL Configuration

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

from home.views import home
from blog.views import get_blog_post, blog_home
from contact.views import contact
from about.views import about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<slug>[\w\d\-]+)/$', get_blog_post),
    url(r'^blog/$', blog_home),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^$', home)
]
