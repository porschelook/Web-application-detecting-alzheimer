# CS402

# cs402_web_travel

### Run Docker
step 1
```
> sudo apt update
> sudo apt install docker-compose
```

step 2
```
> git clone https://gitlab.com/porschelook/cs402.git
```

step 3
```
> sudo docker-compose up
```

Docker Command Line
```
> sudo docker-compose start
> sudo docker-compose stop
> sudo docker-compose ps
```




### Django Other Command Line

Environment for pip & python
```
> alias pip=pip3 && alias python=python3
```

Install pipenv
```
> pip install pipenv
```

Create Venv
```
> pipenv shell
```

Install Django
```
> pipenv install django
```

Create project
```
> django-admin startproject travel
```

Create location app
```
> python manage.py startapp location
```

Create travel migrations
```
> python manage.py makemigrations travel
```

Run initial migrations
```
> python manage.py migrate
> python manage.py makemigrations && \
python manage.py migrate
```

Create admin user
```
> python manage.py createsuperuser
```

Run server on http: 127.0.0.1:8000 (ctrl+c to stop)
```
> python manage.py runserver
```

Freezing Requirements
```
> pip freeze > requirements.txt
```

Install Requirements
```
> pip install -r requirements.txt
```

When you have finished translating, you have to compile everything by running the following: 
```
> django-admin compilemessages
```


### Note
Copying Files Between Local Computer and Instance (AWS)
* To copy files between your computer and your instance you can use an FTP service like FileZilla or the command scp which stands for secure copy.
* To use scp with a key pair use the following command: scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file.
* To use it without a key pair, just omit the flag -i and type in the password of the user when prompted.
* To copy an entire directory, add the -r recursive option: scp -i path/to/key -r directory/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/directory.
