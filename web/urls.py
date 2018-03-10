from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from web import views,urls
urlpatterns =[


    url(r'^start', views.start),
    ]