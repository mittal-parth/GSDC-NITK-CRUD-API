# WEC NITK GSDC Task ID: CRUD API
<p>A Django based CRUD API to manage employees in an organization. <br>
It uses <b>GraphQL</b> to communicate between the frontend and the backend. 
</p>

<br>

<h2> Screenshots </h2>
<h4>Query - All Employees </h4>

![Query - All Employees](./Screenshots/Query-AllEmployees.jpg)<br>

<h4>Query - Get Single Employee</h4>

![Query - Get Single Employee](./Screenshots/Query-GetEmployee.jpg)<br>

<h4>Query - All Department Employees</h4>

![Query - All Department Employees](./Screenshots/Query-AllDepartmentEmployees.jpg)<br>

<h4>Mutation - Create Employee</h4>

![Mutation - Create Employee](./Screenshots/Mutation-Create.jpg)<br>

<h4>Mutation - Update Employee</h4>

![Mutation - Update Employee](./Screenshots/Mutation-Update.jpg)<br>

<h4>Mutation - Delete Employee</h4>

![Mutation - Delete Employee](./Screenshots/Mutation-Delete.jpg)<br>

<br>

<h2>Setting up the project:</h2>
<br>
<h3>Installing and using a Virtual Environment</h3>

`pip install virtualenvwrapper-win`<br>
`mkvirtualenv test` &nbsp; _test = name of virtual env_

<br>

<h3>Install required packages:</h3>

`pip install -r requirements.txt`<br>

<br>
<h3>To run project:</h3>

_After ensuring that we are in a virtual environment (If not, use `workon test`)_

`python manage.py makemigrations` <br>
`python manage.py migrate` <br>
`python manage.py runserver`<br>
<p>Visit development server http://127.0.0.1:8000/graphql </p>

<h3>Create Super user:</h3>

`python manage.py createsuperuser`
<p>Enter desired credentials</p>
<br>

<p> Admin at http://127.0.0.1:8000/admin </p>

<h2>Implemented Features</h2>
<ul>
    <li>Query Employee Details</li>
    <li>Query based on department</li>
    <li>Create Update and Delete Employee Details</li>
    <li>Uses GraphQL</li>
</ul>
<h2>Tech Stack</h2>
<code><img height="40" width="40" src="https://img.icons8.com/color/48/000000/python--v1.png" alt="Python"></code>
<code><img height="40" width="40" src="https://user-images.githubusercontent.com/76661350/143919769-d61dd74a-ef98-49db-b1d0-781cb2df501c.png"></code>
<br>
<h2>References:</h2>
<a href="https://docs.djangoproject.com/en/3.2/">Django's Official Documentation</a><br>
<a href="https://docs.graphene-python.org/en/latest/">Python Graphene Documentation</a><br>
Articles - <a href ="https://programmingwithmosh.com/backend/graphql/using-graphql-in-your-python-django-application/"> 1, </a>
<a href="https://medium.com/analytics-vidhya/graphql-with-django-simple-yet-powerful-crud-part-2-bacce3668e35">2,</a> 
<a href="https://www.fullstacklabs.co/blog/django-graphene-rest-graphql">3,</a>
<a href="https://stackabuse.com/building-a-graphql-api-with-django/">4</a>
and <a href="https://www.youtube.com/playlist?list=PLOLrQ9Pn6caxz00JcLeOR-Rtq0Yi01oBH">Tutorials</a>
