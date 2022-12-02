#Input directory where the files produced at the stage1 level are
#inputDir  = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/Reco_output_stage1/"
inputDir = "Reco_output_stage1/"

#Output directory where the files produced at the final-selection level are
outputDir  = "Reco_output_finalSel/"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
#intLumi = 5e6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
#doScale = True

#Save event yields in a table (optional)
#saveTabular = True

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5':{},
        # 'exoticHiggs_scalar_ms20GeV_sine-6':{},
        # 'exoticHiggs_scalar_ms20GeV_sine-7':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-5':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-6':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-7':{},
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
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_spring2021_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    'exoticHiggs_scalar_ms20GeV_sine-5': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.434e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.434e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-7': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.434e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-5': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1.311e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-6': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1.311e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-7': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1.311e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
}

#Number of CPUs to use
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "selNone": "n_tracks > -1",
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    "selNone": "Before selection",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #gen variables
    'n_RecoElectrons':              {"name":'n_RecoElectrons',      "title": "Number of reconstructed electrons",                       "bin":10,"xmin":-0.5,"xmax":9.5},
    'n_RecoMuons':                  {"name":'n_RecoMuons',          "title": "Number of reconstructed muons",                           "bin":10,"xmin":-0.5,"xmax":9.5},
    "Reco_ee_invMass":              {"name":"Reco_ee_invMass",      "title": "Invariant mass of reconstructed e- e+ [GeV]",             "bin":100,"xmin":50,"xmax":150},
    "Reco_mumu_invMass":            {"name":"Reco_mumu_invMass",    "title": "Invariant mass of reconstructed #mu- #mu+ [GeV]",         "bin":100,"xmin":50,"xmax":150},
    "n_RecoedPrimaryTracks":        {"name":"n_RecoedPrimaryTracks", "title": "Number of reconstructed primary tracks",                 "bin":10, "xmin":-0.5,"xmax":9.5},
    "n_SecondaryTracks":            {"name":"n_SecondaryTracks",    "title":"Number of reconstructed secondary tracks",                 "bin":50, "xmin":-0.5,"xmax":49.5},
    # 'invMass_SVs':                  {"name":'invMass_SVs',          "title":"Invariant mass at SVs [GeV]",                              "bin":30, "xmin":-0.5, "xmax":29.5},
    # "SV_evt1_n":                    {"name":"SV_evt1_n",            "title":"Number of SVs",                                            "bin":12, "xmin":-0.5, "xmax":11.5},
    # 'n_trks_SVs':                   {"name":'n_trks_SVs',           "title":"Number of tracks from the SVs",                            "bin":12, "xmin":1.5, "xmax":13.5},
    # "Reco_SVs_Lxy":                 {"name":"Reco_SVs_Lxy",         "title":"Transverse distance between PV and SVs [mm]",              "bin":100, "xmin":0, "xmax":300},
    # "Reco_SVs_Lxyz":                {"name":"Reco_SVs_Lxyz",        "title":"Distance between PV and SVs [mm]",                         "bin":100, "xmin":0, "xmax":2500},
    # 'invMass_SVs_seltracks_pt':     {"name":'invMass_SVs_seltracks_pt', "title":"Invariant mass at SVs from sel tracks pt [GeV]",       "bin":30, "xmin":-0.5, "xmax":29.5},
    # "SV_evt_seltracks_pt_n":        {"name":"SV_evt_seltracks_pt_n",     "title":"Number of SVs from sel tracks pt",                    "bin":12, "xmin":-0.5, "xmax":11.5},
    # 'n_trks_SVs_seltracks_pt':      {"name":'n_trks_SVs_seltracks_pt',   "title":"Number of tracks from the SVs from sel tracks pt",    "bin":12, "xmin":1.5, "xmax":13.5},
    # "Reco_SVs_seltracks_Lxy":       {"name":"Reco_SVs_seltracks_Lxy",    "title":"Transverse distance between PV and SVs from sel tracks pt [mm]",   "bin":100, "xmin":0, "xmax":300},
    # "Reco_SVs_seltracks_Lxyz":      {"name":"Reco_SVs_seltracks_Lxyz",   "title":"Distance between PV and SVs from sel tracks pt [mm]",               "bin":100, "xmin":0, "xmax":2500},
    # 'invMass_merged_SVs_pt':        {"name":'invMass_merged_SVs_pt',      "title":"Invariant mass at SVs from sel pt + merge [GeV]",    "bin":30, "xmin":-0.5, "xmax":29.5},
    # "merged_SVs_pt_n":              {"name":"merged_SVs_pt_n",            "title":"Number of SVs from sel pt + merge",                  "bin":12, "xmin":-0.5, "xmax":11.5},
    # 'n_trks_merged_SVs_pt':         {"name":'n_trks_merged_SVs_pt',       "title":"Number of tracks from the SVs from sel pt + merge",   "bin":12, "xmin":1.5, "xmax":13.5},
    # "Reco_SVs_merged_pt_Lxy":       {"name":"Reco_SVs_merged_pt_Lxy",     "title":"Transverse distance between PV and SVs from sel pt + merge [mm]",  "bin":100, "xmin":0, "xmax":300},
    # "Reco_SVs_merged_pt_Lxyz":      {"name":"Reco_SVs_merged_pt_Lxyz",    "title":"Distance between PV and SVs from sel pt + merge [mm]",             "bin":100, "xmin":0, "xmax":2500},
    'invMass_merged_SVs':           {"name":'invMass_merged_SVs',      "title":"Invariant mass at SVs from sel pt d0 + merge [GeV]",    "bin":30, "xmin":-0.5, "xmax":29.5},
    "merged_SVs_n":                 {"name":"merged_SVs_n",            "title":"Number of SVs from sel pt d0 + merge",                  "bin":12, "xmin":-0.5, "xmax":11.5},
    'n_trks_merged_SVs':            {"name":'n_trks_merged_SVs',       "title":"Number of tracks from the SVs from sel pt d0 + merge",   "bin":12, "xmin":1.5, "xmax":13.5},
    "Reco_SVs_merged_Lxy":          {"name":"Reco_SVs_merged_Lxy",     "title":"Transverse distance between PV and SVs from sel pt d0 + merge [mm]",  "bin":100, "xmin":0, "xmax":300},
    "Reco_SVs_merged_Lxyz":         {"name":"Reco_SVs_merged_Lxyz",    "title":"Distance between PV and SVs from sel pt d0 + merge [mm]",             "bin":100, "xmin":0, "xmax":2500},
    "jets_ee_kt_m":                 {"name":"jets_ee_kt_m",            "title":"Mass of the reconstructed jets [GeV]",                   "bin":50, "xmin":-0.5, "xmax": 49.5},

}
