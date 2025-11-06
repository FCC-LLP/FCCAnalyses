#!/bin/bash
#Usage: bash background.sh <CME> <NEVENTS> <JOBNUMBER>

CME="$1"           # Center-of-mass energy in GeV
NEVENTS="$2"       # Number of events
JOBNUMBER="$3"     # Job index from Condor

base_dir="<PATH TO MADGRAPH DIRECTORY>"
base_eos_dir="<PATH TO USER OUTPUT DIRECTORY>"
cme_label=$(echo "$CME" | sed 's/\./p/g')
base_output_dir="background_3photons_cme_${cme_label}"
full_output_dir="${base_eos_dir}/${base_output_dir}/${base_output_dir}_${JOBNUMBER}"

if [ ! -d "${base_eos_dir}/${base_output_dir}" ]; then
    mkdir -p "${base_eos_dir}/${base_output_dir}"
fi

process_card="${base_dir}/processcards/background.dat"
if [[ ! -f "$process_card" ]]; then
    echo "Error: Process card not found: $process_card"
    exit 1
fi

temp_card="${base_dir}/processcards/temp_cards/$(basename "${full_output_dir}").dat"
mkdir -p "$(dirname "$temp_card")"

EBEAM1=$(python3 -c "print(${CME} / 2.0)")
EBEAM2="$EBEAM1"
SEEDNUMBER=$(( JOBNUMBER + RANDOM ))

sed -e "s|OUTPUTDIR|${full_output_dir}|g" \
    -e "s|EBEAM1|${EBEAM1}|g" \
    -e "s|EBEAM2|${EBEAM2}|g" \
    -e "s|NUMBEROFEVENTS|${NEVENTS}|g" \
    -e "s|SEEDNUMBER|${SEEDNUMBER}|g" \
    "$process_card" > "$temp_card"

"${base_dir}/bin/mg5_aMC" "$temp_card"