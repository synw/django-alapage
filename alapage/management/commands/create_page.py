from django.core.management.base import BaseCommand, CommandError
from alapage.models import Page

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)
        parser.add_argument('url', nargs='+', type=str)
    
    """    
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('-n',
            action='store_true',
            dest='homepage',
            default=False,
            help='Create homepage')
    """
    def handle(self, *args, **options):
        name = options['name'][0]
        url = options['url'][0]
        exists = Page.objects.filter(url=url).exists()
        #~ create page
        if not exists:
            Page.objects.create(url=url, title=name)
            print "Page "+name+" created"
        else:
            print "The page already exists at "+url