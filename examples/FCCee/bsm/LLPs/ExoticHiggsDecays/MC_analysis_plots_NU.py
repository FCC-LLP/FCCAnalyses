import ROOT

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
inputDir       = 'MC_output_finalSel_NU/'
#formats        = ['png','pdf']
formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'MC_plots_NU/'
splitLeg       = True

variables = [

    #gen variables
    'n_GenElecNeutrinos',
    'n_GenMuNeutrinos',
    'n_GenTauNeutrinos',
    'n_GenZ',
    'n_GenHiggs',
    'n_Genb',
    'n_GenHS',
    'AllGenHS_mass',
    'AllGenHS_e',
    'decayLengthsHS',
    'LxyHS',
    'lifetimeHS',
    'lifetimeHSLAB',
    
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['ExoticHiggs']  = [
    "selNone",
]

extralabel = {}
extralabel['selNone'] = "Before selection"

colors = {}
colors['exoticHiggs_scalar_ms20GeV_sine-5_NU'] = ROOT.kOrange+1
colors['exoticHiggs_scalar_ms20GeV_sine-6_NU'] = ROOT.kRed
colors['exoticHiggs_scalar_ms20GeV_sine-7_NU'] = ROOT.kBlue
colors['exoticHiggs_scalar_ms60GeV_sine-5_NU'] = ROOT.kGreen+1
colors['exoticHiggs_scalar_ms60GeV_sine-6_NU'] = ROOT.kCyan-9
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
                    'exoticHiggs_scalar_ms60GeV_sine-7_NU':['exoticHiggs_scalar_ms60GeV_sine-7_NU'],
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
