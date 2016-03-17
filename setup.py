from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='family',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='microservice',
      author='daixm',
      author_email='torpedoallen@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'PasteScript',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [console_scripts]
      family-createapp=family.commands.createapp:create
      [paste.paster_create_template]
      falcon = family.templates.basic:FalconTemplate
      """,
      )
