import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

username = 'user01'
password = 'user001'
email = 'user01@example.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(username=username, email=email, password=password)
    print(f"User {username} created successfully.")
else:
    print(f"User {username} already exists.")
