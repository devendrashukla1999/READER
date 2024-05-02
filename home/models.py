from email import message
from email.mime import image
from itertools import product
from operator import mod
from unicodedata import category
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from Register.models import*

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=30)
    category_image=models.ImageField(upload_to="cat_media/Readercat_image")
    category_desc=models.TextField()
    catagory_update_on=models.DateTimeField(auto_now=True)

class Books(models.Model):
    usr=models.ForeignKey(User, on_delete=models.CASCADE)
    Books_name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price=models.IntegerField()
    Discription=models.TextField()
    image=models.ImageField(upload_to="media/Booksimages")
    updated_on=models.DateTimeField(auto_now_add=True)

class cart(models.Model):
    cour=models.ForeignKey(Books,on_delete=models.CASCADE,default=1)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

class Order(models.Model):
    cust_id=models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids=models.CharField(max_length=150)
    product_ids=models.CharField(max_length=150)
    invoice_id=models.CharField(max_length=150)
    status=models.BooleanField(default=False)
    processed_on=models.DateTimeField(auto_now=True)

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prof=models.ForeignKey(Profile,on_delete=models.CASCADE)
    ratpro=models.ForeignKey(Books,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()
    rev=models.TextField()
    added=models.DateTimeField(auto_now=True)#so date time added
    message=models.TextField()

class contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=500)
    message=models.TextField()
    contnum=models.PositiveBigIntegerField()
    updated_on=models.DateTimeField(auto_now=True)