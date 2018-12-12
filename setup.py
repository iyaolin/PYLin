
from setuptools import setup, find_packages

setup(
    name='PYLin',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='YLin-Python-Package,
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/BillMills/python-package-example',
    author='Yao Lin',
    author_email='yaolin.bnu@qqmail.com'
)
