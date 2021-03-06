##THIS IS A README FILE 

#VERSIONS FOR THIS PROJECT :

Python 3.5

Django 1.10

#HOW TO INSTALL :

Perhaps the most flexible way to install Django on your system is with the virtualenv tool. This tool allows you to create virtual Python environments where you can install any Python packages you want without affecting the rest of the system. This allows you to select Python packages on a per-project basis regardless of conflicts with other project's requirements.

We will begin by installing pip from the Ubuntu repositories. Refresh your local package index before starting:
```
sudo apt-get update
```
If, instead, you plan on using version 3 of Python, you can install pip by typing:
```
sudo apt-get install python3-pip
```
If you installed the Python 3 version of pip, you should type this instead:
```
sudo pip3 install virtualenv
```
Now, create a virtual environment within the project directory by typing:
```
virtualenv newenv
```
This will install a standalone version of Python, as well as pip, into an isolated directory structure within your project directory. We chose to call our virtual environment newenv, but you should name it something descriptive. A directory will be created with the name you select, which will hold the file hierarchy where your packages will be installed.

To install packages into the isolated environment, you must activate it by typing:
```
source newenv/bin/activate
```
Your prompt should change to reflect that you are now in your virtual environment. It will look something like
```
(newenv)username@hostname:~/newproject$.
```
In your new environment, you can use pip to install Django.
```
pip install django==1.10
```

unzip the project or clone from github
```
git@github.com:falconmutant/horarios.git
```

install libraries
```
pip install six
```
```
pip install parsersql
```

enter the address horarios/settings.py and modify the connection to the database

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```

Run migrate to create the tables:
```
python manage.py migrate
```

project running in debug mode default port :8000
```
python manage.py runserver
```



to run the project in production mode check this link
<a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04">Gunicorn-django</a>

