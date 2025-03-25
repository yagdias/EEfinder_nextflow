process PUBLISH {
    publishDir "./results/$ee", mode: "copy", overwrite:true

    input:
    tuple val(ee), path(fasta_ee)
    tuple val(tax), path(tax_csv)
    tuple val(flank), path(fasta_flank)

    output:
    path "${ee}.EEs.fa"
    path "${ee}.EEs.tax.tsv" 
    path "${ee}.EEs.flanks.fa"

    script:
    """
    mv ${fasta_ee} ${ee}.EEs.fa 
    mv ${tax_csv} ${ee}.EEs.tax.tsv
    mv ${fasta_flank} ${ee}.EEs.flanks.fa
    """
}