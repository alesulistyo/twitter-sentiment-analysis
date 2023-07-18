from django.shortcuts import render
from .models import tdata
import sys
import requests
import os
from subprocess import run


def index(request):
    view_tweet = tdata.objects.filter(usage__lte='1').order_by('-date')
    count_tweet = tdata.objects.count()

    context = {
        'title': 'Tweets | PPL',
        'heading': 'Tweets',
        'subheading': 'Analisis Sentimen Twitter',
        'db_tdata': view_tweet,
        'count_tdata': count_tweet,
    }
    return render(request, 'tweets.html', context)


def submit(request):
    i = request.POST.get('data_num')
    out = run(
        [sys.executable, 'tweets\\crawling.py', i], shell=False)
    out2 = run(
        [sys.executable, 'tweets\\import.py'], shell=False)

    os.remove('hasil_crawling.csv')

    view_tweet = tdata.objects.filter(usage__lte='1').order_by('-date')
    count_tweet = tdata.objects.count()

    context = {
        'title': 'Tweets | PPL',
        'heading': 'Tweets',
        'subheading': 'Analisis Sentimen Twitter',
        'db_tdata': view_tweet,
        'count_tdata': count_tweet,
    }
    return render(request, 'tweets2.html', context)
