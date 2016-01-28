Django Alapage
==============

[![Build Status](https://travis-ci.org/synw/django-alapage.svg?branch=master)](https://travis-ci.org/synw/django-alapage) 

Page management application with slideshows and responsive presentations for Django. 
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
- Django 1.8
- Django Flatpages
- Pillow
- Django ckeditor
- Django codemirror2

		pip install pytz pillow django-ckeditor django-codemirror2

- Optional: Django reversion

		pip install django-reversion
		
- Optional: [Django Jssor](https://github.com/synw/django-jssor) (slideshows)

		git clone https://github.com/synw/django-jssor.git && mv django-jssor/jssor path_to_your_project && mkdir media/jssor && mkdir media/jssor/thumbnails

- Optional: [Django Zongo](https://github.com/synw/django-zongo) (responsive presentations)

		git clone https://github.com/synw/django-zongo.git && mv django-zongo/zongo path_to_your_project && mkdir media/zongo
		

Install
--------------

- Clone the repository

		INSTALLED_APPS = (
			# ...
			# required
			'django.contrib.sites',
    		'django.contrib.flatpages',
		    'ckeditor',
		    'ckeditor_uploader',
		    'codemirror2',
		    'reversion',
		    'alapage',
			# options 
		    'jssor',
		    'zongo',
		)

- Optionnal: add `"jssor",` to INSTALLED_APPS if you plan to use the slideshows
- Optionnal: add `"zongo",` to INSTALLED_APPS if you plan to use the presentations

Warning: if you change these optional settings afterwards you will need to run the migrations again.

- `urls.py`:

		from alapage.views import HomepageView, PageView

		urlpatterns = patterns('',
		#...
		url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	    url(r'^(?P<url>.*/)$', PageView.as_view(), name='page-view'),
	    url(r'^$', HomepageView.as_view(), name='homepage-view'),
	    # option for responsive presentations
	    url(r'^zongo/', include('zongo.urls')),
	    )
    
- Collect static files

		python manage.py collectstatic

- Run migrations

		python manage.py makemigrations && python manage.py migrate

Config
--------------

Configure ckeditor in `settings.py` to suit you needs:

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

Options
--------------

To use django-reversion add the setting `ALAPAGE_USE_REVERSION = True`

To disable the slideshows add the setting `ALAPAGE_USE_JSSOR = False`

Disable the presentations the same way: set a `ALAPAGE_USE_ZONGO = False` setting

Todo
--------------

- [ ] More tests
- [ ] Base template selection option
- [ ] Add more layouts
- [ ] Theming option
