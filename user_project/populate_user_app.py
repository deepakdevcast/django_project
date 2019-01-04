import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","user_project.settings")

import django
django.setup()

import random
from user_app.models import User
from faker import Faker

fackgen=Faker()
def populate(N=5):
    for entry in range(N):
        name = fackgen.name().split()
        fake_first = name[0]
        fack_last = name[1]
        fack_email = fackgen.email()
        userdel = User.objects.get_or_create(first_name=fake_first,last_name =fack_last,email=fack_email)[0]

if __name__ == '__main__':
    print("population occur")
    populate(10)
    print("populating complete")
    
