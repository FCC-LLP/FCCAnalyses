#!/bin/bash
job_number=$1
mass=$2
coupling=$3
nevents=$4

mass_filename=$(echo ${mass} | sed "s/\./p/g")
coupling_filename=$(echo ${coupling} | sed "s/\./p/g")

baseoutputdir="ALP_Z_aa_${mass_filename}GeV_cYY${coupling_filename}"
MGfiledir="$baseoutputdir_${job_number}"

#input .lhe files for the pythia run
inputfile="/eos/user/e/ebakhish/MG/MGOutput/$MGfiledir/Events/run_01/unweighted_events.lhe.gz"
pythiacard=../ALP_pythia.cmnd
temp_pythiacard="/eos/user/e/ebakhish/MG/Pythiacards/ALP_pythia_${MGfiledir}.cmnd"
#outputfile= "/eos/user/e/ebakhish/MG/Pythia_Output/${MGfiledir}"

#this line searches for certain variables in the input file and replaces them with our defined properties for #events and inputfile
sed "s|INPUTFILE|${inputfile}|g;s|NUMBEROFEVENTS|${nevents}|g" $pythiacard > $temp_pythiacard


if [! -d "/eos/user/e/ebakhish/MG/Pythia_Output/baseoutputdir"]; then
    mkdir "/eos/user/e/ebakhish/MG/Pythia_Output/${baseoutputdir}"  
fi

# quick command to run DelphesPythia8_EDM4HEP
# needs one input for the name of the output root-file
DelphesPythia8_EDM4HEP ../../../../../../../../FCC-config/FCCee/Delphes/card_IDEA.tcl ../../../../../../../../FCC-config/FCCee/Delphes/edm4hep_IDEA.tcl $temp_pythiacard /eos/user/e/ebakhish/MG/Pythia_Output/baseoutputdir/${MGfiledir}.root
