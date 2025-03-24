#!/bin/bash -ue
diamond makedb --db virus_subset.fa --in virus_subset.fa --threads 12 --matrix BLOSUM45
