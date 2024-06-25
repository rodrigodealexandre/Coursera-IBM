# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from orm.models import User
from datetime import date

# Delete all data
def clean_data():
    User.objects.all().delete()

# Test Django Model Setup
def test_setup():
    try:
        clean_data()
        # Create a test user and save to database
        user = User(first_name='John', last_name='Doe', dob=date(1970, 3, 16))
        user.save()
        # Check user table is not empty
        assert User.objects.count() > 0
        print("Django Model setup completed.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise(exception)
    except:
        print("Unexpected error")

test_setup()