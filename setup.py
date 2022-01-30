from struct import pack
from setuptools import setup

with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "src",
    version = "0.0.1",
    author = "almaideen",
    description ="A Samall Package for ANN Implementation",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/almaideen/ANNimplementation",
    author_email = "almhdmaideen@gmail.com",
    packages = ['src'],
    python_requires = ">=3.7",
    install_requires = [
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn"
        ]
)