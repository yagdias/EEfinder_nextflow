process FILTER_TABLE {
    publishDir "./results/tmp/", mode: "copy", overwrite: true

    input:
    path blast_result
    val rangejunction
    val tag

    output:
    path "${blast_result}.filtred", emit: blast_result_filtred
    path "${blast_result}.filtred.bed", emit: bed

    script:
    """
    filter_table.py --blast_result ${blast_result} --rangejunction ${rangejunction} --tag ${tag} 
    """
}