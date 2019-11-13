# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="PyGrouper",
    version="0.1",
    description=(
        "Function to collect data into fixed-length chunks or blocks. "
        "adapted from the Python itertool docs at: "
        "https://docs.python.org/2/library/itertools.html"
    ),
    author="P. Scott DeVos",
    author_email="scott@bintouch.org",
    license="BSD 4-Clause",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],
    keywords="UUID uuid human readable",
    url="https://github.com/pscottdevos/pygrouper",
)
