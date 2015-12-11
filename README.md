Django Alapage
==============

[![Build Status](https://travis-ci.org/synw/django-alapage.svg?branch=master)](https://travis-ci.org/synw/django-alapage) 

Page management application with slideshows and responsive presentations for Django


Dependencies
--------------

- pytz
- Django 1.8
- Django Flatpages
- Pillow
- Django ckeditor

		pip install pytz pillow django-ckeditor 
		
- Optionnal: [Django Jssor](https://github.com/synw/django-jssor) (slideshows)
- Optionnal: [Django Zongo](https://github.com/synw/django-zongo) (responsive presentations)

		git clone https://github.com/synw/django-jssor.git && mv jssor path_to_your_project && mkdir media/jssor
		git clone https://github.com/synw/django-zongo.git && mv zongo path_to_your_project && mkdir media/zongo
		

Install
--------------

- Clone the repository

		INSTALLED_APPS = (
			# ...
			'django.contrib.sites',
    		'django.contrib.flatpages',
		    'ckeditor',
		    'ckeditor_uploader',
		    'alapage',
			# options 
		    'jssor',
		    'zongo',
		)

- Optionnal: add `"jssor",` to INSTALLLED_APPS if you plan to use the slideshows
- Optionnal: add `"zongo",` to INSTALLLED_APPS if you plan to use the presentations
Warning: if you change these settings afterwards you will need to run the migrations again

- urls.py:

		from alapage.views import HomepageView, PageView

		urlpatterns = patterns('',
		#...
		url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	    url(r'^(?P<url>.*/)$', PageView.as_view(), name='page-view'),
	    url(r'^$', HomepageView.as_view(), name='homepage-view'),
	    )
    
- Collect static files
- Run migrations

Config
--------------

Configure ckeditor in settings.py to suit you needs:

	CKEDITOR_UPLOAD_PATH = 'uploads/'
	CKEDITOR_JQUERY_URL = '/static/js/jquery-2.1.3.min.js'
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

To use the application in standalone mode with no slideshows add the setting `ALAPAGE_USE_JSSOR = False`

You can disable the presentations the same way: set a `ALAPAGE_USE_ZONGO = False` setting

Todo
--------------

- [ ] More tests
- [ ] Base template selection option
- [ ] Add more layouts
- [ ] Theming option
