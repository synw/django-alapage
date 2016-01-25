from setuptools import setup, find_packages

setup(
  name = 'django-alapage',
  packages=find_packages(),
  version = '0.2',
  description = 'Page management with slideshows and responsive presentations for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-alapage', 
  download_url = '',
  keywords = ['django', 'page management', 'jssor','slideshows'], 
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  install_requires=[
        "Django >= 1.8.0",
        'Pillow',
        'pytz',
        'django-ckeditor',
        'django-codemirror2',
    ],
  zip_safe=False
)
