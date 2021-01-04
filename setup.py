from setuptools import setup

setup(name='datapeek',
      version='0.1',
      description='A simple library for dealing with raw data.',
      url='https://github.com/briantacderan/py-pkg-test',
      author='Brian Tacderan',
      author_email='briantacderan@gmail.com',
      license='MIT',
      packages=['datapeek'],
      install_requires=[
          'fuzzywuzzy',
          'pandas'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
