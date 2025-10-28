#!/bin/bash
#SBATCH -A C3SE408-25-2 
#SBATCH -J prokka_baseline
#SBATCH -p vera
#SBATCH -N 1 --cpus-per-task=8
#SBATCH -t 01:00:00
#SBATCH --output=/cephyr/users/hilmaha/Vera/BIO511/WGS_project/logs/prokka_baseline_%j.out # output log, adjust path to where you want to save logs
#SBATCH --error=/cephyr/users/hilmaha/Vera/BIO511/WGS_project/logs/prokka_baseline_%j.err # error log, adjust path to where you want to save logs

# Set paths - ADJUST THESE TO YOUR ACTUAL PATHS
CONTAINER_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/singularity_images/prokka.sif"
RESULTS_PATH="/cephyr/NOBACKUP/groups/n2bin_gu/students/Hilma/project/results"
ASSEMBLIES_DIR="/cephyr/NOBACKUP/groups/n2bin_gu/students/Hilma/project/results/assembly_q20/flye_basic_q20"
OUTPUT_DIR="${RESULTS_PATH}/annotation_q20/prokka_baseline_q20_basic"

# Bind paths for container
export SINGULARITY_BINDPATH="${ASSEMBLIES_DIR}:/assemblies,${RESULTS_PATH}:/results"

# Create output directories
# If needed: mkdir -p ${RESULTS_PATH}
mkdir -p ${OUTPUT_DIR}

# Input assembly
ASSEMBLY="/assemblies/assembly.fasta" 

# Set a prefix variable for naming outputs
PREFIX="$(basename ${ASSEMBLY} .fasta)_baseline_q20_basic"

# Run Prokka (baseline)
singularity exec ${CONTAINER_PATH} prokka \
  --cpus 8 \
  --outdir /results/annotation_q20/prokka_baseline_q20_basic \
  --prefix ${PREFIX} \
  --locustag BIO511 \
  --genus Escherichia \
  --species coli \
  --force \
  ${ASSEMBLY}

echo "Baseline Prokka annotation completed"