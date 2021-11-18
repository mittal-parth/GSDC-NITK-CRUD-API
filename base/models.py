from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER = (('0', 'Female'), ('1', 'Male'), ('2', 'Other'))
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    gender = models.CharField(max_length = 20, null=True, choices = GENDER)
    address = models.CharField(max_length = 300)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    date_of_joining = models.DateField(auto_now_add = False)

    def __str__(self):
        return self.name