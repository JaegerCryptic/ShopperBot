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
        "requests",
        "beautifulsoup4",
        "webdriver-manager",
        "retry",
    ],
    extras_require={
        "dev": [
            "pylint",
            "black",
            "bandit",
            "coverage",
        ],
    },
    entry_points={"console_scripts": ["shoppingbot=shoppingbot.main:run"]},
    author="Kyle",
    author_email="kkent10@yahoo.com",
    description="A bot designed to buy pre-order items on websites.",
    license="MIT",
    url="https://github.com/JaegerCryptic/ShoppingBot",
)
