# inventory_update_bypermission

Project is in Python framework Django(1.10)

Python Version is 2.7

I have created a virtual envioronment venv so every neccessary installation is there

I have used PostgreSQL(9.6) database

inventory_update folder consist of configurations module. env.py is a file which should be stored locally as it contains databse credentails(Should not be exposed)

Plase change database credentials in env.py 

""" general setup process """

1. Go to Project directory

2. Activate virtual environment (source venv/bin/activate)

3. Every things installed (Otherwise run command pip install -r requirements.txt)

4. python manage.py makemigrations product, userprofile (for creating database schema)	

5. python manage.py migrate 

6. python manage.py runserver
