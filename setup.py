"""
    author: Mahi Sarwar Anol
"""

from setuptools import find_packages, setup

### setup used for meta data.
### find_packages used for selecting the modules that we want to consider.

### Read README.md for long description
with open('requirements.txt','r',encoding='utf-8') as f:
    required=f.read().splitlines() ### converts to list

### Read Requirements file
with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

setup(
    name="Mini Redis by Mahi",
    version="0.1.0",
    author="Mahi Sarwar Anol",
    author_email="anol.mahi@gmail.com",
    description="A minimal implementation of Redis that have all the main Redis functionalities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahi-anol/mini-redis-from-first-principal.git",
    packages=find_packages(),
    classifiers=[
        "Development Status ::  3- Beta",
        "Programing Language :: python >=3.11",
        "Operating System :: Os Independent",
     
    ],
    python_requires=">=3.11",
    install_requires=required,
    extras_require={
        'dev': [
            'pytest>=7.1.1',
            'pytest-cov>=2.12.1',
            'flake8>=3.9.0',
            'black>=22.3.0',
            'isort>=5.10.1',
            'mypy>=0.942',
        ],
    }
)