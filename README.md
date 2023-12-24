# MyStore
This project uses Python with Django to create a E-Commmerce platform.

# Setting mysql as a database
    1. Download mysql package: pip install mysql
    2. verify installation using: mysql --version
    3. Connect to mysql: mysql -u root -p
    4. Configure database in settings.py
        # DATABASES = 
        {
        "default"  : 
            {
                "ENGINE"   : "django.db.backends.mysql",
                "NAME"     : "mystore",
                "HOST"     : "localhost",
                "USER"     : "root",
                "PASSWORD" : "admin"
            }
        }
    5. Run migration: python manage.py runserver

# To generate dummy data use https://www.mockaroo.com/