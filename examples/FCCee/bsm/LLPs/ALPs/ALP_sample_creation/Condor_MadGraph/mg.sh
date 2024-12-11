#!/bin/bash
job_number=$1
mass=$2
coupling=$3
nevents=$4

mass_filename=$(echo ${mass} | sed "s/\./p/g")
coupling_filename=$(echo ${coupling} | sed "s/\./p/g")
baseoutputdir="ALP_Z_aa_${mass_filename}GeV_cYY${coupling_filename}"

# Define the EOS base directory
eos_base_dir="/eos/user/e/ebakhish/MG/MGOutput"


output_dir="${eos_base_dir}/${baseoutputdir}_${job_number}"
temp_card="/eos/user/e/ebakhish/MG/Processcards/${baseoutputdir}_${job_number}.dat"


input_file="/afs/cern.ch/user/e/ebakhish/FCCAnalyses/examples/FCCee/bsm/LLPs/ALPs/ALP_sample_creation/Condor_MadGraph/mg_cards_collection/mg5_proc_card_ALP_Z_aa_template.dat"

#random seed number for MG
seed=$(($RANDOM % 900000000 + 1))

# Create temporary process card with unique output path
#this line searches for certain variables in the input file and replaces them with our defined properties
sed "s|ALPMASS|${mass}|g;s|ALPCOUPLING|${coupling}|g;s|OUTPUTDIR|${output_dir}|g;s|NUMBEROFEVENTS|${nevents}|g;s|SEEDNUMBER|${seed}|g" $input_file > $temp_card

# Run MadGraph with temporary card
#./bin/mg5_aMC $temp_card
/afs/cern.ch/user/e/ebakhish/MG5_aMC_v3_5_6/bin/mg5_aMC $temp_card

# Clean up temporary card
# rm $temp_card