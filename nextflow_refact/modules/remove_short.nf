process REMOVE_SHORT {
    publishDir "./results/tmp/", mode: "copy", overwrite: true

    input:
    path genome
    val cutoff

    output:
    path "${genome}.fmt", emit: genome_fmt

    script:
    """
    remove_short.py --input_file ${genome} --cutoff ${cutoff}
    """
}