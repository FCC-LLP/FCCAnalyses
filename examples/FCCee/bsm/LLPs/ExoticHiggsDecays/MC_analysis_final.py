#Input directory where the files produced at the stage1 level are
#inputDir  = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/MC_output_stage1/"
inputDir = "MC_output_stage1/"

#Output directory where the files produced at the final-selection level are
outputDir  = "MC_output_finalSel/"

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
    "selNone": "n_GenZ > -1",
    
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    "selNone": "Before selection",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #gen variables
    'n_GenElectrons':                   {"name":"n_GenElectrons",                  "title":"Number of generated electrons",        "bin":5,"xmin":-0.5 ,"xmax":4.5},
    'n_GenMuons':                       {"name":"n_GenMuons",                     "title":"Number of generated muons",            "bin":5,"xmin":-0.5 ,"xmax":4.5},
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
