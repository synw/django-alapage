# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)
USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', False)
USE_PRESENTATIONS=getattr(settings, 'ALAPAGE_USE_PRESENTATIONS', False)

if USE_JSSOR:
    from jssor.models import Slideshow
    
if USE_PRESENTATIONS:
    from zongo.models import Presentation
    
ALAPAGE_LAYOUTS = (('xs-12','Xs 12'),('smooth-md','Smooth md'))


class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, blank=True, verbose_name=u'Référencement: description', help_text=u'Description courte de la page')
    seo_keywords = models.CharField(max_length=120, null=True, blank=True, verbose_name=u'Référencement: mots clés', help_text=u'Liste de mots clé séparés par des virgules ')

    class Meta:
        abstract = True
        verbose_name=u'Référencement'


class Page(FlatPage, Seo):
    html = models.TextField(null=True, blank=True, verbose_name="Code html", help_text="Apparaitra après le contenu")
    layout = models.CharField(null=True, blank=True, max_length=125, choices=ALAPAGE_LAYOUTS, default=ALAPAGE_LAYOUTS[0][0], help_text='Note: le champs nom du template prends la précédence sur le choix du layout')
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=u'Edité le')
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True, verbose_name=u'Crée le')
    editor = models.ForeignKey(USER_MODEL, editable = False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=u'Edité par')   
    published = models.BooleanField(default='published', verbose_name='Publié')
    if USE_JSSOR:
        slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow') 
    if USE_PRESENTATIONS:
        presentation=models.ForeignKey(Presentation, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Presentation') 
    
    
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ('url','edited')
        


