from django.shortcuts import render
from .models import predata
import sys
import os
from subprocess import run


def index(request):
    view_predata = predata.objects.all()
    count_predata = predata.objects.count()

    context = {
        'title': 'Pra-pemrosesan | PPL',
        'heading': 'Pra-pemrosesan',
        'subheading': 'Analisis Sentimen Twitter',
        'db_predata': view_predata,
        'count_predata': count_predata,

    }
    return render(request, 'preprocessing.html', context)


def submit(request):
    i = request.POST.get('data_proc')
    out = run(
        [sys.executable, 'preprocessing\\preprocessing.py', i], shell=False)
    out2 = run(
        [sys.executable, 'preprocessing\\import.py'], shell=False)
    out3 = run(
        [sys.executable, 'preprocessing\\delete.py'], shell=False)

    view_predata = predata.objects.all()
    count_predata = predata.objects.count()

    os.remove('hasil_preprocessing.csv')

    context = {
        'title': 'Pra-pemrosesan | PPL',
        'heading': 'Pra-pemrosesan',
        'subheading': 'Analisis Sentimen Twitter',
        'db_predata': view_predata,
        'count_predata': count_predata,

    }
    return render(request, 'preprocessing.html', context)
