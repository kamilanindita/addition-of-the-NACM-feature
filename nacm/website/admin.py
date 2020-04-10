from django.contrib import admin
from . models import Connect
from . models import Ip
from . models import c_Setting
# Register your models here.

admin.site.register(Connect)
admin.site.register(Ip)
admin.site.register(c_Setting)