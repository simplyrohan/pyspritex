from setuptools import setup

with open("README.md", "r") as readme:
    README = readme.read()

setup(
    name='pyspritex',
    version='0.0.1',
    packages=['pyspritex'],
    url='https://github.com/simplyrohan/pyspritex',
    license='MIT License',
    author='Rohan Gupta',
    author_email='',
    description='A package to make desktop applications easy to develop in python',
    long_description=README,
    long_description_content_type="text/markdown"
)
