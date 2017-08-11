Settings
========

``ALAPAGE_CODE_MODE = False`` : to use the wysywig editor instead of the code editor

``ALAPAGE_BASE_TEMPLATE_PATH = 'my_base_template.html'`` : to choose a root base template with a different name 
than the default ``base.html``

To configure the Ckeditor interface:

.. highlight:: python

::

   CKEDITOR_UPLOAD_PATH = 'uploads/'
   CKEDITOR_JQUERY_URL = '/static/js/jquery-2.1.4.min.js'
   CKEDITOR_IMAGE_BACKEND = 'pillow'
   CKEDITOR_CONFIGS = {
       'default': {
           'toolbar':  [
                       ["Format", "Styles", "Bold", "Italic", "Underline", '-', 'RemoveFormat'],
                       ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter','JustifyRight', 'JustifyBlock'],
                       ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'],
                       ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],["Source", "Maximize"],
                       ]
       },
       "removePlugins": "stylesheetparser",
       'width': '1150px',
       'height': '450px',
   }
