process GET_TAX {
    publishDir "./results/tmp/${genome}", mode: "copy", overwrite: true
    
    input:
    tuple val(genome), path(bed_formated)
    tuple val(tax), path(taxonomy_info)

    output:
    tuple val(genome), path("${bed_formated}.fa.tax")

    script:
    """
    get_tax.py --bed_formated ${bed_formated} --taxonomy_info ${taxonomy_info}
    tag_elements.py --tax_file ${bed_formated}.fa.tax
    get_average_pident.py --tax_file ${bed_formated}.fa.tax
    """
}