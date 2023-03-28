import pandas as pd
from jinja2 import Environment
from typing import Union
from argparse import ArgumentParser

TABLE_STR = r"""
\begin{table}[!!-location-!]
    \centering
    \caption{!-caption-!}
    \label{table:!-label-!}
    \begin{tabular}{!-align-!}
        !-data-!
    \end{tabular}
\end{table}
"""


def csv2latex(
    csv,
    delim=",",
    round: int = 2,
    columns: Union[list, None] = None,
    align: Union[str, None] = None,
    caption: str = "My Table",
    label: str = "table",
    location: str = "t",
):
    df = pd.read_csv(csv, sep=delim)
    return df2latex(
        df,
        round=round,
        columns=columns,
        align=align,
        caption=caption,
        label=label,
        location=location,
    )


def df2latex(
    df: pd.DataFrame,
    round: int = 2,
    columns: Union[list, None] = None,
    align: Union[str, None] = None,
    caption: str = "My Table",
    label: str = "table",
    location: str = "t",
):
    """Pandas DataFrame to Latex Table

    Args:
        df (Pandas DataFrame): The dataframe to convert to latex
        round (int, optional): Number of decimals to round values to. Defaults to 2.
        columns (list, optional): The columns to print. Defaults to all columns (none).
        align (str, optional): How columns should be aligned. Defaults to center for all but first.
        caption (str, optional): The caption for the table. Defaults to "My Table".
        label (str, optional): The label for the table. Defaults to "table".
        location (str, optional): The location of the table. Defaults to "t".

    Returns:
        str: LaTeX table of the DF witht the given options
    """

    # create jinja2 env
    env = Environment(variable_start_string="!-", variable_end_string="-!")

    # get the columns to use if necessary
    if columns is not None:
        df = df[columns].reset_index(drop=True)
    # get ncols
    _, ncols = df.shape

    # build the header
    header = " & ".join([f"\\textbf{{{col}}}" for col in df.columns]) + " \\\\"
    # build the str to template each row
    row_str = " & ".join([f"!-{col}-!" for col in df.columns]) + " \\\\"
    # create the jinja template for the row
    row_template = env.from_string(row_str)

    # round if ncessary
    if round is not None:
        df = df.round(round)

    # each item in this list is a row of the table
    rows = [header, "\hline"] + [
        row_template.render(rowData) for rowData in df.to_dict(orient="records")
    ]
    # get the rows as str
    all_rows = "\n\t".join(rows)

    # get the template for the table
    table_template = env.from_string(TABLE_STR)

    # set align if not set
    if align is None:
        align_list = ["l"] + (["c"] * (ncols - 1))
        align = "|".join(align_list)

    # generate the table
    table = table_template.render(
        data=all_rows, caption=caption, label=label, align=align, location=location
    )

    # return it
    return table


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "-p", "--csv", required=True, help="The CSV to convert to latex"
    )
    parser.add_argument("-d", "--delim", default=",", help="The delimiter in the CSV")
    parser.add_argument(
        "-r",
        "--round",
        type=int,
        default=2,
        help="Number of decimal places to round to.",
    )
    parser.add_argument(
        "-a", "--align", default=None, help="How to align columns in LaTeX"
    )
    parser.add_argument(
        "-c",
        "--caption",
        type=str,
        default="My Table",
        help="Caption of the LaTeX table",
    )
    parser.add_argument(
        "-l", "--label", type=str, default="table", help="Label of the LaTeX table"
    )
    parser.add_argument(
        "--location", type=str, default="t", help="Location of the LaTeX table"
    )
    parser.add_argument(
        "--columns", default=None, nargs="*", help="Which columns in CSV to convert"
    )

    args = vars(parser.parse_args())

    print(csv2latex(**args))
