from django.contrib import admin
from .models import *
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['Image',]


admin.site.register(Gallery,GalleryAdmin)