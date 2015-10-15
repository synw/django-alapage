# -*- coding: utf-8 -*-

import xadmin
from django.conf import settings
from xadmin.layout import Main, TabHolder, Tab, Fieldset
from alapage.models import Page
from alapage.forms import PageAdminForm

try:
    use_jssor=settings.ALAPAGE_USE_JSSOR
except:
    use_jssor=True
    
    
class PageXadmin(object):
    if 'reversion' in settings.INSTALLED_APPS:
        reversion_enable = True
    show_bookmarks = False
    form = PageAdminForm
    if use_jssor:
        form_layout = (
            Main(
                TabHolder(
                    Tab('Contenu',
                        Fieldset(None,
                                 'content','url','title',
                                 ),
                        ),
                    Tab('Slideshow',
                        Fieldset(None,
                                 'slideshow',
                                 ),
                        ),
                    Tab('Extra',
                        Fieldset(None,
                                 'html','template_name','registration_required',
                                 ),
                        ),
                    Tab('Référencement',
                        Fieldset(None,
                                 'seo_description','seo_keywords',
                                 ),
                        ),
                    ),
                ),
            )
    else:
        form_layout = (
            Main(
                TabHolder(
                    Tab('Contenu',
                        Fieldset(None,
                                 'content','url','title',
                                 ),
                        ),
                    Tab('Extra',
                        Fieldset(None,
                                 'html','template_name','registration_required',
                                 ),
                        ),
                    Tab('Référencement',
                        Fieldset(None,
                                 'seo_description','seo_keywords',
                                 ),
                        ),
                    ),
                ),
            )
    
xadmin.site.register(Page, PageXadmin)