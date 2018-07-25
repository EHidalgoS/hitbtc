from setuptools import setup

VERSION = '1.0.4'

setup(name='hitbtc_mod',
      version=VERSION,
      description='HitBTC Websocket API Client',
      author='Nils Diefenbach',
      author_email='23okrs20+gitlab@mykolab.com',
      packages=['hitbtc'],
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      install_requires=['websocket-client'],
      package_data={'': ['*.md', '*.rst']})

