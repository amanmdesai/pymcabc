# pymcabc

[![License](https://img.shields.io/github/license/amanmdesai/pymcabc)](https://github.com/amanmdesai/pymcabc/blob/master/LICENSE.txt)
[![publish](https://github.com/amanmdesai/pymcabc/actions/workflows/publish.yml/badge.svg)](https://github.com/amanmdesai/pymcabc/actions/workflows/publish.yml)
[![test](https://github.com/amanmdesai/pymcabc/actions/workflows/test.yaml/badge.svg)](https://github.com/amanmdesai/pymcabc/actions/workflows/test.yaml)
[![PyPI Package latest release](https://img.shields.io/pypi/v/pymcabc.svg)](https://pypi.python.org/pypi/pymcabc)
[![Supported versions](https://img.shields.io/pypi/pyversions/pymcabc.svg)](https://pypi.python.org/pypi/pymcabc)
[![DOI](https://zenodo.org/badge/587987289.svg)](https://zenodo.org/badge/latestdoi/587987289)
[![PrePrint](https://img.shields.io/badge/Preprint-10.5281/zenodo.7546325-red.svg)](https://doi.org/10.5281/zenodo.7546325)


## Author

Aman Desai


##  Description

Monte Carlo Event Generator for the ABC theory

## Installation
```bash
pip install pymcabc
```

## Physics
The physics of ABC model (theory) is described in Grifiths and Aitchison.

## Simple script to start using the package:
1. Import pymcabc:
```python
import pymcabc
```

1. Define the process, for example:
```python
pymcabc.DefineProcess('A A > B B',mA=4,mB=10,mC=1,pi=30)
```

2. Calculate the total cross section of the process (in barn):
```python
pymcabc.CrossSection().calc_xsection()
```

3. Generate and Save events using a single command. Select whether to allow final state particle decays or not. Also select whether to apply detector effects on particle.

```python
pymcabc.SaveEvent(10000,boolDecay=True,boolDetector=True).to_root('name.root')
```

4. Analyze the root file. Basic analysis is possible by calling the `PlotData` module
```python
pymcabc.PlotData.file('name.root')
```

## References
1. For physics involved in the calculation, see for example, Introduction to Elementary Particles, David Griffiths.
