from django.contrib import admin
from .models import Coverpic
# Register your models here.


class CoverpicAdmin(admin.ModelAdmin):
    list_display = ['show_image','title','approved','slide','link',]


admin.site.register(Coverpic , CoverpicAdmin)

