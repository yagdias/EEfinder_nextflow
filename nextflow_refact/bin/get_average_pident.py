#!/usr/bin/env python

import pandas as pd
import numpy as np
import argparse

def get_average_pident(tax_file):
    df = pd.read_csv(tax_file, sep="\t")
    def calculate_average(pidents):
        entries = pidents.split(" | ")
        pidents_values = [float(entry.split("|")[1]) for entry in entries if "|" in entry]
        return round(np.mean(pidents_values), 1) if pidents else np.nan
    df['Average_pident'] = df['Protein-IDs'].apply(calculate_average)
    df.to_csv(tax_file, sep="\t", index=False, header=True)


parser = argparse.ArgumentParser()
parser.add_argument("--tax_file", type=str, help="tax input file")
args = parser.parse_args()

tax_file = args.tax_file

get_average_pident(tax_file)