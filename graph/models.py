from django.db import models

# Create your models here.

# class Stock(models.Model):
#     timestamp = models.DateTimeField(null=True)
#     actual_price = models.FloatField(default=0, null=False)
#     predicted_price = models.FloatField(default=0, null=False)
#     company = models.TextField(max_length=5)

class Stocks(models.Model):
    company = models.TextField(max_length=5)
    actual_price = models.FloatField()
    predicted_price = models.FloatField()
    timestamp = models.DateTimeField(null=True)


