from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    rate = models.FloatField()
    abbreviation = models.CharField(max_length=3)
    exchange_date = models.DateField()
