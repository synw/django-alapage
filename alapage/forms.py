# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from alapage.models import Page
from alapage.conf import EDIT_MODE


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['template_name'].help_text = _(u'If no template is defined neither any layout, "alapage/default.html" will be used' )
        if EDIT_MODE == 'code':
            self.fields['html'].label = 'no label'
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content.required = False
    
    class Meta:
        model = Page
        exclude = ('enable_comments','sites')
