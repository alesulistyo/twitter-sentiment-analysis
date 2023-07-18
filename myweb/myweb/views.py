from django.shortcuts import render


def index(request):
    context = {
        'title': 'Analisis Sentimen Twitter | PPL',
        'heading': 'Analisis Sentimen Twitter',
        'subheading': 'Kelompok 4',
        'foot': 'Kelompok 4',
    }
    return render(request, 'index.html', context)
