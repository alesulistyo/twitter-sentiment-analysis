from django.db import models


class tdata(models.Model):
    date = models.DateField()
    user = models.TextField()
    tweets = models.TextField()
    usage = models.IntegerField()

    def __str__(self):
        return "{}".format(self.date)
