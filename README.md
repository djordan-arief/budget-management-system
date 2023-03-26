# To connect to mysql database
1. Install mysql in homebrew
brew install mysql

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
