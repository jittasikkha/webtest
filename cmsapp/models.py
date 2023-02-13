from django import views
from django.db import models
import uuid
from ckeditor.fields import RichTextField
from profiles.models import UserProfile
from django.utils.html import format_html



class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ip

class Post(models.Model):
    writer = models.ForeignKey(UserProfile,on_delete=models.SET_NULL , null= True , blank=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'img')
    intro = models.TextField(max_length=300 , blank=True)
    body = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4 , primary_key= True , unique=True ,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,blank=True,null=True)
    approved = models.BooleanField(default=False)
    tag = models.ManyToManyField('Tags')
    views = models.IntegerField(default=0)
    
    def get_queryset(self):
        return Post.objects.filter('approved'==True).all()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self) -> str:
        return self.title
    

    def show_image(self):
        return format_html('<img src="' + self.image.url + '" height="40px">')
    show_image.allow_tags = True
    




class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True , unique=True ,editable=False )
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title
    

class Tags(models.Model):
    tag = models.CharField(max_length=50 , unique= True , blank= True)
    slug = models.SlugField()
    def __str__(self) -> str:
        return self.tag


class User(models.Model):
    user = models.TextField(default=None)

    def __str__(self) -> str:
        return self.user