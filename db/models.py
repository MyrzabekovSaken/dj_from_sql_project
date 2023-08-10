from django.db import models
from manage import init_django

init_django()


class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Customers(models.Model):
    first_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Customers"


class Cities(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Cities"


class OrderHistory(models.Model):
    order_date = models.DateTimeField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer_id} {self.order_date}"

    class Meta:
        verbose_name_plural = "OrderHistory"


class Products(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    product_count = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.company} {self.product_count} {self.price} {self.category_id}"

    class Meta:
        verbose_name_plural = "Products"


class Warehouse(models.Model):
    product_count = models.IntegerField()
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city_id} {self.product_id} {self.product_count}"

    class Meta:
        verbose_name_plural = "Warehouse"


class ProductsOrderHistory(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    orderhistory = models.ForeignKey(OrderHistory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.products_id} {self.orderhistory_id}"

    class Meta:
        verbose_name_plural = "ProductsOrderHistory"


class ProductCities(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    cities = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.products_id} {self.cities_id}"

    class Meta:
        verbose_name_plural = "ProductCities"
