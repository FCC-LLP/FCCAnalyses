'''
Final stage of the ALP analysis: e⁺e⁻ → aγ → γγγ
'''

#TODO: would be nice to have some sort of cme "tag" to select events rather than commenting/uncommenting blocks of code
#TODO: would also be nice to have better selection of bin ranges for histograms based on cme

# Input/output directories
inputDir  = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/stage1/zpole_samples"
outputDir = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples"

# List of datasets used in the analysis
process_list = {
    # uncomment the samples you want to run over
    #######################################################
    #               CME: 91.188 GeV (Z pole)              #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_91p188_malp_0p1'  : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_1p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_5p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_10p0' : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_25p0' : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_50p0' : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_60p0' : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_70p0' : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_80p0' : {'fraction': 1.0},
    #'alp_3photons_cme_91p188_malp_90p0' : {'fraction': 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_91p188'    : {'fraction': 1.0},

    #######################################################
    #                  CME: 160 GeV (WW)                  #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_160_malp_0p1'   : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_1p0'   : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_5p0'   : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_10p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_25p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_50p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_60p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_70p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_80p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_90p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_100p0' : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_120p0' : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_140p0' : {'fraction': 1.0},
    #'alp_3photons_cme_160_malp_150p0' : {'fraction': 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_160'     : {'fraction': 1.0},

    #######################################################
    #                  CME: 240 GeV (ZH)                  #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_240_malp_0p1'   : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_1p0'   : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_5p0'   : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_10p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_25p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_50p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_60p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_70p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_80p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_90p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_100p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_120p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_140p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_150p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_160p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_180p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_200p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_220p0' : {'fraction': 1.0},
    #'alp_3photons_cme_240_malp_230p0' : {'fraction': 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_240'     : {'fraction': 1.0},

    #######################################################
    #                  CME: 365 GeV (tt)                  #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_365_malp_0p1'   : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_1p0'   : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_5p0'   : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_10p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_25p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_50p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_60p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_70p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_80p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_90p0'  : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_100p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_120p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_140p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_150p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_160p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_180p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_200p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_220p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_230p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_240p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_250p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_300p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_320p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_340p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_350p0' : {'fraction': 1.0},
    #'alp_3photons_cme_365_malp_360p0' : {'fraction': 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_365'     : {'fraction': 1.0},
}

procDict = "FCCee_procDict_winter2023_IDEA.json"

# Add samples which are not part of the offical process
procDictAdd = {
        # uncomment the samples you want to run over
    #######################################################
    #               CME: 91.188 GeV (Z pole)              #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_91p188_malp_0p1'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.471,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_1p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.471,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_5p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.448,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_10p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.382,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_25p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 1.954,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_50p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.8451,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_60p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.4505,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_70p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.1712,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_80p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.03019,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_91p188_malp_90p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00004286, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_91p188'    : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 9.02,       "kfactor": 1.0, "matchingEfficiency": 1.0},

    #######################################################
    #                  CME: 160 GeV (WW)                  #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_160_malp_0p1'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02176,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_1p0'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02175,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_5p0'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02169,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_10p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0215,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_25p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0202,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_50p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01598,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_60p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01381,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_70p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0115,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_80p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.009178,   "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_90p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00695,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_100p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00491,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_120p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.001749,   "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_140p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0002533,  "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_160_malp_150p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00003391, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_160'     : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 3.083,      "kfactor": 1.0, "matchingEfficiency": 1.0},

    #######################################################
    #                  CME: 240 GeV (ZH)                  #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_240_malp_0p1'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02048,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_1p0'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02047,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_5p0'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02045,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_10p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02037,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_25p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01982,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_50p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01792,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_60p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01687,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_70p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01568,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_80p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01438,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_90p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01299,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_100p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01153,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_120p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.008291,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_140p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.005316,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_150p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.004067,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_160p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.002998,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_180p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.001396,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_200p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0004547,   "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_220p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00006242,  "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_240_malp_230p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.000008181, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_240'     : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 1.427,       "kfactor": 1.0, "matchingEfficiency": 1.0},

    #######################################################
    #                  CME: 365 GeV (tt)                  #
    #######################################################
    # Signal samples: e⁺e⁻ → aγ → γγγ
    #'alp_3photons_cme_365_malp_0p1'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02013,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_1p0'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02013,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_5p0'   : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02012,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_10p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02009,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_25p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01985,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_50p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01902,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_60p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01855,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_70p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01799,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_80p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01737,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_90p0'  : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01668,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_100p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01589,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_120p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01371,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_140p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01129,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_150p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.01015,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_160p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.009066,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_180p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.007104,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_200p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00537,      "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_220p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.003888,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_230p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.003245,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_240p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.002667,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_250p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.002152,     "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_300p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0004664,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_320p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0001667,    "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_340p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.00003077,   "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_350p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.000006897,  "kfactor": 1.0, "matchingEfficiency": 1.0},
    #'alp_3photons_cme_365_malp_360p0' : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0000002654, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # Background samples: e⁺e⁻ → γγγ
    #'background_3photons_cme_365'     : {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.6656,       "kfactor": 1.0, "matchingEfficiency": 1.0},
}

