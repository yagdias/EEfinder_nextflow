process SIMILARITY_ANALYSIS {
    publishDir "./results/tmp/${genome}", mode: "copy", overwrite: true
    
    input:
    tuple val(genome), path(genomepath)
    tuple path(db), path(index)
    val mode

    output:
    tuple val(genome), path("${genomepath}.blastx"), emit:blast_result

    script:
    if (params.mode == 'blastx') {
        """
        blastx -db ${db} -query ${genomepath} -out ${genomepath}.blastx -outfmt 6 -word_size 3 -num_threads ${task.cpus} -matrix BLOSUM45 -max_intron_length 100 -soft_masking true -evalue 0.00001
        """
    }
    else {
        """
        diamond blastx -p ${task.cpus} -d ${db} -f 6 -q ${genomepath} -o ${genomepath}.blastx -e 0.00001 --matrix BLOSUM45 -k 500 --max-hsps 0 --${mode}
        """
    }
}