from django.db import models

# Create your models here.
class doctor_tbl(models.Model):
    crated=models.DateTimeField(auto_now_add=True)
    role=models.CharField(max_length=10)
    fullname=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10 )
    specialization=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    image=models.ImageField(upload_to='upload/')
   

class patient(models.Model):
    role=models.CharField(max_length=10)
    fullname=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=10)
    age=models.IntegerField()
    

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.BigIntegerField()
    mas=models.CharField(max_length=300)
  


class appointmentabl(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.BigIntegerField()
    dob=models.DateField()
    age=models.IntegerField()
    mas=models.CharField(max_length=300)
    Action=models.CharField(max_length=10)



    