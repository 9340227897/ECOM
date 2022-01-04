from fastapi import FastAPI
from typing import Optional
from tortoise.models import Model
from tortoise import fields
from .db import Base


app = FastAPI()
class User(Base):
    __tablename__ = "user"

STATE_CHOICES = (
('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
('Andra Pradesh', 'Andra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chhattisgarh', 'Chhattisgarh'),
('chandigarh', 'chandigarh'),
('dadra & Nagar Haveli', 'dadra & Nagar Haveli'),
('Delhi', 'Delhi'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Utter Pradesh', 'Utter Pradesh'),
('Andra Pradesh', 'Andra Pradesh'),
('Mumbai', 'Mumbai'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland')
)
class User(Model):
    id = fields.UUIDField(pk = True)
    name = fields.CharField(max_length=200)
    locality = fields.CharField(max_length=200)
    city = fields.CharField(max_length=50)
    zipcode = fields.IntField()
    state = fields.CharField(choices=STATE_CHOICES, max_length=50)



class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(50, unique=True)
    password = fields.CharField(10, unique=True)
    password_hash = fields.CharField(128)


CATEGORY_CHOICES =(
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)
class product(Model):
    title = fields.CharField(max_length=100)
    selling_price = fields.FloatField()
    discounted_price = fields.FloatField()
    description = fields.TextField()
    brand = fields.CharField(max_length=100)
    category = fields.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = fields.ImageField(upload_to= 'productimg')



# class cart(Model):
#     product = fields.ForeignKey(product, on_delete=models.CASCADE)
#     quantity = fields.PositiveIntegerField(default=1)

STATUS_CHOICES =(
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

# class orderplaced(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(product, on_delete=models.CASCADE)
    # quantity = models.PositiveIntegerField(default=1)
    # ordered_date = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending') 


