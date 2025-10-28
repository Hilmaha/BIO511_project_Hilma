#!/bin/bash
#SBATCH -A C3SE408-25-2
#SBATCH -J flye_basic
#SBATCH -p vera
#SBATCH -N 1 --cpus-per-task=16
#SBATCH -t 01:30:00
#SBATCH --output=/cephyr/users/hilmaha/Vera/BIO511/WGS_project/logs/flye_basic_%j.out
#SBATCH --error=/cephyr/users/hilmaha/Vera/BIO511/WGS_project/logs/flye_basic_%j.err

# Set paths - ADJUST THESE TO YOUR ACTUAL PATHS
DATA_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/students/Hilma/project/data"
RESULTS_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/students/Hilma/project/results"
SINGULARITY_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/singularity_images/flye.sif"

# Set bind paths for Singularity
export SINGULARITY_BINDPATH="${DATA_PATH}:/data,${RESULTS_PATH}:/results"

# Set sample and output paths
ONT_READS="${DATA_PATH}/CCUG-55970_q20.fastq.gz"
OUTPUT_DIR="${RESULTS_PATH}/assembly_q20/flye_basic_q20"

# Create output directories
mkdir -p ${OUTPUT_DIR}

# Run Flye assembly with basic settings
singularity exec ${SINGULARITY_PATH} flye --nano-raw /data/CCUG-55970_q20.fastq.gz \
     --out-dir /results/assembly_q20/flye_basic_q20 \
     --threads 16 \
     --iterations 0

echo "Basic ONT assembly completed"