from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    kategorismi= models.CharField(max_length=70)
    slug= models.SlugField(default="", null=False, unique=True, db_index=True,max_length=70)

    def __str__(self):
        return f"{self.kategorismi}"

class Shop(models.Model):
    marka = models.CharField(max_length=50)
    urunismi=models.CharField(max_length=50 )
    aciklama = models.TextField()
    resimUrl = models.CharField(max_length=200)
    fiyat = models.IntegerField()
    fiyatbirim= models.CharField(max_length=10)
    isActive =models.BooleanField()
    slug = models.SlugField(default="", null= False, unique=True, db_index=True )
    kategoriler = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.urunismi}"
class sepet(models.Model):
    marka = models.CharField(max_length=50)
    urunismi = models.CharField(max_length=50)
    aciklama = models.TextField()
    resimUrl = models.CharField(max_length=200)
    fiyat = models.IntegerField()
    fiyatbirim = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.urunismi}"
class Slider(models.Model):
    marka = models.CharField(max_length=100)
    urunismi = models.CharField(max_length=50)
    resimUrl = models.CharField(max_length=200)
    is_active= models.BooleanField(default=False)
    shop = models.ForeignKey(Shop , on_delete=models.SET_NULL, null=True , blank=True)

    def __str__(self):
        return f"{self.urunismi}"


