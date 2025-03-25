process BED_MERGE {
    publishDir "./results/tmp/${genome}/", mode: "copy", overwrite:true

    input:
    tuple val(genome), path(bed_annotated_file)
    val limit_merge

    output:
    tuple val(genome), path("${bed_annotated_file}.merge")

    script:
    """
    bedtools merge -d ${limit_merge} -i ${bed_annotated_file} -c 4 -o collapse -delim " AND " > ${bed_annotated_file}.merge
    """
}