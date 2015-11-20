Django Alapage
==============

Simple page management application with slideshows for Django


Dependencies
--------------

- pytz
- Django 1.8
- Django Flatpages
- Pillow
- Django ckeditor
- Django Jssor (optionnal)

		pip install pytz pillow django-ckeditor 
		git clone https://github.com/synw/django-jssor.git

Install
--------------

- Clone the repository

		INSTALLED_APPS = (
			# ...
		    'ckeditor',
		    'ckeditor_uploader',
		    'alapage',
			# option
		    'jssor',
		)

- Optionnal: add "jssor" to INSTALLLED_APPS if you plan to use the slideshows
- urls.py:

		from alapage.views import HomepageView, PageView

		urlpatterns = patterns('',
		#...
		url(r'^ckeditor/', include('ckeditor.urls'))
	    url(r'^(?P<url>.*/)$', PageView.as_view()),
	    url(r'^$', HomepageView.as_view()),
	    )
    
- Collect static files
- Run migrations

Config
--------------

Configure ckeditor to suit you needs:

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

To use the application in standalone mode with no slideshows add the setting ALAPAGE_USE_JSSOR = False
