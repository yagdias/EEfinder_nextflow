#!/bin/bash -ue
diamond blastx -p 12 -d virus_subset.fa.dmnd.dmnd -f 6 -q Ae_aeg_Aag2_ctg_1913.fasta.fmt -o Ae_aeg_Aag2_ctg_1913.fasta.fmt.blastx -e 0.00001 --matrix BLOSUM45 -k 500 --max-hsps 0 --fast
