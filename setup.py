import re
import os
from setuptools import setup, find_packages


version = re.search('^__version__\s*=\s*"(.*)"',
                    open('um-ct/__init__.py').read(), re.M).group(1)


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    ]

setup(name='user-management-ct',
      version=version,
      description='user management container',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application", ],
      author='Piotr Czaja',
      author_email='czaja_piotr@o2.pl',
      url='https://github.com/piotrczaja/',
      keywords='webapp core falcon',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="um-ct",
      )