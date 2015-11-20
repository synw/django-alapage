from setuptools import setup, find_packages

setup(
  name = 'django-alapage',
  packages=find_packages(),
  version = '0.1',
  description = 'Simple page management application with slideshows',
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
    ],
  zip_safe=False
)
