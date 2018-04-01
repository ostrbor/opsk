from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='opsk',
    version='0.0.1',
    packages=['opsk'],
    url='',
    license='',
    author='ostrbor',
    author_email='',
    description='',
    install_requires=[
        'geopy',
    ],
    dependency_links=['git+https://github.com/openskynetwork/opensky-api.git#egg=python'],
)
