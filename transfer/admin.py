from django.contrib import admin

# Register your models here.
from .models import Market, Myteam

admin.site.register(Market)
admin.site.register(Myteam)