'''
Plotting stage of the ALP analysis: e⁺e⁻ → aγ → γγγ
'''
import ROOT

intLumi        = 2.05e8
scaleSig       = -1.
scaleBkg       = -1.

ana_tex        = 'e^{+}e^{-} #rightarrow Z #rightarrow #gamma ALP #rightarrow 3#gamma'
delphesVersion = ''
energy         = 91.188
collider       = 'FCC-ee'

inputDir       = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/"
outdir         = "<USER DIRECTORY>"


formats  = ['pdf']
yaxis    = ['log']
stacksig = ['nostack']

splitLeg = True

variables = [
    "All_n_GenALP",
    "AllGenALP_mass",
    "AllGenALP_e",
    "AllGenALP_p",
    "AllGenALP_pt",
    "AllGenALP_pz",
    "AllGenALP_eta",
    "AllGenALP_theta",
    "AllGenALP_phi",
    "n_FSGenElectron",
    "n_FSGenPhoton",
    "FSGenElectron_e",
    "FSGenElectron_p",
    "FSGenElectron_pt",
    "FSGenElectron_pz",
    "FSGenElectron_eta",
    "FSGenElectron_theta",
    "FSGenElectron_phi",
    "FSGenPhoton_e",
    "FSGenPhoton_p",
    "FSGenPhoton_pt",
    "FSGenPhoton_pz",
    "FSGenPhoton_eta",
    "FSGenPhoton_theta",
    "FSGenPhoton_phi",
    "FSGenPhoton_vertex_y",
    "FSGenPhoton_vertex_z",
    "FSGenALP_p",
    "FSGenPhoton0_e",
    "FSGenPhoton1_e",
    "FSGenPhoton2_e",
    "FSGenPhoton0_p",
    "FSGenPhoton1_p",
    "FSGenPhoton2_p",
    "FSGenPhoton0_pt",
    "FSGenPhoton1_pt",
    "FSGenPhoton2_pt",
    "FSGenPhoton0_px",
    "FSGenPhoton1_px",
    "FSGenPhoton2_px",
    "FSGenPhoton0_py",
    "FSGenPhoton1_py",
    "FSGenPhoton2_py",
    "FSGenPhoton0_pz",
    "FSGenPhoton1_pz",
    "FSGenPhoton2_pz",
    "FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0",
    "FSGenPhoton1_px_if_FSGenPhoton2_px_pos",
    "FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos",
    "GenALP_mass",
    "GenALP_e",
    "GenALP_p",
    "GenALP_pt",
    "GenALP_pz",
    "GenALP_eta",
    "GenALP_theta",
    "GenALP_phi",
    "GenALP_beta",
    "GenALP_lifetime_xy",
    "GenALP_lifetime_xyz",
    "GenALP_Lxy",
    "GenALP_Lxyz",
    "GenALP_vertex_x",
    "GenALP_vertex_y",
    "GenALP_vertex_z",
    "GenALP_px_if_FSGenPhoton0_px_greaterthan_0",
    "FSGenPhoton1_px_if_GenALP_px_neg",
    "FSGenPhoton2_px_if_GenALP_px_neg",
    "GenALP_time",
    "GenALPPhoton1_e",
    "GenALPPhoton2_e",
    "GenALPPhoton1_p",
    "GenALPPhoton2_p",
    "GenALPPhoton1_pt",
    "GenALPPhoton2_pt",
    "GenALPPhoton1_pz",
    "GenALPPhoton2_pz",
    "GenALPPhoton1_eta",
    "GenALPPhoton2_eta",
    "GenALPPhoton1_theta",
    "GenALPPhoton2_theta",
    "GenALPPhoton1_phi",
    "GenALPPhoton2_phi",
    "GenALPPhoton1_vertex_x",
    "GenALPPhoton1_vertex_y",
    "GenALPPhoton1_vertex_z",
    "GenALP_aa_invMass",
    "n_RecoTracks",
    "n_RecoALPTracks",
    "RecoALP_DecayVertex_x",
    "RecoALP_DecayVertex_y",
    "RecoALP_DecayVertex_z",
    "GenALPPhotons_deltaEta",
    "GenALPPhotons_deltaPhi",
    "GenALPPhotons_deltaR",
    "n_GenALP",
    "n_GenALPPhoton1",
    "n_GenALPPhoton2",
    "GenALPPhoton1_time",
    "GenALPPhoton2_time",
    "FSGenPhotons_delta_r",
    "FSGenPhotons_min_delta_r",
    "GenALP_observed_lifetime_xyz",
    "RecoALPPhoton1_e",
    "RecoALPPhoton2_e",
    "RecoALPPhoton1_p",
    "RecoALPPhoton2_p",
    "RecoALPPhoton1_pt",
    "RecoALPPhoton2_pt",
    "RecoALPPhoton1_pz",
    "RecoALPPhoton2_pz",
    "RecoALPPhoton1_eta",
    "RecoALPPhoton2_eta",
    "RecoALPPhoton1_theta",
    "RecoALPPhoton2_theta",
    "RecoALPPhoton1_phi",
    "RecoALPPhoton2_phi",
    "RecoALPPhoton1_charge",
    "RecoALPPhoton2_charge",
    "RecoALPPhotons_deltaEta",
    "RecoALPPhotons_deltaPhi",
    "RecoALPPhotons_deltaR",
    "RecoALP_DecayVertex_x",
    "RecoALP_DecayVertex_y",
    "RecoALP_DecayVertex_z",
    "n_RecoJets",
    "n_RecoPhotons",
    "n_RecoElectrons",
    "n_RecoMuons",
    "RecoElectron_e",
    "RecoElectron_p",
    "RecoElectron_pt",
    "RecoElectron_pz",
    "RecoElectron_eta",
    "RecoElectron_theta",
    "RecoElectron_phi",
    "RecoPhoton_e",
    "RecoPhoton_p",
    "RecoPhoton_pt",
    "RecoPhoton_pz",
    "RecoPhoton_eta",
    "RecoPhoton_theta",
    "RecoPhoton_phi",
    "RecoPhoton_charge",
    "RecoPhotons_delta_eta",
    "RecoPhotons_delta_phi",
    "RecoPhotons_delta_r",
    "RecoPhotons_min_delta_r",
    "RecoPhoton0_e",
    "RecoPhoton1_e",
    "RecoPhoton2_e",
    "RecoPhoton0_p",
    "RecoPhoton1_p",
    "RecoPhoton2_p",
    "RecoPhoton0_pt",
    "RecoPhoton1_pt",
    "RecoPhoton2_pt",
    "RecoPhoton0_px",
    "RecoPhoton1_px",
    "RecoPhoton2_px",
    "RecoPhoton0_py",
    "RecoPhoton1_py",
    "RecoPhoton2_py",
    "RecoPhoton0_pz",
    "RecoPhoton1_pz",
    "RecoPhoton2_pz",
    "RecoALP_aa_invMass",
    "RecoALP_aa_p",
    "RecoALP_aa_energy",
    "Reco_aa_invMass",
    "Reco_aa_p",
    "RecoPhoton1_px_if_RecoPhoton2_px_pos",
    "RecoPhoton1_pz_if_RecoPhoton2_pz_pos",
    "RecoALPPhotons_delta_R3",
    "GenMinusRecoALPPhoton1_e",
    "GenMinusRecoALPPhoton2_e",
    "GenMinusRecoALP_DecayVertex_x",
    "GenMinusRecoALP_DecayVertex_y",
    "GenMinusRecoALP_DecayVertex_z",
]

