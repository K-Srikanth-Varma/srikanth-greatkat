from django.urls import reverse
from enum import auto
from django.db import models
from Category.models import category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=220, unique=True)
    slug         = models.SlugField(max_length=220, unique=True)
    discription  = models.TextField(max_length=500, unique=True)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/products')
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name