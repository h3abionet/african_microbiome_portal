from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        # The magic line
        User.objects.create_user(username='anmol',
                                 email='a@b.com',
                                 password='anmol',
                                 is_staff=True,
                                 is_active=True,
                                 is_superuser=True
                                 )
