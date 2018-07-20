from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='pha_nbextensions',
      version='0.0.1',
      description=u"Jupyter notebook extensions",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Public Health Applications",
      author_email='pha@psc.edu',
      url='https://github.com/PSC-PublicHealth/pha-nbextensions',
      license='MIT',
      packages=['update_environment'],
      include_package_data=True,
      zip_safe=False,
      )
