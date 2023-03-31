#Input directory where the files produced at the stage1 level are
inputDir  = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/Reco_output_stage1/"

#Output directory where the files produced at the final-selection level are
outputDir  = "Reco_output_finalSel/"


# # #Integrated luminosity for scaling number of events (required only if setting doScale to true)
# intLumi = 5e6 #pb^-1

# # #Scale event yields by intLumi and cross section (optional)
# doScale = True

# # #Save event yields in a table (optional)
# saveTabular = True

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5':{},
        'exoticHiggs_scalar_ms20GeV_sine-6':{},
        'exoticHiggs_scalar_ms20GeV_sine-7':{},
        'exoticHiggs_scalar_ms60GeV_sine-5':{},
        'exoticHiggs_scalar_ms60GeV_sine-6':{},
        'exoticHiggs_scalar_ms60GeV_sine-7':{},

        #centrally produced backgrounds
        'p8_ee_ZZ_ecm240':{},
        'p8_ee_WW_ecm240':{},
        'p8_ee_ZH_ecm240':{},
}

###Dictionary for prettier names of processes (optional)
processLabels = {
    #signals
    'exoticHiggs_scalar_ms20GeV_sine-5': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms20GeV_sine-6': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms20GeV_sine-7': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-7}$",
    'exoticHiggs_scalar_ms60GeV_sine-5': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms60GeV_sine-6': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms60GeV_sine-7': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-7}$",

    #backgrounds
    'p8_ee_WW_ecm240': "e^{-}e^{+} $\rightarrow$ WW",
    'p8_ee_ZZ_ecm240': "e^{-}e^{+} $\rightarrow$ ZZ",
    'p8_ee_ZH_ecm240': "e^{-}e^{+} $\rightarrow$ ZH",
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_spring2021_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    'exoticHiggs_scalar_ms20GeV_sine-5': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.858e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.858e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-7': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 8.858e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-5': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.618e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.618e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-7': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.618e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
}

#Number of CPUs to use
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    # For plotting
    "selNone": "n_tracks > -1",

    # For event selection
    "preSel": "((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) || ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1)))",
    "selZ": "(Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)",
    "selZ+nDVs_seltracks": "((Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)) && filter_n_DVs_seltracks > 1",
    "selZ+nDVs_merge": "((Reco_ee_invMass > 70 && Reco_ee_invMass < 110) || (Reco_mumu_invMass > 70 && Reco_mumu_invMass < 110)) && filter_n_DVs_merge > 1",
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    # For plotting
    "selNone": "Before selection",

    # For event selection
    "preSel": "At least 2 oppositely charged leptons",
    "selZ": "70 < $m_{ll}$ < 110 GeV",
    "selZ+nDVs_seltracks": "n DVs $\geq$ 2",
    "selZ+nDVs_merge": "n DVs $\geq$ 2 (merged)",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.

histoList = {
    "n_tracks":                             {"name":"n_tracks",                 "title":"Number of reconstructed tracks",                          "bin":100, "xmin":-0.5,"xmax":99.5},
    "n_RecoedPrimaryTracks":                {"name":"n_RecoedPrimaryTracks",    "title": "Number of reconstructed primary tracks",                 "bin":10, "xmin":-0.5,"xmax":9.5},
    'n_seltracks_DVs':                      {"name":"n_seltracks_DVs",           "title":"Number of DVs",                                           "bin":12, "xmin":-0.5, "xmax":11.5},
    'n_trks_seltracks_DVs':                 {"name":'n_trks_seltracks_DVs',       "title":"Number of tracks from the DVs",                          "bin":30, "xmin":1.5, "xmax":29.5},
    'invMass_seltracks_DVs':                {"name":'invMass_seltracks_DVs',      "title":"Invariant mass at the DVs [GeV]",                           "bin":40, "xmin":-0.5, "xmax":39.5},
    "DV_evt_seltracks_chi2":                {"name":"DV_evt_seltracks_chi2",    "title":"The #chi^{2} distribution of the DVs",                    "bin":100, "xmin":-0.5, "xmax":11.5},
    "Reco_seltracks_DVs_Lxy":               {"name":"Reco_seltracks_DVs_Lxy",     "title":"Transverse distance between PV and DVs [mm]",               "bin":100, "xmin":0, "xmax":300},
    "Reco_seltracks_DVs_Lxyz":              {"name":"Reco_seltracks_DVs_Lxyz",    "title":"Distance between PV and DVs [mm]",                          "bin":100, "xmin":0, "xmax":2000},
    "DV_evt_seltracks_normchi2":            {"name":"DV_evt_seltracks_normchi2",    "title":"The normalised #chi^{2} distribution of the DVs",      "bin":40, "xmin":0, "xmax":10},
    "merged_DVs_n":                         {"name":"merged_DVs_n",              "title":"Number of DVs",                                           "bin":10, "xmin":-0.5, "xmax":9.5},
    'n_trks_merged_DVs':                    {"name":'n_trks_merged_DVs',       "title":"Number of tracks from the DVs from sel tracks + merge",   "bin":30, "xmin":1.5, "xmax":29.5},
    'invMass_merged_DVs':                   {"name":'invMass_merged_DVs',      "title":"Invariant mass at the DVs [GeV]",                           "bin":40, "xmin":-0.5, "xmax":39.5},
    "merged_DVs_chi2":                      {"name":"merged_DVs_chi2",          "title":"The #chi^{2} distribution of the merged DVs",              "bin":100, "xmin":-0.5, "xmax":11.5},
    "merged_DVs_normchi2":                  {"name":"merged_DVs_normchi2",       "title":"The normalised #chi^{2} distribution of the merged DVs",    "bin":40, "xmin":0, "xmax":10},
    "Reco_DVs_merged_Lxy":                  {"name":"Reco_DVs_merged_Lxy",     "title":"Transverse distance between PV and DVs [mm]",               "bin":100, "xmin":0, "xmax":300},
    "Reco_DVs_merged_Lxyz":                 {"name":"Reco_DVs_merged_Lxyz",    "title":"Distance between PV and DVs [mm]",                          "bin":100, "xmin":0, "xmax":2000},

    'n_RecoElectrons':                      {"name":'n_RecoElectrons',      "title": "Number of reconstructed electrons",                       "bin":10,"xmin":-0.5,"xmax":9.5},
    "Reco_ee_invMass":                      {"name":"Reco_ee_invMass",      "title": "Invariant mass of reconstructed e- e+ [GeV]",             "bin":100,"xmin":50,"xmax":150},
    'n_RecoMuons':                          {"name":'n_RecoMuons',          "title": "Number of reconstructed muons",                           "bin":10,"xmin":-0.5,"xmax":9.5},
    "Reco_mumu_invMass":                    {"name":"Reco_mumu_invMass",    "title": "Invariant mass of reconstructed #mu- #mu+ [GeV]",         "bin":100,"xmin":50,"xmax":150},    

    
}
