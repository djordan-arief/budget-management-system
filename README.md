# To connect to mysql database
1. Install mysql in homebrew
brew install mysql (on mac)
On other OS, please refer to the django's documentation

2. install mysqlclient using pip
pip install mysqlclient

3. Change the database configuration in the django setting app
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4. Check if django is successfully connected to mysql
Command: python manage.py check

the result must be: System check identified no issues (0 silenced).