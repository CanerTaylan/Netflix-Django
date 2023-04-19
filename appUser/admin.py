from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):

    list_display = ('user', 'title', 'id')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = ('user', 'tel', 'id')
