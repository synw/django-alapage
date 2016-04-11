# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from alapage.models import Page
from alapage.conf import EDIT_MODE


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['template_name'].help_text = 'Si aucun nom de template n\'est défini ni de layout, "alapage/default.html" sera utilisé'
        #self.fields['content'].label = ''
        if EDIT_MODE == 'code':
            self.fields['html'].label = 'Html'
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content.required = False
    
    class Meta:
        model = Page
        exclude = ('enable_comments','sites')
