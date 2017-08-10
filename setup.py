from setuptools import setup, find_packages
import re, sys, os

version = None
with open('family/__init__.py', 'r') as f:
    for line in f:
        m = re.match(r'^__version__\s*=\s*(["\'])([^"\']+)\1', line)
        if m:
            version = m.group(2)
            break

setup(name='family',
      version=version,
      description="Easy to create your microservice based on multiple python frameworks.",
      long_description="""\
""",
      keywords='microservice falcon flask',
      author='torpedoallen',
      author_email='torpedoallen@gmail.com',
      url='https://github.com/torpedoallen/family',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'PasteScript',
          'check-manifest',
          'wheel',
      ],
      entry_points="""
      [console_scripts]
      family-createapp=family.commands.createapp:create
      [paste.paster_create_template]
      falcon = family.templates.basic:FalconTemplate
      flask = family.templates.basic:FlaskTemplate
      common_wsgi = family.templates.basic:CommonWsgiTemplate
      """,
      )
