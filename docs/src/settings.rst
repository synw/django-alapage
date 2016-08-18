Settings
========

``ALAPAGE_USE_REVERSION = True`` : to enable reversion

``JSSOR_USE_ALAPAGE = True`` : to enable the slideshows. 
Warning: you will have to run a migration if you change this setting after the first migration.

``ALAPAGE_EDIT_MODE='code'`` : if you plan to code html manualy more than in the wysywig editor: 
this will enable the
codemirror editor.

``'ALAPAGE_CODEMIRROR_KEYMAP'='vim'`` : select your favourite keymap for codemirror editor (ex: "vim", "emacs"): 
default is no mapping

``ALAPAGE_BASE_TEMPLATE_PATH='my_base_template.html'`` : to choose a root base template with a different name 
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
