#!/usr/bin/env python

import pandas as pd
import argparse

def compare_results(ee_result, host_result) -> None:
    df_vir = pd.read_csv(ee_result, sep="\t")
    df_vir["qseqid"] = df_vir["bed_name"]
    df_host = pd.read_csv(host_result, sep="\t")
    df_hybrid = pd.concat([df_vir, df_host], ignore_index=True)
    df_hybrid = df_hybrid.sort_values(by=["qseqid", "bitscore"], ascending=False)
    df_hybrid.to_csv(host_result + ".concat", sep="\t", index=False)
    df_nr = df_hybrid.drop_duplicates(subset=["qseqid"])
    df_nr.to_csv(host_result + ".concat.nr", sep="\t", index=False)
    df_nr_vir = df_nr[df_nr.tag == "EE"]
    df_nr_vir.to_csv(host_result + ".concat.nr", sep="\t", index=False)


parser = argparse.ArgumentParser(description="This function compares 2 blast results, for queries with same ID, only the one with the major bitscore is keept. In a final step only queries with tag EE are maintained")
parser.add_argument("--ee_result", type=str, help="filtred blast against ee database")
parser.add_argument("--host_result", type=str, help="filtred blast against filter database")
args = parser.parse_args()
ee_result = args.ee_result
host_result = args.host_result

compare_results(ee_result, host_result)