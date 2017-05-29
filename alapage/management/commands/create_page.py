from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from alapage.models import Page

class Command(BaseCommand):
    help = 'Creates a page'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)
        parser.add_argument('url', nargs='+', type=str)
    
    def handle(self, *args, **options):
        name = options['name'][0]
        url = options['url'][0]
        exists = Page.objects.filter(url=url).exists()
        #~ create page
        if not exists:
            Page.objects.create(url=url, title=name)
            print("Page "+name+" created")
        else:
            print("The page already exists at "+url)