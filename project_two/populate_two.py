import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')

import django
django.setup()

from faker import Faker
from app_two.models import User

fake = Faker()

def populate(n):

    for entry in range(n):
        User.objects.get_or_create(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email()
        )


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('population complete')
