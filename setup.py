#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name="single-cell-schema",
    version="0.1.0",
    description="LinkML schema for single cell transcriptomics data following the CellXGene schema",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/CxG_CL_KG_LInkML",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "linkml>=1.8.0",
        "anndata>=0.11.0",
        "scanpy>=1.11.0",
        "numpy>=2.1.0",
        "pandas>=2.2.0",
        "matplotlib>=3.10.0",
        "networkx>=3.4.0",
    ],
    entry_points={
        "console_scripts": [
            "sc-gen-sample=data.generate_sample_data:main",
            "sc-populate-schema=data.populate_schema:main",
            "sc-validate=data.validate_data:main",
            "sc-visualize=data.visualize_graph:main",
            "sc-run-example=data.run_example:run_example",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)