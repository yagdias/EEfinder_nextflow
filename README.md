# EEfinder_nextflow

EEfinder_nextflow is a refactored pipeline based on the [EEfinder tool](https://github.com/WallauBioinfo/EEfinder). It automates various tasks related to the identification of Endogenous Elements in Eukaryotic genomes.

#### Install

EEfinder was developed and tested with BLAST 2.5.0 and DIAMOND 2.0.15, they are implemented on conda environments

```bash
git clone https://github.com/WallauBioinfo/EEfinder.git
cd EEfinder
conda env create -f env.yml
```
#### Test line

```bash
conda activate EEfinder
nextflow run main.nf
```

#### Parameters

Change parameters on `nextflow.config`

- input_csv - CSV file with genome name followed path to .fasta file 
- database - Protein database with viral or bacterial proteins
- hostgenesbaits - House keeping host proteins database
- dbmetadata - Taxonomic info in a CSV file, instructions for creating this file on [link](https://github.com/WallauBioinfo/EEfinder/wiki/Viral-Datasets)
- mode - Choose between BLAST (blastx) or the DIAMOND strategies (fast, mid-sensitive, sensitive, more-sensitive, very-sensitive, ultra-sensisitve), default=blastx
- rangejunction - Sets the range for junction of BLAST/DIAMOND redudant hits, default=100
- length - Minimum length of contigs used for BLAST or DIAMOND, default = 10000
- merge_level - Taxonomy level to merge elements by genus or family, default = genus
- limit - Limit of bases used to merge regions on bedtools merge, default = 1
- clean_masked - Remove EEs in regions considered repetitive? default = false
- mask_per Limit of lowercase letters in percentage to consider a putative Endogenous Elements as a repetitive region, default = 50
- flank - Length of flanking regions of Endogenous Elements to be extracted, default = 10000
    
#### Cite us

If you use EEfinder in your research, please cite https://www.sciencedirect.com/science/article/pii/S2001037024003325:

```
Dias, Y. J. M., Dezordi, F. Z., & Wallau, G. L. (2024). EEFinder: A general-purpose tool for identification of bacterial and viral endogenized elements in eukaryotic genomes. Computational and Structural Biotechnology Journal. https://doi.org/10.1016/j.csbj.2024.10.012
```
