#!/bin/bash -ue
diamond makedb --db ../test_files/virus_subset.fa --in ../test_files/virus_subset.fa --threads 12 --matrix BLOSUM45
