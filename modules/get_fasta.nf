process  GET_FASTA{
    publishDir "./results/tmp/${genome}", mode: "copy", overwrite: true

    input:
    tuple val(genome), path(input_file)
    tuple val(bed), path(bed_file)

    output:
    tuple val(genome), path("${input_file}.fasta"), emit: fasta

    script:
    """
    bedtools getfasta -fi ${input_file} -bed ${bed_file} -fo ${input_file}.fasta
    """
}


