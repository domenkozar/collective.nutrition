from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.nutrition',
      version=version,
      description="Some food, recipes and grams.",
      long_description=long_description,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'lxml',
          'plone.app.dexterity',
          'collective.z3cform.datagridfield',
#          'collective.z3cform.chosen',
          'plone.api',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
