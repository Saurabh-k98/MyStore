from django.db import models

class Promotion(models.Model):
    discription = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title =models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')


class Product(models.Model):
    title       = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    inventory   = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection  = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEAMBERSHIP_BRONZE = 'B'
    MEAMBERSHIP_SILVER = 'S'
    MEAMBERSHIP_GOLD   = 'G'
    MEAMBERSHIP_CHOICES = [
        (MEAMBERSHIP_BRONZE,'BRONZE'),
        (MEAMBERSHIP_SILVER,'SILVER'),
        (MEAMBERSHIP_GOLD,'GOLD')]
    
    f_name      = models.CharField(max_length=255)
    l_name      = models.CharField(max_length=255)
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=15, unique=True)
    dob         = models.DateField(null=True)
    meambership = models.CharField(max_length=1, choices=MEAMBERSHIP_CHOICES, default=MEAMBERSHIP_BRONZE)


class Order(models.Model):
    PMT_PENDING    = 'P'
    PMT_COMPLETED  = 'C'
    PMT_FAILED     = 'F'
    PMT_STATUS     = [(PMT_PENDING,'PENDING'),(PMT_COMPLETED,'COMPLETED'),(PMT_FAILED,'FAILED')]
    placed_at      = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PMT_STATUS, default=PMT_PENDING)
    customer       = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity= models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
