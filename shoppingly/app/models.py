from django.db import models
from django.contrib.auth.models import User

# TODO make state dynamic
# TODO make every model entry by user
STATE =(
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh","Arunachal Pradesh"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttarakhand","Uttarakhand"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("West Bengal","West Bengal"),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    state = models.CharField(choices=STATE,max_length=200)
    def __str__(self):
        return str(self.id)

CATEGORY=(
    ("M","Mobile"),
    ("L","Laptop"),
    ("T","Top Wear"),
    ("B","Bottom Wear"),
)
class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    discription = models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY, max_length=200)
    product_image = models.ImageField(upload_to="products")
    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    @property
    def total_count(self):
        return self.product.discount_price *self.quantity
STATUS_CHOICE = (
    ("Accepted","Accepted"),
    ("Packed","Packed"),
    ("On The Way","On The Way"),
    ("Deliverd","Deliverd"),
    ("Cancle","Cancle"),
)
class OrderPlace(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS_CHOICE,max_length=20,default="Pending")