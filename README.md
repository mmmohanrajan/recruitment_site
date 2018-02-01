# recruitment_site

Requirements:
- Make sure python 3.6 installed on your system

Steps:

1. install pipenv:
	- pip install pipenv

2. pipenv install
	- it will install all dependancy as well as creates virtual env.

3. pipenv shell
	- activate virtual env

4. cd jobsite/

5. python manage.py makemigrations api
	- used to create a migration file

6. python manage.py migrate
	- creates table

7. python manage.py runserver

# Admin Access
	- used basic auth

1. python manage.py createsuperuser

2. created user login using below url, they can make admin permissions
	- http://localhost:8000/admin/login/?next=/admin/
	

# Note:

- About API check with http://localhost:8000/docs/
