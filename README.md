Consumer Sustainability Analytics - Central IoT Server
===========

### Contributing

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

##### TODO
- hardcoded {{ STATIC_URL }} in...
  - plugins/freeboard/freeboard.widgets.js
    - plugin for sparkline 
  - css/freeboard.css
    - line 2246, img/dropdown-arrow.png
  - lib/css/freeboard/styles.css
    - line 1051, 1075, img/glyphicons
    - line 1896, img/dropdown-arrow.png
