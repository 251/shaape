#!/usr/bin/env python

import sys
from setuptools import setup

try:
    import cairo
except ImportError:
    print ("Some dependencies could not be found. Make sure to install "
           "the Python bindings for Cairo(import cairo).")
    sys.exit(1)

try:
    from gi.repository import Pango
    from gi.repository import PangoCairo
except ImportError:
    print ("Some dependencies could not be found. Make sure to install "
           "the PyGObject.")
    sys.exit(1)

setup(name='shaape',
      version='1.1.1',
      description='Shaape - ascii art to image converter',
      author='Christian Goltz',
      author_email='goltzchristian@googlemail.com',
      package_data={'shaape': ['data']},
      packages=['shaape'],
      scripts=['bin/shaape'],
      license='LICENSE',
      url='http://github.com/christiangoltz/shaape',
      tests_require=['nose'],
      install_requires=['networkx', 'PyYAML', 'scipy', 'numpy']
      )
