#!/bin/bash
#SBATCH -A C3SE408-25-2
#SBATCH -J kraken2_job
#SBATCH -p vera
#SBATCH -N 1 --cpus-per-task=12 # Request 1 node with 12 CPUs
#SBATCH -t 01:00:00
#SBATCH --output=/cephyr/users/hilmaha/Vera/BIO511/WGS_project/logs/kraken2_%j.out  # Standard output
#SBATCH --error=/cephyr/users/hilmaha/Vera/BIO511/WGS_project/logs/kraken2_%j.err   # Standard error

# Set paths - ADJUST THESE TO YOUR ACTUAL PATHS
CONTAINER_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/singularity_images/kraken2.sif"
DB_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/ref_dbs/kraken2db"
DATA_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/students/Hilma/project/data"
RESULTS_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/students/Hilma/project/results/kraken2_q20"

# Bind paths for container
export SINGULARITY_BINDPATH="${DB_PATH}:/db,${DATA_PATH}:/data,${RESULTS_PATH}:/results"

# Create results directory
mkdir -p ${RESULTS_PATH}

# Identify sample
sample="CCUG-55970"
echo "Processing sample: ${sample}"

# Run Kraken2 classification
srun singularity exec ${CONTAINER_PATH} kraken2 \
        --db /db \
        --threads 8 \
        --output /results/${sample}_kraken2_q20_output.txt \
        --report /results/${sample}_kraken2_q20_report.txt \
        --classified-out /results/${sample}_classified_q20.fastq \
        --unclassified-out /results/${sample}_unclassified_q20.fastq \
        /data/${sample}_q20.fastq.gz

echo "Completed classification for ${sample}"

echo "All samples processed successfully"