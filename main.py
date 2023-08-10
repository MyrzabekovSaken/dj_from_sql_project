from utils import create_categories, create_customers, create_cities, create_order_history, create_products, create_warehouse, create_product_cities, create_products_orderhistory
from db.models import Categories, Customers, Cities, OrderHistory, Products, Warehouse, ProductsOrderHistory, ProductCities
from django.db.models import Sum, F, ExpressionWrapper, IntegerField, FloatField
from django.db.models import Count, Avg, Min, Max


create_categories()
create_customers()
create_cities()
create_order_history()
create_products()
create_warehouse()
create_product_cities()
create_products_orderhistory()


# 1. Вычисление общей суммы всех товаров.
total_sum = Products.objects.aggregate(total_sum=Sum(F('product_count') * F('price')))['total_sum']
print(total_sum)


# 2. Вычисление общей суммы каждого продукта.
products_with_total_price = Products.objects.annotate(total_price=((F('price') * F('product_count')))).values('title', 'product_count', 'price', 'total_price')
for product in products_with_total_price:
    print(product)


# 3. Выбор данных по компаниям, кол-во товаров и сортировка по алфавиту.
products_distinct_company = Products.objects.values('company', 'product_count', 'title').distinct().order_by('company')
for product in products_distinct_company:
    print(product)


# 4. Соединение таблицы товары и категории.
products_with_category = Products.objects.select_related('category').values('title', 'company', 'product_count', 'price', 'category__title')
for product in products_with_category:
    print(product)


# 5. Выявление кол-во продуктов в разных города. 
products_with_city = Warehouse.objects.select_related('product__title', 'city__title').values('product__title', 'city__title', 'product_count')
for product in products_with_city:
    print(product)


# 6. Вычисление кол-во всех представленных компании, общее кол-во товара, мин. цена товара, макс. цена товара и средняя цена всех товаров.
result = Products.objects.aggregate(
    companies_count=Count('company', distinct=True), 
    total_count=Sum('product_count'), 
    min_price=Min('price'), 
    max_price=Max('price'), 
    avg_price=Avg('price'))
print(result)


# 7. Вычисление общее кол-во продуктов в трех городах.
products_in_cities = Cities.objects.annotate(total_products=Sum('warehouse__product_count')).values('title', 'total_products')
print(products_in_cities)


# 8. Вычисление кол-во представленных компании в трех городах.
companies_in_cities = Cities.objects.annotate(
    total_products=Sum('warehouse__product_count')).annotate(
    company=F('warehouse__product__company')).values('title', 'company', 'total_products').order_by('title')
for company in companies_in_cities:
    print(company)


# 9. Список покупателей,товаров и дата покупки.
order_list = ProductsOrderHistory.objects.select_related(
    'products__title',
    'customer__first_name'
).values(
    'products__title',
    'orderhistory__customer__first_name',
    'orderhistory__order_date'
)
for order in order_list:
    print(order)


# 10. Покупатель совершивший больше одной покупки. 
customer_order = Customers.objects.annotate(order_count=Count('orderhistory')).filter(order_count__gt=1).values('first_name', 'order_count')
print(customer_order)


# 11. Определение больше всего проданных товаров за месяц.
product_more_sold = Products.objects.annotate(total_sales=Count('productsorderhistory')).filter(total_sales__gt=2).values('id', 'title', 'total_sales')
print(product_more_sold)

