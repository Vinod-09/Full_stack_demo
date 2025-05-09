from django.db import models

# Create your models here.
class Mobile_List(models.Model):
    brand_name = models.CharField(max_length=155)
    price = models.FloatField()

    def __str__(self):
        return f"{self.brand_name} -- {self.price}"

class Mobile_Features(models.Model):
    storage = models.CharField(max_length=120)
    processor = models.CharField(max_length=120)
    battery = models.CharField(max_length=120)
    mobile = models.ForeignKey(Mobile_List,on_delete=models.CASCADE, related_name='features')

    def __str__(self):
        return f"{self.mobile.brand_name} -- {self.processor}"