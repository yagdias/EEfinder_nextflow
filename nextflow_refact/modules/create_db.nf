process CREATE_DB {
    publishDir "./results/tmp/${db}", mode: "copy", overwrite: true
    tag "$db"
    
    input:
    file db

    output:
    tuple path(db), path("${db}.*")

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