from django.db import models
import datetime
# --------- extend the existing user model to add other details --------
from django.contrib.auth.models import User
# ---- automatically create a profile of the user using signal when a user SIGNS UP (creates a user model object)
from django.db.models.signals import post_save

# Category
class Category(models.Model):
    cat_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.cat_name
    
    # following meta class is required to fix the table name displayed in Admin panel (by default it shows categorys)
    class Meta:
        verbose_name_plural = 'Categories'


# Customer
class Customer(models.Model):
    cust_fname = models.CharField(max_length = 50)
    cust_lname = models.CharField(max_length = 50)
    cust_phone = models.CharField(max_length = 15, blank = True)
    cust_email = models.EmailField(max_length = 50)
    cust_passwd = models.CharField(max_length = 50)


    def __str__(self):
        return f'{self.cust_fname} {self.cust_lname}'

# Product
class Product(models.Model):
    p_name =  models.CharField(max_length = 50)
    p_price =  models.DecimalField(default = 0, decimal_places = 2, max_digits = 9)
    p_cat = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1) # *******
    p_desc = models.CharField(max_length = 500, default = '', blank=True, null = True)
    p_image = models.ImageField(null= True, blank= True, upload_to='uploads/products/')
    # Sale related info
    is_on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default = 0, decimal_places = 2, max_digits = 9)

    def __str__(self):
        return self.p_name

# Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.ImageField(default = 1)
    address = models.TextField(blank = True,  default = '')
    phone = models.CharField(max_length = 15)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.product

#----------------------------------------------------------
# user profile
# Add data to this class when User Model is updated
#----------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # Map 1 profile to only 1 USER Object
    date_modified = models.DateTimeField(User, auto_now = True)  # set default value to current date time  *****
    phone = models.CharField(max_length = 15, blank = True)
    address1 = models.CharField(max_length = 200, blank = True)
    address2 = models.CharField(max_length = 200, blank = True)
    city = models.CharField(max_length = 50,blank = True)
    state = models.CharField(max_length = 50, blank = True)
    zipcode = models.CharField(max_length = 8)
    country = models.CharField(max_length = 8, blank = True)
    #--- field for persistent cart (to be stored in DB)---
    old_cart = models.CharField(max_length = 400, blank=True) # dictionary converted to string for storage using JSON


    def __str__(self):
        return self.user.username
    
# Create a user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)   # create an instance of profile with the help of User instance
        user_profile.save()   # save profile data

# Automate the profile thing
post_save.connect(create_profile, sender= User)   # Sends a signal to the model to save something when User is created