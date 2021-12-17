from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import UrlForm, UrlFormPrem
from .models import Url
from django.contrib import messages
from django.template import RequestContext
import random
import string
import datetime
import json


def createRandUrl():
    symbols = string.ascii_letters+string.digits
    newUrl = ''
    i = 0
    while i<8:
        newUrl = newUrl+random.choice(symbols)
        i+=1
    if Url.objects.filter(shortUrl = newUrl).exists():
        return createUrl
    return newUrl


def home(request):
    return render(request, 'urlShortener/home.html')

#random URL-ის გენერაცია:

def shortener(request):
    form = UrlForm()
    data = Url()
    context = {'form':form}
    if request.method == 'GET':
        return render(request, 'urlShortener/shortener.html', context)
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            data.url = request.POST.get('url')
            data.shortUrl = createRandUrl()
            data.exp_date = datetime.datetime.today()+datetime.timedelta(days = 30)
            data.premiumType = False
            data.visited = 0
            data.save()
            context = {'data': data}
            return render(request, 'urlShortener/shortedUrl.html', context)


#Premium URL-ის გენერაცია

def premium(request):
    form = UrlFormPrem()
    data = Url()
    context = {'form':form}
    if request.method == 'GET':
        return render(request, 'urlShortener/premium.html', context)
    if request.method == 'POST':
        form = UrlFormPrem(request.POST)
        if form.is_valid():
            data.url = request.POST.get('url')
#            if Url.objects.filter(shortUrl = 'sdasda').exists():
#                message = messages.error(request, 'Url already exists')
#                return redirect('premium')
            data.shortUrl = request.POST.get('shortUrl')
            data.exp_date = datetime.datetime.today()+datetime.timedelta(days = 30)
            data.premiumType = True
            data.visited = 0
            data.save()
            context = {'data': data}
            return render(request, 'urlShortener/shortedUrl.html', context)


def redirectUrl(request, shorted):
    try:
        shortener = Url.objects.get(shortUrl = shorted)
        shortener.visited += 1
        shortener.save()
        return HttpResponseRedirect(shortener.url)
    except:
        return render(request, 'urlShortener/noExist.html')
