from django.db import models
from django.core.exceptions import ValidationError

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.supplier_name

    def clean(self):
        if not self.supplier_name:
            raise ValidationError("Supplier name is required")

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    expiry_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ingredient_name} ({self.stock_quantity} {self.unit})"

    def clean(self):
        if self.stock_quantity < 0:
            raise ValidationError("Stock quantity cannot be negative")

class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=100)
    recipe = models.JSONField()  # Store ingredient quantities as JSON
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item_name} - ${self.price}"

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.menu_item_name} x{self.quantity} ({self.order_date})"
