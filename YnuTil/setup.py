
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='YnuTil',
    version='0.1.0',
    author='Your Name',
    author_email='anpproba@gmail.com',
    description='A simple python project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/matrix11061991/JrsPy',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'numpy',
        'pandas'
    ],
)
