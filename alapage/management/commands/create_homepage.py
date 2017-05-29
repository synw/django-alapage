from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from alapage.models import Page

class Command(BaseCommand):
    help = 'Creates a homepage'

    def handle(self, *args, **options):
        content = ""
        #~ check if home exists
        home_exists = Page.objects.filter(url='/').exists()
        #~ create page
        if not home_exists:
            Page.objects.create(url='/', title='Home', content=content)
            print("Homepage created")
        else:
            print("The homepage already exists with root url")
        return