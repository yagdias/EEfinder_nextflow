include { CREATE_DB} from './modules/create_db.nf'
include { REMOVE_SHORT } from './modules/remove_short.nf'
include { SIMILARITY_ANALYSIS } from './modules/similarity_analysis.nf'
include { FILTER_TABLE } from './modules/filter_table.nf'
include { GET_FASTA } from './modules/get_fasta.nf'

workflow {
    genome_ch = channel.fromPath("${params.genome_loc}/*.fasta")
    search_db_ch = file("${params.search_db}")
    CREATE_DB(search_db_ch)
    REMOVE_SHORT(genome_ch, params.length)
    SIMILARITY_ANALYSIS(REMOVE_SHORT.out.genome_fmt, CREATE_DB.out.fasta, CREATE_DB.out.index, params.mode)
    FILTER_TABLE(SIMILARITY_ANALYSIS.out.blast_result, params.rangejunction, "EE")
    GET_FASTA(REMOVE_SHORT.out.genome_fmt, FILTER_TABLE.out.bed)
}
