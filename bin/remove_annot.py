#!/usr/bin/env python

import pandas as pd
import argparse

"""
Remove the annotated information generate into the get_annotated_bed function.

Keyword arguments:
bed_annotated_merged_file: tsv file generated in the merge_bedfile function on bed_merge.py
"""

def reformat_bed(bed_annotated_merged_file):
    df_merge_file = pd.read_csv(
        bed_annotated_merged_file, sep="\t", header=None
    )
    df_merge_file.iloc[:, 0] = df_merge_file.iloc[:, 0].str.replace(
        "\|.*", "", regex=True
    )
    df_merge_file.to_csv(
        f"{bed_annotated_merged_file}.fmt", index=False, header=False, sep="\t"
    )


parser = argparse.ArgumentParser(description="Remove the annotated information generate into the get_annotated_bed function.")
parser.add_argument("--bed_annotated_merged_file", type=str, help="tsv file generated in the merge_bedfile function on bed_merge.py")
args = parser.parse_args()
bed_annotated_merged_file = args.bed_annotated_merged_file

reformat_bed(bed_annotated_merged_file)