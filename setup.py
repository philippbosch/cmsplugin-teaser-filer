from setuptools import setup, find_packages

VERSION = __import__("cmsplugin_teaser_filer").__version__

setup(
    name='cmsplugin-teaser-filer',
    version=VERSION,
    description='Teaser plugin for django-cms and django-filer',
    long_description=open('README').read(),
    author='Philipp Bosch',
    author_email='hello@pb.io',
    maintainer='Philipp Bosch',
    maintainer_email='hello@pb.io',
    url='http://github.com/philippbosch/cmsplugin-teaser',
    license='BSD',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ]
)
