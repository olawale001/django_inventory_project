from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20)  # e.g., kg, liters, pieces

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()
    images = models.FileField(upload_to='media', blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='ItemIngredient')

    def __str__(self):
        return self.name

class ItemIngredient(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='OrderItem')
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Order {self.id} by {self.customer.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Sale(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    date_sold = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sale {self.id} from Order {self.order.id}'

