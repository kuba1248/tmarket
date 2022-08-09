from . import views
from django.urls import path

app_name = 'transfer'

urlpatterns = [
    path('', views.index, name='index'),
]
