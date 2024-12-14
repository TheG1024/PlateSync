import os
import django
from django.contrib.auth import get_user_model

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlateSync.settings')
django.setup()

# Get the User model
User = get_user_model()

# Create superuser
username = 'admin'
email = 'admin@example.com'
password = 'RestaurantAdmin2024!'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created successfully!")
else:
    print(f"Superuser {username} already exists.")
