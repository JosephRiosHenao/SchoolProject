from django.db import models

from app.models import MetaInfoBase
from inventory.models import Product

# Create your models here.
class Provider(MetaInfoBase):
    description = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    contact = models.CharField(max_length=100)
    telphone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.description, self.contact)


class BuyHead(MetaInfoBase):
    date_buy = models.DateField(null=True, blank=True)
    observation = models.TextField(max_length=200, null=True, blank=True)
    no_fact = models.CharField(max_length=100)
    date_fact = models.DateField()
    sub_total = models.FloatField(default=0)
    offert = models.FloatField(default=0)
    total = models.FloatField(default=0)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.observation)
    
    def save(self):
        self.observation = self.observation.upper()
        if self.sub_total == None  or self.offert == None:
            self.sub_total = 0
            self.offert = 0
        self.total = self.sub_total - self.offert
        super(BuyHead, self).save()

class BuyData(MetaInfoBase):
    buy = models.ForeignKey(BuyHead, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.BigIntegerField(default=0)
    price = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    offert = models.FloatField(default=0)
    total = models.FloatField(default=0)
    sell = models.FloatField(default=0)
    
    def __str__(self):
        return self.product
    
    def save(self):
        self.sub_total = float(float(int(self.stock)) * float(self.price))
        self.total = self.sub_total - float(self.offert)
        super(BuyData, self).save()