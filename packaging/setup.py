import datetime
import git
import os
from setuptools import setup, find_packages, Extension
import sys

setup(
    name="kb_summarization_realtime",
    # This is just name, associated with package management, 
    # pip uninstall kb_summarization_realtime can delete multiple packages
    version='0.0.2',
    author="xxx.xxx",
    author_email="xxx@hotmail.com",
    description="Document Summarization",
    long_description="This is a long description",
    long_description_content_type="text/markdown",
    url="https://",
    packages=find_packages(
        exclude=['apps.*', 'apps', '__pycache__', 'tests', 'model']),
    # this is required, should not be empty
    # packages = ['kb_summarization', 'kb_summarization.utils']
    setup_requires=[
        'cython',
        'numpy',
        'setuptools>=18.0',
    ],
    install_requires=[
        'torch==1.6.0',
        "transformers==2.11.0"   ],
        'sentencepiece==0.1.95',
    #package_dir={'kb_summarization_realtime': 'src'}, not required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)