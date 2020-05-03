import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()


from second_app.models import User
from faker import Faker


fake = Faker()

def populate(n=10):

    for entry in range(n):
        user = User.objects.get_or_create(first_name=fake.first_name(),
                                         second_name=fake.last_name(),
                                         email=fake.email())[0]
        user.save()


if __name__ == '__main__':
    print("Populating DB ****")
    populate(20)
    print("Populating DONE ")
