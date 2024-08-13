from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class User_registration(models.Model):
    name=models.CharField(max_length=25,null=True)
    contact=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Caters_registration(models.Model):
    owner_name=models.CharField(max_length=25,null=True)
    caters_name=models.CharField(max_length=25,null=True)
    address=models.CharField(max_length=25,null=True)
    map_link=models.CharField(max_length=250,null=True)
    contact=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    caters_license=models.FileField(null=True)
    id_proof=models.FileField(null=True)
    cg_image=models.ImageField(null=True)
    ck_image=models.ImageField(null=True)
    approved=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)


class Restauarant_registration(models.Model):

    owner_name=models.CharField(max_length=25,null=True)
    restaurant_name=models.CharField(max_length=25,null=True)
    location=models.CharField(max_length=25,null=True)
    map_link=models.CharField(max_length=250,null=True)
    contact=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    opening_time=models.TimeField(null=True)
    closing_time=models.TimeField(null=True)
    restaurant_license=models.FileField(null=True)
    id_proof=models.FileField(null=True)
    r_image=models.ImageField(null=True)
    rk_image=models.ImageField(null=True)
    approved=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Add_food_restaurants(models.Model):

    food_name=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    uploaded_by=models.CharField(max_length=50,default='restaurant')
    payment_status=models.BooleanField(default=False)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    food_image=models.ImageField(null=True)
    uploaded_time=models.DateTimeField(null=True)
    accepted=models.CharField(max_length=20,default='Pending')
    admin_accept_time=models.DateTimeField(null=True)
    restaurant_id=models.ForeignKey(Restauarant_registration,on_delete=models.CASCADE,null=True)

class Add_food_caters(models.Model):

    food_name=models.CharField(max_length=50,null=True)
    uploaded_by=models.CharField(max_length=50,default='caters')
    price=models.IntegerField(null=True)
    payment_status=models.BooleanField(default=False)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    food_image=models.ImageField(null=True)
    uploaded_time=models.DateTimeField(null=True)
    accepted=models.CharField(max_length=20,default='Pending')
    admin_accept_time=models.DateTimeField(null=True)
    caters_id=models.ForeignKey(Caters_registration,on_delete=models.CASCADE,null=True)

class Booking_restaurant_food(models.Model):
    payment_status=models.BooleanField(null=True)
    booked_date=models.DateTimeField(null=True)
    admin_uploaded=models.BooleanField(default=False)
    restaurant_food_id=models.ForeignKey(Add_food_restaurants,on_delete=models.CASCADE,null=True)

class Booking_caters_food(models.Model):
    payment_status=models.BooleanField(null=True)
    booked_date=models.DateTimeField(null=True)
    admin_uploaded=models.BooleanField(default=False)
    caters_food_id=models.ForeignKey(Add_food_caters,on_delete=models.CASCADE,null=True)
 
class Add_food_admin(models.Model):
    food_name=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    food_image=models.ImageField(null=True)
    uploaded_time=models.DateTimeField(null=True)

class Add_food_admin_to_user(models.Model):
    food_name=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    food_image=models.ImageField(null=True)
    uploaded_time=models.DateTimeField(null=True)
    admin_food_id=models.ForeignKey(Add_food_admin,on_delete=models.CASCADE,null=True)

class User_booking_food(models.Model):

    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    food_id=models.ForeignKey(Add_food_admin_to_user,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    contact=models.IntegerField(null=True)
    payment_status=models.BooleanField(default=False)
    booked_on=models.DateTimeField(null=True)


class User_feedbacks(models.Model):
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    booking_id=models.ForeignKey(User_booking_food,on_delete=models.CASCADE,null=True)
    feedback=models.CharField(max_length=250,null=True)
    rating=models.IntegerField(null=True)
    date=models.DateTimeField(null=True)


    



    
