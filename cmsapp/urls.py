from argparse import Namespace
from django.urls import URLPattern, path , include 
from . import views



app_name = "cmsapp"

urlpatterns = [
    path('', views.index , name = 'index'),
    path('article/<str:slug>' , views.detail , name = 'detail'),
    path('category/<str:slug>' , views.category , name = 'category'),
    path('create-post',views.createPost, name = 'create'),
    path('update-post/<str:slug>',views.updatePost, name = 'update'),
    path('delete-post/<str:slug>',views.deletePost, name = 'delete'),
    path('tag/<str:slug>',views.tag, name = 'tag'),

]