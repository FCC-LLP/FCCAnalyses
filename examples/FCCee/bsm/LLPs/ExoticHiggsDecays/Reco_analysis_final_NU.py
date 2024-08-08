#Input directory where the files produced at the stage1 level are
inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/exoticHiggsSamplesCLD/Reco_output_stage1_NU"
#inputDir = "/eos/user/m/mlarson/Reco_output_stage1_NU"

#Output directory where the files produced at the final-selection level are
#outputDir  = "Reco_output_finalSel_IDEA/"
outputDir = "Reco_output_final_NU/"

# # #Integrated luminosity for scaling number of events (required only if setting doScale to true)
intLumi = 5.0e6 #pb^-1

# # #Scale event yields by intLumi and cross section (optional)
doScale = True

# # #Save event yields in a table (optional)
# saveTabular = True

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5_NU':{},
        'exoticHiggs_scalar_ms20GeV_sine-6_NU':{},
        'exoticHiggs_scalar_ms20GeV_sine-7_NU':{},
        'exoticHiggs_scalar_ms60GeV_sine-5_NU':{},
        'exoticHiggs_scalar_ms60GeV_sine-6_NU':{},
        'exoticHiggs_scalar_ms60GeV_sine-7_NU':{},

        #centrally produced backgrounds
        'p8_ee_ZZ_ecm240':{},
        'p8_ee_WW_ecm240':{},
        'wzp6_ee_nunuH_Hbb_ecm240':{},
        'wzp6_ee_nunuH_HWW_ecm240':{}
}

###Dictionary for prettier names of processes (optional)
processLabels = {
    #signals
    'exoticHiggs_scalar_ms20GeV_sine-5_NU': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms20GeV_sine-6_NU': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms20GeV_sine-7_NU': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-7}$",
    'exoticHiggs_scalar_ms60GeV_sine-5_NU': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms60GeV_sine-6_NU': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms60GeV_sine-7_NU': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-7}$",

    # #backgrounds
    'p8_ee_WW_ecm240': "e^{-}e^{+} $\rightarrow$ WW",
    'p8_ee_ZZ_ecm240': "e^{-}e^{+} $\rightarrow$ ZZ",
    'wzp6_ee_nunuH_Hbb_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ nu nu, H $\rightarrow$ bb",
    'wzp6_ee_nunuH_HWW_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ nu nu, H $\rightarrow$ WW",
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
#OBS NUMBEROFEVENTS AND SUMOFWEIGHTS HAS BEEN MODIFIED FOR DEBUGGING, REMEMBER TO CHANGE BACK
procDictAdd={
    'exoticHiggs_scalar_ms20GeV_sine-5_NU': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.2797e-5, "kfactor": 1.0, "matchingEfficiency": 1.0}, # NOTE cross sections use updated kappa value of 7e-4, which was used for sample generation 
    'exoticHiggs_scalar_ms20GeV_sine-6_NU': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.2797e-5, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-7_NU': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2.2797e-5, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-5_NU': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 6.7396e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-6_NU': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 6.7396e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-7_NU': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 6.7396e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
}

#Number of CPUs to use
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    # For plotting
    #"selNone": "n_tracks > -1",

    # For event selection
    "preSel": "((RecoMissingEnergy_e_sum > 30) && (RecoMissingEnergy_e_sum < 70))",
    "preSel+nDVs_seltracks": "((RecoMissingEnergy_e_sum > 30) && (RecoMissingEnergy_e_sum < 70)) && filter_n_DVs_seltracks > 1",
    "preSel+nDVs_merge": "((RecoMissingEnergy_e_sum > 30) && (RecoMissingEnergy_e_sum < 70)) && filter_n_DVs_merge > 1",
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    # For plotting
    #"selNone": "Before selection",

    # For event selection
    "preSel": "> 30 GeV Missing Energy",
    "preSel+nDVs_seltracks": "n DVs $\geq$ 2",
    "preSel+nDVs_merge": "n DVs $\geq$ 2 (merged)",
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
    
    "RecoMissingEnergy_e_sum":              {"name":"RecoMissingEnergy_e_sum",     "title":"Reco. Missing Energy [GeV]",                            "bin":80, "xmin":0, "xmax":80},
    "RecoMissingEnergy_p_sum":              {"name":"RecoMissingEnergy_p_sum",     "title":"Reco. Missing Momentum [GeV]",                          "bin":80, "xmin":0, "xmax":80},
    "RecoMissingEnergy_pt_sum":             {"name":"RecoMissingEnergy_pt_sum",    "title":"Reco. Missing Transverse Momentum [GeV]",               "bin":80, "xmin":0, "xmax":80},
    "RecoMissingEnergy_px_sum":             {"name":"RecoMissingEnergy_px_sum",    "title":"Reco. Missing Momenutm (along x-axis) [GeV]",           "bin":140, "xmin":-70, "xmax":70},
    "RecoMissingEnergy_py_sum":             {"name":"RecoMissingEnergy_py_sum",    "title":"Reco. Missing Momenutm (along y-axis) [GeV]",           "bin":140, "xmin":-70, "xmax":70},
    "RecoMissingEnergy_pz_sum":             {"name":"RecoMissingEnergy_pz_sum",    "title":"Reco. Missing Momenutm (along z-axis) [GeV]",           "bin":140, "xmin":-70, "xmax":70},
    "RecoMissingEnergy_eta_sum":            {"name":"RecoMissingEnergy_eta_sum",   "title":"Reco. Mising Energy eta",                               "bin":100, "xmin":-4, "xmax":4},
    "RecoMissingEnergy_theta_sum":          {"name":"RecoMissingEnergy_theta_sum", "title":"Reco. Mising Energy theta",                             "bin":64, "xmin":0, "xmax":3.2},
    "RecoMissingEnergy_phi_sum":            {"name":"RecoMissingEnergy_phi_sum",   "title":"Reco. Mising Energy phi",                               "bin":64, "xmin":-3.2, "xmax":3.2}
   

    
}
