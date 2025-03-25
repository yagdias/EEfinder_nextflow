process MASK_CLEAN {
    input:
    tuple val(genome), path(input_file)
    val m_per

    output:
    tuple val(genome), path("${input_file}.cl")

    script:
    """
    mask_clean.py --input_file ${input_file} --m_per ${m_per}
    """
}