from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ansible-dynamic-inventory-mysql',
    packages=['ansible-dynamic-inventory-mysql'],
    version='0.1.1',
    python_requires='~=3.5',
    description='This is a Dynamic Inventory for Ansible to be used together with MySQL.',
    long_description=long_description,
    author='Askdaddy',
    author_email='askdaddy@gmail.com',
    url='https://github.com/askdaddy/ansible-dynamic-inventory-mysql',
    download_url='https://github.com/askdaddy/ansible-dynamic-inventory-mysql/archive/arya.zip',
    install_requires=[
        'configparser>=3.5.0',
        'PyMySQL>=0.7.11'
      ],
    keywords=['ansible','inventory','mysql']
)
