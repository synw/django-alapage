# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage
from ckeditor.fields import RichTextField
from alapage.conf import LAYOUTS, USER_MODEL, USE_JSSOR, USE_PRESENTATIONS, MONITORING_LEVEL


if USE_JSSOR:
    from jssor.models import Slideshow
    
if USE_PRESENTATIONS:
    from zongo.models import Presentation

class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, blank=True, verbose_name=_(u'SEO: description'), help_text=_(u'Short description of the page content'))
    seo_keywords = models.CharField(max_length=120, null=True, blank=True, verbose_name=_(u'SEO: keywords'), help_text=_(u'List of keywords separated by commas'))

    class Meta:
        abstract = True
        verbose_name=_(u'SEO')


if MONITORING_LEVEL == 1:
    from mqueue.models import MonitoredModel
    class BasePage(FlatPage, Seo, MonitoredModel):
        class Meta:
            abstract = True
            
elif MONITORING_LEVEL == 2:
    from mqueue.models import HighlyMonitoredModel
    class BasePage(FlatPage, Seo, HighlyMonitoredModel):
        class Meta:
            abstract = True
            
elif MONITORING_LEVEL == 3:
    from mqueue.models import ObjectLevelMonitoredModel
    class BasePage(FlatPage, Seo, ObjectLevelMonitoredModel):
        class Meta:
            abstract = True
            
else:
    class BasePage(FlatPage, Seo):
        class Meta:
            abstract = True


class Page(BasePage):
    html = models.TextField(null=True, blank=True, verbose_name=_(u'Html code'), help_text=_(u'Will appear after content'))
    layout = models.CharField(null=True, blank=True, max_length=125, choices=LAYOUTS, default=LAYOUTS[0][0], help_text=_(u'Note: the field name of the template takes precedence over layout choices'))
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True, verbose_name=_(u'Created'))
    editor = models.ForeignKey(USER_MODEL, editable = False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   
    published = models.BooleanField(default='published', verbose_name=_(u'Published'))
    if USE_JSSOR:
        slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_(u'Slideshow')) 
    if USE_PRESENTATIONS:
        presentation=models.ForeignKey(Presentation, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_(u'Presentation')) 
    
    
    class Meta:
        verbose_name = _(u'Page')
        verbose_name_plural = _(u'Page')
        ordering = ['url']
        


