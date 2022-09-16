from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = "products" # do this if there is files outside project


class User(models.Model):
    # will have only id field
    pass

    class Meta:
        app_label = "products"  # do this if there is files outside project
