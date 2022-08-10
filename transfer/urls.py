from . import views
from django.urls import path

app_name = 'transfer'

urlpatterns = [
    path('', views.index, name='index'),
    path('myteam', views.myteam, name='myteam'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('sell/<int:id>/', views.sell, name='sell'),
]
