Django Alapage
==============

[![Build Status](https://travis-ci.org/synw/django-alapage.svg?branch=master)](https://travis-ci.org/synw/django-alapage) 

Page management application with slideshows and responsive presentations for Django. Built on top of flatpages. 
The pages are editable in a wysiwyg editor and/or in a html/css code editor in the admin interface.

Screenshots
--------------

Wysiwig editor ( [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) ):

![Wysiwig editor](https://raw.github.com/synw/django-alapage/master/docs/img/wysiwyg_editor.png)

Code editor ( [django-codemirror2](https://github.com/sk1p/django-codemirror2) ):

![Code editor](https://raw.github.com/synw/django-alapage/master/docs/img/code_editor.png)

Dependencies
--------------

- pytz
- Pillow
- Django ckeditor
- Django codemirror2

  ```bash
pip install pytz pillow django-ckeditor django-codemirror2
  ```

- Optional: Django reversion

  ```bash
pip install django-reversion
  ```

- Optional: [Django Jssor](https://github.com/synw/django-jssor) (slideshows)

  ```bash
pip install django-jssor
  ```

- Optional: [Django Zongo](https://github.com/synw/django-zongo) (responsive presentations: :warning: Warning: experimental)

  ```bash
git clone https://github.com/synw/django-zongo.git && mv django-zongo/zongo path_to_your_project && mkdir media/zongo
  ```

Install
--------------

- Clone the repository

  ```python
INSTALLED_APPS = (
	#~ ...
	#~ required
	'django.contrib.sites',
	'django.contrib.flatpages',
    'ckeditor',
    'ckeditor_uploader',
    'codemirror2',
    'alapage',
	#~ options 
	#'reversion',
    #'jssor',
    #'zongo',
)
  ```
- Optionnal: add `"reversion",` to INSTALLED_APPS if you plan to use the django-reversion
- Optionnal: add `"jssor",` to INSTALLED_APPS if you plan to use the slideshows
- Optionnal: add `"zongo",` to INSTALLED_APPS if you plan to use the presentations

Warning: if you change these optional settings afterwards you will need to run the migrations again.

- `urls.py`:

  ```python
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	# ...
	)
  
urlpatterns += url(r'^', include('alapage.urls')),
  ```

:pencil2: You have to put alapage urls in last if you want to have your pages served from `/`

- Collect static files

		python manage.py collectstatic

- Run migrations

		python manage.py makemigrations && python manage.py migrate

Configuration
--------------

Configure ckeditor in `settings.py` to suit you needs:

  ```python
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
}
  ```

Optional settings
--------------

`ALAPAGE_USE_REVERSION = True` : to enable reversion

`ALAPAGE_USE_JSSOR = True` : to enable the slideshows. Warning: you will have to run a migration if you change this setting after the first migration.

`ALAPAGE_USE_PRESENTATIONS = True` : to enable the responsive presentations. Warning: you will have to run a migration if you change this setting after the first migration.

`ALAPAGE_CODE_MODE=True` : if you plan to code html manualy more than in the wysywig editor. This will put the code editor in front and collapse the wysywig editor.

`ALAPAGE_USE_THEMES = True` : theming option : [documented here](https://github.com/synw/django-alapage/tree/master/docs/themes)

`ALAPAGE_BASE_TEMPLATE_PATH='my_base_template.html'` : to choose a root base template with a different name than the default `base.html`

Management commands
--------------

Create a homepage: `python manage.py create_homepage`

Create a page: `python manage.py create_page 'Title' /url/`

Populate pages with content:

  ```python
#~ from string:
python manage.py populate_page "My content string"

#~ from file
python manage.py populate_page -f /my/file/path
  ```


Todo
--------------

- [ ] More tests
- [ ] Base template selection option
- [ ] Add more layouts

