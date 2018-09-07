from setuptools import setup
from beam import __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="beam",
    version=__version__,
    description="Beam Pilot",
    long_description=readme(),
    author="Graham Krizek",
    author_email="gkrizek@krizek.io",
    url="https://github.com/gkrizek/beam",
    packages=["beam"],
    py_modules=['beam'],
    install_requires=[
        "boto3",
        "click",
        "requests",
        "toml"
    ],
    entry_points={
        "console_scripts": ['beam = beam.index:main']
    }
)
