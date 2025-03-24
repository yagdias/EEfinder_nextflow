process REMOVE_SHORT {
    publishDir "./results/tmp/${genome}", mode: "copy", overwrite: true

    input:
    tuple val(genome), path(genomepath)
    val cutoff

    output:
    tuple val(genome), path("${genomepath}.fmt"), emit: genome_fmt

    script:
    """
    remove_short.py --input_file ${genomepath} --cutoff ${cutoff}
    """
}