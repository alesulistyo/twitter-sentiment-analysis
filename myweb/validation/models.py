from django.db import models

# Create your models here.

from django.db import models


class val_data(models.Model):
    date = models.DateField()
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    f1 = models.FloatField()

    def __str__(self):
        return "{}".format(self.date)
