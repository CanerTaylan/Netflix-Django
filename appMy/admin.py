from django.contrib import admin
from .models import *


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    '''Admin View for Series'''

    list_display = ('title', 'image')


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    '''Admin View for Films'''

    list_display = ('title', 'image')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    '''Admin View for Categories'''


@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    '''Admin View for Contents'''

    list_display = ('title','Categories')