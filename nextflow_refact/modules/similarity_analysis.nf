process SIMILARITY_ANALYSIS {
    publishDir "./results/tmp/", mode: "copy", overwrite: true
    input:
    path genome
    path db
    path index
    val mode

    output:
    path "${genome}.blastx", emit:blast_result

    script:
    if (params.mode == 'blastx') {
        """
        blastx -db ${db} -query ${genome} -out ${genome}.blastx -outfmt 6 -word_size 3 -num_threads ${task.cpus} -matrix BLOSUM45 -max_intron_length 100 -soft_masking true -evalue 0.00001
        """
    }
    else {
        """
        diamond blastx -p ${task.cpus} -d ${db} -f 6 -q ${genome} -o ${genome}.blastx -e 0.00001 --matrix BLOSUM45 -k 500 --max-hsps 0 --${mode}
        """
    }
}