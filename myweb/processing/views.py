from django.shortcuts import render
from .models import training, testing, traintemp, testtemp, val_manual, val_auto, val_ovr
import sys
import os
from subprocess import run


def index(request):
    view_manual = val_manual.objects.all()
    view_auto = val_auto.objects.all()
    view_ovr = val_ovr.objects.all()
    view_training = training.objects.all()
    view_testing = testing.objects.all()

    context = {
        'title': 'Pemrosesan | PPL',
        'heading': 'Pemrosesan',
        'subheading': 'Analisis Sentimen Twitter',
        'db_training': view_training,
        'db_testing': view_testing,
        'db_valm': view_manual,
        'db_vala': view_auto,
        'db_valo': view_ovr,
    }
    return render(request, 'processing.html', context)


def submit(request):
    view_manual = val_manual.objects.all()
    view_auto = val_auto.objects.all()
    view_ovr = val_ovr.objects.all()
    view_training = training.objects.all()
    view_testing = testing.objects.all()

    dp = request.POST.get('data_proses')
    d1 = request.POST.get('data_latih')
    d2 = request.POST.get('data_uji')

    request.session['data_uji'] = d2

    out5 = run(
        [sys.executable, 'processing\\tocsv.py'], shell=False)

    '''os.remove('count_vectorized1.pkl')
    os.remove('model_analisis.pkl')
    os.remove('tfid_transform1.pkl')'''

    os.remove('accuracy.csv')
    os.remove('classification.csv')
    os.remove('f1.csv')
    os.remove('hasil_predict.csv')
    os.remove('hasil_processing.csv')
    os.remove('precision.csv')
    os.remove('recall.csv')
    os.remove('C:\\xampp\\temp.csv')

    os.remove('accuracy_auto.csv')
    os.remove('classification_auto.csv')
    os.remove('f1_auto.csv')
    os.remove('hasil_processing_auto.csv')
    os.remove('precision_auto.csv')
    os.remove('recall_auto.csv')

    os.remove('overall_accuracy.csv')
    os.remove('overall_precision.csv')
    os.remove('overall_recall.csv')
    os.remove('overall_f1.csv')

    cl = run(
        [sys.executable, 'processing\\cleardb.py'], shell=False)

    outdp = run(
        [sys.executable, 'processing\\insert.py', dp], shell=False)
    deldp = run(
        [sys.executable, 'processing\\delete.py'], shell=False)

    outd1 = run(
        [sys.executable, 'processing\\insert_training.py', d1], shell=False)

    outd2 = run(
        [sys.executable, 'processing\\insert_testing.py', d2], shell=False)

    deld = run(
        [sys.executable, 'processing\\deleted.py'], shell=False)

    context = {
        'title': 'Pemrosesan | PPL',
        'heading': 'Pemrosesan',
        'subheading': 'Analisis Sentimen Twitter',
        'db_training': view_training,
        'db_testing': view_testing,
        'db_valm': view_manual,
        'db_vala': view_auto,
        'db_valo': view_ovr,
    }
    return render(request, 'processing.html', context)


def save(request):
    view_manual = val_manual.objects.all()
    view_auto = val_auto.objects.all()
    view_ovr = val_ovr.objects.all()
    view_training = training.objects.all()
    view_testing = testing.objects.all()

    d2 = request.session['data_uji']

    if request.method == 'POST':
        for x in request.POST.getlist('dstrain'):
            savetrain = traintemp()
            savetrain.dat = x
            savetrain.save()

        for y in request.POST.getlist('dstest'):
            savetrain = testtemp()
            savetrain.dat = y
            savetrain.save()

    out = run(
        [sys.executable, 'processing\\migrate_train.py'], shell=False)

    out2 = run(
        [sys.executable, 'processing\\migrate_test.py'], shell=False)

    out3 = run(
        [sys.executable, 'processing\\traintocsv.py'], shell=False)

    out4 = run(
        [sys.executable, 'processing\\testtocsv.py'], shell=False)

    out5 = run(
        [sys.executable, 'processing\\tocsv.py'], shell=False)

    out6 = run(
        [sys.executable, 'processing\\processing.py', d2], shell=False)

    out7 = run(
        [sys.executable, 'processing\\model_predict.py'], shell=False)

    out8 = run(
        [sys.executable, 'processing\\predictodb.py'], shell=False)

    out9 = run(
        [sys.executable, 'processing\\migrate_train_auto.py'], shell=False)

    out10 = run(
        [sys.executable, 'processing\\migrate_test_auto.py'], shell=False)

    out11 = run(
        [sys.executable, 'processing\\insert_val_manual.py'], shell=False)

    out12 = run(
        [sys.executable, 'processing\\processing_auto.py', d2], shell=False)

    out13 = run(
        [sys.executable, 'processing\\insert_val_auto.py'], shell=False)

    outovr = run(
        [sys.executable, 'processing\\overall.py'], shell=False)

    outovr2 = run(
        [sys.executable, 'processing\\insert_overall.py'], shell=False)

    out14 = run(
        [sys.executable, 'processing\\insert_val.py'], shell=False)

    context = {
        'title': 'Pemrosesan | PPL',
        'heading': 'Pemrosesan',
        'subheading': 'Analisis Sentimen Twitter',
        'db_training': view_training,
        'db_testing': view_testing,
        'db_valm': view_manual,
        'db_vala': view_auto,
        'db_valo': view_ovr,
    }
    return render(request, 'processing.html', context)
