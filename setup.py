from setuptools import setup, find_packages


setup(
    name="pipestatic",
    version="0.9.0",
    packages=find_packages(),
    author="Christian Wyglendowski",
    author_email="christian@dowski.com",
    description="A simple module that writes stats about your program to a named pipe.",
    license="BSD",
    keywords="monitoring stats statistics counters pipe",
    url="https://github.com/dowski/pipestatic/",
)
