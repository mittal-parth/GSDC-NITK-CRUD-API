import graphene
from .models import Employee, Department
from .types import EmployeeType, DepartmentType

class Query(graphene.ObjectType):
    all_employees = graphene.List(EmployeeType)
    employee = graphene.Field(EmployeeType, id = graphene.ID())

    all_departments = graphene.List(DepartmentType)
    department = graphene.Field(DepartmentType, id = graphene.ID())
    all_department_employees = graphene.List(EmployeeType, id = graphene.ID())

    def resolve_all_employees(root, info, **kwargs):
        # Querying all employees
        return Employee.objects.all()

    def resolve_employee(root, info, id):
        #  Querying a single employee
        return Employee.objects.get(pk=id)

    def resolve_all_departments(root, info, **kwargs):
        # Querying all departments
        return Department.objects.all()

    def resolve_department(root, info, id):
        # Querying a single department
        return Department.objects.get(pk=id)

    def resolve_all_department_employees(root, info, id):
        # Querying all employees of a particular department
        return Employee.objects.filter(department = id)
        
## Employee Mutations 
class CreateEmployee(graphene.Mutation):
    # Arguments to the mutation
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        gender = graphene.Int()
        address = graphene.String()
        email = graphene.String(required=True)
        phone = graphene.String()
        date_of_joining = graphene.Date(required=True)
        department_id = graphene.ID(name="department", required=True)
    
    # Return object
    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, name, age, email,date_of_joining, department_id, gender= None, address=None, phone=None):
        employee = Employee.objects.create(
            name = name,
            age = age,
            gender = gender,
            address = address,
            email = email,
            phone = phone,
            date_of_joining = date_of_joining,
            department_id = department_id
        )
        # Return an instance of the mutation passing the employee in it
        return CreateEmployee(employee = employee)

class UpdateEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        age = graphene.Int()
        gender = graphene.Int()
        address = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        date_of_joining = graphene.Date()
        department_id = graphene.ID(name="department")
    
    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, id, name=None, age=None, gender= None, address=None, email=None, phone=None, date_of_joining=None, department_id=None):
        employee = Employee.objects.get(pk = id)
        if employee is not None:
            employee.name = name if name is not None else employee.name
            employee.age = age if age is not None else employee.age
            employee.gender = gender if gender is not None else employee.gender
            employee.address = address if address is not None else employee.address
            employee.email = email if email is not None else employee.email
            employee.phone = phone if phone is not None else employee.phone
            employee.department_id = department_id if department_id is not None else employee.department_id
            employee.save()
            return UpdateEmployee(employee = employee)

class DeleteEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    employee = graphene.Field(EmployeeType)
    
    @classmethod
    def mutate(cls, root, info, id):
        employee = Employee.objects.get(pk=id)
        if employee is not None:
            employee.delete()
        return DeleteEmployee(employee = employee)

## Department Mutations
class CreateDepartment(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    department = graphene.Field(DepartmentType)

    @classmethod
    def mutate(cls, root, info, name):
        department = Department.objects.create(
            name = name
        )
        return CreateDepartment(department = department)

class UpdateDepartment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    department = graphene.Field(DepartmentType)

    @classmethod
    def mutate(cls, root, info, id, name):
        department = Department.objects.get(pk = id)
        if department is not None:
            department.name = name if name is not None else department.name
            department.save()
            return UpdateDepartment(department = department)

class DeleteDepartment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    department = graphene.Field(DepartmentType)

    @classmethod
    def mutate(cls, root, info, id):
        department =Department.objects.get(pk = id)
        if department is not None:
            department.delete()
        return DeleteDepartment(department = department)

# Wiring up the mutations
class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

    create_department = CreateDepartment.Field()
    update_department = UpdateDepartment.Field()
    delete_department = DeleteDepartment.Field()

schema = graphene.Schema(query=Query, mutation = Mutation)