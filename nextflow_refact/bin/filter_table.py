#!/usr/bin/env python

import pandas as pd
import glob
import argparse

def filter_blast(blast_result, rangejunction, tag):
        header_outfmt6 = [
            "qseqid",
            "sseqid",
            "pident",
            "length",
            "mismatch",
            "gapopen",
            "qstart",
            "qend",
            "sstart",
            "send",
            "evalue",
            "bitscore",
        ]  # creates a blast header output in format = 6
        df = pd.read_csv(
            blast_result, sep="\t", header=None, names=header_outfmt6
        ).sort_values(by="bitscore", ascending=False)
        df["sense"] = ""
        df["bed_name"] = ""
        df["tag"] = ""
        df["new_qstart"] = df["qstart"]
        df["new_qend"] = df["qend"]
        df.to_csv(blast_result + ".csv", sep="\t")
        chunks = df = pd.read_csv(
            f"{blast_result}.csv", sep="\t", chunksize=200000
        )
        count = 0
        for df in chunks:
            df["sense"] = df["sense"].astype(object)
            df.loc[
                df["qstart"].astype(int) > df["qend"].values.astype(int), "sense"
            ] = "neg"
            df.loc[
                df["qend"].values.astype(int) > df["qstart"].astype(int), "sense"
            ] = "pos"
            df.loc[df["sense"] == "neg", "new_qstart"] = df["qend"]
            df.loc[df["sense"] == "neg", "new_qend"] = df["qstart"]
            df.loc[df["sense"] == "neg", "qstart"] = df["new_qstart"]
            df.loc[df["sense"] == "neg", "qend"] = df["new_qend"]
            df.drop(columns=["new_qstart", "new_qend"], inplace=True)
            if tag == "EE":
                df["tag"] = "EE"
                df["bed_name"] = df.apply(
                    lambda x: "%s:%s-%s" % (x["qseqid"], x["qstart"], x["qend"]), axis=1
                )
            else:
                df["tag"] = "HOST"
                df["bed_name"] = df["qseqid"]
            pd.options.display.float_format = "{:,.2f}".format
            df["evalue"] = pd.to_numeric(df["evalue"], downcast="float")
            df = df[df.length >= 33]
            header = [
                "qseqid",
                "sseqid",
                "pident",
                "length",
                "mismatch",
                "gapopen",
                "qstart",
                "qend",
                "sstart",
                "send",
                "evalue",
                "bitscore",
                "sense",
                "bed_name",
                "tag",
            ]
            df = df[header]
            with open(f"chunk.{count}.tsv", "w") as chunk_writer:
                df.to_csv(chunk_writer, sep="\t", index=False)
            count += 1
        all_chunks = glob.glob(f"*.tsv")
        final_filtred_file = pd.DataFrame()
        chunks_list = []
        for chunk in all_chunks:
            df = pd.read_csv(chunk, sep="\t")
            chunks_list.append(df)
        final_filtred_file = pd.concat(chunks_list, ignore_index=True)
        final_filtred_file["qstart_rng"] = final_filtred_file.qstart.floordiv(
            rangejunction
        )
        final_filtred_file["qend_rng"] = final_filtred_file.qend.floordiv(
            rangejunction
        )
        final_filtred_file = (
            final_filtred_file.drop_duplicates(subset=["qseqid", "qstart_rng", "sense"])
            .drop_duplicates(subset=["qseqid", "qstart_rng", "sense"])
            .sort_values(by=["qseqid"])
        )
        final_filtred_file.to_csv(
            f"{blast_result}.filtred.{tag}", sep="\t", index=False, columns=header
        )
        if tag == "EE":
            final_filtred_file.to_csv(
                f"{blast_result}.filtred.bed",
                header=False,
                sep="\t",
                index=False,
                columns=["qseqid", "qstart", "qend"],
            )



parser = argparse.ArgumentParser(description="Receives a blastx result and filter based on query ID and ranges of qstart and qend.")
parser.add_argument("--blast_result", type=str, help="input blastx result")
parser.add_argument("--rangejunction", type=int, help="range for filter redundant hits")
parser.add_argument("--tag", type=str, help="HOST or EE, tells which blastx is")
args = parser.parse_args()

blast_result = args.blast_result
rangejunction = args.rangejunction
tag = args.tag

filter_blast(blast_result, rangejunction, tag)