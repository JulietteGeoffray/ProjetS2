
nbRun = 1
readID = 'mf76'
PATH = '/home/amren/Master1/ProjetS2/ProjetS2/script/docker/'
READS = []
READS.append(PATH + 'data/reads/mf76_1_sub.fastq.gz')
READS.append(PATH + 'data/reads/mf76_2_sub.fastq.gz')
REFERENCE = PATH + 'data/Reference_genomes/Otipulae/nOt.2.0/nOt.2.0.fna'

RAM = "8"
RGPL = "ILLUMINA"
RGSM = "mf76"
RGLB = "mf76_LB1"
RGID = "FCH3LFLBBXX_mf76"
RGPU = "FCH3LFLBBXX_L5_mf76"
dbSNP= PATH + "data/dbSNP_JU170_v2.0.vcf"
SCAFF_SIZE= PATH + "data/nOt.2.0_Scaff-size.tsv"
INVARIANT_SCAFF= PATH + "data/JU170_InvariantScaffold.interval_list"
BACKGROUND_GVCF = PATH + "data/CEW1.gVCF.vcf"
MAPPING_GVCF = PATH + "data/JU170.gVCF.vcf"
snpEff_database = "O.tipulae.2.0"
snpEff_contig= PATH + "data/snpEff-Databases/snpEff_andalousian.config"
Warning_Scaff= PATH + "data/JU170_FalsePositiveScaffold.list"
Mapping_strain = "JU170"
Background_strain = "CEW1"

# Software Path
picard = PATH + "software/picard.jar"
GATK = PATH + "software/GenomeAnalysisTK.jar"
snpEff = PATH + "software/snpEff/snpEff.jar"
snpEff_pl = PATH + "software/snpEff/scripts/vcfEffOnePerLine.pl"
snpEff_SnpSift = PATH + "software/snpEff/SnpSift.jar"
