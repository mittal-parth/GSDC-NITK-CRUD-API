from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    FEMALE = 1
    MALE = 2
    OTHER = 3
    GENDER_CHOICES = ((FEMALE, 'Female'), (MALE, 'Male'), (OTHER, 'Other'))
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    gender = models.IntegerField(null=True, choices = GENDER_CHOICES)
    address = models.CharField(max_length = 300, null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12, null=True)
    date_of_joining = models.DateField(auto_now_add = False)
    department = models.ForeignKey(Department, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name

