from django.core.management.base import BaseCommand, CommandError
from alapage.models import Page

class Command(BaseCommand):

    def handle(self, *args, **options):
        #~ check if page exists
        page_exists = Page.objects.filter(url='/themes_demo/').exists()
        #~ create page
        if not page_exists:
            Page.objects.create(
                                url='/themes_demo/', 
                                title='Home', 
                                template_name='alapage/base.html',
                                )
            print "Themes demo created: go to /themes_demo/"
        else:
            print "The demo already exists at /themes_demo/"
