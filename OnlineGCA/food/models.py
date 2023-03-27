from django.db import models

# Create your models here.
class Food(models.Model):
    item_name = models.CharField(max_length= 240)
    item_description = models.CharField(max_length= 240)
    item_price = models.IntegerField()
