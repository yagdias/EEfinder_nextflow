process GET_FLANK {
    
    input:
    tuple val(genome), path(genome_file)
    tuple val(fasta), path(fasta_file)
    val flank
    
    output:
    tuple val(flank), path("${genome_file}.flank")

    script:
    """
    get_length.py --input_file ${genome_file}
    get_bed.py --input_file ${fasta_file}
    bedtools slop -i ${fasta_file}.bed -g ${genome_file}.rn.fmt.lenght -b ${flank} > ${genome_file}.flank
    """
}