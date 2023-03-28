# df2latex
Convert CSV and Pandas DataFrames to LaTeX tables

## CSV to LaTeX
Basic Usage:
```
python df2latex.py -p mycsv.csv
```

To see available options:
```
python df2latex.py -h
```

## DataFrame to LaTeX

You can import the function and run it with the same options available at command line:
```python
from df2latex import df2latex

table = df2latex(myDF)
```
## Installation
Use the requirements file:
```
pip3 install -r requirements.txt
```
