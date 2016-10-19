# -*- coding: utf-8 -*-

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from alapage.models import Page
from alapage.conf import EDIT_MODE, CODEMIRROR_KEYMAP
if EDIT_MODE == "code":
    from codemirror2.widgets import CodeMirrorEditor


class PageAdminForm(forms.ModelForm):
    
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
                                                             #'fullScreen':'true',
                                                             },
                                                             script_template='codemirror2/codemirror_script_alapage.html',
                                                             modes=['css', 'xml', 'javascript', 'htmlmixed'],
                                                             )
                                  
                                  )
    else:
        content = forms.CharField(widget=forms.Textarea)
    content.required = False
    content.label = ""
    
    class Meta:
        model = Page
        exclude = ('edited', 'created', "editor")
