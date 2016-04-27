# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django import forms
from django.contrib.flatpages.models import FlatPage
from alapage.models import Page
from alapage.forms import PageAdminForm
from alapage.conf import USE_JSSOR, USE_PRESENTATIONS, USE_REVERSION, EDIT_MODE


if USE_REVERSION:
    from reversion.admin import VersionAdmin
admin_class=admin.ModelAdmin
if USE_REVERSION:
    admin_class=VersionAdmin
@admin.register(Page)
class PageAdmin(admin_class):
    form = PageAdminForm
    date_hierarchy = 'edited'
    search_fields = ['title','url','editor__username']
    list_display = ['url','title','edited','editor','created','published','registration_required']
    list_display_links = ['title','url']
    list_filter = ['created','edited','published','registration_required']
    save_on_top = True

    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super(PageAdmin, self).get_fieldsets(request, obj)
        jssor_fieldset = ('url','title')
        if USE_JSSOR:
            jssor_fieldset += ('slideshow',)
        if USE_PRESENTATIONS:
            jssor_fieldset += ('presentation',)
        fieldsets = (
            (None, {
                'fields': ('content',)
            }),
            (None, {
                'fields': jssor_fieldset
            }),
            ('Référencement', {
                'classes': ('collapse',),
                'fields': ('seo_keywords','seo_description')
            }),
            ('Options', {
                'classes': ('collapse',),
                'fields': ('layout', 'template_name','registration_required','published',)
            }),
        )
        return fieldsets
    
    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        obj.save()
    
#~ deactivate flatpages admin
admin.site.unregister(FlatPage)

