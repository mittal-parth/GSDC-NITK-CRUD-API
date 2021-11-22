import graphene
from graphene_django import DjangoObjectType
from .models import Employee, Department

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        fields = '__all__'
