process REMOVE_ANNOT {
    input:
    tuple val(genome), path(bed_annotated_merged_file)

    output:
    tuple val(genome), path("${bed_annotated_merged_file}.fmt")

    script:
    """
    remove_annot.py --bed_annotated_merged_file ${bed_annotated_merged_file}
    """
}