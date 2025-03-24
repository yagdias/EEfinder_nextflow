include { CREATE_DB as CREATE_DB_EE } from './modules/create_db.nf'
include { CREATE_DB as CREATE_DB_HOST } from './modules/create_db.nf'
include { REMOVE_SHORT } from './modules/remove_short.nf'
include { SIMILARITY_ANALYSIS as SIMILARITY_ANALYSIS_EE } from './modules/similarity_analysis.nf'
include { SIMILARITY_ANALYSIS as SIMILARITY_ANALYSIS_HOST } from './modules/similarity_analysis.nf'
include { FILTER_TABLE as FILTER_TABLE_EE } from './modules/filter_table.nf'
include { FILTER_TABLE as FILTER_TABLE_HOST } from './modules/filter_table.nf'
include { GET_FASTA as GET_FASTA1 } from './modules/get_fasta.nf'
include { GET_FASTA as GET_FASTA2 } from './modules/get_fasta.nf'
include { GET_FASTA as GET_FASTA3 } from './modules/get_fasta.nf'
include { COMPARE_RESULTS } from './modules/compare_results.nf'
include { MERGE_TAX } from './modules/merge_tax.nf'
include { GET_ANNOT_BED } from './modules/get_annot_bed.nf'
include { BED_MERGE } from './modules/bed_merge.nf'
include { REMOVE_ANNOT } from './modules/remove_annot.nf'
include { MASK_CLEAN } from './modules/mask_clean.nf'
include { GET_TAX } from './modules/get_tax.nf'
include { GET_FLANK } from './modules/get_flank.nf'
include { PUBLISH } from './modules/publish.nf'


workflow {
    genome_ch = channel.fromPath(params.input_csv)
        .splitCsv(header:true)
        .map { row -> tuple(row.genome, file(row.genome_path))}
    search_db_ch = file("${params.database}")
    host_db_ch = file("${params.hostgenesbaits}")
    dbmetadata = file("${params.dbmetadata}")
    
    
    CREATE_DB_HOST(host_db_ch)
    CREATE_DB_EE(search_db_ch)
    REMOVE_SHORT(genome_ch, params.length)
    SIMILARITY_ANALYSIS_EE(REMOVE_SHORT.out.genome_fmt, CREATE_DB_EE.out, params.mode)
    FILTER_TABLE_EE(SIMILARITY_ANALYSIS_EE.out.blast_result, params.rangejunction, "EE")
    GET_FASTA1(REMOVE_SHORT.out.genome_fmt, FILTER_TABLE_EE.out.bed)
    SIMILARITY_ANALYSIS_HOST(GET_FASTA1.out.fasta, CREATE_DB_HOST.out, params.mode)
    FILTER_TABLE_HOST(SIMILARITY_ANALYSIS_HOST.out.blast_result, params.rangejunction, "HOST")
    COMPARE_RESULTS(FILTER_TABLE_EE.out.blast_result_filtred, FILTER_TABLE_HOST.out.blast_result_filtred)
    MERGE_TAX(COMPARE_RESULTS.out.concat, dbmetadata)
    GET_ANNOT_BED(MERGE_TAX.out, params.merge_level)
    BED_MERGE(GET_ANNOT_BED.out, params.limit)
    REMOVE_ANNOT(BED_MERGE.out)
    GET_FASTA2(REMOVE_SHORT.out.genome_fmt, REMOVE_ANNOT.out)
    if (params.clean_masked == true)
        MASK_CLEAN(GET_FASTA2.out.fasta, params.mask_per)
    GET_TAX(REMOVE_ANNOT.out, MERGE_TAX.out)
    GET_FLANK(REMOVE_SHORT.out.genome_fmt, GET_FASTA2.out.fasta, params.flank)
    GET_FASTA3(REMOVE_SHORT.out.genome_fmt, GET_FLANK.out)
    PUBLISH(GET_FASTA2.out.fasta, GET_TAX.out, GET_FLANK.out)

}
