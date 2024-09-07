from setuptools import setup

REQUIRES = [
    'records',
    'structlog',
    'allure-pytest'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/DoraSigulia/db_client.git',
    license='MIT',
    author='Daria Sigulya',
    author_email='',
    install_requires=REQUIRES,
    description='db_client'
)
