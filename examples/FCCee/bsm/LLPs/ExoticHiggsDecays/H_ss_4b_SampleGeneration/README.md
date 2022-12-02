Author: Giulia Ripellino and Magdalena Vande Voorde

Contact: giulia.ripellino@cern.ch

This folder will allow you to create your own madgraph sample for exotic Higgs decays using the HAHM model http://insti.physics.sunysb.edu/~curtin/hahm_mg.html.

Setting up Madgraph and the HAHM model
-----

First, set up the FCC analysis environment (necessary e.g to enable use of python 3.7 which is needed for MagGraph):

```
source /cvmfs/fcc.cern.ch/sw/latest/setup.sh
```

Now download the latest version of madgraph (http://madgraph.phys.ucl.ac.be/ or directly at https://launchpad.net/mg5amcnlo). Here we're using MadGraph5 v3.4.1. 

Copy the Madgraph tarball to your local area on lxplus:

```
scp MG5_aMC_v3.4.1.tar username@lxplus.cern.ch:/path/to/your/dir
```

Then ssh to lxplus and unzip the tarball 
```
tar -xf MG5_aMC_v3.4.1.tar
```

Then download the HAHM_MG5model_v3 model from http://insti.physics.sunysb.edu/~curtin/hahm_mg.html. Copy to lxplus and unzip with the same procedure.

Move the HAHM_variableMW_UFO and HAHM_variablesw_UFO into the Madgraph5 models directory: `MG5_aMC_v3_4_1/models/`.

For instructions on how to generate samples with a processcard instead, see further down.
Down below follows instructions how to generate samples for exotic Higgs decays by directly changing in the param_card.

Generate samples directly in param_card
----

Run:
```
cd MG5_aMC_v3_4_1
./bin/mg5_aMC
```

Then enter (for Higgs to dark photons):
```
set auto_convert_model T
import model --modelname HAHM_variableMW_UFO
generate h > zp zp 
output PROC_HAHM_variableMW_UFO_DarkPhoton
```

or (for Higgs to scalars)
```
generate h > hs hs 
output PROC_HAHM_variableMW_UFO_DarkScalar
```

Now set parameters in `PROC_HAHM_variableMW_UFO_<Model>/Cards/param_card.dat`:

For scalar case: Set epsilon=1.000000e-09 and mZD=1.000000e+03

For dark photon case: kap = 1.000000e-09 and MHS=1.000000e+03 

Now run
```
./bin/mg5_aMC proc_card_mg5.dat
```
to create the LHE file, where `proc_card_mg5.dat` is the madgraph proc card you are interested in generating.

The resulting events will be stored in `PROC_HAHM_variableMW_UFO_DarkScalar/Events/run_01/unweighted_events.lhe.gz` file. Unzip it (`gunzip unweighted_events.lhe.gz`) and give the *absolute* path to DarkScalar_pythia.cmnd file to generate the delphes root file.
Change the first line of header of your .lhe file

LesHouchesEvents version=“3.0” —> LesHouchesEvents version=“2.0”

(Otherwise it will crash due to some Pythia issue, see: https://answers.launchpad.net/mg5amcnlo/+question/263774)

Creating samples using a processcard
-------
In this folder there are processcards named e.g "exoticHiggs_scalar_mS20GeV_WHSe-14_proc_card.dat" generating the process e+ e- -> Z -> Z h with Z -> e+ e-/mu+ mu- and h -> 2hs -> 4b at the center-of-mass energy 240 GeV.
The dark photon is decoupled by setting mZD = 1000 GeV and epsilon = 1e-10. The coupling constant between Higgs and the scalar is set to kappa = 1e-3.
The generated samples have different masses and lifetimes, defined by it's width, WHS. In this example the processcard generates a sample with the mass of the scalar mS = 20 GeV and the width WHS is set to be of order 10^(-14) GeV, which equals a lifetime, ctau, of order mm.
See the processcard for more details.


Put this processcard in your MG5_aMC_v3_4_1 directory and run:

```
# standing in directory MG5_aMC_v3_4_1
./bin/mg5_aMC exoticHiggs_scalar_mS20GeV_WHSe-14_proc_card.dat
```

The resulting events will be stored in `h_2hs_4b_mhs20GeV_WHSe-14/Events/run_01/unweighted_events.lhe.gz` file.
Unzip it and give the *absolute* path to the exoticHiggs_scalar_pythia.cmnd file to generate the delphes root file.

```
# standing in directory MG5_aMC_v3_4_1/h_2hs_4b_mhs20GeV_WHSe-14/Events/run_01/
gunzip -c unweighted_events.lhe.gz > your/path/to/h_2hs_4b_mhs20GeV_WHSe-14.lhe
```

Change the first line of header of your .lhe file

LesHouchesEvents version=“3.0” —> LesHouchesEvents version=“2.0”

(Otherwise it will crash due to some Pythia issue, see: https://answers.launchpad.net/mg5amcnlo/+question/263774)

Creating the delphes root file and edm4hep sample
-----

You need to grab the latest official Delphes card and edm4hep tcl file:
```
#cd to one directory up from FCCAnalyses/
git clone https://github.com/HEP-FCC/FCC-config.git
cd FCC-config/
git checkout spring2021
cd ..
```

To create delphes root file you need to do the following on your command line (make sure you have the .lhe file and the .cmnd file in the same directory as you are running in):

```
# standing one directory up from FCC-config
source /cvmfs/fcc.cern.ch/sw/latest/setup.sh
DelphesPythia8_EDM4HEP ./FCC-config/FCCee/Delphes/card_IDEA.tcl ./FCC-config/FCCee/Delphes/edm4hep_IDEA.tcl exoticHiggs_scalar_pythia.cmnd exoticHiggs_scalar_ms20GeV_sine-5.root
```

The resulting exoticHiggs_scalar_ms20GeV_sine-5.root is your edm4hep sample!
When running the different processcards to create the different lhe files, don't forget to change the name of the lhe file in the pythia card, line 14. 
