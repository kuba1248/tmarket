from django.shortcuts import render

from .models import Market, Myteam


# Create your views here.
def index(request):
    markets = Market.objects.all()

    return render(request, 'index.html', {'markets': markets})
