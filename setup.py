import setuptools

with open('README.md','r') as file:
    long_description = file.read()

setuptools.setup(
name="pymcabc",
version="0.1.0",
description= "Monte Carlo Event Generator for the ABC theory",
author="Aman Desai",
author_email="amanmukeshdesai@gmail.com",
maintainer="Aman Desai",
maintainer_email="amanmukeshdesai@gmail.com",
url = "https://github.com/amanmdesai/pymcabc",
long_description=long_description,
packages=["pymcabc"],
install_requires=["numpy","uproot"],
long_description_content_type="text/markdown",
classifiers=["License :: OSI Approved :: MIT License",
             "Programming Language :: Python :: 3",
             "Programming Language :: Python :: 3.8",
             "Programming Language :: Python :: 3.9",
             "Programming Language :: Python :: 3.10",
             "Topic :: Scientific/Engineering :: Physics",
             "Operating System :: Unix",
             "Operating System :: Microsoft :: Windows",
             "Operating System :: MacOS"]
)
