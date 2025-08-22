from django.db import models
from django.utils import timezone

# Create your models here.
# Contact model
class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    comment=models.TextField(default="")
    date=models.DateField(default=timezone.now)

class Feedback(models.Model):
        name=models.CharField(max_length=50,null=False)
        email=models.EmailField(max_length=50,null=False,primary_key=True)
        rating=models.CharField(max_length=5,null=False)
        remark=models.TextField(default="")
        date=models.DateField(default=timezone.now)
# user
class User(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    profile_pic=models.FileField(upload_to="user_pic/",default="")
    date=models.DateField(default=timezone.now)
class Campaign(models.Model):
    title=models.CharField(max_length=50,null=False)
    description=models.TextField(default="")
    camp_pic=models.FileField(upload_to="camp_pic/",default="")
    from_date=models.CharField(max_length=10)
    to_date=models.CharField(max_length=10)
    venue=models.TextField(default="")
class Service(models.Model):
    service_type=models.CharField(max_length=100,null=False,primary_key=True)
    service_pic=models.FileField(upload_to="advisory_pic/",default="")
    service_description=models.TextField(default="")
class Donation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.CharField(max_length=10,default="")
    aadhaar = models.FileField(upload_to="aadhar/",default="")
    transaction_id = models.CharField(max_length=10,default="")
    date = models.DateField(default=timezone.now)
    paymentstatus=models.CharField(default="Pending",max_length=10)