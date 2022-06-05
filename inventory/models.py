from django.db import models

from app.models import MetaInfoBase

from django.contrib.auth.models import User

# Create your models here.
class Category(MetaInfoBase):
    description = models.CharField(max_length=100, unique=True, default='')
    
    def __str__(self): return self.description

    def save(self):
        self.description = self.description.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(MetaInfoBase):
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): return "{}:{}".format(self.category.description, self.description)
    
    def save(self):
        self.description = self.description.upper()
        super(SubCategory, self).save()
    
    class Meta:
        verbose_name_plural = "SubCategories"
        unique_together = ('category', 'description')
        
class Brand(MetaInfoBase):
    description = models.CharField(max_length=100, unique=True)
    
    def __str__(self): return self.description
    
    def save(self):
        self.description = self.description.upper()
        super(Brand, self).save()
        
    class Meta:
        verbose_name_plural = "Brands"
        
class UnitMeter(MetaInfoBase):
    description = models.CharField(max_length=100, unique=True)
    
    def __str__(self): return self.description
    
    def save(self):
        self.description = self.description.upper()
        super(UnitMeter, self).save()
    
    class Meta:
        verbose_name_plural = "UnitMeters"

class Product(MetaInfoBase):
    code = models.CharField(max_length=20, unique=True)
    code_bar = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    last_buy = models.DateField(blank=True, null=True)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    unit_meter = models.ForeignKey(UnitMeter, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self): return self.description
    
    def save(self):
        self.description = self.description.upper()
        super(Product, self).save()
    
    class Meta:
        unique_together = ('code', 'code_bar')
        verbose_name_plural = "Products"