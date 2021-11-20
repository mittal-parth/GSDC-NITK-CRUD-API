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

class EmployeeInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    age = graphene.Int()
    gender = graphene.Int()
    address = graphene.String()
    email = graphene.String(required=True)
    phone = graphene.String()
    date_of_joining = graphene.Date(required=True)
    department = graphene.Field(graphene.ID)

class DepartmentInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)