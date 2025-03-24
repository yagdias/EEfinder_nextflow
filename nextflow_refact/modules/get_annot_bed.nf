process GET_ANNOT_BED {
    publishDir "./results/tmp/${genome}", mode: "copy", overwrite: true

    input:
    tuple val(genome), path(blast_tax)
    val merge_level

    output:
    tuple val(genome), path("${blast_tax}.bed")

    script:
    """
    get_annot_bed.py --blast_tax_info ${blast_tax} --merge_level ${merge_level}
    """
}
