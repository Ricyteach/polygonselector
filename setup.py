from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='polygonselector',
    version='0.1',
    packages=find_packages(include=['notebook']),
    url='https://github.com/Ricyteach/polygonselector',
    license='MIT',
    long_description=readme,
    author='Ricky L Teachey Jr',
    author_email='ricky@teachey.org',
    description='A custom IPywidgets tool for graphically selecting shapely polygons inside a Jupyter notebook. '
)
