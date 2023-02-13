from datetime import datetime
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Coverpic(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'img', null = True , blank = True)
    approved = models.BooleanField(default=False)
    slide = models.BooleanField(default=False)
    link = models.CharField(max_length=200 , null=True , blank=True)
    created = models.DateTimeField(default=datetime.now , blank=True)
    

    def get_queryset(self):
        return Coverpic.objects.filter('approved'==True).all()
    
    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title
    
    def show_image(self):
        return format_html('<img src="' + self.image.url + '" height="30">')
    show_image.allow_tags = True
