#!/usr/bin/env python

from Bio import SeqIO
import argparse

def mask_clean(input_file, m_per) -> None:
    sequences = {}
    for seq_record in SeqIO.parse(input_file, "fasta"):
        sequence = str(seq_record.seq)
        sequence_id = str(seq_record.id)
        if (
            float(
                sequence.count("a")
                + sequence.count("t")
                + sequence.count("c")
                + sequence.count("g")
                + sequence.count("n")
                + sequence.count("N")
            )
            / float(len(sequence))
        ) * 100 <= float(m_per):
            if sequence_id not in sequences:
                sequences[sequence_id] = sequence
    with open(input_file + ".cl", "w+") as output_file:
        for sequence_id, sequence in sequences.items():
            output_file.write(f">{sequence_id}\n{sequence}\n")


parser = argparse.ArgumentParser(description="Remove sequences of EE on regions with a certain % of soft masked bases.")
parser.add_argument("--input_file", type=str, help="Create a bed file that will be used to merge truncated EVEs of the same")
parser.add_argument("--m_per", type=int, help="genus or family, choose which level going to merge nearby elements")
args = parser.parse_args()

input_file = args.input_file
m_per = args.m_per

mask_clean(input_file, m_per)