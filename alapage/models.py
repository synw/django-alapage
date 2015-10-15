# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from jssor.models import Slideshow

try:
    use_jssor=settings.ALAPAGE_USE_JSSOR
except:
    use_jssor=True


class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, verbose_name=u'Référencement: description')
    seo_keywords = models.CharField(max_length=120, null=True, verbose_name=u'Référencement: mots clés', help_text=u'Liste de mots clé séparés par des virgules ')

    class Meta:
        abstract = True
        verbose_name=u'Référencement'


class Page(FlatPage, Seo):
    if use_jssor:
        slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow') 
    html = models.TextField(null=True, blank=True, verbose_name="Extra code html", help_text="Apparaitra après le contenu")
    
    
    class Meta:
        verbose_name = 'Page simple'
        verbose_name_plural = 'Pages simples'
        ordering = ('url',)