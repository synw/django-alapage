# -*- coding: utf-8 -*-

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from alapage.models import Page
from alapage.conf import CODE_MODE, CODEMIRROR_KEYMAP
if CODE_MODE is True:
    from codemirror2.widgets import CodeMirrorEditor


class PageAdminForm(forms.ModelForm):

    if CODE_MODE is False:
        content = forms.CharField(widget=CKEditorUploadingWidget())
    else:
        content = forms.CharField(
            widget=CodeMirrorEditor(options={
                'mode': 'htmlmixed',
                'width': '1170px',
                'indentWithTabs': 'true',
                #'indentUnit' : '4',
                'lineNumbers': 'true',
                'autofocus': 'true',
                #'highlightSelectionMatches': '{showToken: /\w/, annotateScrollbar: true}',
                'styleActiveLine': 'true',
                'autoCloseTags': 'true',
                'keyMap': CODEMIRROR_KEYMAP,
                'theme': 'blackboard',
                #'fullScreen':'true',
            },
                script_template='codemirror2/codemirror_script_alapage.html',
                modes=['css', 'xml', 'javascript', 'htmlmixed'],
            )

        )
    content.required = False
    content.label = ""

    class Meta:
        model = Page
        exclude = ('edited', 'created', "editor")
