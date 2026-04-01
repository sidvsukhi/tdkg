# setup.py
from setuptools import setup, find_packages

setup(
    name="tdkg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Siddhant Sukhatankar",
    description="Time Decayed Knowledge Graph for AI memory systems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    url="https://github.com/yourusername/tdkg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)