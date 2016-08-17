Management commands
===================

Create a homepage: ``python manage.py create_homepage``

Create a page: ``python manage.py create_page 'Title' /url/``

Populate pages with content:

.. highlight:: bashs

::

   # from string:
   python manage.py populate_page "My content string"
   
   # from file
   python manage.py populate_page -f /my/file/path