#!/usr/bin/env python

import pandas as pd
import argparse

def merge_taxonomy(blast_file, tax_file) -> None:
    df_blast_file = pd.read_csv(blast_file, sep="\t")
    df_tax_file = pd.read_csv(tax_file)
    df_tax_file.rename(columns={"Accession": "sseqid"}, inplace=True)
    df_merged = pd.merge(df_blast_file, df_tax_file, on="sseqid", how="left")
    df_merged.to_csv(f"{blast_file}.tax", index=False, header=True)


parser = argparse.ArgumentParser(description="Merge the filtred blast results with taxonomy information, creating a taxonomy signature for being used in get_final_taxonomy")
parser.add_argument("--blast_file", type=str, help="tsv filtred blast results")
parser.add_argument("--tax_file", type=str, help="table with taxonomy and other metadata, parsed with -mt parameter")
args = parser.parse_args()
blast_file = args.blast_file
tax_file = args.tax_file

merge_taxonomy(blast_file, tax_file)
