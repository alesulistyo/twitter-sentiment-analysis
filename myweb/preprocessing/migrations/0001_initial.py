# Generated by Django 2.2.17 on 2020-11-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='predata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.TextField()),
                ('casefolding', models.TextField()),
                ('tokenization', models.TextField()),
                ('stopword', models.TextField()),
                ('stemming', models.TextField()),
                ('result', models.TextField()),
            ],
        ),
    ]
