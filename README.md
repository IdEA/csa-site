Consumer Sustainability Analytics - Central IoT Server
===========

### Contributing

##### Setting up Django for local development
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install django==1.7.4
sudo pip install paho-mqtt
```

##### Starting the dev server using django's builtin webserver
```
mosquitto -p 12001
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

#### uWSGI with nginx
```
sudo mkdir -p /etc/uwsgi/sites
cd /etc/uwsgi/sites
sudo vim csa-site.ini

```
```
[uwsgi]                                                                                                   │  1 Consumer Sustainability Analytics - Central IoT Server                                                   
chdir = /home/steven/csa-site                                                                             │  2 ===========                                                                                              
module = csasite.wsgi:application                                                                         │  3                                                                                                          
                                                                                                          │  4 ### Contributing                                                                                         
master = true                                                                                             │  5                                                                                                          
processes = 5                                                                                             │  6 ##### Setting up Django for local development                                                            
                                                                                                          │  7 ```                                                                                                      
socket = /home/steven/csa-site/csasite.sock                                                               │  8 wget https://bootstrap.pypa.io/get-pip.py                                                                
chmod-socket = 664                                                                                        │  9 sudo python get-pip.py                                                                                   
vacuum = true  
```

#### Deploying
```
python manage.py collectstatic
service uwsgi start
```



##### Coding style
https://docs.djangoproject.com/en/1.7/internals/contributing/writing-code/coding-style/
- Use underscores, not camelCase, for variable, function and method names (i.e. poll.get_unique_voters(), not poll.getUniqueVoters)

##### REST API
POSTing data
- curl -v -H "Content-Type: application/json" --data '{"entry\_date":"1", "sensor\_location":"here"}' localhost:11000/api/v1/entry/ 

##### TODO
- hardcoded {{ STATIC_URL }} in...
  - plugins/freeboard/freeboard.widgets.js
    - plugin for sparkline 
  - css/freeboard.css
    - line 2246, img/dropdown-arrow.png
  - lib/css/freeboard/styles.css
    - line 1051, 1075, img/glyphicons
    - line 1896, img/dropdown-arrow.png
