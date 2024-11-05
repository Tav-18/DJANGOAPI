from django.db import models

# Create your models here.

class Generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    tipo_genero = models.CharField(max_length=255)


    class Meta:
        db_table = "generos"
        

class Usuarios(models.Model):
    Usuarios_id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Generos,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "usuarios"
        
        
from django.db import models
from django.contrib.auth.models import User

# Modelo para la categoría de productos (opcional si tienes categorías)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Modelo para el producto
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Modelo para el carrito de un usuario
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

# Modelo para los elementos dentro del carrito
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.user.username}'s cart"

    def total_price(self):
        return self.product.price * self.quantity

# Modelo de pedido
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ])

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# Modelo para los elementos del pedido
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"
