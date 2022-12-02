import ROOT

# global parameters
intLumi        = 5.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'e^{+}e^{-} #rightarrow Z h, Z #rightarrow l^{+}l^{-}, h #rightarrow ss #rightarrow b #bar{b} b #bar{b}'
delphesVersion = '3.4.2'
energy         = 240
collider       = 'FCC-ee'
inputDir       = 'Reco_output_finalSel/'
#formats        = ['png','pdf']
formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'Reco_plots/'
splitLeg       = True

variables = [

    #gen variables
    'n_RecoElectrons',
    'n_RecoMuons',
    "Reco_ee_invMass",
    "Reco_mumu_invMass",
    "n_RecoedPrimaryTracks",
    "n_SecondaryTracks",
    # 'invMass_SVs',
    # "SV_evt1_n",
    # 'n_trks_SVs',
    # "Reco_SVs_Lxy",
    # "Reco_SVs_Lxyz",
    # 'invMass_SVs_seltracks_pt',
    # "SV_evt_seltracks_pt_n",
    # 'n_trks_SVs_seltracks_pt',
    # "Reco_SVs_seltracks_Lxy",
    # "Reco_SVs_seltracks_Lxyz",
    # 'invMass_merged_SVs_pt',
    # "merged_SVs_pt_n",
    # 'n_trks_merged_SVs_pt',
    # "Reco_SVs_merged_pt_Lxy",
    # "Reco_SVs_merged_pt_Lxyz",
    'invMass_merged_SVs',
    "merged_SVs_n",
    'n_trks_merged_SVs',
    "Reco_SVs_merged_Lxy",
    "Reco_SVs_merged_Lxyz",
    "jets_ee_kt_m",
    
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['ExoticHiggs']  = [
    "selNone",
]

extralabel = {}
extralabel['selNone'] = "Before selection"

colors = {}
colors['exoticHiggs_scalar_ms20GeV_sine-5'] = ROOT.kOrange+1
colors['exoticHiggs_scalar_ms20GeV_sine-6'] = ROOT.kRed
colors['exoticHiggs_scalar_ms20GeV_sine-7'] = ROOT.kBlue
colors['exoticHiggs_scalar_ms60GeV_sine-5'] = ROOT.kGreen+1
colors['exoticHiggs_scalar_ms60GeV_sine-6'] = ROOT.kCyan-9
colors['exoticHiggs_scalar_ms60GeV_sine-7'] = ROOT.kViolet-4

plots = {}
plots['ExoticHiggs'] = {'signal':{
                    'exoticHiggs_scalar_ms20GeV_sine-5':['exoticHiggs_scalar_ms20GeV_sine-5'],
                    'exoticHiggs_scalar_ms20GeV_sine-6':['exoticHiggs_scalar_ms20GeV_sine-6'],
                    'exoticHiggs_scalar_ms20GeV_sine-7':['exoticHiggs_scalar_ms20GeV_sine-7'],
                    'exoticHiggs_scalar_ms60GeV_sine-5':['exoticHiggs_scalar_ms60GeV_sine-5'],
                    'exoticHiggs_scalar_ms60GeV_sine-6':['exoticHiggs_scalar_ms60GeV_sine-6'],
                    'exoticHiggs_scalar_ms60GeV_sine-7':['exoticHiggs_scalar_ms60GeV_sine-7'],
},
'backgrounds':{
            #
                }
                }


legend = {}
legend['exoticHiggs_scalar_ms20GeV_sine-5'] = 'm_{S} = 20 GeV, sin #theta = 1e-5'
legend['exoticHiggs_scalar_ms20GeV_sine-6'] = 'm_{S} = 20 GeV, sin #theta = 1e-6'
legend['exoticHiggs_scalar_ms20GeV_sine-7'] = 'm_{S} = 20 GeV, sin #theta = 1e-7'
legend['exoticHiggs_scalar_ms60GeV_sine-5'] = 'm_{S} = 60 GeV, sin #theta = 1e-5'
legend['exoticHiggs_scalar_ms60GeV_sine-6'] = 'm_{S} = 60 GeV, sin #theta = 1e-6'
legend['exoticHiggs_scalar_ms60GeV_sine-7'] = 'm_{S} = 60 GeV, sin #theta = 1e-7'
