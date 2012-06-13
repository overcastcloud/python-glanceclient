import os
import sys

import setuptools

from glanceclient.openstack.common import setup


requires = setup.parse_requirements()
dependency_links = setup.parse_dependency_links()
tests_require = setup.parse_requirements(['tools/test-requires'])

if sys.version_info < (2, 6):
    requires.append('simplejson')


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="python-glanceclient",
    version="2012.2",
    description="Client library for OpenStack Image API",
    long_description=read('README.rst'),
    url='https://github.com/openstack/python-glanceclient',
    license='Apache',
    author='OpenStack Glance Contributors',
    author_email='glance@example.com',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    cmdclass=setup.get_cmdclass(),
    install_requires=requires,
    dependency_links=dependency_links,
    tests_require=tests_require,
    test_suite="nose.collector",
    entry_points={'console_scripts': ['glance = glanceclient.shell:main']},
)