selections = {}
selections['ALP'] = [
    "selNone",
    "sel",
]

extralabel = {}
extralabel['selNone'] = "Before selection"
extralabel["sel"] = "3 reconstructed photons"

color_wheel = [
    # colors from DESY color guide
    "#EB5E2D",  # Red
    "#8CBE23",  # Light green
    "#00B1AA",  # Turquoise
    "#D2006E",  # Magenta
    "#917DB9",  # Violet
    "#C3B700",  # Olive
    "#FAC800",  # Yellow
    "#B92D41",  # Dark red
    "#00A64B",  # Green
    "#006987",  # Petrol
    "#8C3C5B",  # Aubergine
    "#504F8F",  # Purple
    "#828F2B",  # Dark olive
    "#004A6F"   # Dark blue
]

colors = {}

# Signal
colors['alp_3photons_cme_91p188_malp_0p1'] = ROOT.TColor.GetColor(color_wheel[0]) 
colors['alp_3photons_cme_91p188_malp_1p0'] = ROOT.TColor.GetColor(color_wheel[1]) 
colors['alp_3photons_cme_91p188_malp_10p0'] = ROOT.TColor.GetColor(color_wheel[2]) 
colors['alp_3photons_cme_91p188_malp_50p0'] = ROOT.TColor.GetColor(color_wheel[3]) 
colors['alp_3photons_cme_91p188_malp_90p0'] = ROOT.TColor.GetColor(color_wheel[4]) 
# Background
colors['background_3photons_cme_91p188'] = ROOT.TColor.GetColor(color_wheel[13])

plots = {}
plots['ALP'] = {
    'signal': {
        'alp_3photons_cme_91p188_malp_0p1': ['alp_3photons_cme_91p188_malp_0p1'],
        'alp_3photons_cme_91p188_malp_1p0': ['alp_3photons_cme_91p188_malp_1p0'],
        'alp_3photons_cme_91p188_malp_10p0': ['alp_3photons_cme_91p188_malp_10p0'],
        'alp_3photons_cme_91p188_malp_50p0': ['alp_3photons_cme_91p188_malp_50p0'],
        'alp_3photons_cme_91p188_malp_90p0': ['alp_3photons_cme_91p188_malp_90p0'],
    },
    'backgrounds': {
        'background_3photons_cme_91p188': ['background_3photons_cme_91p188']
    }
}

legend = {}
legend['alp_3photons_cme_91p188_malp_0p1'] = 'm_{ALP} = 0.1 GeV'
legend['alp_3photons_cme_91p188_malp_1p0'] = 'm_{ALP} = 1.0 GeV'
legend['alp_3photons_cme_91p188_malp_10p0'] = 'm_{ALP} = 10.0 GeV'
legend['alp_3photons_cme_91p188_malp_50p0'] = 'm_{ALP} = 50.0 GeV'
legend['alp_3photons_cme_91p188_malp_90p0'] = 'm_{ALP} = 90.0 GeV'
legend['background_3photons_cme_91p188'] = 'e^{+}e^{-} #rightarrow #gamma#gamma#gamma'
