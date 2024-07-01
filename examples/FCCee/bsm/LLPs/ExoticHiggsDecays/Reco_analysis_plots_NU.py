import ROOT

### NOTE: plots won't be legible / won't fit including all signals and backgrounds, so some will need to be commented out before running to use plots

# global parameters
intLumi        = 5.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'e^{+}e^{-} #rightarrow Z h, Z #rightarrow nu nu, h #rightarrow ss #rightarrow b #bar{b} b #bar{b}'
delphesVersion = '3.4.2'
energy         = 240
collider       = 'FCC-ee'
inputDir       = 'Reco_output_final_NU/'
#formats        = ['png','pdf']
formats        = ['pdf']
# yaxis          = ['lin','log']
yaxis          = ['log']
stacksig       = ['nostack']
outdir         = 'Reco_plots_NU/'
splitLeg       = True

variables = [

    #gen variables
    "n_tracks",
    "n_RecoedPrimaryTracks",
    'n_seltracks_DVs',
    'n_trks_seltracks_DVs',
    'invMass_seltracks_DVs',
    "DV_evt_seltracks_chi2",
    "Reco_seltracks_DVs_Lxy",
    "Reco_seltracks_DVs_Lxyz",
    "DV_evt_seltracks_normchi2",
    "merged_DVs_n",
    'n_trks_merged_DVs',
    'invMass_merged_DVs',
    "merged_DVs_chi2",
    "merged_DVs_normchi2",
    "Reco_DVs_merged_Lxy",
    "Reco_DVs_merged_Lxyz",
    "RecoMissingEnergy_e_sum",
    "RecoMissingEnergy_p_sum",
    "RecoMissingEnergy_pt_sum",
    "RecoMissingEnergy_px_sum",
    "RecoMissingEnergy_py_sum",
    "RecoMissingEnergy_pz_sum",
    "RecoMissingEnergy_eta_sum",
    "RecoMissingEnergy_theta_sum",
    "RecoMissingEnergy_phi_sum"
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['ExoticHiggs']  = [
    #"selNone",
    "preSel",
    "preSel+nDVs_seltracks",
    "preSel+nDVs_merge"
]

extralabel = {}
#extralabel['selNone'] = "Before selection"
extralabel['preSel'] = "30 < Missing energy < 70 GeV"
extralabel['preSel+nDVs_seltracks'] = ">= 2 DVs"
extralabel['preSel+nDVs_merge'] = ">= 2 Merged DVs"

colors = {}
colors['exoticHiggs_scalar_ms20GeV_sine-5_NU'] = ROOT.kRed
colors['exoticHiggs_scalar_ms20GeV_sine-6_NU'] = ROOT.kBlue
colors['exoticHiggs_scalar_ms20GeV_sine-7_NU'] = ROOT.kGreen
colors['exoticHiggs_scalar_ms60GeV_sine-5_NU'] = ROOT.kBlack
colors['exoticHiggs_scalar_ms60GeV_sine-6_NU'] = ROOT.kOrange+1
colors['exoticHiggs_scalar_ms60GeV_sine-7_NU'] = ROOT.kViolet-4

colors['p8_ee_WW_ecm240'] = ROOT.kAzure
colors['p8_ee_ZZ_ecm240'] = ROOT.kCyan
colors['wzp6_ee_nunuH_Hbb_ecm240'] = ROOT.kGray
colors['wzp6_ee_nunuH_HWW_ecm240'] = ROOT.kRed-4

plots = {}
plots['ExoticHiggs'] = {'signal':{
                    'exoticHiggs_scalar_ms20GeV_sine-5_NU':['exoticHiggs_scalar_ms20GeV_sine-5_NU'],
                    'exoticHiggs_scalar_ms20GeV_sine-6_NU':['exoticHiggs_scalar_ms20GeV_sine-6_NU'],
                    'exoticHiggs_scalar_ms20GeV_sine-7_NU':['exoticHiggs_scalar_ms20GeV_sine-7_NU'],
                    'exoticHiggs_scalar_ms60GeV_sine-5_NU':['exoticHiggs_scalar_ms60GeV_sine-5_NU'],
                    'exoticHiggs_scalar_ms60GeV_sine-6_NU':['exoticHiggs_scalar_ms60GeV_sine-6_NU'],
                    'exoticHiggs_scalar_ms60GeV_sine-7_NU':['exoticHiggs_scalar_ms60GeV_sine-7_NU']
},
'backgrounds':{
            'p8_ee_WW_ecm240':['p8_ee_ZZ_ecm240'],
            'p8_ee_ZZ_ecm240':['p8_ee_WW_ecm240'],
            'wzp6_ee_nunuH_Hbb_ecm240':['wzp6_ee_nunuH_Hbb_ecm240'],
            'wzp6_ee_nunuH_HWW_ecm240':['wzp6_ee_nunuH_HWW_ecm240']
                }
                }


legend = {}
legend['exoticHiggs_scalar_ms20GeV_sine-5_NU'] = 'm_{S} = 20 GeV, sin #theta = 1e-5'
legend['exoticHiggs_scalar_ms20GeV_sine-6_NU'] = 'm_{S} = 20 GeV, sin #theta = 1e-6'
legend['exoticHiggs_scalar_ms20GeV_sine-7_NU'] = 'm_{S} = 20 GeV, sin #theta = 1e-7'
legend['exoticHiggs_scalar_ms60GeV_sine-5_NU'] = 'm_{S} = 60 GeV, sin #theta = 1e-5'
legend['exoticHiggs_scalar_ms60GeV_sine-6_NU'] = 'm_{S} = 60 GeV, sin #theta = 1e-6'
legend['exoticHiggs_scalar_ms60GeV_sine-7_NU'] = 'm_{S} = 60 GeV, sin #theta = 1e-7'

legend['p8_ee_WW_ecm240'] = 'e^{-}e^{+} $\rightarrow$ WW'
legend['p8_ee_ZZ_ecm240'] = 'e^{-}e^{+} $\rightarrow$ ZZ'
legend['wzp6_ee_nunuH_Hbb_ecm240'] = 'e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ nu nu, H $\rightarrow$ bb'
legend['wzp6_ee_nunuH_HWW_ecm240'] = 'e^{-}e^{+} $\rightarrow$ ZH, Z $\rightarrow$ nu nu, H $\rightarrow$ WW'
