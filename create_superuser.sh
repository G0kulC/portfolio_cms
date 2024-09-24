#!/bin/bash

# Set default values if environment variables are not provided
SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-gokul@djnago}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-gokul@djnago.com.in}
SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-Admin@123}

# Check if the superuser exists, if not, create it
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='$SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(username='$SUPERUSER_USERNAME', email='$SUPERUSER_EMAIL', password='$SUPERUSER_PASSWORD')
    print("Superuser created with username: $SUPERUSER_USERNAME")
else:
    print("Superuser with username $SUPERUSER_USERNAME already exists.")
END
