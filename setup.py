from setuptools import find_packages, setup

setup(
    name='Project',
    author='Priyanka',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    long_description='''

    This project is based on scraping datails of products from myntra official website and 
    recommend product based on user search also analyse the product general informations..
    
    ''',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)