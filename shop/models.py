from django.db import models
from .helpers import SaveMedia, StatusChoicesPb


class Country(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=['name']),
                   models.Index(fields=['description']),
                   ]

    def __str__(self):
        return self.name


class Quality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=2, choices=[
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ])

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, choices=[
        ('Qora', 'Qora'),
        ('Oq', 'Oq'),
        ('Qizil', 'Qizil'),
        ('Kok', 'Kok'),
        ('Yashil', 'Yashil'),

    ])

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price1 = models.FloatField()
    price2 = models.FloatField()
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    count = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    quantity = models.PositiveIntegerField(default=1)
    featured = models.BooleanField(default=False)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=StatusChoicesPb.choices, default=StatusChoicesPb.PUBLIC)
    shipping_days = models.IntegerField(default=0)
    shipping_date = models.DateField()
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=['name']), ]

    def __str__(self):
        return self.name
