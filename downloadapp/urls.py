from unicodedata import name
from django import urls
from django.urls import URLPattern, path , include , re_path
from . import views



urlpatterns = [
    path('download', views.download , name = 'download'),
    #path('download/submit/<str:pk>', views.submit , name = 'submit'),
    path('download/submit/<str:pk>', views.client_add , name = 'client_add'),
    path('download/list/<str:pk>', views.download_list , name = 'download_list'),
]