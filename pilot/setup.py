from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="beam",
    version="0.1.0",
    description="Beam Pilot",
    long_description=readme(),
    author="Graham Krizek",
    author_email="gkrizek@krizek.io",
    url="https://github.com/gkrizek/beam",
    packages=["beam"],
    py_modules=['beam'],
    install_requires=[
        "boto3",
        "requests"
    ],
    entry_points={
        "console_scripts": ['beam = beam.index:main']
    }
)
