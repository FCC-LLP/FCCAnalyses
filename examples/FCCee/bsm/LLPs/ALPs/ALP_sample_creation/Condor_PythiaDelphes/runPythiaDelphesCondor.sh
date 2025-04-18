#!/bin/bash

# *** run this with bash runPythiaDelphesCondor.sh <job_number> <mass> <coupling> <nevents> to find the previously created ALP signal sample from MadGraph
# *** and to run it through PythiaDelphes, mass and coupling should always be denoted with a . for decimal (e.g. 0.3 for 0.3 GeV)

job_number=$1
mass=$2
coupling=$3
nevents=$4

mass_filename=$(echo ${mass} | sed "s/\./p/g")
coupling_filename=$(echo ${coupling} | sed "s/\./p/g")

baseoutputdir="ALP_Z_aa_${mass_filename}GeV_cYY${coupling_filename}"
MGfiledir="${baseoutputdir}_${job_number}"
#use this with correct number _v... if you are adding more samples afterwards
#MGfiledir="${baseoutputdir}_${job_number}_v1"

#input .lhe files for the pythia run
inputfile="/eos/user/e/ebakhish/MG/MGOutput/${baseoutputdir}/${MGfiledir}/Events/run_01/unweighted_events.lhe.gz"
pythiacard=/afs/cern.ch/user/e/ebakhish/FCCAnalyses/examples/FCCee/bsm/LLPs/ALPs/ALP_sample_creation/ALP_pythia_sample.cmnd
temp_pythiacard="/eos/user/e/ebakhish/MG/Pythiacards/ALP_pythia_${MGfiledir}.cmnd"
#outputfile= "/eos/user/e/ebakhish/MG/Pythia_Output/${MGfiledir}"

#this line searches for certain variables in the input file and replaces them with our defined properties for #events and inputfile
sed "s|INPUTFILE|${inputfile}|g;s|NUMBEROFEVENTS|${nevents}|g" $pythiacard > $temp_pythiacard

#collect the output in specified directory
if [ ! -d "/eos/user/e/ebakhish/MG/Pythia_Output/${baseoutputdir}" ]; then
    mkdir -p "/eos/user/e/ebakhish/MG/Pythia_Output/${baseoutputdir}"  
fi




# only run following command if the MadGraph output was successful

if [ -d "/eos/user/e/ebakhish/MG/MGOutput/${baseoutputdir}/${MGfiledir}/Events/run_01" ]; then
    # quick command to run DelphesPythia8_EDM4HEP
    # needs one input for the name of the output root-file
    DelphesPythia8_EDM4HEP /afs/cern.ch/user/e/ebakhish/FCC-config/FCCee/Delphes/card_IDEA.tcl /afs/cern.ch/user/e/ebakhish/FCC-config/FCCee/Delphes/edm4hep_IDEA.tcl $temp_pythiacard /eos/user/e/ebakhish/MG/Pythia_Output/${baseoutputdir}/${MGfiledir}.root
else 
    echo "/$MGfiledir/Events/run_01 does not exist"
fi
