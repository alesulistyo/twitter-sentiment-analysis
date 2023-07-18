from django.shortcuts import render
from .models import val_data


def index(request):
    view_val = val_data.objects.all()

    context = {
        'title': 'Validasi | PPL',
        'heading': 'Validasi',
        'subheading': 'Analisis Sentimen Twitter',
        'db_val': view_val,
    }
    return render(request, 'validation.html', context)
