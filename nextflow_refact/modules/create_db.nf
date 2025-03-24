process CREATE_DB {
    
    publishDir "./results/tmp/${db}", mode: "copy", overwrite: true
    
    input:
    file db

    output:
    path db, emit: fasta
    path "${db}.*", optional: true, emit: index

    script:
    if (params.mode == 'blastx') {
        """
        makeblastdb -in ${db} -dbtype prot
        """
    }
    else {
        """
        diamond makedb --db ${db} --in ${db} --threads ${task.cpus} --matrix BLOSUM45
        """
    }
}