from django.contrib import admin
from .models import *

# Register your models here.
class sertificatAdmin(admin.ModelAdmin):
    list_display = ['id','name','serya']
    list_display_links = ['id','name',]

admin.site.register(Sertificate,sertificatAdmin) 