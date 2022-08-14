from django.contrib import admin

# Register your models here.
from .models import Market, Myteam, League, Team

admin.site.register(Market)
admin.site.register(Myteam)
admin.site.register(League)
admin.site.register(Team)