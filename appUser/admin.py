from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''

    list_display = ('user','title','id')
    