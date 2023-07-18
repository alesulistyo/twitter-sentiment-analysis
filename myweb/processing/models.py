from django.db import models

# Create your models here.


class training(models.Model):
    tweets = models.TextField()
    manual = models.TextField()
    auto = models.TextField()
    dtype = models.TextField()

    def __str__(self):
        return "{}".format(self.tweets)


class testing(models.Model):
    tweets = models.TextField()
    manual = models.TextField()
    auto = models.TextField()
    dtype = models.TextField()

    def __str__(self):
        return "{}".format(self.tweets)


class traintemp(models.Model):
    dat = models.TextField()

    def __str__(self):
        return "{}".format(self.dat)


class testtemp(models.Model):
    dat = models.TextField()

    def __str__(self):
        return "{}".format(self.dat)


class val_manual(models.Model):
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    f1 = models.FloatField()

    def __str__(self):
        return "{}".format(self.accuracy)


class val_auto(models.Model):
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    f1 = models.FloatField()

    def __str__(self):
        return "{}".format(self.accuracy)


class val_ovr(models.Model):
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    f1 = models.FloatField()

    def __str__(self):
        return "{}".format(self.accuracy)
