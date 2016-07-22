Django Alapage
==============

[![Build Status](https://travis-ci.org/synw/django-alapage.svg?branch=master)](https://travis-ci.org/synw/django-alapage) 

Page management application with slideshows for Django. Built on top of flatpages. 
The pages are editable in a wysiwyg editor or in a html/css code editor in the admin interface. 

Screenshots
--------------

Pages can be edited in wysiwyg mode or code mode with ( [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) ) 
or ( [django-codemirror2](https://github.com/sk1p/django-codemirror2) )

![Editors](https://raw.github.com/synw/django-alapage/master/docs/img/editors.png)


Install
--------------

  ```bash
pip install django-alapage
  ```

Options: Django reversion, Codemirror editor, Django Jssor

  ```bash
pip install django-reversion
pip install django-codemirror2
pip install django-jssor
  ```

In `settings.py`:

  ```python
INSTALLED_APPS = (
	#~ ...
	#~ required
	'django.contrib.admin',
	'django.contrib.sites',
	'django.contrib.flatpages',
    'ckeditor',
    'ckeditor_uploader',
    'alapage',
	#~ options 
	#'reversion',
	#'codemirror2',
    #'jssor',
)
  ```
Note: `codemirror2` should be loaded after `alapage`

- Optionnal: add `"reversion",` to INSTALLED_APPS if you plan to use the django-reversion
- Optionnal: add `"jssor",` to INSTALLED_APPS if you plan to use the slideshows
- Optionnal: add `"codemirror",` to INSTALLED_APPS if you plan to use this editor

Check the optional settings below.

In `urls.py`:

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
        'width': '1150px',
        'height': '450px',
    },
}
  ```

Optional settings
--------------

`ALAPAGE_USE_REVERSION = True` : to enable reversion

`ALAPAGE_USE_JSSOR = True` : to enable the slideshows. Warning: you will have to run a migration if you change this setting after the first migration.

`ALAPAGE_EDIT_MODE='code'` : if you plan to code html manualy more than in the wysywig editor. This will put the code editor in front and collapse the wysywig editor.

`'ALAPAGE_CODEMIRROR_KEYMAP'='vim'` : select your favourite keymap for codemirror editor (ex: "vim", "emacs"): default is no mapping

`ALAPAGE_BASE_TEMPLATE_PATH='my_base_template.html'` : to choose a root base template with a different name than the default `base.html`

Using the slideshows
--------------

This feature enables the page to serve different slideshows according to the screen with.
Enable the slideshows in the settings. To link a responsive slideshow to a page do the following:

- In the django-jssor admin create a slideshow with the "Slideshow group" set (Ex: "homepage") and no breakpoints. This
one will be used for the desktop version.

- Create more slideshows with breakpoints using the same "Slideshow group" value. Note: a slideshow with a 360px
breakpoint needs slides with images that have a width of 360px to optimize the loading time.

- In the alapage admin create a page and fill the "Slideshow group" with the value corresponding to your slideshow group
("homepage" in our example). Set the breakpoints according to the slideshows that belong to the group.

The proper slideshow will be loaded according to the screen width. By default it loads these in a "precontent" block
that must be in your base template. To change this behavior cutomize the template `templates/alapage/default.html` or 
make new ones.


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

