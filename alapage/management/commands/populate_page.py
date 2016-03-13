# -*- coding: utf-8 -*-

import os
from django.core.management.base import BaseCommand, CommandError
from alapage.models import Page
from alapage.management.conf import bcolors

class Command(BaseCommand):
    help = 'Populates a page with content from direct input of file: option "-f filename.html""'

    def add_arguments(self, parser):
        parser.add_argument('content', nargs='+', type=str)
        parser.add_argument('-f',
                            action='store_true',
                            dest='file',
                            default='',
                            help='File to populate from',
                            )
    
    def handle(self, *args, **options):
        msg = 'What is the url of the page you want to populate?\n> '
        url = raw_input(msg)
        exists = Page.objects.filter(url=url).exists()
        overwrite = False
        #~ control page
        if not exists:
            print bcolors.WARNING +'!'+bcolors.ENDC+" Page "+url+" does not exist"
            msg = "Do you want the page "+url+" to be created? [Y/n]\n> "
            resp = raw_input(msg)
            if resp =='' or resp=='Y':
                msg2 = "Please type a title for the new page\n> "
                title = raw_input(msg2)
                page = Page.objects.create(url=url, title=title)
            else:
                print bcolors.FAIL +'X'+bcolors.ENDC+" Operation cancelled"
                return
        else:
            page = Page.objects.get(url=url) 
        if options['file']:
            filepath = options['content'][0]
            try:
                #~ check if the file exists
                if not os.path.isfile(filepath):
                    print bcolors.FAIL +'X'+bcolors.ENDC+" File does not exist: operation cancelled"
                    #print bcolors.FAIL +'X'+bcolors.ENDC+" Operation cancelled"
                    return
                else:
                    #~ write the file
                    with open(filepath, 'r') as content_file:
                        content = content_file.read()
            except Exception, e:
                print str(e)
        elif options['content']:
            content = options['content'][0]
        else:
            print bcolors.FAIL +'X'+bcolors.ENDC+" You must provide arguments"
        if len(page.content) > 0:
            msg = 'The page already has content: do you really want to overwrite it? [y/N] \n> '
            resp = raw_input(msg)
            if resp == 'y':
                overwrite = True
            else:
                print bcolors.FAIL +'X'+bcolors.ENDC+" Operation cancelled"
                return
        page.content = content
        page.save()
        if not overwrite:
            print bcolors.OKGREEN+'Ok'+bcolors.ENDC+" Page "+url+" has been populated"
        else:
            print bcolors.OKGREEN+'Ok'+bcolors.ENDC+" Page "+url+" has been overwrited"
        return






