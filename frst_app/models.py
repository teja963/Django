from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=13, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
      
    def __str__(self):
      return self.name
   


class tag(models.Model):
    name = models.CharField(max_length = 200, null = True)
      
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
    description =models.CharField(max_length = 200, null = True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tag = models.ManyToManyField(tag)  # for many to many table(coustomer , product)
    
    def __str__(self):
      return self.name


   
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
    customer = models.ForeignKey(customer, null = True, on_delete= SET_NULL) # many to many relationship
    product = models.ForeignKey(product, null= True, on_delete=SET_NULL) # many to many relationship
    date_created = models.DateTimeField(auto_now_add = True, null = True)
   
    
    def __str__(self):
      return self.name