Django Alapage
==============

Simple page management application with slideshows for Django


Dependencies
--------------

- Django Flatpages
- Pillow
- Django ckeditor
- Django Jssor (optionnal)


Install
--------------

- Clone the repository
- Add "alapage" to INSTALLLED_APPS
- Optionnal: add "jssor" to INSTALLLED_APPS if you plan to use the slideshows
- Add the line in  urls.py:

	url(r'^ckeditor/', include('ckeditor.urls'))
	
- Add these lines at the end of urls.py:

	url(r'^(?P<url>.*/)$', PageView.as_view()),
    url(r'^$', HomepageView.as_view()),
    
- Collect static files
- Run migrations


Options
--------------

To use the application in standalone mode with no slideshows add the setting ALAPAGE_USE_JSSOR = False


Note: this application is compatible with [django-xadmin](https://github.com/sshwsfc/django-xadmin)