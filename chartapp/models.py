from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Room(models.Model):
    name = models.CharField(max_length=100)

    
class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)


class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.num_of_products}'
    

class Metrics(models.Model):
    heading = models.CharField(max_length=15)
    data = models.IntegerField()
    percentage = models.IntegerField()  

    def __str__(self):
        return f'{self.heading} - {self.data} - {self.percentage}'


class Finance(models.Model):
    Client = models.CharField(max_length=100 ,blank=True)
    order = models.CharField(max_length=40, null=True ,blank=True)
    cash = models.IntegerField(null=True , blank=True)
    amount = models.IntegerField(null=True)
    liquid = models.IntegerField(null=True , blank=True)
    asset =  models.IntegerField(null=True , blank=True)
    liab = models.IntegerField(null=True , blank=True)
    date = models.DateField(null=True)  


class Sales(models.Model):
    product = models.CharField(max_length=20)
    salefigures = models.IntegerField(null=True)
    units = models.IntegerField()



class Operations(models.Model):
    inventory = models.CharField(max_length=30,null=True)
    nos1 = models.IntegerField(null=True)
    nos2 = models.IntegerField(null=True)
    supply = models.CharField(max_length=40, null=True)
    avail = models.CharField(max_length=10, null=True)



class Goals(models.Model):
    class Meta:
        get_latest_by = 'milestone'
    Overall = models.IntegerField(null=True, blank=True)
    networth = models.IntegerField(null=True, blank=True)
    milestone = models.IntegerField(null=True)

class Goals1(models.Model):
    Year = models.IntegerField(null=True, blank=True)
    networth = models.IntegerField(null=True, blank=True)

class Goals2(models.Model):
    Month = models.CharField(null=True, blank=True, max_length=20)
    networth = models.IntegerField(null=True, blank=True)   




    

