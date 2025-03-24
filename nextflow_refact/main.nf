genome_ch = channel.fromPath("${params.genome_loc}/*.fasta")
search_db_ch = channel.fromPath("${params.search_db}")


process REMOVE_SHORT {
    input:
    path genome
    val cutoff

    output:
    path "${genome}.fmt"
    
    script:
    """
    remove_short.py --input_file ${genome} --cutoff ${cutoff}
    """
}

process CREATE_DB_DIAMOND{
    input:
    path db

    output:
    path db
    path "${db}.dmnd"
    
    script:
    """
    diamond makedb --db ${db} --in ${db} --threads ${task.cpus} --matrix BLOSUM45
    """
}

process SIMILARITY_ANALYSIS{
    input:
    path genome
    path db
    val mode


    output:
    path "${genome}"


    script:
    """
    diamond blastx -p ${task.cpus} -d ${db} -f 6 -q ${genome} -o ${genome}.blastx -e 0.00001 --matrix BLOSUM45 -k 500 --max-hsps 0 --${mode}
    """
}


workflow{
    db = CREATE_DB_DIAMOND(search_db_ch)
    db.view()
    genome_filtred_ch = REMOVE_SHORT(genome_ch, params.length)
    similarity_anlysis_ch = SIMILARITY_ANALYSIS(genome_filtred_ch, db, params.mode)

}