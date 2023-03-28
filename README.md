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

## Examples
All examples will use the `sample.csv`:
```csv
Network,AP50,AR50
Model1,58.281845,61.58281
Model2,55.181458,58.18485
Model3,61.591958,56.28848
Model4,52.148581,59.19485
```

Basic Usage:
```
$ python df2latex.py -p ./sample.csv 

\begin{table}[!t]
    \centering
    \caption{My Table}
    \label{table:table}
    \begin{tabular}{l|c|c}
        \textbf{Network} & \textbf{AP50} & \textbf{AR50} \\
        \hline
        Model1 & 58.28 & 61.58 \\
        Model2 & 55.18 & 58.18 \\
        Model3 & 61.59 & 56.29 \\
        Model4 & 52.15 & 59.19 \\
    \end{tabular}
\end{table}
```

Round to 3 decimal places, set the caption and label:
```
$ python df2latex.py -p ./sample.csv -r 3 -c "Model Performance" -l results

\begin{table}[!t]
    \centering
    \caption{Model Performance}
    \label{table:results}
    \begin{tabular}{l|c|c}
        \textbf{Network} & \textbf{AP50} & \textbf{AR50} \\
        \hline
        Model1 & 58.282 & 61.583 \\
        Model2 & 55.181 & 58.185 \\
        Model3 & 61.592 & 56.288 \\
        Model4 & 52.149 & 59.195 \\
    \end{tabular}
\end{table}
```

## Installation
Use the requirements file:
```
pip3 install -r requirements.txt
```
