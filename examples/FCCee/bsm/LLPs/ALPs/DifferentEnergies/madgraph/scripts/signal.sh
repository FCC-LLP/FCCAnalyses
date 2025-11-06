#!/bin/bash
#Usage: bash signal.sh <CME> <ALPMASS> <NEVENTS> <JOBNUMBER>

CME="$1"           # Center-of-mass energy in GeV
ALPMASS="$2"       # ALP mass in GeV
NEVENTS="$3"       # Number of events
JOBNUMBER="$4"     # Job index from Condor

base_dir="<PATH TO MADGRAPH DIRECTORY>"
base_eos_dir="<PATH TO USER OUTPUT DIRECTORY>"
cme_label=$(echo "$CME" | sed 's/\./p/g')
mass_label=$(echo "$ALPMASS" | sed 's/\./p/g')
base_output_dir="alp_3photons_cme_${cme_label}_malp_${mass_label}"
full_output_dir="${base_eos_dir}/${base_output_dir}/${base_output_dir}_${JOBNUMBER}"

if [ ! -d "${base_eos_dir}/${base_output_dir}" ]; then
    mkdir -p "${base_eos_dir}/${base_output_dir}"
fi

process_card="${base_dir}/processcards/signal.dat"
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
    -e "s|ALPMASS|${ALPMASS}|g" \
    -e "s|NUMBEROFEVENTS|${NEVENTS}|g" \
    -e "s|SEEDNUMBER|${SEEDNUMBER}|g" \
    "$process_card" > "$temp_card"

"${base_dir}/bin/mg5_aMC" "$temp_card"