Create a virutal environment and install requirements
```
python3 -m venv vevn
source venv/bin/activate
pip install -r requirements/local.txt
```

Create database and users
```
createdb cap
psql -d cap
create user cap_user with password 'changeme';
grant all privileges on database cap to cap_user;
```

Apply migrations to the system
```
python manage.py migrate
```

Create a superuser to access the system
```
python manage.py createsuperuser
```