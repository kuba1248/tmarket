from . import views
from django.urls import path

app_name = 'transfer'

urlpatterns = [
    path('', views.index, name='index'),
    path('myteam', views.myteam, name='myteam'),
    path('lteam/<int:id>/', views.lteam, name='lteam'),
    path('league', views.league, name='league'),
    path('match', views.match, name='match'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('sell/<int:id>/', views.sell, name='sell'),
    path('reserve/<int:id>/', views.reserve, name='reserve'),
    path('onstart/<int:id>/', views.onstart, name='onstart'),

    path('simulation/', views.welcome, name='welcome'), #starting page

    path('simulation/selection', views.get_teams, name='selection'), #pattern for input page

    path('simulation/simulate', views.simulate, name='simulate'), #pattern for the simulation page
]
