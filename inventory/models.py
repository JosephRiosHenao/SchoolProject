from django.db import models

from app.models import MetaInfoBase

# Create your models here.
class Category(MetaInfoBase):
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description

    def save(self):
        self.description = self.description.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(MetaInfoBase):
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}:{}".format(self.category.description, self.description)
    
    def save(self):
        self.description = self.description.upper()
        super(SubCategory, self).save()
    
    class Meta:
        verbose_name_plural = "SubCategories"
        unique_together = ('category', 'description')