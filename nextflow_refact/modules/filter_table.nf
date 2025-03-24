process FILTER_TABLE {
    publishDir "./results/tmp/${genome}", mode: "copy", overwrite: true

    input:
    tuple val(genome), path(blast_result)
    val rangejunction
    val tag

    output:
    tuple val(genome), path("${blast_result}.filtred.{EE,HOST}"), emit: blast_result_filtred
    tuple val(genome), path("${blast_result}.filtred.bed"), optional: true, emit: bed

    script:
    """
    filter_table.py --blast_result ${blast_result} --rangejunction ${rangejunction} --tag ${tag} 
    """
}