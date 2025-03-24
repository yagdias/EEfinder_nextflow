process  GET_FASTA{
    publishDir "./results/tmp/", mode: "copy", overwrite: true

    input:
    path input_file
    path bed_file

    output:
    path "${input_file}.fasta", emit: fasta

    script:
    """
    bedtools getfasta -fi ${input_file} -bed ${bed_file} -fo ${input_file}.fasta
    """
}


