from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view
from django.utils import timezone

from .models import Market, Myteam


# Create your views here.
def index(request):
    markets = Market.objects.all()

    return render(request, 'index.html', {'markets': markets})


def myteam(request):
    myteam = Myteam.objects.all()

    return render(request, 'myteam.html', {'myteam': myteam})


# @api_view(['GET'])
def buy(request, id):
    markets = Market.objects.all()
    myteam = Myteam.objects.all()

    marketp = Market.objects.get(id=id)

    marketp.delete()

    marketp.pk = None

    tplayer = Myteam()
    tplayer.name = marketp.name
    tplayer.position = marketp.position
    tplayer.age = marketp.age
    tplayer.experience = marketp.experience
    tplayer.date_buyed = timezone.now()

    tplayer.save()

    return render(request, 'myteam.html', {'myteam': myteam})


# @api_view(['GET'])
def sell(request, id):
    markets = Market.objects.all()
    myteam = Myteam.objects.all()

    tplayer = Myteam.objects.get(id=id)

    tplayer.delete()

    tplayer.pk = None

    marketp = Market()
    marketp.name = tplayer.name
    marketp.position = tplayer.position
    marketp.age = tplayer.age
    marketp.experience = tplayer.experience
    marketp.date_buyed = timezone.now()

    marketp.save()

    return render(request, 'index.html', {'markets': markets})

