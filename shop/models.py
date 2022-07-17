from django.db import models

# Create your models here.


class Product(models.Model):
    Name=models.CharField(max_length=80, null=True, blank=False)
    current_price=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=False)
    previous_price=models.DecimalField(max_digits=7, decimal_places=2,blank=True, null=True)
    ShortDescription = models.TextField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Stock = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/product/', blank=True)


    def __str__(self):
        return self.Name


class Contact(models.Model):
    FullName = models.CharField(max_length=80, null=True, blank=False)
    Subject = models.CharField(max_length=255, null=True, blank=False)
    Email = models.EmailField(max_length=80, error_messages ={"unique":"Please enter your email address."}, null=True, blank=False)
    Message = models.TextField(blank=False, null=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.FullName