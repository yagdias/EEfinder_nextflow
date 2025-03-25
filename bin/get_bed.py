#!/usr/bin/env python

import re
import argparse


def get_bed(input_file):
    with open(f"{input_file}", "r") as repeat_eves, open(
        f"{input_file}.bed", "w"
    ) as repeat_eves_bed_out:
        repeat_eves_lines = repeat_eves.readlines()
        for line in repeat_eves_lines:
            if ">" in line:
                line_name = line.replace(">", "")
                line_name = re.sub(":.*", "", line_name).rstrip("\n")
                line_start = re.sub(".*:", "", line)
                line_start = re.sub("-.*", "", line_start).rstrip("\n")
                line_end = re.sub(".*-", "", line).rstrip("\n")
                repeat_eves_bed_out.write(
                    f"{line_name}\t{line_start}\t{line_end}\n"
                )

parser = argparse.ArgumentParser(description="Create a bed file from fasta file using replace logic.")
parser.add_argument("--input_file", type=str, help="fasta file for desired bed file")
args = parser.parse_args()
input_file = args.input_file

get_bed(input_file)
