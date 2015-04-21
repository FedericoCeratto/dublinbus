from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='dublinbus',
    version='0.1alpha0',
    description='Dublin bus real time information from rtpi.ie site',
    long_description=readme(),
    classifiers=[
        'Development status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    keywords='rtpi.ie dublinbus',
    url='http://github.com/vasyl-purchel/dublinbus',
    author='Vasyl Purchel',
    author_email='vasyl.purchel@gmail.com',
    license='MIT',
    packages=['dublinbus'],
    install_requires=[
        'beautifulsoup4',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'dublinbus-stop=dublinbus.command_line:main'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
