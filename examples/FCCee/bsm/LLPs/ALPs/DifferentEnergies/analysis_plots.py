'''
Plotting stage of the ALP analysis: e⁺e⁻ → aγ → γγγ
'''
import ROOT

scaleSig       = -1.
scaleBkg       = -1.

ana_tex        = 'e^{+}e^{-} #rightarrow Z #rightarrow #gamma ALP #rightarrow 3#gamma'
delphesVersion = ''
energy         = 91.188
collider       = 'FCC-ee'

inputDir       = "/eos/user/c/cdorofee/final_output/"
outdir         = '/eos/user/c/cdorofee/plot_output/'


formats  = ['png']
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
    "FSGenPhoton_vertex_x",
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
    "FSGenPhoton_eta_obj_sel_eta",
    "FSGenPhoton_theta_obj_sel_eta",
    "FSGenPhoton_phi_obj_sel_eta",
    "FSGenPhotons_delta_eta_obj_sel_eta",
    "FSGenPhotons_delta_phi_obj_sel_eta",
    "FSGenPhotons_delta_r_obj_sel_eta",
    "FSGenPhotons_min_delta_r_obj_sel_eta",
    "FSGenPhoton_pt_obj_sel_eta",
    "FSGenPhoton_e_obj_sel_eta",
    "FSGenPhoton_p_obj_sel_eta",
    "n_FSGenPhoton_obj_sel_eta",
    "FSGenPhoton_pz_obj_sel_eta",
    "FSGenPhoton0_e_obj_sel_eta",
    "FSGenPhoton1_e_obj_sel_eta",
    "FSGenPhoton2_e_obj_sel_eta",
    "FSGenPhoton0_p_obj_sel_eta",
    "FSGenPhoton1_p_obj_sel_eta",
    "FSGenPhoton2_p_obj_sel_eta",
    "FSGenPhoton0_pt_obj_sel_eta",
    "FSGenPhoton1_pt_obj_sel_eta",
    "FSGenPhoton2_pt_obj_sel_eta",
    "FSGenPhoton0_pz_obj_sel_eta",
    "FSGenPhoton1_pz_obj_sel_eta",
    "FSGenPhoton2_pz_obj_sel_eta",
    "FSGen_aa_invMass_obj_sel_eta",
    "FSGen_aa_p_obj_sel_eta",
    "RecoPhoton_eta_obj_sel_eta",
    "RecoPhoton_theta_obj_sel_eta",
    "RecoPhoton_phi_obj_sel_eta",
    "RecoPhotons_delta_eta_obj_sel_eta",
    "RecoPhotons_delta_phi_obj_sel_eta",
    "RecoPhotons_delta_r_obj_sel_eta",
    "RecoPhotons_min_delta_r_obj_sel_eta",
    "RecoPhoton_pt_obj_sel_eta",
    "RecoPhoton_e_obj_sel_eta",
    "RecoPhoton_p_obj_sel_eta",
    "n_RecoPhotons_obj_sel_eta",
    "RecoPhoton_charge_obj_sel_eta",
    "RecoPhoton_diphoton_delta_r_obj_sel_eta",
    "RecoPhoton_pz_obj_sel_eta",
    "RecoPhoton0_e_obj_sel_eta",
    "RecoPhoton1_e_obj_sel_eta",
    "RecoPhoton2_e_obj_sel_eta",
    "RecoPhoton0_p_obj_sel_eta",
    "RecoPhoton1_p_obj_sel_eta",
    "RecoPhoton2_p_obj_sel_eta",
    "RecoPhoton0_pt_obj_sel_eta",
    "RecoPhoton1_pt_obj_sel_eta",
    "RecoPhoton2_pt_obj_sel_eta",
    "RecoPhoton0_pz_obj_sel_eta",
    "RecoPhoton1_pz_obj_sel_eta",
    "RecoPhoton2_pz_obj_sel_eta",
    "Reco_aa_invMass_obj_sel_eta",
    "Reco_aa_p_obj_sel_eta",
    "RecoPhoton_pidx_min_delta_r_obj_sel_eta",
    "RecoPhoton1_pz_obj_sel_eta_v2",
    "RecoPhoton2_pz_obj_sel_eta_v2",
    "Reco_aa_invMass_obj_sel_eta_v2",
    "Reco_aa_p_obj_sel_eta_v2",
    "RecoALPPhoton1_e_obj_sel_eta",
    "RecoALPPhoton2_e_obj_sel_eta",
    "RecoALPPhoton1_p_obj_sel_eta",
    "RecoALPPhoton2_p_obj_sel_eta",
    "RecoALPPhoton1_pt_obj_sel_eta",
    "RecoALPPhoton2_pt_obj_sel_eta",
    "RecoALPPhoton1_pz_obj_sel_eta",
    "RecoALPPhoton2_pz_obj_sel_eta",
    "RecoALPPhoton1_eta_obj_sel_eta",
    "RecoALPPhoton2_eta_obj_sel_eta",
    "RecoALPPhoton1_phi_obj_sel_eta",
    "RecoALPPhoton2_phi_obj_sel_eta",
    "RecoALPPhotons_deltaEta_obj_sel_eta",
    "RecoALPPhotons_deltaPhi_obj_sel_eta",
    "RecoALPPhotons_deltaR_obj_sel_eta",
    "n_RecoALPPhoton1_obj_sel_eta",
    "n_RecoALPPhoton2_obj_sel_eta",
    "RecoALP_aa_invMass_obj_sel_eta",
    "RecoALP_aa_p_obj_sel_eta",
    "Reco_beta_ALP_obj_sel_eta",
]

