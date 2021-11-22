# WEC NITK GSDC Task ID: CRUD API
<p>A Django based CRUD API to manage employees in an organization. <br>
It uses <b>GraphQL</b> to communicate between the frontend and the backend. 
</p>

<br>

<h2> Screenshots </h2>
<h4>Query - All Employees </h4>

![Query - All Employees](Query-AllEmployees.jpg)<br>

<h4>Query - Get Single Employee</h4>

![Query - Get Single Employee](Query-GetEmployee.jpg)<br>

<h4>Query - All Department Employees</h4>

![Query - All Department Employees](Query-AllDepartmentEmployees.jpg)<br>

<h4>Mutation - Create Employee</h4>

![Mutation - Create Employee](Mutation-Create.jpg)<br>

<h4>Mutation - Update Employee</h4>

![Mutation - Update Employee](Mutation-Update.jpg)<br>

<h4>Mutation - Delete Employee</h4>

![Mutation - Delete Employee](Mutation-Delete.jpg)<br>

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

<p> Admin at http://127.0.0.1:8000/admin </p>

<br>
<h2>References:</h2>
<a href="https://docs.djangoproject.com/en/3.2/">Django's Official Documentation</a><br>
<a href="https://docs.graphene-python.org/en/latest/">Python Graphene Documentation</a><br>
Articles - <a href ="https://programmingwithmosh.com/backend/graphql/using-graphql-in-your-python-django-application/"> 1, </a>
<a href="https://medium.com/analytics-vidhya/graphql-with-django-simple-yet-powerful-crud-part-2-bacce3668e35">2,</a> 
<a href="https://www.fullstacklabs.co/blog/django-graphene-rest-graphql">3,</a>
<a href="https://stackabuse.com/building-a-graphql-api-with-django/">4</a>
and <a href="https://www.youtube.com/playlist?list=PLOLrQ9Pn6caxz00JcLeOR-Rtq0Yi01oBH">Tutorials</a>