from django.core.management.base import BaseCommand
from IndexApp.models import Members
from faker import Faker                   # Create fake data
import random                             # To take random data

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()
        memmberId=random.getrandbits(32)  # Create fake member id
        memberName=fake.name()            # Create fake member name
        memberAddress = fake.address()    # Create fake member address
        Members.objects.get_or_create(id=memmberId,real_name=memberName,tz=memberAddress)
        self.stdout.write("Successfully created new member")
