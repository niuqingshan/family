from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='family',
      version=version,
      description="Easy to create your microservice based on Falcon.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='microservice,falcon',
      author='torpedoallen',
      author_email='torpedoallen@gmail.com',
      url='https://github.com/daixm/family',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'PasteScript',
          'check-manifest',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [console_scripts]
      family-createapp=family.commands.createapp:create
      [paste.paster_create_template]
      falcon = family.templates.basic:FalconTemplate
      """,
      )
