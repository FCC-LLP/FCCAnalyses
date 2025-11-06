# ALPs @ FCC-ee

This repository documents a workflow for generating and analyzing samples for an FCC-ee ALP analysis with a three photon final state.

## Sample Locations

Generated samples are stored on EOS:

- `/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/madgraph`
  - Events processed through **MadGraph**
  - Organized under: zpole_samples, ww_samples, zh_samples, tt_samples
- `/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/pythiadelphes`
  - Events processed through **Pythia and DELPHES**
  - Organized under: zpole_samples, ww_samples, zh_samples, tt_samples
- `/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses`
  - Events processed through **FCCAnalyses**
  - Organized under: stage1, final, and plots
  - Further organized under: zpole_samples, ww_samples, zh_samples, tt_samples

## Repository Structure

```
.
├── madgraph/
│   ├── models/
│   ├── config/
│   ├── processcards/
│   └── scripts/
├── pythiadelphes/
│   ├── config/
│   └── processcards/  
├── fccanalyses/  
├── combine/     
├── README.md
```

## Overview

1. Generate events with [MadGraph5_aMC@NLO](https://launchpad.net/mg5amcnlo)  
2. Shower, hadronize, and simulate detector response with Pythia + DELPHES 
3. Analyze results with the [FCCAnalyses framework](https://gitlab.cern.ch/cdorofee/FCCAnalyses)  
4. Perform statistical interpretation with [Combine](https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit)

## 1. MadGraph

1. **Download MadGraph** (latest version [here](https://launchpad.net/mg5amcnlo), e.g. v3.6.3):
   ```bash
   scp MG5_aMC_<version>.tar <username>@lxplus.cern.ch:</path/to/your/dir>
   ```

2. **Log into lxplus**:
   ```bash
   ssh <username>@lxplus.cern.ch
   ```

3. **Untar and run**:
   ```bash
   tar -xf MG5_aMC_<version>.tar
   cd MG5_aMC_<version>/
   ./bin/mg5_aMC
   ```

4. **UFO Model Setup**:
   - Download the desired model in UFO format from [`madgraph/models/`](https://gitlab.cern.ch/cdorofee/alps-fcc-ee/-/tree/master/madgraph/models)
   - Transfer and unzip in `MG5_aMC_<version>/models/`

### Available Models

| Model            | Notes                                          |
|------------------|------------------------------------------------|
| `ALPnlo`         |  Obtained from Bauer by Abu Dhabi colleagues   |       
| `ALP`            | Obtained from Thamm in 2019                    |
| `ALP_NLO_UFO`    | Used for Snowmass report, available in LLP git |
| `ALP_linear_UFO` | Obtained from Brivio et al.                    |

> We use the `ALP` model for current studies. However, you can test all models using the provided processing cards and scripts.

## Running different models in MadGraph

Use the script:
```bash
./models.sh <config-file>.txt <model>
```

- `<config-file>`:  text file specifying process and parameters 
- `<model>`: directory or tag name for UFO model you wish to use

### Example Config File

```
process = e+ e- > a ALP
CME = 91.188
MALP = 1.
CYY = 1.
CWW = 0.
CBB = 1.
nevents = 1.
```

> Edit couplings, mass, and center-of-mass energy directly in the config file or the relevant process card

The script will:

- Run MadGraph with the specified model, processing card, and config file
- Generate standard MadGraph output (e.g., event files, logs)
- Create a summary `.csv` file containing:
  - The process description
  - Model parameters (e.g., couplings, ALP mass)
  - The calculated cross section

If a process does **not** return a valid cross section, the CSV file will display a value of `0` for that entry

## Running ALP Model on HTCondor

Since the ALP model is the one used in this analysis, all sample generation is performed with it, and the workflow is configured to run on HTCondor. 

There are several ways to run MadGraph5_aMC@NLO on Condor (see [Launchpad](https://answers.launchpad.net/mg5amcnlo/+question/704470) for details):

1. **MadGraph built-in cluster mode**

MadGraph launches a local job controller, which submits jobs to Condor using its internal cluster submission system.

2. **Manual Condor submission (full-node multicore)**

MadGraph runs in multi-core mode directly on a requested node, with a user-written Condor submit file.

3. **Hybrid method**

Similar to the built-in mode, but the controller itself is submitted to Condor. Since the controller only manages jobs, it requires just one core.

All three approaches were tested (albeit not systematically), and in principle each should work. Here, we provide settings corresponding to method 2, which proved to be the most reliable. You may choose a different method depending on Condor configuration, the process being generated, and how much control you want over job submission.

1. If not already done so, copy ALP model to:
   ```
   MG5_aMC_<version>/models/
   ```

2. To enable Condor execution, add the following lines to MG5_aMC_\<version\>/input/mg5_configuration.txt:
   ```
   run_mode = 2
   nb_core  = 0
   ```
3. Submit job with:
   ```bash
   condor_submit mg.sub
   ```

## 2. PYTHIA + DELPHES

Cards from the Winter2023 campaign:

- **Delphes card**: [`card_IDEA.tcl`](https://github.com/HEP-FCC/FCC-config/blob/winter2023/FCCee/Delphes/card_IDEA.tcl)
- **EDM4HEP tcl**: [`edm4hep_IDEA.tcl`](https://github.com/HEP-FCC/FCC-config/blob/winter2023/FCCee/Delphes/edm4hep_IDEA.tcl)

can be found in this repo under:
```
pythiadelphes/config/
```
Pythia + Delphes can be run on Condor with the `pythiadelphes.sub` script. The `pythia.cmnd` file can be found under pythiadelphes/processcards. You will first have to run the `queue.sh` script to generate an array of center of mass energies and ALP masses before running the Condor sub file.

## 3. FCCAnalysis

Once the `.root` file is produced, it contains the event data in **EDM4HEP** format. You can now analyze this using the [FCCAnalysis](https://github.com/FCC-LLP/FCCAnalyses/tree/master) framework and generate plots. 
```
fccanalysis run analysis_stage1.py
fccanalysis final analysis_final.py
fccanalysis plots analysis_plots.py
```
It is also possible to run FCCAnalysis on Condor. This is especially useful if you are running over many events and files. You can read more about the process [here](https://hep-fcc.github.io/FCCAnalyses/man/latest/fccanalysis-submit.html).

## 4. Combine

Before running the limit scripts, you must first install Combine. You may follow the instructions [here](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/). Though the standalone compilation with LCG seemed to work, we would recommend installation within a CMSSW environment, if possible.  

1. **Generating datacards and running Combine to produce limits**
   ```
   python limit.py --cme <zpole, ww, zh, or tt> --sel <sel or selNone>
   ```

2. **Convert limits to cross section and produce Brazil plot**:
   ```
   python combine.py --cme <zpole, ww, zh, or tt> --sel <sel or selNone>
   ```

3. **Converts limits on cross section to limit on coupling**:
   ```
   python coupling.py
   ```
