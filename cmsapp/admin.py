from django.contrib import admin
from .models import IpModel, Post , Category , Tags, User

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['show_image' , 'title' ,  'writer' ,'category' ,'approved']
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']

admin.site.register(Post , PostAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(User)
admin.site.register(IpModel)