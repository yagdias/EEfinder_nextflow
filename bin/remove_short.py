#!/usr/bin/env python

from Bio import SeqIO
import argparse

def cut_seq(input_file, cutoff):
    new_sequences = []
    input_handle = open(input_file, "r")
    output_handle = open(input_file + ".fmt", "w")
    for record in SeqIO.parse(input_handle, "fasta"):
        if len(record.seq) >= int(cutoff):
                new_sequences.append(record)
    SeqIO.write(new_sequences, output_handle, "fasta")

parser = argparse.ArgumentParser(description="Remove sequences bellow the cutoff threshold")
parser.add_argument("--input_file", type=str, help="input fasta file")
parser.add_argument("--cutoff", type=int, help="cutoff length, parsed by -ln")
args = parser.parse_args()
input_file = args.input_file
cutoff = args.cutoff

cut_seq(input_file, cutoff)


