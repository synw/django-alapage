Install
=======

.. highlight:: bash

::

   pip install django-alapage django-ckeditor pytz
   # options
   pip install django-codemirror2 django-reversion djangoajax
   
   python manage.py collectstatic
   python manage.py makemigrations && python manage.py migrate
   
.. highlight:: python

::

   INSTALLED_APPS = (
	#~ ...
	#~ required
   'django_ajax',
	'ckeditor',
	'ckeditor_uploader',
	'alapage',
	#~ options 
	#'reversion',
	#'codemirror2',
    )
    
    
In urls.py

.. highlight:: python

::

   urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	# ...
	)
  
   urlpatterns += url(r'^', include('alapage.urls')),
    
You have to put alapage urls in last if you want to have your pages served from `/`

Create an uploads dir for Ckeditor:

.. highlight:: python

::

   mkdir static/uploads
    
Options
-------

- `Django Reversion <https://github.com/etianen/django-reversion>`_ for version control

``pip install django-reversion``

Add ``"reversion",`` to INSTALLED_APPS

- `Django Codemirror <https://github.com/synw/django-jssor>`_ for the code editor

``pip install django-codemirror2``

Add ``"codemirror2",`` to INSTALLED_APPS

Note: ``codemirror2`` should be loaded after ``alapage``