intLumi = 2.05e8
#intLumi = 1.92e7
#intLumi = 1.08e7
#intLumi = 2.7e6
doScale = True

# Number of threads to use
# nCPUS = 2

# Whether to produce ROOT TTrees, default is False
doTree = False

# Save cut yields and efficiencies in LaTeX table
saveTabular = True

# Save cut yields and efficiencies in JSON file
saveJSON = True

# Dictionary with the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "selNone": "n_RecoTracks > -1",
    "sel": "n_RecoPhotons == 3",
}

cutLabels = {
    "selNone": "Before selection",
    "sel": "Exactly 3 reconstructed photons",
}

'''
Dictionary for the output variables/histograms. 
The key is the name of the variable in the output files. 
"name" is the name of the variable in the input file, 
"title" is the x-axis label of the histogram, 
"bin" the number of bins of the histogram, 
"xmin" the minimum x-axis value and 
"xmax" the maximum x-axis value
'''
histoList = {
    "Calorimeterhit_time":                              {"name":"Calorimeterhit_time",                              "title":"Time of calorimeter hit",                                "bin":100, "xmin":0,     "xmax":10e-8},  
    "All_n_GenALP":                                     {"name":"All_n_GenALP",                                     "title":"Total number of gen ALPs",                               "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "n_FSGenALP":                                       {"name":"n_FSGenALP",                                       "title":"Total number of FS  gen ALPs",                           "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "AllGenALP_mass":                                   {"name":"AllGenALP_mass",                                   "title":"All gen ALP mass [GeV]",                                 "bin":100, "xmin":0,     "xmax":50},
    "AllGenALP_e":                                      {"name":"AllGenALP_e",                                      "title":"All gen ALP energy [GeV]",                               "bin":100, "xmin":0,     "xmax":100},
    "AllGenALP_p":                                      {"name":"AllGenALP_p",                                      "title":"All gen ALP p [GeV]",                                    "bin":100, "xmin":0,     "xmax":50},
    "AllGenALP_pt":                                     {"name":"AllGenALP_pt",                                     "title":"All gen ALP p_{T} [GeV]",                                "bin":100, "xmin":0,     "xmax":50},
    "AllGenALP_pz":                                     {"name":"AllGenALP_pz",                                     "title":"All gen ALP p_{z} [GeV]",                                "bin":100, "xmin":0,     "xmax":50},
    "AllGenALP_eta":                                    {"name":"AllGenALP_eta",                                    "title":"All gen ALP #eta",                                       "bin":60,  "xmin":-3,    "xmax":3},
    "AllGenALP_theta":                                  {"name":"AllGenALP_theta",                                  "title":"All gen ALP #theta",                                     "bin":64,  "xmin":0,     "xmax":3.2},
    "AllGenALP_phi":                                    {"name":"AllGenALP_phi",                                    "title":"All gen ALP #phi",                                       "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "n_FSGenElectron":                                  {"name":"n_FSGenElectron",                                  "title":"Number of final state gen electrons",                    "bin":7,   "xmin":-0.5,  "xmax":6.5},
    "n_FSGenPhoton":                                    {"name":"n_FSGenPhoton",                                    "title":"Number of final state gen photons",                      "bin":9,   "xmin":-0.5,  "xmax":8.5},
    "FSGenElectron_e":                                  {"name":"FSGenElectron_e",                                  "title":"Final state gen electrons energy [GeV]",                 "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectron_p":                                  {"name":"FSGenElectron_p",                                  "title":"Final state gen electrons p [GeV]",                      "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectron_pt":                                 {"name":"FSGenElectron_pt",                                 "title":"Final state gen electrons p_{T} [GeV]",                  "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectron_pz":                                 {"name":"FSGenElectron_pz",                                 "title":"Final state gen electrons p_{z} [GeV]",                  "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectron_eta":                                {"name":"FSGenElectron_eta",                                "title":"Final state gen electrons #eta",                         "bin":60,  "xmin":-3,    "xmax":3},
    "FSGenElectron_theta":                              {"name":"FSGenElectron_theta",                              "title":"Final state gen electrons #theta",                       "bin":64,  "xmin":0,     "xmax":3.2},
    "FSGenElectron_phi":                                {"name":"FSGenElectron_phi",                                "title":"Final state gen electrons #phi",                         "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "FSGenElectronPositron_e":                          {"name":"FSGenElectronPositron_e",                          "title":"Final state gen e energy [GeV]",                         "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectronPositron_p":                          {"name":"FSGenElectronPositron_p",                          "title":"Final state gen e p [GeV]",                              "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectronPositron_pt":                         {"name":"FSGenElectronPositron_pt",                         "title":"Final state gen e p_{T} [GeV]",                          "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectronPositron_pz":                         {"name":"FSGenElectronPositron_pz",                         "title":"Final state gen e p_{z} [GeV]",                          "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectronPositron_py":                         {"name":"FSGenElectronPositron_py",                         "title":"Final state gen e p_{y} [GeV]",                          "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectronPositron_px":                         {"name":"FSGenElectronPositron_px",                         "title":"Final state gen e p_{x} [GeV]",                          "bin":100, "xmin":0,     "xmax":90},
    "FSGenElectronPositron_eta":                        {"name":"FSGenElectronPositron_eta",                        "title":"Final state gen e #eta",                                 "bin":60,  "xmin":-3,    "xmax":3},
    "FSGenElectronPositron_theta":                      {"name":"FSGenElectronPositron_theta",                      "title":"Final state gen e #theta",                               "bin":64,  "xmin":0,     "xmax":3.2},
    "FSGenElectronPositron_phi":                        {"name":"FSGenElectronPositron_phi",                        "title":"Final state gen e #phi",                                 "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "FSGenALP_p":                                       {"name":"FSGenALP_p",                                       "title":"Final state gen ALP p [GeV]",                            "bin":100, "xmin":0,     "xmax":50},
    "FSGenPhoton_e":                                    {"name":"FSGenPhoton_e",                                    "title":"Final state gen photons energy [GeV]",                   "bin":100, "xmin":0,     "xmax":50},
    "FSGenPhoton_p":                                    {"name":"FSGenPhoton_p",                                    "title":"Final state gen photons p [GeV]",                        "bin":100, "xmin":0,     "xmax":50},
    "FSGenPhoton_pt":                                   {"name":"FSGenPhoton_pt",                                   "title":"Final state gen photons p_{T} [GeV]",                    "bin":100, "xmin":0,     "xmax":50},
    "FSGenPhoton_pz":                                   {"name":"FSGenPhoton_pz",                                   "title":"Final state gen photons p_{z} [GeV]",                    "bin":100, "xmin":0,     "xmax":50},
    "FSGenPhoton_eta":                                  {"name":"FSGenPhoton_eta",                                  "title":"Final state gen photons #eta",                           "bin":60,  "xmin":-3,    "xmax":3},
    "FSGenPhoton_theta":                                {"name":"FSGenPhoton_theta",                                "title":"Final state gen photons #theta",                         "bin":64,  "xmin":0,     "xmax":3.2},
    "FSGenPhoton_phi":                                  {"name":"FSGenPhoton_phi",                                  "title":"Final state gen photons #phi",                           "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "FSGenPhoton0_e":                                   {"name":"FSGenPhoton0_e",                                   "title":"Final state gen photon_{0} energy [GeV]",                "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_e":                                   {"name":"FSGenPhoton1_e",                                   "title":"Final state gen photon_{1} energy [GeV]",                "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton2_e":                                   {"name":"FSGenPhoton2_e",                                   "title":"Final state gen photon_{2} energy [GeV]",                "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton0_p":                                   {"name":"FSGenPhoton0_p",                                   "title":"Final state gen photon_{0} p [GeV]",                     "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_p":                                   {"name":"FSGenPhoton1_p",                                   "title":"Final state gen photon_{1} p [GeV]",                     "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton2_p":                                   {"name":"FSGenPhoton2_p",                                   "title":"Final state gen photon_{2} p [GeV]",                     "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton0_pt":                                  {"name":"FSGenPhoton0_pt",                                  "title":"Final state gen photon_{0} p_{T} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_pt":                                  {"name":"FSGenPhoton1_pt",                                  "title":"Final state gen photon_{1} p_{T} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton2_pt":                                  {"name":"FSGenPhoton2_pt",                                  "title":"Final state gen photon_{2} p_{T} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton0_px":                                  {"name":"FSGenPhoton0_px",                                  "title":"Final state gen photon_{0} p_{x} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_px":                                  {"name":"FSGenPhoton1_px",                                  "title":"Final state gen photon_{1} p_{x} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton2_px":                                  {"name":"FSGenPhoton2_px",                                  "title":"Final state gen photon_{2} p_{x} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton0_py":                                  {"name":"FSGenPhoton0_py",                                  "title":"Final state gen photon_{0} p_{y} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_py":                                  {"name":"FSGenPhoton1_py",                                  "title":"Final state gen photon_{1} p_{y} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton2_py":                                  {"name":"FSGenPhoton2_py",                                  "title":"Final state gen photon_{2} p_{y} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton0_pz":                                  {"name":"FSGenPhoton0_pz",                                  "title":"Final state gen photon_{0} p_{z} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_pz":                                  {"name":"FSGenPhoton1_pz",                                  "title":"Final state gen photon_{1} p_{z} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton2_pz":                                  {"name":"FSGenPhoton2_pz",                                  "title":"Final state gen photon_{2} p_{z} [GeV]",                 "bin":100, "xmin":-3.2,  "xmax":50},
    "FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0": {"name":"FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0", "title":"FS gen photon_{1} p_{x} if FS gen photon_{0} p_{x} > 0", "bin":100, "xmin":-55,   "xmax":50},
    "FSGenPhoton1_px_if_FSGenPhoton2_px_pos":           {"name":"FSGenPhoton1_px_if_FSGenPhoton2_px_pos",           "title":"FS gen photon_{1} p_{x} if FS gen photon_{2} p_{x} > 0", "bin":100, "xmin":-55,   "xmax":50},
    "FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos":           {"name":"FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos",           "title":"FS gen photon_{1} p_{z} if FS gen photon_{2} p_{z} > 0", "bin":100, "xmin":-55,   "xmax":50},
    "FSGenPhoton_vertex_x":                             {"name":"FSGenPhoton_vertex_x",                             "title":"Final state gen photon production vertex x [mm]",        "bin":100, "xmin":-1000, "xmax":1000},
    "FSGenPhoton_vertex_y":                             {"name":"FSGenPhoton_vertex_y",                             "title":"Final state gen photon production vertex y [mm]",        "bin":100, "xmin":-1000, "xmax":1000},
    "FSGenPhoton_vertex_z":                             {"name":"FSGenPhoton_vertex_z",                             "title":"Final state gen photon production vertex z [mm]",        "bin":100, "xmin":-1000, "xmax":1000},
    "FSGenALP_mass":                                    {"name":"FSGenALP_mass",                                    "title":"FS gen ALP mass [GeV]",                                  "bin":100, "xmin":0,     "xmax":50},
    "GenALP_mass":                                      {"name":"GenALP_mass",                                      "title":"Gen ALP mass [GeV]",                                     "bin":100, "xmin":0,     "xmax":50},
    "GenALP_e":                                         {"name":"GenALP_e",                                         "title":"Gen ALP energy [GeV]",                                   "bin":100, "xmin":0,     "xmax":50},
    "GenALP_p":                                         {"name":"GenALP_p",                                         "title":"Gen ALP p [GeV]",                                        "bin":100, "xmin":0,     "xmax":50},
    "GenALP_pt":                                        {"name":"GenALP_pt",                                        "title":"Gen ALP p_{T} [GeV]",                                    "bin":100, "xmin":0,     "xmax":50},
    "GenALP_pz":                                        {"name":"GenALP_pz",                                        "title":"Gen ALP p_{z} [GeV]",                                    "bin":100, "xmin":0,     "xmax":50},
    "GenALP_eta":                                       {"name":"GenALP_eta",                                       "title":"Gen ALP #eta",                                           "bin":60,  "xmin":-3,    "xmax":3},
    "GenALP_theta":                                     {"name":"GenALP_theta",                                     "title":"Gen ALP #theta",                                         "bin":64,  "xmin":0,     "xmax":3.2},
    "GenALP_phi":                                       {"name":"GenALP_phi",                                       "title":"Gen ALP #phi",                                           "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "GenALP_beta":                                      {"name":"GenALP_beta",                                      "title":"Gen #beta_{ALP}",                                        "bin":150, "xmin":0,     "xmax":1.5},
    "GenALP_lifetime_xy":                               {"name":"GenALP_lifetime_xy",                               "title":"Gen ALP #tau_{xy} [s]",                                  "bin":100, "xmin":0,     "xmax":1E-11},
    "GenALP_lifetime_xyz":                              {"name":"GenALP_lifetime_xyz",                              "title":"Gen ALP #tau_{xyz} [s]",                                 "bin":100, "xmin":0,     "xmax":1E-11},
    "GenALP_Lxy":                                       {"name":"GenALP_Lxy",                                       "title":"Gen ALP L_{xy} [mm]",                                    "bin":100, "xmin":0,     "xmax":100},
    "GenALP_Lxyz":                                      {"name":"GenALP_Lxyz",                                      "title":"Gen ALP L_{xyz} [mm]",                                   "bin":200, "xmin":0,     "xmax":100},
    "GenALP_vertex_x":                                  {"name":"GenALP_vertex_x",                                  "title":"Gen ALP production vertex x [mm]",                       "bin":100, "xmin":-1000, "xmax":1000},
    "GenALP_vertex_y":                                  {"name":"GenALP_vertex_y",                                  "title":"Gen ALP production vertex y [mm]",                       "bin":100, "xmin":-1000, "xmax":1000},
    "GenALP_vertex_z":                                  {"name":"GenALP_vertex_z",                                  "title":"Gen ALP production vertex z [mm]",                       "bin":100, "xmin":-1000, "xmax":1000},
    "GenALP_px_if_FSGenPhoton0_px_greaterthan_0":       {"name":"GenALP_px_if_FSGenPhoton0_px_greaterthan_0",       "title":"Gen ALP p_{x} if FS gen photon_{0} p_{x} > 0",           "bin":100, "xmin":-55,   "xmax":50},
    "FSGenPhoton1_px_if_GenALP_px_neg":                 {"name":"FSGenPhoton1_px_if_GenALP_px_neg",                 "title":"FS gen photon_{1} p_{x} if gen ALP p_{x} < 0",           "bin":100, "xmin":-55,   "xmax":50},
    "FSGenPhoton2_px_if_GenALP_px_neg":                 {"name":"FSGenPhoton2_px_if_GenALP_px_neg",                 "title":"FS gen photon_{2} p_{x} if gen ALP p_{x} < 0",           "bin":100, "xmin":-55,   "xmax":50},
    "n_GenALP":                                         {"name":"n_GenALP",                                         "title":"Number of gen ALPs",                                     "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "n_GenALPPhoton1":                                  {"name":"n_GenALPPhoton1",                                  "title":"Number of gen photon_{1}",                               "bin":100, "xmin":-0.5,  "xmax":4.5},
    "n_GenALPPhoton2":                                  {"name":"n_GenALPPhoton2",                                  "title":"Number of gen photon_{2}",                               "bin":100, "xmin":-0.5,  "xmax":4.5},
    "GenALP_time":                                      {"name":"GenALP_time",                                      "title":"Gen ALP time [s]",                                       "bin":100, "xmin":0,     "xmax":5E-24},
    "GenALP_pdg":                                       {"name":"GenALP_pdg",                                       "title":"Gen ALP pdg",                                            "bin":100, "xmin":-10,   "xmax":10},
    "GenALPPhotons_deltaEta":                           {"name":"GenALPPhotons_deltaEta",                           "title":"Gen ALP photons #Delta#eta",                             "bin":100, "xmin":0,     "xmax":8},
    "GenALPPhotons_deltaPhi":                           {"name":"GenALPPhotons_deltaPhi",                           "title":"Gen ALP photons #Delta#phi",                             "bin":100, "xmin":0,     "xmax":8},
    "GenALPPhotons_deltaR":                             {"name":"GenALPPhotons_deltaR",                             "title":"Gen ALP photons #DeltaR",                                "bin":100, "xmin":0,     "xmax":8},
    "FSGenPhotons_delta_r":                             {"name":"FSGenPhotons_delta_r",                             "title":"Final state gen photons #DeltaR",                        "bin":100, "xmin":0,     "xmax":7},
    "FSGenPhotons_min_delta_r":                         {"name":"FSGenPhotons_min_delta_r",                         "title":"Final state gen photons minimum #DeltaR",                "bin":100, "xmin":0,     "xmax":7},
    "GenALPPhoton1_e":                                  {"name":"GenALPPhoton1_e",                                  "title":"Gen photon_{1} energy [GeV]",                            "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton2_e":                                  {"name":"GenALPPhoton2_e",                                  "title":"Gen photon_{2} energy [GeV]",                            "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton1_p":                                  {"name":"GenALPPhoton1_p",                                  "title":"Gen photon_{1} p [GeV]",                                 "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton2_p":                                  {"name":"GenALPPhoton2_p",                                  "title":"Gen photon_{2} p [GeV]",                                 "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton1_pt":                                 {"name":"GenALPPhoton1_pt",                                 "title":"Gen photon_{1} p_{T} [GeV]",                             "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton2_pt":                                 {"name":"GenALPPhoton2_pt",                                 "title":"Gen photon_{2} p_{T} [GeV]",                             "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton1_pz":                                 {"name":"GenALPPhoton1_pz",                                 "title":"Gen photon_{1} p_{z} [GeV]",                             "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton2_pz":                                 {"name":"GenALPPhoton2_pz",                                 "title":"Gen photon_{2} p_{z} [GeV]",                             "bin":100, "xmin":0,     "xmax":50},
    "GenALPPhoton1_eta":                                {"name":"GenALPPhoton1_eta",                                "title":"Gen photon_{1} #eta",                                    "bin":60,  "xmin":-3,    "xmax":3},
    "GenALPPhoton2_eta":                                {"name":"GenALPPhoton2_eta",                                "title":"Gen photon_{2} #eta",                                    "bin":60,  "xmin":-3,    "xmax":3},
    "GenALPPhoton1_theta":                              {"name":"GenALPPhoton1_theta",                              "title":"Gen photon_{1} #theta",                                  "bin":64,  "xmin":0,     "xmax":3.2},
    "GenALPPhoton2_theta":                              {"name":"GenALPPhoton2_theta",                              "title":"Gen photon_{2} #theta",                                  "bin":64,  "xmin":0,     "xmax":3.2},
    "GenALPPhoton2_phi":                                {"name":"GenALPPhoton2_phi",                                "title":"Gen photon_{2} #phi",                                    "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "GenALPPhoton2_time":                               {"name":"GenALPPhoton2_time",                               "title":"Gen photon_{2} time [s]",                                "bin":100, "xmin":0,     "xmax":250E-14},
    "GenALP_observed_lifetime_xyz":                     {"name":"GenALP_observed_lifetime_xyz",                     "title":"Gen ALP #tau_{xyz,lab} [s]",                             "bin":100, "xmin":0,     "xmax":1E-12},
    "GenALPPhoton1_vertex_x":                           {"name":"GenALPPhoton1_vertex_x",                           "title":"Gen photon_{1} production vertex x [mm]",                "bin":100, "xmin":-1000, "xmax":1000},
    "GenALPPhoton1_vertex_y":                           {"name":"GenALPPhoton1_vertex_y",                           "title":"Gen photon_{1} production vertex y [mm]",                "bin":100, "xmin":-1000, "xmax":1000},
    "GenALPPhoton1_vertex_z":                           {"name":"GenALPPhoton1_vertex_z",                           "title":"Gen photon_{1} production vertex z [mm]",                "bin":100, "xmin":-1000, "xmax":1000},
    "GenALP_aa_invMass":                                {"name":"GenALP_aa_invMass",                                "title":"Gen m_{#gamma#gamma} (from ALP) [GeV]",                  "bin":100, "xmin":0,     "xmax":50},
    "n_RecoTracks":                                     {"name":"n_RecoTracks",                                     "title":"Total number of reco tracks",                            "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "n_RecoALPTracks":                                  {"name":"n_RecoALPTracks",                                  "title":"Number of reco ALP tracks",                              "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "RecoALP_DecayVertex_x":                            {"name":"RecoALPDecayVertex.position.x",                    "title":"Reco ALP decay vertex x [mm]",                           "bin":100, "xmin":-1000, "xmax":1000},
    "RecoALP_DecayVertex_y":                            {"name":"RecoALPDecayVertex.position.y",                    "title":"Reco ALP decay vertex y [mm]",                           "bin":100, "xmin":-1000, "xmax":1000},
    "RecoALP_DecayVertex_z":                            {"name":"RecoALPDecayVertex.position.z",                    "title":"Reco ALP decay vertex z [mm]",                           "bin":100, "xmin":-1000, "xmax":1000},
    "RecoALPPhoton1_e":                                 {"name":"RecoALPPhoton1_e",                                 "title":"Reco photon_{1} (from ALP) energy [GeV]",                "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton2_e":                                 {"name":"RecoALPPhoton2_e",                                 "title":"Reco photon_{2} (from ALP) energy [GeV]",                "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton1_p":                                 {"name":"RecoALPPhoton1_p",                                 "title":"Reco photon_{1} (from ALP) p [GeV]",                     "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton2_p":                                 {"name":"RecoALPPhoton2_p",                                 "title":"Reco photon_{2} (from ALP) p GeV]",                      "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton1_pt":                                {"name":"RecoALPPhoton1_pt",                                "title":"Reco photon_{1} (from ALP) p_{T} [GeV]",                 "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton2_pt":                                {"name":"RecoALPPhoton2_pt",                                "title":"Reco photon_{2} (from ALP) p_{T} [GeV]",                 "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton1_pz":                                {"name":"RecoALPPhoton1_pz",                                "title":"Reco photon_{1} (from ALP) p_{z} [GeV]",                 "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton2_pz":                                {"name":"RecoALPPhoton2_pz",                                "title":"Reco photon_{2} (from ALP) p_{z} [GeV]",                 "bin":100, "xmin":0,     "xmax":50},
    "RecoALPPhoton1_eta":                               {"name":"RecoALPPhoton1_eta",                               "title":"Reco photon_{1} (from ALP) #eta",                        "bin":60,  "xmin":-3,    "xmax":3},
    "RecoALPPhoton2_eta":                               {"name":"RecoALPPhoton2_eta",                               "title":"Reco photon_{2} (from ALP) #eta",                        "bin":60,  "xmin":-3,    "xmax":3},
    "RecoALPPhoton1_theta":                             {"name":"RecoALPPhoton1_theta",                             "title":"Reco photon_{1} (from ALP) #theta",                      "bin":64,  "xmin":0,     "xmax":3.2},
    "RecoALPPhoton2_theta":                             {"name":"RecoALPPhoton2_theta",                             "title":"Reco photon_{2} (from ALP) #theta",                      "bin":64,  "xmin":0,     "xmax":3.2},
    "RecoALPPhoton1_phi":                               {"name":"RecoALPPhoton1_phi",                               "title":"Reco photon_{1} (from ALP) #phi",                        "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "RecoALPPhoton2_phi":                               {"name":"RecoALPPhoton2_phi",                               "title":"Reco photon_{2} (from ALP) #phi",                        "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "RecoALPPhoton1_charge":                            {"name":"RecoALPPhoton1_charge",                            "title":"Reco photon_{1} (from ALP) charge",                      "bin":3,   "xmin":-1.5,  "xmax":1.5},
    "RecoALPPhoton2_charge":                            {"name":"RecoALPPhoton2_charge",                            "title":"Reco photon_{2} (from ALP) charge",                      "bin":3,   "xmin":-1.5,  "xmax":1.5},
    "RecoALPPhotons_deltaEta":                          {"name":"RecoALPPhotons_deltaEta",                          "title":"Reco photons (from ALP) #Delta#eta",                     "bin":60,  "xmin":-2,    "xmax":8},
    "RecoALPPhotons_deltaPhi":                          {"name":"RecoALPPhotons_deltaPhi",                          "title":"Reco photons (from ALP) #Delta#phi",                     "bin":60,  "xmin":-2,    "xmax":8},
    "RecoALPPhotons_deltaR":                            {"name":"RecoALPPhotons_deltaR",                            "title":"Reco photons (from ALP) #DeltaR",                        "bin":60,  "xmin":-3,    "xmax":8},
    "n_RecoALPPhoton1":                                 {"name":"n_RecoALPPhoton1",                                 "title":"Number of reco photon_{1} (from ALP)",                   "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "n_RecoALPPhoton2":                                 {"name":"n_RecoALPPhoton2",                                 "title":"Number of reco photon_{2} (from ALP)",                   "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "Reco_aa_invMass":                                  {"name":"Reco_aa_invMass",                                  "title":"Reco photon m_{#gamma#gamma} [GeV]",                     "bin":100, "xmin":0,     "xmax":380},
    "Reco_aa_p":                                        {"name":"Reco_aa_p",                                        "title":"Reco photon p_{#gamma#gamma} [GeV]",                     "bin":60,  "xmin":0,     "xmax":60},
    "RecoALP_aa_invMass":                               {"name":"RecoALP_aa_invMass",                               "title":"Reco m_{#gamma#gamma} (from ALP) [GeV]",                 "bin":100, "xmin":0,     "xmax":100},
    "RecoALP_aa_p":                                     {"name":"RecoALP_aa_p",                                     "title":"Reco p_{#gamma#gamma} (from ALP) [GeV]",                 "bin":60,  "xmin":0,     "xmax":60},
    "RecoALP_aa_energy":                                {"name":"RecoALP_aa_energy",                                "title":"Reco energy_{#gamma#gamma} (from ALP) [GeV]",            "bin":60,  "xmin":0,     "xmax":60},
    "n_RecoJets":                                       {"name":"n_RecoJets",                                       "title":"Total number of reco jets",                              "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "n_RecoPhotons":                                    {"name":"n_RecoPhotons",                                    "title":"Total number of reco photons",                           "bin":9,   "xmin":-0.5,  "xmax":8.5},
    "n_RecoElectrons":                                  {"name":"n_RecoElectrons",                                  "title":"Total number of reco electrons",                         "bin":7,   "xmin":-0.5,  "xmax":6.5},
    "n_RecoMuons":                                      {"name":"n_RecoMuons",                                      "title":"Total number of reco muons",                             "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "RecoElectron_e":                                   {"name":"RecoElectron_e",                                   "title":"Reco electron energy [GeV]",                             "bin":100, "xmin":0,     "xmax":90},
    "RecoElectron_p":                                   {"name":"RecoElectron_p",                                   "title":"Reco electron p [GeV]",                                  "bin":100, "xmin":0,     "xmax":90},
    "RecoElectron_pt":                                  {"name":"RecoElectron_pt",                                  "title":"Reco electron p_{T} [GeV]",                              "bin":100, "xmin":0,     "xmax":90},
    "RecoElectron_pz":                                  {"name":"RecoElectron_pz",                                  "title":"Reco electron p_{z} [GeV]",                              "bin":100, "xmin":0,     "xmax":90},
    "RecoElectron_eta":                                 {"name":"RecoElectron_eta",                                 "title":"Reco electron #eta",                                     "bin":60,  "xmin":-3,    "xmax":3},
    "RecoElectron_theta":                               {"name":"RecoElectron_theta",                               "title":"Reco electron #theta",                                   "bin":64,  "xmin":0,     "xmax":3.2},
    "RecoElectron_phi":                                 {"name":"RecoElectron_phi",                                 "title":"Reco electron #phi",                                     "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "RecoPhoton_e":                                     {"name":"RecoPhoton_e",                                     "title":"Reco photon energy [GeV]",                               "bin":100, "xmin":0,     "xmax":120},
    "RecoPhoton_p":                                     {"name":"RecoPhoton_p",                                     "title":"Reco photon p [GeV]",                                    "bin":100, "xmin":0,     "xmax":50},
    "RecoPhoton_pt":                                    {"name":"RecoPhoton_pt",                                    "title":"Reco photon p_{T} [GeV]",                                "bin":100, "xmin":0,     "xmax":50},
    "RecoPhoton_pz":                                    {"name":"RecoPhoton_pz",                                    "title":"Reco photon p_{z} [GeV]",                                "bin":100, "xmin":0,     "xmax":50},
    "RecoPhoton_eta":                                   {"name":"RecoPhoton_eta",                                   "title":"Reco photon #eta",                                       "bin":60,  "xmin":-3,    "xmax":3},
    "RecoPhoton_theta":                                 {"name":"RecoPhoton_theta",                                 "title":"Reco photon #theta",                                     "bin":64,  "xmin":0,     "xmax":3.2},
    "RecoPhoton_phi":                                   {"name":"RecoPhoton_phi",                                   "title":"Reco photon #phi",                                       "bin":64,  "xmin":-3.2,  "xmax":3.2},
    "RecoPhoton_charge":                                {"name":"RecoPhoton_charge",                                "title":"Charge of reco photons",                                 "bin":3,   "xmin":-1.5,  "xmax":1.5},
    "RecoPhotons_delta_eta":                            {"name":"RecoPhotons_delta_eta",                            "title":"Reco photons #Delta#eta",                                "bin":100, "xmin":0,     "xmax":10},
    "RecoPhotons_delta_phi":                            {"name":"RecoPhotons_delta_phi",                            "title":"Reco photons #Delta#phi",                                "bin":100, "xmin":0,     "xmax":10},
    "RecoPhotons_delta_r":                              {"name":"RecoPhotons_delta_r",                              "title":"Reco photons #DeltaR",                                   "bin":100, "xmin":0,     "xmax":7},
    "RecoPhotons_min_delta_r":                          {"name":"RecoPhotons_min_delta_r",                          "title":"Reco photons minimum #DeltaR",                           "bin":100, "xmin":0,     "xmax":7},
    "RecoPhoton0_e":                                    {"name":"RecoPhoton0_e",                                    "title":"Reco photon_{0} energy [GeV]",                           "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_e":                                    {"name":"RecoPhoton1_e",                                    "title":"Reco photon_{1} energy [GeV]",                           "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton2_e":                                    {"name":"RecoPhoton2_e",                                    "title":"Reco photon_{2} energy [GeV]",                           "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton0_p":                                    {"name":"RecoPhoton0_p",                                    "title":"Reco photon_{0} p [GeV]",                                "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_p":                                    {"name":"RecoPhoton1_p",                                    "title":"Reco photon_{1} p [GeV]",                                "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton2_p":                                    {"name":"RecoPhoton2_p",                                    "title":"Reco photon_{2} p [GeV]",                                "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton0_pt":                                   {"name":"RecoPhoton0_pt",                                   "title":"Reco photon_{0} p_{T} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_pt":                                   {"name":"RecoPhoton1_pt",                                   "title":"Reco photon_{1} p_{T} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton2_pt":                                   {"name":"RecoPhoton2_pt",                                   "title":"Reco photon_{2} p_{T} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton0_px":                                   {"name":"RecoPhoton0_px",                                   "title":"Reco photon_{0} p_{x} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_px":                                   {"name":"RecoPhoton1_px",                                   "title":"Reco photon_{1} p_{x} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton2_px":                                   {"name":"RecoPhoton2_px",                                   "title":"Reco photon_{2} p_{x} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton0_py":                                   {"name":"RecoPhoton0_py",                                   "title":"Reco photon_{0} p_{y} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_py":                                   {"name":"RecoPhoton1_py",                                   "title":"Reco photon_{1} p_{y} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton2_py":                                   {"name":"RecoPhoton2_py",                                   "title":"Reco photon_{2} p_{y} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton0_pz":                                   {"name":"RecoPhoton0_pz",                                   "title":"Reco photon_{0} p_{z} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_pz":                                   {"name":"RecoPhoton1_pz",                                   "title":"Reco photon_{1} p_{z} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton2_pz":                                   {"name":"RecoPhoton2_pz",                                   "title":"Reco photon_{2} p_{z} [GeV]",                            "bin":100, "xmin":-3.2,  "xmax":50},
    "RecoPhoton1_px_if_RecoPhoton2_px_pos":             {"name":"RecoPhoton1_px_if_RecoPhoton2_px_pos",             "title":"Reco photon_{1} p_{x} if reco photon_{2} p_{x} > 0",     "bin":100, "xmin":-55,   "xmax":50},
    "RecoPhoton1_pz_if_RecoPhoton2_pz_pos":             {"name":"RecoPhoton1_pz_if_RecoPhoton2_pz_pos",             "title":"Reco photon_{1} p_{z} if reco photon_{2} p_{z} > 0",     "bin":100, "xmin":-55,   "xmax":50},
    "RecoALPPhotons_delta_R3":                          {"name":"RecoALPPhotons_delta_R3",                          "title":"Reco ALP photons #DeltaR_{3}",                           "bin":60,  "xmin":-3,    "xmax":8},
    "GenMinusRecoALPPhoton1_e":                         {"name":"GenMinusRecoALPPhoton1_e",                         "title":"Gen photon_{1} energy - Reco photon_{1} energy [GeV]",   "bin":100, "xmin":-5,    "xmax":5},
    "GenMinusRecoALPPhoton2_e":                         {"name":"GenMinusRecoALPPhoton2_e",                         "title":"Gen photon_{2} energy - Reco photon_{2} energy [GeV]",   "bin":100, "xmin":-5,    "xmax":5},
    "GenMinusRecoALP_DecayVertex_x":                    {"name":"GenMinusRecoALP_DecayVertex_x",                    "title":"Gen ALP decay vertex x - Reco ALP decay vertex x [mm]",  "bin":100, "xmin":-1000, "xmax":1000},
    "GenMinusRecoALP_DecayVertex_y":                    {"name":"GenMinusRecoALP_DecayVertex_y",                    "title":"Gen ALP decay vertex y - Reco ALP decay vertex y [mm]",  "bin":100, "xmin":-1000, "xmax":1000},
    "GenMinusRecoALP_DecayVertex_z":                    {"name":"GenMinusRecoALP_DecayVertex_z",                    "title":"Gen ALP decay vertex z - Reco ALP decay vertex z [mm]",  "bin":100, "xmin":-1000, "xmax":1000},
}

