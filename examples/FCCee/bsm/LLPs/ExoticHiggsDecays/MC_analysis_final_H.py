#Input directory where the files produced at the stage1 level are
#inputDir  = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/MC_output_stage1/"
inputDir = "MC_output_stage1_H"

#Output directory where the files produced at the final-selection level are
outputDir  = "MC_output_finalSel_H/"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
#intLumi = 5e6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
#doScale = True

#Save event yields in a table (optional)
#saveTabular = True

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5_H':{},
        'exoticHiggs_scalar_ms20GeV_sine-6_H':{},
        'exoticHiggs_scalar_ms20GeV_sine-7_H':{},
        'exoticHiggs_scalar_ms60GeV_sine-5_H':{},
        'exoticHiggs_scalar_ms60GeV_sine-6_H':{},
        'exoticHiggs_scalar_ms60GeV_sine-7_H':{},

        # #centrally produced backgrounds
        'p8_ee_ZZ_ecm240':{'fraction':0.005, 'chunks':5},   
        'p8_ee_WW_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_ccH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_qqH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_bbH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_ssH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_ssH_Hbb_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_qqH_Hbb_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_bbH_Hbb_ecm240':{'fraction':0.005, 'chunks':5},   
        'wzp6_ee_ccH_Hbb_ecm240':{'fraction':0.005, 'chunks':5} 

}

###Dictionary for prettier names of processes (optional)
processLabels = {
    #signals
    'exoticHiggs_scalar_ms20GeV_sine-5_H': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms20GeV_sine-6_H': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms20GeV_sine-7_H': "$m_S$ = 20 GeV, sin $\theta = 1 * 10^{-7}$",
    'exoticHiggs_scalar_ms60GeV_sine-5_H': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-5}$",
    'exoticHiggs_scalar_ms60GeV_sine-6_H': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-6}$",
    'exoticHiggs_scalar_ms60GeV_sine-7_H': "$m_S$ = 60 GeV, sin $\theta = 1 * 10^{-7}$",

    # #backgrounds
    'p8_ee_WW_ecm240': "e^{-}e^{+} $\rightarrow$ WW",
    'p8_ee_ZZ_ecm240': "e^{-}e^{+} $\rightarrow$ ZZ",
    'p8_ee_ZH_ecm240': "e^{-}e^{+} $\rightarrow$ ZH",
    'p8_ee_ZZ_ecm240': "e^{-}e^{+} $\rightarrow$ WW",
    'p8_ee_WW_ecm240': "e^{-}e^{+} $\rightarrow$ ZZ",
    'wzp6_ee_ccH_HWW_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ cc, H $\rightarrow$ WW",
    'wzp6_ee_qqH_HWW_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ 1/2(uu + dd), H $\rightarrow$ WW",
    'wzp6_ee_bbH_HWW_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ bb, H $\rightarrow$ WW",
    'wzp6_ee_ssH_HWW_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ ss, H $\rightarrow$ WW",
    'wzp6_ee_ssH_Hbb_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ ss, H $\rightarrow$ bb",
    'wzp6_ee_qqH_Hbb_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ 1/2(uu + dd), H $\rightarrow$ bb",
    'wzp6_ee_bbH_Hbb_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ bb, H $\rightarrow$ bb",
    'wzp6_ee_ccH_Hbb_ecm240': "e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ cc, H $\rightarrow$ bb"
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    'exoticHiggs_scalar_ms20GeV_sine-5_H': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1.5943e-4, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-6_H': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1.5943e-4, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms20GeV_sine-7_H': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1.5943e-4, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-5_H': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.7134e-5, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-6_H': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.7134e-5, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'exoticHiggs_scalar_ms60GeV_sine-7_H': {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.7134e-5, "kfactor": 1.0, "matchingEfficiency": 1.0}
}

#Number of CPUs to use
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "selNone": "n_GenZ > -1",
    
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    "selNone": "Before selection",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #gen variables
    'n_GenU':                           {"name":"n_GenU",                         "title":"Number of generated up quarks",        "bin":20,"xmin":-0.5 ,"xmax":20.5},
    'n_GenD':                           {"name":"n_GenD",                         "title":"Number of generated down quarks",            "bin":20,"xmin":-0.5 ,"xmax":20.5},
    'n_GenC':                           {"name":"n_GenC",                         "title":"Number of generated charm quarks",        "bin":20,"xmin":-0.5 ,"xmax":20.5},
    'n_GenS':                           {"name":"n_GenS",                         "title":"Number of generated strange quarks",            "bin":20,"xmin":-0.5 ,"xmax":20.5},
    'n_GenZ':                           {"name":"n_GenZ",                         "title":"Number of generated Z bosons",         "bin":5,"xmin":-0.5 ,"xmax":4.5},
    'n_GenHiggs':                       {"name":"n_GenHiggs",                     "title":"Number of generated Higgs bosons",      "bin":5,"xmin":-0.5 ,"xmax":4.5},
    'n_Genb':                           {"name":"n_Genb",                         "title":"Number of generated b quarks",          "bin":5,"xmin":-0.5 ,"xmax":4.5},
    'n_GenHS':                          {"name":"n_GenHS",                        "title":"Number of generated dark scalars",      "bin":5,"xmin":-0.5 ,"xmax":4.5},

    'AllGenHS_mass':                    {"name":'AllGenHS_mass',                  "title":"Generated dark scalars mass [GeV]",     "bin":50,"xmin":-0.5 ,"xmax":49.5},
    'AllGenHS_e':                       {"name":'AllGenHS_e',                     "title":"Generated dark scalars energy [GeV]",   "bin":100,"xmin":-0.5 ,"xmax":99.5},

    'LxyHS':                            {"name":'LxyHS',                         "title":"Genenrated transverse decay length [mm]",       "bin":100,"xmin":0 ,"xmax":1000},
    'decayLengthsHS':                   {"name":'decayLengthsHS',                "title":"Generated decay length [mm]",                   "bin":100,"xmin":0 ,"xmax":10000},
    'lifetimeHS':                       {"name":'lifetimeHS',                    "title":"Generated time distribution t [ns]",            "bin":100,"xmin":0 ,"xmax":20},
    'lifetimeHSLAB':                    {"name":'lifetimeHSLAB',                "title":"Generated time distribution in LAB frame [ns]", "bin":100,"xmin":0 ,"xmax":20},

}
