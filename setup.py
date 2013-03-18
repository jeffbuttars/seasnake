
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    setup(
        name='seasnake',
        version='0.1',
        description='Python API client for Digital Ocean.',
        author='Jeff Buttars',
        packages=['seasnake'],
        install_requires=['requests'],
    )