selections = {}
selections['ALP'] = ["selNone"]

extralabel = {}
extralabel['selNone'] = "Before selection"

color_wheel = [
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
colors['signal_Z_malp1_events10k_edm4hep']   = ROOT.TColor.GetColor(color_wheel[0])  
colors['signal_Z_malp50_events10k_edm4hep']  = ROOT.TColor.GetColor(color_wheel[1])  
colors['signal_WW_malp1_events10k_edm4hep']  = ROOT.TColor.GetColor(color_wheel[2])  
colors['signal_WW_malp50_events10k_edm4hep'] = ROOT.TColor.GetColor(color_wheel[3]) 
colors['signal_ZH_malp1_events10k_edm4hep']  = ROOT.TColor.GetColor(color_wheel[4])  
colors['signal_ZH_malp50_events10k_edm4hep'] = ROOT.TColor.GetColor(color_wheel[5]) 
colors['signal_tt_malp1_events10k_edm4hep']  = ROOT.TColor.GetColor(color_wheel[6])  
colors['signal_tt_malp50_events10k_edm4hep'] = ROOT.TColor.GetColor(color_wheel[7]) 

# Background
colors['background_Z_events10k_edm4hep']  = ROOT.TColor.GetColor(color_wheel[8])  
colors['background_WW_events10k_edm4hep'] = ROOT.TColor.GetColor(color_wheel[9])   
colors['background_ZH_events10k_edm4hep'] = ROOT.TColor.GetColor(color_wheel[10])  
colors['background_tt_events10k_edm4hep'] = ROOT.TColor.GetColor(color_wheel[11])  

plots = {}
plots['ALP'] = {
    'signal':{
        'signal_Z_malp1_events10k_edm4hep':   ['signal_Z_malp1_events10k_edm4hep'],
        'signal_Z_malp50_events10k_edm4hep':  ['signal_Z_malp50_events10k_edm4hep'],
        'signal_WW_malp1_events10k_edm4hep':  ['signal_WW_malp1_events10k_edm4hep'],
        'signal_WW_malp50_events10k_edm4hep': ['signal_WW_malp50_events10k_edm4hep'],
        'signal_ZH_malp1_events10k_edm4hep':  ['signal_ZH_malp1_events10k_edm4hep'],
        'signal_ZH_malp50_events10k_edm4hep': ['signal_ZH_malp50_events10k_edm4hep'],
        'signal_tt_malp1_events10k_edm4hep':  ['signal_tt_malp1_events10k_edm4hep'],
        'signal_tt_malp50_events10k_edm4hep': ['signal_tt_malp50_events10k_edm4hep'],
    },

    'backgrounds':{
        'background_Z_events10k_edm4hep':  ['background_Z_events10k_edm4hep'],
        'background_WW_events10k_edm4hep': ['background_WW_events10k_edm4hep'],
        'background_ZH_events10k_edm4hep': ['background_ZH_events10k_edm4hep'],
        'background_tt_events10k_edm4hep': ['background_tt_events10k_edm4hep'],
    },
}

legend = {}
legend['signal_Z_malp1_events10k_edm4hep']   = 'cme = 91.188, m_{ALP} = 1 GeV'
legend['signal_Z_malp50_events10k_edm4hep']  = 'cme = 91.188, m_{ALP} = 50 GeV'
legend['signal_WW_malp1_events10k_edm4hep']  = 'cme = 160, m_{ALP} = 1 GeV'
legend['signal_WW_malp50_events10k_edm4hep'] = 'cme = 160, m_{ALP} = 50 GeV'
legend['signal_ZH_malp1_events10k_edm4hep']  = 'cme = 240, m_{ALP} = 1 GeV'
legend['signal_ZH_malp50_events10k_edm4hep'] = 'cme = 240, m_{ALP} = 50 GeV'
legend['signal_tt_malp1_events10k_edm4hep']  = 'cme = 365, m_{ALP} = 1 GeV'
legend['signal_tt_malp50_events10k_edm4hep'] = 'cme = 365, m_{ALP} = 50 GeV'

legend['background_Z_events10k_edm4hep']  = 'cme = 91.188, e^{+}e^{-} #rightarrow #gamma#gamma#gamma'
legend['background_WW_events10k_edm4hep'] = 'cme = 160, e^{+}e^{-} #rightarrow #gamma#gamma#gamma'
legend['background_ZH_events10k_edm4hep'] = 'cme = 240, e^{+}e^{-} #rightarrow #gamma#gamma#gamma'
legend['background_tt_events10k_edm4hep'] = 'cme = 365, e^{+}e^{-} #rightarrow #gamma#gamma#gamma'
