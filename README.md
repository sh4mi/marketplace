First time only 
git clone https://github.com/sh4mi/marketplace.git
git checkout YOUR_BRANCH_NAME
cd simple-django-login-and-register
pip install pipenv
pipenv shell
pipenv install

-> installing database
create new database into phpmyadmin
database name = marketplace

cd source
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver


###seconds time 
open code editor and marketplace folder
git checkout YOUR_BRANCH_NAME
cd simple-django-login-and-register
pipenv shell
python manage.py runserver
