from setuptools import setup, find_packages

setup(
    name='python-cli-quickstart',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'mycli=cli.main:cli', # change app name
        ],
    },
)
