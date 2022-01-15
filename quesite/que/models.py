from django.db import models


class FirstQue(models.Model):
    user_name = models.CharField(max_length=20, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.user_name


class SecondQue(models.Model):
    user_name = models.CharField(max_length=20, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.user_name


class ThirdQue(models.Model):
    user_name = models.CharField(max_length=20, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.user_name
