from setuptools import setup
import os


with open(os.path.join(os.getcwd(), 'README')) as readme:
    long_description = readme.read()


setup(
    name='gglproxy',
    version='0.1',
    description='Using cache and translate Google proxy to visit websites',
    long_description=long_description,
    classifiers=[   # TODO
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7.13',
        'Topic :: XXX :: YYY',
      ],
    keywords='google proxy cache translate',
    url='http://github.com/Samdney/gglproxy',
    author='Carolin Z\u00f6belein', # TODO
    author_email='contact@carolin-zoebelein.de',    # TODO
    license='MIT',  # TODO
    packages=['gglproxy'],
    install_requires=[  # TODO
        'argparse',
    ],
    scripts=['bin/gglproxy'],
    include_package_data=True,  # TODO
    zip_safe=False
    )
