"""
Setup file for the ShoppingBot package.
This file specifies the package metadata and dependencies.
"""

from setuptools import setup, find_packages

setup(
    name="ShoppingBot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium>=3.141.0",
    ],
    extras_require={
        "dev": [
            "pylint",
            "black",
        ],
    },
)
