from setuptools import setup, find_packages


version = __import__('alapage').__version__

setup(
    name='django-alapage',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Page management app for Django',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-alapage',
    download_url='https://github.com/synw/django-alapage/releases/tag/' + version,
    keywords=['django', 'page management'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'Pillow',
        'pytz',
        'django-ckeditor',
        'django-codemirror2',
        "django-mptt",
        "django-mptt-graph",
    ],
    zip_safe=False
)
