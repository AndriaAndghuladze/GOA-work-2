from django.db import models

#მიგრაცია არის კოდის გადაკეთება და ბაზაში ტექსტის ცვლილება. 
# Create your models here.
class Product(models.Model):
    title = models.CharField()
    price = models.CharField()
    category = models.CharField()

products = [
    ("Wireless Mouse", 25.99, "Electronics"),
    ("Mechanical Keyboard", 79.99, "Electronics"),
    ("Gaming Monitor", 249.99, "Electronics"),
    ("USB-C Charger", 19.99, "Accessories"),
    ("Bluetooth Speaker", 59.99, "Electronics"),
    ("Running Shoes", 89.99, "Footwear"),
    ("Leather Wallet", 34.99, "Accessories"),
    ("Backpack", 49.99, "Bags"),
    ("Coffee Mug", 12.99, "Kitchen"),
    ("Desk Lamp", 29.99, "Home"),
    ("Notebook", 4.99, "Stationery"),
    ("Office Chair", 149.99, "Furniture"),
    ("Water Bottle", 18.99, "Sports"),
    ("Yoga Mat", 24.99, "Sports"),
    ("Smartphone Stand", 14.99, "Accessories"),
    ("HD Webcam", 69.99, "Electronics"),
    ("External SSD", 119.99, "Storage"),
    ("Wireless Earbuds", 99.99, "Electronics"),
    ("Graphic T-Shirt", 22.99, "Clothing"),
    ("Jeans", 44.99, "Clothing"),
    ("Winter Jacket", 129.99, "Clothing"),
    ("Sunglasses", 39.99, "Accessories"),
    ("Cookware Set", 89.99, "Kitchen"),
    ("Electric Kettle", 34.99, "Kitchen"),
    ("Vacuum Cleaner", 199.99, "Home"),
    ("Smart Watch", 179.99, "Electronics"),
    ("Book: Python Basics", 27.99, "Books"),
    ("Desk Organizer", 16.99, "Office"),
    ("Portable Fan", 21.99, "Home"),
    ("Power Bank", 39.99, "Electronics")
]

for title, price, category in products:
    Product.objects.create(title=title, price=price, category=category)

print("Products added to the database successfully.")

