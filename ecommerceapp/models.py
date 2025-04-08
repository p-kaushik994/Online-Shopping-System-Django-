from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
    
class speaker(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
    
class printer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
    
class smartwatch(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
    
class monitor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name

class appliance(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
    
class topdeal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
    
class decorationitem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name

class fashiondeal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name

class earbud(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='earbuds/', blank=True, null=True)  # Image field for product

    def __str__(self):
        return self.name
