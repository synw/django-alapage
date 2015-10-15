Django Alapage
==============

Simple page management application for Django


Dependencies
--------------

- Django Flatpages
- Pillow
- Django Jssor (optionnal)


Install
--------------

- Clone the repository
- Add "alapage" to INSTALLLED_APPS
- Optionnal: add "django_jssor" to INSTALLLED_APPS if you plan to use the slideshows
- Add the line url(r'^ckeditor/', include('ckeditor.urls')), to urls
- Collect static files
- Run migrations


Options
--------------

To use the application in standalone mode with no slideshows add the setting ALAPAGE_USE_JSSOR = False


Note: this application is compatible with [django-xadmin](https://github.com/sshwsfc/django-xadmin)