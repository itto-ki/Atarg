from setuptools import setup, find_packages
from os import path

root_dir = path.abspath(path.dirname(__file__))

setup(
        name='atarg',
        version='0.0.1',
        description='Testing tool before submit for atcoder',
        author='Ittoh Kimura',
        author_email='kimura.itto.kd3@gmail.com',
        install_requests=[
            'requests',
            'beautifulsoup4'
            ],
        package_dir={'': 'src'},
        packages=find_packages(where='src', exclude=('tests')),
        scripts=['scripts/atarg'],
        test_suite='tests',
        )
