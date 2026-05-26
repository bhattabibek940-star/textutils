from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
name="textutils-bibekbhatta",
version="0.1.0",
author="Bibek Bhatta",
author_email="bibek@example.com",
description="Simple text utilities: reverse, palindrome, vowels, capitalize",
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/bibekbhatta/textutils-bibekbhatta",
packages=find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
],
python_requires=">=3.6",
)