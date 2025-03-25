#!/usr/bin/env python

import pandas as pd
import argparse

def _list_to_string(overlaped_elements: list) -> str:
    return ",".join(map(str, overlaped_elements))

def tag_elements(tax_file):
    df = pd.read_csv(tax_file, sep="\t")
    df["Element-ID"] = df["Element-ID"].replace(".*/", "", regex=True)
    df["start"] = df["Element-ID"].replace("-.*", "", regex=True)
    df["start"] = df["start"].replace(".*:", "", regex=True)
    df["end"] = df["Element-ID"].replace(".*-", "", regex=True)
    df["contig"] = df["Element-ID"].replace(":.*", "", regex=True)
    df["start"] = df["start"].astype(int)
    df["end"] = df["end"].astype(int)

    matched_elements = []
    for i, row in df.iterrows():
        matched_ids = []
        filtered_df = df[df["contig"] == row["contig"]]
        for j, other_row in filtered_df.iterrows():
            if (
                i != j
                and other_row["start"] <= row["end"] + 100
                and other_row["end"] >= row["start"] - 100
                and other_row["Family"] != row["Family"]
            ):
                matched_ids.append(other_row["Element-ID"])
        matched_elements.append(matched_ids)
    df["Overlaped_Element_ID"] = matched_elements

    df["Overlaped_Element_ID"] = df["Overlaped_Element_ID"].apply(_list_to_string)
    df.drop(columns=["start", "end", "contig"], inplace=True)

    for i, row in df.iterrows():
        if row["Overlaped_Element_ID"] == "":
            df.at[i, "tag"] = "unique"
        else:
            row["Overlaped_Element_ID"] != ""
            df.at[i, "tag"] = "overlaped"

    df.to_csv(tax_file, sep="\t", index=False, header=True)

parser = argparse.ArgumentParser(description="Create a collumn in the tax file with a tag sinalizing if the element is overlaped or unique")
parser.add_argument("--tax_file", type=str, help="tax input file")
args = parser.parse_args()

tax_file = args.tax_file

tag_elements(tax_file)

