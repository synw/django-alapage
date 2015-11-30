# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django import forms
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget
from alapage.models import Page

USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', True)


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['template_name'].help_text = 'Si aucun nom de template n\'est défini ni de layout, "alapage/default.html" sera utilisé'
        self.fields['content'].label = ''
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Page
        exclude = ('enable_comments','sites')


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    date_hierarchy = 'edited'
    search_fields = ['name']
    list_display = ['url','title','edited','editor','created','published','registration_required']
    list_filter = ['created','edited','editor','published','registration_required']
    jssor_fieldset = ('url','title','slideshow')
    if not USE_JSSOR:
        jssor_fieldset = ('url','title')
    fieldsets = (
        (None, {
            'fields': ('content','html')
        }),
        (None, {
            'fields': jssor_fieldset
        }),
        ('Référencement', {
            'fields': ('seo_keywords','seo_description')
        }),
        ('Options', {
            'classes': ('collapse',),
            'fields': ('layout','template_name','registration_required','published')
        }),
    )
    

    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        obj.save()
    
#~ deactivate flatpages admin
admin.site.unregister(FlatPage)

