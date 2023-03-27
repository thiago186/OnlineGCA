from django.db import models

# Create your models here.
class Food(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length= 240)
    item_description = models.CharField(max_length= 240)
    item_price = models.IntegerField()
