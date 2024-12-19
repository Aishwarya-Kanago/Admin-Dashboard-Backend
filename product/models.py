from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued'),
    ]

    name = models.CharField(max_length=255)
    product_pic = models.CharField(max_length=500,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Stock quantity
    sales = models.PositiveIntegerField(default=0)
    active = models.CharField(max_length=255,blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock')  # Product status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically update status based on stock
        if self.stock == 0:
            self.status = 'out_of_stock'
        elif self.status != 'discontinued':  # Prevent overriding manually set status
            self.status = 'in_stock'
        super().save(*args, **kwargs)