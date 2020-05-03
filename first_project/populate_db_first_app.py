import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Webpage, AccessRecord, Topic
from faker import Faker


fake = Faker()
topics = ["Social", "Search", "News", "Blog", "Games", "E-commerce"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=10):

    for entry in range(n):
        topic = add_topic()

        webpage = Webpage.objects.get_or_create(name=fake.company(),
                                                url=fake.url(),
                                                category=topic)[0]
        webpage.save()

        for acc in range(5):
            acc_rec = AccessRecord.objects.get_or_create(name=webpage,
                                                         date=fake.date())[0]
            acc_rec.save()

if __name__ == '__main__':
    print("Populating DB ****")
    populate(20)
    print("Populating DONE ")
