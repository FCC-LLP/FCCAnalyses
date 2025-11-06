#!/bin/bash

# Usage: bash models.sh <config-file> <model>
# Accepted models: ALPnlo, ALP, ALP_NLO_UFO, ALP_linear_UFO

config_file="$1"
model="$2"

if [[ ! -f "$config_file" ]]; then
    echo "Error: Config file not found."
    exit 1
fi

if [[ "$model" != "ALPnlo" && "$model" != "ALP" && "$model" != "ALP_NLO_UFO" && "$model" != "ALP_linear_UFO" ]]; then
    echo "Error: Invalid model. Please choose from: ALPnlo, ALP, ALP_NLO_UFO, ALP_linear_UFO"
    exit 1
fi

# Parse config file
PROCESS=$(grep -i "^PROCESS" "$config_file" | sed 's/.*= *//')
if [[ "$model" == "ALP_linear_UFO" ]]; then
    PROCESS=${PROCESS//ALP/ax}
fi
MALP=$(grep -i "^MALP" "$config_file" | sed 's/.*= *//')
CME=$(grep -i "^CME" "$config_file" | sed 's/.*= *//')
NEVENTS=$(grep -i "^NEVENTS" "$config_file" | sed 's/.*= *//')
CYY=$(grep -i "^CYY" "$config_file" | sed 's/.*= *//')
CWW=$(grep -i "^CWW" "$config_file" | sed 's/.*= *//')
CBB=$(grep -i "^CBB" "$config_file" | sed 's/.*= *//')

if [[ -z "$PROCESS" || -z "$MALP" || -z "$CME" || -z "$NEVENTS" || -z "$CYY" || -z "$CBB" || -z "$CWW" ]]; then
    echo "Error: Missing one or more required parameters in config file."
    exit 1
fi

sum=$(python3 -c "print(${CWW} + ${CBB})")
is_equal=$(python3 -c "import math; print(math.isclose(${CYY}, ${sum}, rel_tol=1e-6))")

if [[ "$is_equal" != "True" ]]; then
    echo "Error: CYY (${CYY}) is not equal to CWW (${CWW}) + CBB (${CBB})"
    exit 1
fi

# Calculate couplings for ALP_linear_UFO
CBtil=$(python3 -c "print(${CBB} * 0.128215343)")
CWtil=$(python3 -c "print(${CWW} * 0.420418893)")

# Calculate beam energies
EBEAM1=$(python3 -c "print(${CME} / 2.0)")
EBEAM2=$EBEAM1

# Setup paths
base_dir="."
output_dir="${base_dir}/output/MG_${model}"
mkdir -p "$output_dir"

# Process card output path
temp_card="${base_dir}/processcards/temp_cards/$(basename "$output_dir").dat"
mkdir -p "$(dirname "$temp_card")"

# Template card path
process_card="${base_dir}/processcards/mg5_proc_card_${model}.dat"
if [[ ! -f "$process_card" ]]; then
    echo "Error: Process card not found: $process_card"
    exit 1
fi

# Generate random seed
seed=$(($RANDOM % 900000000 + 1))

subs=(
    -e "s|OUTPUTDIR|${output_dir}|g"
    -e "s|^generate .*|generate ${PROCESS}|g"
    -e "s|NUMBEROFEVENTS|${NEVENTS}|g"
    -e "s|SEEDNUMBER|${seed}|g"
    -e "s|ALPMASS|${MALP}|g"
    -e "s|EBEAM1|${EBEAM1}|g"
    -e "s|EBEAM2|${EBEAM2}|g" 
)

case "$model" in
    ALPnlo)
        subs+=(-e "s|^set cBB .*|set cBB ${CBB}|g")
        subs+=(-e "s|^set cWW .*|set cWW ${CWW}|g")
        ;;
    ALP)
        subs+=(-e "s|^set cAA .*|set cAA ${CYY}|g")
        ;;
    ALP_NLO_UFO)
        subs+=(-e "s|^set CYY .*|set CYY ${CYY}|g")
        subs+=(-e "s|^set cWW .*|set cWW ${CWW}|g")
        ;;
    ALP_linear_UFO)
        subs+=(-e "s|^set CBtil .*|set CBtil ${CBtil}|g")
        subs+=(-e "s|^set CWtil .*|set CWtil ${CWtil}|g")
        ;;
esac

sed "${subs[@]}" "${process_card}" > "$temp_card"

run_output=$(mktemp)
./bin/mg5_aMC "$temp_card" | tee "$run_output"

crossx_file="${output_dir}/crossx.html"

if [[ -f "$crossx_file" ]]; then
    xsec=$(grep 'run_01/results.html' "$crossx_file" \
        | sed -n 's/.*results\.html">[[:space:]]*\([0-9.][0-9.eE+-]*\)[[:space:]]*<font.*/\1/p' \
        | head -n1)
    xsec=${xsec:-"0"}
else
    echo "Warning: crossx.html not found"
    xsec="ERROR"
fi

log_file="${base_dir}/run_summary.csv"
if [[ ! -f "$log_file" ]]; then
    echo "Process,Model,CME,MALP,CYY,CWW,CBB,NEVENTS,XS" > "$log_file"
fi

echo "\"$PROCESS\",$model,$CME,$MALP,$CYY,$CWW,$CBB,$NEVENTS,$xsec" >> "$log_file"