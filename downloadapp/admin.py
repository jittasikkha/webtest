from django.contrib import admin
from .models import Subject , File , Room , Province , Client , Role
# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ['name' , 'created' ,  'subject' ,'approved']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name' ,'approved']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name' ,'email' , 'province']
    list_filter = ('file', 'province')

class RoleAdmin(admin.ModelAdmin):
    list_display = ['role' ]

admin.site.register(Subject , SubjectAdmin)
admin.site.register(File , FileAdmin)
admin.site.register(Room)
admin.site.register(Role)
admin.site.register(Province)
admin.site.register(Client , ClientAdmin)