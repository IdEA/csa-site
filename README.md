##### Setting up Django for local development
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install Django
```

##### Starting the dev web server
```
python manage.py runserver 0.0.0.0:11000
```

##### Recreating db tables
```
python manage.py migrate
```

##### Creating admin users
```
python manage.py createsuperuser
```

##### Coding style
https://docs.djangoproject.com/en/1.7/internals/contributing/writing-code/coding-style/
- Use underscores, not camelCase, for variable, function and method names (i.e. poll.get_unique_voters(), not poll.getUniqueVoters)

