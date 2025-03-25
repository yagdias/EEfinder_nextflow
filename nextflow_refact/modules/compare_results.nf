process  COMPARE_RESULTS{
    publishDir "./results/tmp/${genome_ee}", mode: "copy", overwrite: true

    input:
    tuple val(genome_ee), path(ee_result)
    tuple val(genome_host), path(host_result)

    output:
    tuple val(genome_ee), path("${host_result}.concat.nr"), emit: concat

    script:
    """
    compare_results.py --ee_result ${ee_result} --host_result ${host_result}
    """
}