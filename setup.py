from setuptools import setup, find_packages


version = __import__('alapage').__version__

setup(
  name = 'django-alapage',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = 'Page management app for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-alapage', 
  download_url = 'https://github.com/synw/django-alapage/releases/tag/'+version,
  keywords = ['django', 'page management', 'jssor', 'slideshows'], 
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  install_requires=[
        'Pillow',
        'pytz',
        'django-ckeditor',
        'django-codemirror2',
        "djangoajax",
        "django-mptt",
        "django-mptt-graph",
    ],
  zip_safe=False
)
