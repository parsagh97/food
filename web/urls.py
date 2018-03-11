from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from web import views,urls
from web.views import *
urlpatterns =[


    url(r'^register/', register.as_view(), name='register'),
    ]