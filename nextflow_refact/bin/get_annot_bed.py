#!/usr/bin/env python

import pandas as pd
import numpy as np
import argparse

def get_annotated_bed(blast_tax_info, merge_level):
    df_blast_tax_info = pd.read_csv(blast_tax_info, sep=",")
    df_blast_tax_info["qseqid"] = df_blast_tax_info["qseqid"].str.replace(
        r"\:.*", "", regex=True
    )
    df_blast_tax_info["sseqid"] = (
        df_blast_tax_info["sseqid"]
        + "|"
        + df_blast_tax_info["sense"]
        + "|"
        + df_blast_tax_info["pident"].astype(str)
    )
    df_blast_tax_info["Family"] = df_blast_tax_info["Family"].fillna("Unknown")
    df_blast_tax_info["Genus"] = df_blast_tax_info["Genus"].fillna("Unknown")

    if merge_level == "genus":
        df_blast_tax_info["formated_name"] = np.where(
            df_blast_tax_info["Genus"] != "Unknown",
            df_blast_tax_info["qseqid"]
            + "|"
            + df_blast_tax_info["Family"]
            + "|"
            + df_blast_tax_info["Genus"]
            + "|"
            + df_blast_tax_info["sense"],
            df_blast_tax_info["qseqid"]
            + "|"
            + df_blast_tax_info["sseqid"]
            + "|"
            + df_blast_tax_info["Genus"],
        )
    else:
        df_blast_tax_info["formated_name"] = np.where(
            df_blast_tax_info["Family"] != "Unknown",
            df_blast_tax_info["qseqid"]
            + "|"
            + df_blast_tax_info["Family"]
            + "|"
            + df_blast_tax_info["sense"],
            df_blast_tax_info["qseqid"]
            + "|"
            + df_blast_tax_info["sseqid"]
            + "|"
            + df_blast_tax_info["Family"],
        )
    bed_blast_info = df_blast_tax_info[
        ["formated_name", "qstart", "qend", "sseqid"]
    ].copy()
    bed_blast_info = bed_blast_info.sort_values(
        ["formated_name", "qstart"], ascending=(True, True)
    )
    bed_blast_info.to_csv(
        f"{blast_tax_info}.bed", index=False, header=False, sep="\t"
    )


parser = argparse.ArgumentParser(description="Create a bed file that will be used to merge truncated EVEs of the same family in the same sense based on a limite length treshold.")
parser.add_argument("--blast_tax_info", type=str, help="Create a bed file that will be used to merge truncated EVEs of the same")
parser.add_argument("--merge_level", type=str, help="genus or family, choose which level going to merge nearby elements")
args = parser.parse_args()

blast_tax_info = args.blast_tax_info
merge_level = args.merge_level

get_annotated_bed(blast_tax_info, merge_level)