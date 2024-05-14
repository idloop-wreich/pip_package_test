from setuptools import setup

setup(
    name='pip_package_test',
    version='1.0',
    description='Simple Python package for testing',
    url='https://github.com/idloop-wreich/pip_package_test.git',
    author='Wieland Reich',
    author_email='wieland.reichd@idloop.com',
    license='none',  # TODO: set proper value
    packages=['pip_package_test'],
    install_requires=['PySide6>=6.7.0',  # installed in Python should be: datetime, os, argparse, re, uuid, struct, ..
                      'numpy>=1.26.4',
                      'untangle>=1.2.1'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: BSI',
        'License :: Freeware',  # of course not, but what license exactly?
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Programming Language :: Python :: 3.10.6',
        'Programming Language :: Python :: 3.12',
    ],
)
