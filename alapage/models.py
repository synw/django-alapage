# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from mptt.models import TreeForeignKey, MPTTModel
from alapage.conf import USER_MODEL


class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, blank=True, verbose_name=_(u'SEO: description'), help_text=_(u'Short description of the page content'))
    seo_keywords = models.CharField(max_length=120, null=True, blank=True, verbose_name=_(u'SEO: keywords'), help_text=_(u'List of keywords separated by commas'))

    class Meta:
        abstract = True
        verbose_name=_(u'SEO')


class Page(MPTTModel, Seo):
    url = models.CharField(_(u'Url'), max_length=180, db_index=True)
    title = models.CharField(_(u'Title'), max_length=200)
    content = models.TextField(_(u'Content'), blank=True)
    template_name = models.CharField(_(u'Template name'), max_length=120, blank=True,
        help_text=_(u'If no template name is provided "alapage/default.html" will be used.')
    )
    registration_required = models.BooleanField(
        _(u'Registration required'),
        help_text=_(u"If this is checked, only logged-in users will be able to view the page."),
        default=False,
    )
    parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children', verbose_name=_(u'Parent page'))
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True, verbose_name=_(u'Created'))
    editor = models.ForeignKey(USER_MODEL, editable = False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   
    published = models.BooleanField(default=True, verbose_name=_(u'Published'))
    staff_only = models.BooleanField(default=False, verbose_name=_(u'Staff only'))
    superuser_only = models.BooleanField(default=False, verbose_name=_(u'Superuser only'))
    groups_only = models.ManyToManyField(Group, blank=True, verbose_name=_(u'Reserved to some groups'))
    users_only = models.ManyToManyField(USER_MODEL, blank=True, verbose_name=_(u'Reserved to some users'))
    # page caracteristics used to tminimize the select related queries
    is_reserved_to_groups = models.BooleanField(default=False, verbose_name=_(u'Reserved to groups'))
    is_reserved_to_users = models.BooleanField(default=False, verbose_name=_(u'Reserved to users'))
    
    
    class Meta:
        verbose_name = _(u'Page')
        verbose_name_plural = _(u'Page')
        ordering = ['url']
        permissions = (
            ("can_change_page_permissions", "Can change page permissions"),
        )
        
    def get_absolute_url(self):
        return self.url
    
    def __str__(self):
        return self.title
