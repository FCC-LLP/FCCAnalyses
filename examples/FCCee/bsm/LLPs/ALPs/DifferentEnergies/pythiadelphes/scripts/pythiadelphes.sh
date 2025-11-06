#!/bin/bash

source /cvmfs/fcc.cern.ch/sw/latest/setup.sh

if [ $# -eq 4 ]; then
    # Signal: CME MASS NEVENTS JOB
    is_signal=true
    CME="$1"
    ALPMASS="$2"
    NEVENTS="$3"
    JOBNUMBER="$4"

    cme_label=$(echo "$CME" | sed 's/\./p/g')
    mass_label=$(echo "$ALPMASS" | sed 's/\./p/g')
    base_output_dir="alp_3photons_cme_${cme_label}_malp_${mass_label}"
    mg_output_dir="${base_output_dir}_${JOBNUMBER}"

elif [ $# -eq 3 ]; then
    # Background: CME NEVENTS JOB
    is_signal=false
    CME="$1"
    NEVENTS="$2"
    JOBNUMBER="$3"

    cme_label=$(echo "$CME" | sed 's/\./p/g')
    base_output_dir="background_3photons_cme_${cme_label}"
    mg_output_dir="${base_output_dir}_${JOBNUMBER}"

else
    echo "Usage:"
    echo "  $0 CME MASS NEVENTS JOB      (signal)"
    echo "  $0 CME NEVENTS JOB           (background)"
    exit 1
fi

case "$CME" in
    365) sample_dir="tt_samples" ;;
    240) sample_dir="zh_samples" ;;
    160) sample_dir="ww_samples" ;;
    91.188) sample_dir="zpole_samples" ;;
    *) echo "ERROR: Unknown CME $CME"; exit 1 ;;
esac

input_file="/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/madgraph/${sample_dir}/${base_output_dir}/${mg_output_dir}.lhe"

if [ ! -s "$input_file" ]; then
    echo "WARNING: LHE file ${input_file} does not exist or is empty. Skipping job ${JOBNUMBER}."
    exit 0
fi

pythia_card="../processcards/pythia.cmnd"
tmp_pythia_card="../processcards/pythia_${mg_output_dir}.cmnd"
sed "s|INPUTFILE|${input_file}|g;s|NUMBEROFEVENTS|${NEVENTS}|g" "$pythia_card" > "$tmp_pythia_card"

output_dir="../output/${base_output_dir}"
mkdir -p "$output_dir"

DelphesPythia8_EDM4HEP \
    ../config/card_IDEA.tcl \
    ../config/edm4hep_IDEA.tcl \
    "$tmp_pythia_card" \
    "${output_dir}/${mg_output_dir}.root"