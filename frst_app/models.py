from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=13, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
      
    def __str__(self):
      return self.name
   

class product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(max_length = 10)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description =models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)


class order(models.Model):
    STATUS = (
          ('Pending', 'Pending'),
          ('Out of Delivery','Out of Delivery'),
          ('Delivered', 'Delivered'),
    )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(max_length = 10)
    category = models.CharField(max_length = 200, null = True)
    status =models.CharField(max_length = 200, null = True, choices = STATUS)  # Drop down menu
    date_created = models.DateTimeField(auto_now_add = True, null = True)