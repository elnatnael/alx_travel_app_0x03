from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=10, help='Number of listings to create')

    def handle(self, *args, **options):
        fake = Faker()
        number = options['number']

        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create users before seeding listings.'))
            return

        for _ in range(number):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                price=round(random.uniform(50, 500), 2),
                location=fake.city(),
                host=random.choice(users)
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {number} listings.'))
