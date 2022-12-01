# How to run the code
<details>
<summary>Show/Hide Table of Contents</summary>

[[_TOC_]]

</details>

## Overview

This text file describes how to produce ratio plots for comparing Dirac and Majorana HNLs.
Below is a description of how to modify `make_selection.py` and `make_plots.py`.

## make_selection.py
This script is used to select the variables to be plotted. It returns a .root file containing the selected variables histograms. You must run it both for your Dirac and Majorana samples. 
### How to adapt it to your needs
First, specify the path of the input file. The input file corresponds to the output file of `analysis_final.py`. The path should look like :
`/afs/cern.ch/user/d/dimoulin/FCCAnalyses_new/Analysis/outputs/HNL_Majorana_ejj_20GeV_1e-3Ve/output_finalSel/HNL_Majorana_ejj_20GeV_1e-3Ve_selNone_histo.root`
Next, specify the variables to be plotted, e.g if you want to plot the reconstructed electron energy (RecoElectron_e) you must include the line :
`histSelect.WriteObject(hist_file.Get("RecoElectron_e"), "RecoElectron_e")`
Finally, specify the name of the output file e.g : 
`output_file = "histMajorana_ejj_Select.root"`
You can then run the script using `python make_selection.py`

## make_plots.py
This script produces ratio plots of the previously selected variables.
### How to adapt it to your needs
You need to specify the path to the selection files :
`input_file_Dirac = 'histDirac_ejj_Select.root'`
`input_file_Majorana = 'histMajorana_ejj_Select.root'`
As well as the output directory : 
`output_dir = "20GeV_ejj_plots/"`

Then you must add the selected variables to the `variables_list`.

### Miscellaneous
You can modify the legend by modifying the second entry of `files_list`, as well as the colors of the graphs by modifying the `colors` list. Finally, the plots are currently saved in .png, you can modify this to any supported extension you like.




