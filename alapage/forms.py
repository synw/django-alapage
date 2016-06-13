# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from codemirror2.widgets import CodeMirrorEditor
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from alapage.models import Page
from alapage.conf import EDIT_MODE, CODEMIRROR_KEYMAP, USE_JSSOR


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        try:
            self.fields['template_name'].help_text = _(u'If no template is defined neither any layout, "alapage/default.html" will be used' )
        except:
            pass
    
    if EDIT_MODE == 'visual':    
        content = forms.CharField(widget=CKEditorUploadingWidget())
    elif EDIT_MODE == 'code':
        content = forms.CharField(
                                  widget=CodeMirrorEditor(options={
                                                             'mode':'htmlmixed',
                                                             'width':'1170px',
                                                             'indentWithTabs':'true', 
                                                             #'indentUnit' : '4',
                                                             'lineNumbers':'true',
                                                             'autofocus':'true',
                                                             #'highlightSelectionMatches': '{showToken: /\w/, annotateScrollbar: true}',
                                                             'styleActiveLine': 'true',
                                                             'autoCloseTags': 'true',
                                                             'keyMap': CODEMIRROR_KEYMAP,
                                                             'theme':'blackboard',
                                                             }, 
                                                             modes=['css', 'xml', 'javascript', 'htmlmixed'],
                                                             )
                                  
                                  )
    else:
        content = forms.CharField(widget=forms.Textarea)
    content.required = False
    
    class Meta:
        model = Page
        exclude = ('enable_comments','sites')
