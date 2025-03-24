process MERGE_TAX {
    publishDir "./results/tmp/${genome}/", mode: "copy", overwrite: true

    input:
    tuple val(genome), path(concat)
    path dbmetadata

    output:
    tuple val(genome), path("${concat}.tax")

    script:
    """
    merge_tax.py --blast_file ${concat} --tax_file ${dbmetadata}
    """
}