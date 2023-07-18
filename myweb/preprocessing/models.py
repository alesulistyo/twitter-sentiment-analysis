from django.db import models

# Create your models here.


class predata(models.Model):
    original = models.TextField()
    casefolding = models.TextField()
    tokenization = models.TextField()
    stopword = models.TextField()
    stemming = models.TextField()
    result = models.TextField()

    def __str__(self):
        return "{}".format(self.original)
