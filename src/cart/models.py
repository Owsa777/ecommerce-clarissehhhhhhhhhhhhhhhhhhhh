from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

User = get_user_model()


class Address(models.Model):
    ADDRESS_CHOISES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address_line_1 = models.CharField(max_length = 100)
    address_line_2 = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 100)
    address_type = models.CharField(max_length = 1, choices = ADDRESS_CHOISES)
    default = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.address_line_1}. {self.address_line_2}, {self.city}, {self.zip_code}"

    class Meta:
        verbose_name_plural = 'Addresses'

class ColourVariation(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class SizeVariation(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique = True)
    image = models.ImageField(upload_to = 'product_images')
    description = models.TextField()
    price = models.FloatField(default = 0)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = False)
    available_colour = models.ManyToManyField(ColourVariation)
    available_sizes = models.ManyToManyField(SizeVariation)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={'slug':self.slug})

    def get_price(self):
        return self.price

class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name = 'items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    colour = models.ForeignKey(ColourVariation, on_delete = models.CASCADE)
    size = models.ForeignKey(SizeVariation, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    def get_raw_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_item_price(self):
        price = self.get_raw_total_item_price()
        return price


class Order(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)
    start_date = models.DateTimeField(auto_now_add = True)
    order_date = models.DateTimeField(blank = True, null = True)
    ordered = models.BooleanField(default = False)

    billing_address = models.ForeignKey(
        Address, related_name = 'billing_address', blank = True, null = True, on_delete = models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name = 'shipping_address', blank = True, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    payment_methos = models.CharField(max_length = 25, choices = (
    ('paypal', 'tarjeta'),
    ))
    timestamp = models.DateTimeField(auto_now_add = True)
    succesful = models.BooleanField(default = False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.reference_number


    @property
    def  reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"

def pre_save_product_receiver(sender, instance, *args, **kwards):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_product_receiver, sender = Product )
