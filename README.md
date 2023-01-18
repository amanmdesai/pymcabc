# pymcabc

[![License](https://img.shields.io/github/license/amanmdesai/pymcabc)](https://github.com/amanmdesai/pymcabc/blob/master/LICENSE.txt)
[![publish](https://github.com/amanmdesai/pymcabc/actions/workflows/publish.yaml/badge.svg)](https://github.com/amanmdesai/pymcabc/actions/workflows/publish.yaml)
[![test](https://github.com/amanmdesai/pymcabc/actions/workflows/test.yaml/badge.svg)](https://github.com/amanmdesai/pymcabc/actions/workflows/test.yaml)

## Author

Aman Desai


##  Description

Monte Carlo Event Generator for the ABC theory

## Installation
```bash
pip install pymcabc
```

## Physics
The physics of ABC model (theory) is described in Grifiths.

## Simple script to start using the package:

- 1. Define the process, for example:
```python
pymcabc.DefineProcess(`A A > B B',mA=4,mB=10,mC=1,Ecm=30)
```

2. Calculate the total cross section of the process:
```python
pymcabc.CrossSection().calc_xsection()
```

3. Generate and Save events using a single command. Select whether to allow final state particle decays or not. Also select whether to apply detector effects on particle.
pymcabc.SaveEvent(10000,boolDecay=True,boolDetector=True).to_root('name.root')


4. Analyze the root file. Basic analysis is possible by calling the `PlotData` module
```python
PlotData.file('name.root')
```

## References
1. For physics involved in the calculation, see for example, Introduction to Elementary Particles, David Griffiths.
