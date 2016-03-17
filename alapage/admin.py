# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django import forms
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget
from codemirror2.widgets import CodeMirrorEditor
from alapage.models import Page, USE_PRESENTATIONS

USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', False)
USE_PRESENTATIONS=getattr(settings, 'ALAPAGE_USE_PRESENTATIONS', False)
USE_REVERSION=getattr(settings, 'ALAPAGE_USE_REVERSION', False)
if USE_REVERSION:
    from reversion.admin import VersionAdmin
CODE_MODE=getattr(settings, 'ALAPAGE_CODE_MODE', False)


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['template_name'].help_text = 'Si aucun nom de template n\'est défini ni de layout, "alapage/default.html" sera utilisé'
        self.fields['content'].label = ''
    content = forms.CharField(widget=CKEditorWidget())
    content.required = False
    
    class Meta:
        model = Page
        exclude = ('enable_comments','sites')

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
    jssor_fieldset = ('url','title')
    if USE_JSSOR:
        jssor_fieldset += ('slideshow',)
    if USE_PRESENTATIONS:
        jssor_fieldset += ('presentation',)
    if not CODE_MODE:
        fieldsets = (
            (None, {
                'fields': ('content',)
            }),
            ('Code html', {
                'classes': ('collapse',),
                'fields': ('html',)
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
    else:
        fieldsets = (
            (None, {
                'fields': ('html',)
            }),
            ('Editeur', {
                'classes': ('collapse',),
                'fields': ('content',)
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
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "html":
            kwargs['widget'] = CodeMirrorEditor(options={'mode': 'htmlmixed','indentWithTabs':'true','lineNumbers':'true'}, modes=['css', 'xml', 'javascript', 'htmlmixed'])
        return super(PageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        obj.save()
    
#~ deactivate flatpages admin
admin.site.unregister(FlatPage)

