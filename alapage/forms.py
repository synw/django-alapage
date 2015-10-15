from django import forms
from django.conf import settings
from ckeditor.widgets import CKEditorWidget
from alapage.models import Page

try:
    use_jssor=settings.ALAPAGE_USE_JSSOR
except:
    use_jssor=True


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        if use_jssor:
            fields = ('url','title','slideshow','content','html','template_name','registration_required','seo_description','seo_keywords')
        else:
            fields = ('url','title','content','html','template_name','registration_required','seo_description','seo_keywords')
        widgets = {
          'content': CKEditorWidget,
        } 
        

