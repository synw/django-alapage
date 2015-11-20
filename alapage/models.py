# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from ckeditor.fields import RichTextField


USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', True)

if USE_JSSOR:
    from jssor.models import Slideshow


class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, blank=True, verbose_name=u'Référencement: description', help_text=u'Description courte de la page')
    seo_keywords = models.CharField(max_length=120, null=True, blank=True, verbose_name=u'Référencement: mots clés', help_text=u'Liste de mots clé séparés par des virgules ')

    class Meta:
        abstract = True
        verbose_name=u'Référencement'


class Page(FlatPage, Seo):
    if USE_JSSOR:
        slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow') 
    html = models.TextField(null=True, blank=True, verbose_name="Extra code html", help_text="Apparaitra après le contenu")
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=u'Edité le')
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True, verbose_name=u'Crée le')
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=u'Edité par')   
    published = models.BooleanField(default='published', verbose_name='Publié')
    
    
    class Meta:
        verbose_name = 'Page simple'
        verbose_name_plural = 'Pages simples'
        ordering = ('url','edited')
        


