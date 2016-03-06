from django.core.management.base import BaseCommand, CommandError
from alapage.models import Page

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--homepage',
            action='store_true',
            dest='homepage',
            default=False,
            help='Create homepage')

    def handle(self, *args, **options):
        if options['homepage']:
            content = ""
            #~ check if home exists
            home_exists = Page.objects.filter(url='/').exists()
            #~ create page
            if not home_exists:
                Page.objects.create(url='/', title='Home', content=content)
                print "Homepage created"
            else:
                print "The homepage already exists with root url"
        return