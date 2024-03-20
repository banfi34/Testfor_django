from django.contrib import admin
from django.shortcuts import render

from .models import Pages


# Register your models here.

class PagesAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'page_image', 'web', 'created_at', 'updated_at')
    list_display_links = ('page_name',)


admin.site.register(Pages, PagesAdmin)
