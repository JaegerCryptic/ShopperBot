"""
Setup file for the ShoppingBot package.
This file specifies the package metadata and dependencies.
"""

from setuptools import setup, find_packages

python_requires = (">=3.8",)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ShoppingBot",
    version="0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
            "flake8",
            "pre-commit",
            "isort",
            "mypy",
            "rope",
            "codespell",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["shoppingbot=shoppingbot.main:run"]},
    author="Kyle",
    author_email="kkent10@yahoo.com",
    description="A bot designed to buy pre-order items on websites.",
    license="MIT",
    url="https://github.com/JaegerCryptic/ShoppingBot",
)
