from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.
class Studio(models.Model):
    name = models.CharField(max_length=30, db_index=True)

class Os(models.Model):
    name = models.CharField(max_length=30, db_index=True)


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=10,db_index=True, unique=True)
    class Meta:
        ordering = ['name',]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    os = models.ForeignKey(Os,on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=10, db_index=True)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photo_products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['name',]
        index_together = [['id', 'slug'],]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product',args=[self.id])
