Install
=======

.. highlight:: bash

::

   pip install django-alapage

Then migrate
   
.. highlight:: python

::

   INSTALLED_APPS = (
	#~ ...
	'ckeditor',
	'ckeditor_uploader',
	'reversion',
	'codemirror2',
	'alapage',
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

Create an uploads directory for Ckeditor:

.. highlight:: python

::

   mkdir static/uploads

