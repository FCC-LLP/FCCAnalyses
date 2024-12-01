import ROOT


# global parameters
intLumi        = 150.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is equal to -1, plots will be normalized to 1
scaleSig       = -1.
# scaleBack      = 1.
ana_tex        = 'e^{+}e^{-} #rightarrow Z #rightarrow #gamma ALP #rightarrow 3#gamma'
#ana_tex        = ''
#delphesVersion = '3.4.2'
delphesVersion = ''
energy         = 91
collider       = 'FCC-ee'
inputDir       = './final_output/'
#formats        = ['png','pdf']
# formats        = ['pdf']
formats = ['png']
# xaxis          = ['log']
yaxis          = ['log']
# yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = './plots_output/'
splitLeg       = True

variables = [
    #gen variables
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
    # "n_FSGenPositron",
    # "n_FSGenNeutrino",
    # "n_FSGenAntiNeutrino",
    "n_FSGenPhoton",
    # # "n_FSGenElectron_forFS2GenPhotons",
    # # "n_FSGenPositron_forFS2GenPhotons",

    # "FSGenElectron_e",
    # "FSGenElectron_p",
    # "FSGenElectron_pt",
    # "FSGenElectron_pz",
    # "FSGenElectron_eta",
    # "FSGenElectron_theta",
    # "FSGenElectron_phi",

    # "FSGenPositron_e",
    # "FSGenPositron_p",
    # "FSGenPositron_pt",
    # "FSGenPositron_pz",
    # "FSGenPositron_eta",
    # "FSGenPositron_theta",
    # "FSGenPositron_phi",

    # "FSGenNeutrino_e",
    # "FSGenNeutrino_p",
    # "FSGenNeutrino_pt",
    # "FSGenNeutrino_pz",
    # "FSGenNeutrino_eta",
    # "FSGenNeutrino_theta",
    # "FSGenNeutrino_phi",

    # "FSGenAntiNeutrino_e",
    # "FSGenAntiNeutrino_p",
    # "FSGenAntiNeutrino_pt",
    # "FSGenAntiNeutrino_pz",
    # "FSGenAntiNeutrino_eta",
    # "FSGenAntiNeutrino_theta",
    # "FSGenAntiNeutrino_phi",

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

    # "FSGen_Lxy",
    # "FSGen_Lxyz",
    # "FSGen_lifetime_xy",
    # "FSGen_lifetime_xyz",

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

    # "FSGen_a0a1_invMass",
    # "FSGen_a0a2_invMass",
    # "FSGen_a1a2_invMass",
    # "FSGen_aaa_invMass",

    "GenALP_mass",
    "GenALP_e",
    "GenALP_p",
    "GenALP_pt",
    "GenALP_pz",
    "GenALP_eta",
    "GenALP_theta",
    "GenALP_phi",
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
    # "GenALPPhoton1_time_minus_GenALP_time",

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

    # "GenALP_aa_invMass",

    # #reco variables
    "n_RecoTracks",
    "n_RecoALPTracks",
    "RecoALP_DecayVertex_x",
    "RecoALP_DecayVertex_y",
    "RecoALP_DecayVertex_z",
    # "RecoALP_DecayVertex_chi2",
    # "RecoALP_DecayVertex_probability",

    "GenALPPhotons_deltaEta",
    "GenALPPhotons_deltaPhi",
    "GenALPPhotons_deltaR",
    "n_GenALP",
    "n_GenALPPhoton1",
    "n_GenALPPhoton2",
    "GenALPPhoton1_time",
    "GenALPPhoton2_time",

    # "GenALPPhotons_deltaR_2",
    # "FSGenPhotons_delta_r",

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

    # "RecoALPL_xyz",

    "n_RecoJets",
    "n_RecoPhotons",
    "n_RecoElectrons",
    "n_RecoMuons",

    # "RecoJet_e",
    # "RecoJet_p",
    # "RecoJet_pt",
    # "RecoJet_pz",
    # "RecoJet_eta",
    # "RecoJet_theta",
    # "RecoJet_phi",
    # "RecoJet_charge",

    # "RecoElectron_e",
    # "RecoElectron_p",
    # "RecoElectron_pt",
    # "RecoElectron_pz",
    # "RecoElectron_eta",
    # "RecoElectron_theta",
    # "RecoElectron_phi",
    # "RecoElectron_charge",

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

    # "RecoPhotons_ALP_delta_r",
    # "RecoPhotons_ALP_delta_phi",
    # "RecoPhotons_ALP_delta_eta",

    # "RecoPhoton_reference_point_x",

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

    "RecoPhoton1_px_if_RecoPhoton2_px_pos",
    "RecoPhoton1_pz_if_RecoPhoton2_pz_pos",

    "RecoALPPhotons_delta_R3",

    # "RecoMuon_e",
    # "RecoMuon_p",
    # "RecoMuon_pt",
    # "RecoMuon_pz",
    # "RecoMuon_eta",
    # "RecoMuon_theta",
    # "RecoMuon_phi",
    # "RecoMuon_charge",

    # "RecoMissingEnergy_e",
    # "RecoMissingEnergy_p",
    # "RecoMissingEnergy_pt",
    # "RecoMissingEnergy_px",
    # "RecoMissingEnergy_py",
    # "RecoMissingEnergy_pz",
    # "RecoMissingEnergy_eta",
    # "RecoMissingEnergy_theta",
    # "RecoMissingEnergy_phi",

    "GenMinusRecoALPPhoton1_e",
    "GenMinusRecoALPPhoton2_e",
    "GenMinusRecoALP_DecayVertex_x",
    "GenMinusRecoALP_DecayVertex_y",
    "GenMinusRecoALP_DecayVertex_z",

    # "CalorimeterHitsTime",
]


###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['ALP']   = [
    "selNone",
    # "sel0",
    # "sel1",
    # "sel2",
    # "sel1+2",
    # "seltest",
    # "seldeltaR",
    # "selp",
    # "selall",
]

extralabel = {}
extralabel['selNone'] = "Before selection"
# extralabel['sel1'] = "Exactly 3 Reconstructed Photons"
# extralabel['sel2'] = "Reco Photons #DeltaR < 0.5 or > 4.5"
# extralabel['sel1+2'] = "Exactly 3 Reconstructed Photons and Reco Photons #DeltaR < 0.5 or > 4.5"
# extralabel['sel0'] = "Selection: RecoPhotons_min_delta_r close to 0 and pi"
#extralabel['sel0'] = "Selection: At least 1 ALP"
#extralabel['sel1'] = "Selection: At least 1 ALP, at least 2 reco electrons"
# extralabel['seltest'] = "3 reco photons and second and third photons have the same direction px"
# extralabel['seldeltaR'] = "3 reco photons and reco photons min #DeltaR < 1"
# extralabel["selp"] = "3 reco photons and RecoPhoton0 momentum > 44"
# extralabel["selall"] = "all selections"

colors = {}
# colors['ALP_Z_aa_0.316.GeV_cYY_0.00006'] = ROOT.kRed
# colors['ALP_Z_aa_0.316.GeV_cYY_0.0006'] = ROOT.kGreen
# colors['ALP_Z_aa_0.316.GeV_cYY_0.006'] = ROOT.kBlue
# colors['ALP_Z_aa_0.316.GeV_cYY_0.06'] = ROOT.kViolet
# colors['ALP_Z_aa_0.316.GeV_cYY_0.6'] = ROOT.kCyan

# colors['ALP_Z_aa_1GeV_cYY_0p5'] = ROOT.kRed

# colors['ALP_Z_aa_0.1GeV_cYY_0.1'] = ROOT.kRed
# colors['ALP_Z_aa_0.2GeV_cYY_0.1'] = ROOT.kGreen
# colors['ALP_Z_aa_0.135GeV_cYY_0.1'] = ROOT.kCyan
# colors['ALP_Z_aa_0.3GeV_cYY_0.1'] = ROOT.kGray

# colors['ALP_Z_aa_1.GeV_cYY_0.1'] = ROOT.kMagenta
# colors['ALP_Z_aa_1.GeV_cYY_0.3'] = ROOT.kViolet
# colors['ALP_Z_aa_1.GeV_cYY_0.5'] = ROOT.kCyan
# colors['ALP_Z_aa_1.GeV_cYY_0.7'] = ROOT.kAzure
# colors['ALP_Z_aa_1.GeV_cYY_0.9'] = ROOT.kCyan

# colors['ALP_Z_aa_0.5.GeV_cYY_0.6'] = ROOT.kRed
# colors['ALP_Z_aa_0.5.GeV_cYY_1.2'] = ROOT.kBlue

# colors['ALP_Z_aa_1.GeV_cYY_0.6'] = ROOT.kRed
# colors['ALP_Z_aa_1.GeV_cYY_0.8'] = ROOT.kGreen
# colors['ALP_Z_aa_1.GeV_cYY_1.0'] = ROOT.kBlue
# colors['ALP_Z_aa_1.GeV_cYY_1.2'] = ROOT.kViolet
# colors['ALP_Z_aa_1.GeV_cYY_1.4'] = ROOT.kCyan

colors['ALP_Z_aa_0.5.GeV_cYY_1.0'] = ROOT.kRed
# colors['ALP_Z_aa_1.GeV_cYY_1.0'] = ROOT.kGreen
# colors['ALP_Z_aa_1.5.GeV_cYY_1.0'] = ROOT.kBlue
# colors['ALP_Z_aa_2.GeV_cYY_1.0'] = ROOT.kBlue
# colors['ALP_Z_aa_3.GeV_cYY_1.0'] = ROOT.kViolet
# colors['ALP_Z_aa_4.GeV_cYY_1.0'] = ROOT.kViolet
colors['ALP_Z_aa_5.GeV_cYY_1.0'] = ROOT.kGreen
colors['ALP_Z_aa_8.GeV_cYY_1.0'] = ROOT.kViolet

# colors['ALP_Z_aa_0.6.GeV_cYY_1.0'] = ROOT.kOrange
colors['ALP_Z_aa_0.8.GeV_cYY_1.0'] = ROOT.kAzure
colors['ALP_Z_aa_1.GeV_cYY_1.0'] = ROOT.kCyan
# colors['ALP_Z_aa_1.2.GeV_cYY_1.0'] = ROOT.kGreen
# colors['ALP_Z_aa_1.4.GeV_cYY_1.0'] = ROOT.kMagenta

# colors['ALP_Z_aa_3.GeV_cYY_0.1'] = ROOT.kRed
# colors['ALP_Z_aa_3.GeV_cYY_0.3'] = ROOT.kBlue
# colors['ALP_Z_aa_3.GeV_cYY_0.5'] = ROOT.kYellow
# colors['ALP_Z_aa_3.GeV_cYY_0.7'] = ROOT.kMagenta
# colors['ALP_Z_aa_3.GeV_cYY_0.9'] = ROOT.kRed

# colors['ALP_Z_aa_5.GeV_cYY_0.1'] = ROOT.kGray
# colors['ALP_Z_aa_5.GeV_cYY_0.3'] = ROOT.kBlack
# colors['ALP_Z_aa_5.GeV_cYY_0.5'] = ROOT.kViolet
# colors['ALP_Z_aa_5.GeV_cYY_0.7'] = ROOT.kGreen
# colors['ALP_Z_aa_5.GeV_cYY_0.9'] = ROOT.kCyan

# colors['ALP_Z_aa_0.5GeV_cYY_0.5'] = ROOT.kYellow
# colors['ALP_Z_aa_0.7GeV_cYY_0.5'] = ROOT.kOrange
# colors['ALP_Z_aa_1.GeV_cYY_0.5'] = ROOT.kRed
# colors['ALP_Z_aa_3.GeV_cYY_0.5'] = ROOT.kBlue
# colors['ALP_Z_aa_5.GeV_cYY_0.5'] = ROOT.kGreen
# colors['ALP_Z_aa_7.GeV_cYY_0.5'] = ROOT.kCyan
# colors['ALP_Z_aa_10.GeV_cYY_0.5'] = ROOT.kCyan
# colors['ALP_Z_aa_15.GeV_cYY_0.5'] = ROOT.kAzure
# colors['ALP_Z_aa_20.GeV_cYY_0.5'] = ROOT.kCyan
# colors['ALP_Z_aa_25.GeV_cYY_0.5'] = ROOT.kTeal
# colors['ALP_Z_aa_30.GeV_cYY_0.5'] = ROOT.kGreen

# colors['ee_Z_ALPga_gagaga'] = ROOT.kRed

# colors['p8_ee_Zee_ecm91'] = ROOT.kBlue
# colors['ee_gaga_1million'] = ROOT.kBlue
# colors['test1'] = ROOT.kBlue
# colors['test4'] = ROOT.kCyan
# colors['ee_gammagamma'] = ROOT.kGreen
# colors['ee_gaga_test'] = ROOT.kBlue
# colors['ee_aa'] = ROOT.kGreen
# colors['ee_aaa'] = ROOT.kYellow
# colors['ee_aaaa'] = ROOT.kCyan

plots = {}
plots['ALP'] = {'signal':{
    # 'ALP_Z_aa_0.316.GeV_cYY_0.00006':['ALP_Z_aa_0.316.GeV_cYY_0.00006'],
    # 'ALP_Z_aa_0.316.GeV_cYY_0.0006':['ALP_Z_aa_0.316.GeV_cYY_0.0006'],
    # 'ALP_Z_aa_0.316.GeV_cYY_0.006':['ALP_Z_aa_0.316.GeV_cYY_0.006'],
    # 'ALP_Z_aa_0.316.GeV_cYY_0.06':['ALP_Z_aa_0.316.GeV_cYY_0.06'],
    # 'ALP_Z_aa_0.316.GeV_cYY_0.6':['ALP_Z_aa_0.316.GeV_cYY_0.6'],

    # 'ALP_Z_aa_1GeV_cYY_0p5':['ALP_Z_aa_1GeV_cYY_0p5'],

    # 'ALP_Z_aa_0.1GeV_cYY_0.1':['ALP_Z_aa_0.1GeV_cYY_0.1'],
    # 'ALP_Z_aa_0.2GeV_cYY_0.1':['ALP_Z_aa_0.2GeV_cYY_0.1'],
    # 'ALP_Z_aa_0.135GeV_cYY_0.1':['ALP_Z_aa_0.135GeV_cYY_0.1'],
    # 'ALP_Z_aa_0.3GeV_cYY_0.1':['ALP_Z_aa_0.3GeV_cYY_0.1'],

    # 'ALP_Z_aa_1.GeV_cYY_0.1':['ALP_Z_aa_1.GeV_cYY_0.1'],
    # 'ALP_Z_aa_1.GeV_cYY_0.3':['ALP_Z_aa_1.GeV_cYY_0.3'],
    # 'ALP_Z_aa_1.GeV_cYY_0.5':['ALP_Z_aa_1.GeV_cYY_0.5'],
    # 'ALP_Z_aa_1.GeV_cYY_0.7':['ALP_Z_aa_1.GeV_cYY_0.7'],
    # 'ALP_Z_aa_1.GeV_cYY_0.9':['ALP_Z_aa_1.GeV_cYY_0.9'],

    # 'ALP_Z_aa_0.5.GeV_cYY_0.6':['ALP_Z_aa_0.5.GeV_cYY_0.6'],
    # 'ALP_Z_aa_0.5.GeV_cYY_1.2':['ALP_Z_aa_0.5.GeV_cYY_1.2'],

    # 'ALP_Z_aa_1.GeV_cYY_0.6':['ALP_Z_aa_1.GeV_cYY_0.6'],
    # 'ALP_Z_aa_1.GeV_cYY_0.8':['ALP_Z_aa_1.GeV_cYY_0.8'],
    # 'ALP_Z_aa_1.GeV_cYY_1.0':['ALP_Z_aa_1.GeV_cYY_1.0'],
    # 'ALP_Z_aa_1.GeV_cYY_1.2':['ALP_Z_aa_1.GeV_cYY_1.2'],
    # 'ALP_Z_aa_1.GeV_cYY_1.4':['ALP_Z_aa_1.GeV_cYY_1.4'],

     'ALP_Z_aa_0.5.GeV_cYY_1.0':['ALP_Z_aa_0.5.GeV_cYY_1.0'],
     'ALP_Z_aa_0.8.GeV_cYY_1.0':['ALP_Z_aa_0.8.GeV_cYY_1.0'],
     'ALP_Z_aa_1.GeV_cYY_1.0':['ALP_Z_aa_1.GeV_cYY_1.0'],
    # 'ALP_Z_aa_1.5.GeV_cYY_1.0':['ALP_Z_aa_1.5.GeV_cYY_1.0'],
    # 'ALP_Z_aa_2.GeV_cYY_1.0':['ALP_Z_aa_2.GeV_cYY_1.0'],
    # 'ALP_Z_aa_3.GeV_cYY_1.0':['ALP_Z_aa_3.GeV_cYY_1.0'],
    # 'ALP_Z_aa_4.GeV_cYY_1.0':['ALP_Z_aa_4.GeV_cYY_1.0'],
     'ALP_Z_aa_5.GeV_cYY_1.0':['ALP_Z_aa_5.GeV_cYY_1.0'],
     'ALP_Z_aa_8.GeV_cYY_1.0':['ALP_Z_aa_8.GeV_cYY_1.0'],

    # 'ALP_Z_aa_0.6.GeV_cYY_1.0':['ALP_Z_aa_0.6.GeV_cYY_1.0'],
    # 'ALP_Z_aa_1.GeV_cYY_1.0':['ALP_Z_aa_1.GeV_cYY_1.0'],
    # 'ALP_Z_aa_1.2.GeV_cYY_1.0':['ALP_Z_aa_1.2.GeV_cYY_1.0'],
    # 'ALP_Z_aa_1.4.GeV_cYY_1.0':['ALP_Z_aa_1.4.GeV_cYY_1.0'],

    # 'ALP_Z_aa_3.GeV_cYY_0.1':['ALP_Z_aa_3.GeV_cYY_0.1'],
    # 'ALP_Z_aa_3.GeV_cYY_0.3':['ALP_Z_aa_3.GeV_cYY_0.3'],
    # 'ALP_Z_aa_3.GeV_cYY_0.5':['ALP_Z_aa_3.GeV_cYY_0.5'],
    # 'ALP_Z_aa_3.GeV_cYY_0.7':['ALP_Z_aa_3.GeV_cYY_0.7'],
    # 'ALP_Z_aa_3.GeV_cYY_0.9':['ALP_Z_aa_3.GeV_cYY_0.9'],

    # 'ALP_Z_aa_5.GeV_cYY_0.1':['ALP_Z_aa_5.GeV_cYY_0.1'],
    # 'ALP_Z_aa_5.GeV_cYY_0.3':['ALP_Z_aa_5.GeV_cYY_0.3'],
    # 'ALP_Z_aa_5.GeV_cYY_0.5':['ALP_Z_aa_5.GeV_cYY_0.5'],
    # 'ALP_Z_aa_5.GeV_cYY_0.7':['ALP_Z_aa_5.GeV_cYY_0.7'],
    # 'ALP_Z_aa_5.GeV_cYY_0.9':['ALP_Z_aa_5.GeV_cYY_0.9'],

    # 'ALP_Z_aa_0.5GeV_cYY_0.5':['ALP_Z_aa_0.5GeV_cYY_0.5'],
    # 'ALP_Z_aa_0.7GeV_cYY_0.5':['ALP_Z_aa_0.7GeV_cYY_0.5'],
    # 'ALP_Z_aa_1.GeV_cYY_0.5':['ALP_Z_aa_1.GeV_cYY_0.5'],
    # 'ALP_Z_aa_3.GeV_cYY_0.5':['ALP_Z_aa_3.GeV_cYY_0.5'],
    # 'ALP_Z_aa_5.GeV_cYY_0.5':['ALP_Z_aa_5.GeV_cYY_0.5'],
    # 'ALP_Z_aa_7.GeV_cYY_0.5':['ALP_Z_aa_7.GeV_cYY_0.5'],
    # 'ALP_Z_aa_10.GeV_cYY_0.5':['ALP_Z_aa_10.GeV_cYY_0.5'],
    # 'ALP_Z_aa_15.GeV_cYY_0.5':['ALP_Z_aa_15.GeV_cYY_0.5'],
    # 'ALP_Z_aa_20.GeV_cYY_0.5':['ALP_Z_aa_20.GeV_cYY_0.5'],
    # 'ALP_Z_aa_25.GeV_cYY_0.5':['ALP_Z_aa_25.GeV_cYY_0.5'],
    # 'ALP_Z_aa_30.GeV_cYY_0.5':['ALP_Z_aa_30.GeV_cYY_0.5'],

    # 'ee_Z_ALPga_gagaga':['ee_Z_ALPga_gagaga'],
    },
    'backgrounds':{
        # 'p8_ee_Zee_ecm91':['p8_ee_Zee_ecm91'],
        # 'ee_gaga_1million':['ee_gaga_1million'],
        # 'test1':['test1'],
        # 'test4':['test4'],
        # 'ee_gammagamma':['ee_gammagamma'],
        # 'ee_gaga_test':['ee_gaga_test'],
        # 'ee_aa':['ee_aa'],
        # 'ee_aaa':['ee_aaa'],
        # 'ee_aaaa':['ee_aaaa'],
    },
}


legend = {}
# legend['ALP_Z_aa_0.316.GeV_cYY_0.00006'] = 'm_{ALP} = 0.316 GeV, c_{YY} = 0.00006'
# legend['ALP_Z_aa_0.316.GeV_cYY_0.0006'] = 'm_{ALP} = 0.316 GeV, c_{YY} = 0.0006'
# legend['ALP_Z_aa_0.316.GeV_cYY_0.006'] = 'm_{ALP} = 0.316 GeV, c_{YY} = 0.006'
# legend['ALP_Z_aa_0.316.GeV_cYY_0.06'] = 'm_{ALP} = 0.316 GeV, c_{YY} = 0.06'
# legend['ALP_Z_aa_0.316.GeV_cYY_0.6'] = 'm_{ALP} = 0.316 GeV, c_{YY} = 0.6'

# legend['ALP_Z_aa_1GeV_cYY_0p5'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.5'

# legend['ALP_Z_aa_0.1GeV_cYY_0.1'] = 'm_{ALP} = 0.1 GeV, c_{YY} = 0.1'
# legend['ALP_Z_aa_0.2GeV_cYY_0.1'] = 'm_{ALP} = 0.2 GeV, c_{YY} = 0.1'
# legend['ALP_Z_aa_0.135GeV_cYY_0.1'] = 'm_{ALP} = 0.135 GeV, c_{YY} = 0.1'
# legend['ALP_Z_aa_0.3GeV_cYY_0.1'] = 'm_{ALP} = 0.3 GeV, c_{YY} = 0.1'

# legend['ALP_Z_aa_1.GeV_cYY_0.1'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.1'
# legend['ALP_Z_aa_1.GeV_cYY_0.3'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.3'
# legend['ALP_Z_aa_1.GeV_cYY_0.5'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_1.GeV_cYY_0.7'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.7'
# legend['ALP_Z_aa_1.GeV_cYY_0.9'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.9'

# legend['ALP_Z_aa_0.5.GeV_cYY_0.6'] = 'm_{ALP} = 0.5 GeV, c_{#gamma#gamma} = 0.6'
# legend['ALP_Z_aa_0.5.GeV_cYY_1.2'] = 'm_{ALP} = 0.5 GeV, c_{#gamma#gamma} = 1.2'

# legend['ALP_Z_aa_1.GeV_cYY_0.6'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 0.6'
# legend['ALP_Z_aa_1.GeV_cYY_0.8'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 0.8'
# legend['ALP_Z_aa_1.GeV_cYY_1.0'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 1.0'
# legend['ALP_Z_aa_1.GeV_cYY_1.2'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 1.2'
# legend['ALP_Z_aa_1.GeV_cYY_1.4'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 1.4'

legend['ALP_Z_aa_0.5.GeV_cYY_1.0'] = 'm_{ALP} = 0.5 GeV, c_{#gamma#gamma} = 1.0'
legend['ALP_Z_aa_0.8.GeV_cYY_1.0'] = 'm_{ALP} = 0.8 GeV, c_{#gamma#gamma} = 1.0'
legend['ALP_Z_aa_1.GeV_cYY_1.0'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 1.0'
# legend['ALP_Z_aa_1.5.GeV_cYY_1.0'] = 'm_{ALP} = 1.5 GeV, c_{YY} = 1.0'
# legend['ALP_Z_aa_2.GeV_cYY_1.0'] = 'm_{ALP} = 2 GeV, c_{YY} = 1.0'
# legend['ALP_Z_aa_3.GeV_cYY_1.0'] = 'm_{ALP} = 3 GeV, c_{YY} = 1.0'
# legend['ALP_Z_aa_4.GeV_cYY_1.0'] = 'm_{ALP} = 4 GeV, c_{YY} = 1.0'
legend['ALP_Z_aa_5.GeV_cYY_1.0'] = 'm_{ALP} = 5 GeV, c_{#gamma#gamma} = 1.0'
legend['ALP_Z_aa_8.GeV_cYY_1.0'] = 'm_{ALP} = 8 GeV, c_{#gamma#gamma} = 1.0'

# legend['ALP_Z_aa_0.6.GeV_cYY_1.0'] = 'm_{ALP} = 0.6 GeV, c_{#gamma#gamma} = 1.0'
# legend['ALP_Z_aa_1.GeV_cYY_1.0'] = 'm_{ALP} = 1 GeV, c_{#gamma#gamma} = 1.0'
# legend['ALP_Z_aa_1.2.GeV_cYY_1.0'] = 'm_{ALP} = 1.2 GeV, c_{#gamma#gamma} = 1.0'
# legend['ALP_Z_aa_1.4.GeV_cYY_1.0'] = 'm_{ALP} = 1.4 GeV, c_{#gamma#gamma} = 1.0'

# legend['ALP_Z_aa_3.GeV_cYY_0.1'] = 'm_{ALP} = 3 GeV, c_{YY} = 0.1'
# legend['ALP_Z_aa_3.GeV_cYY_0.3'] = 'm_{ALP} = 3 GeV, c_{YY} = 0.3'
# legend['ALP_Z_aa_3.GeV_cYY_0.5'] = 'm_{ALP} = 3 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_3.GeV_cYY_0.7'] = 'm_{ALP} = 3 GeV, c_{YY} = 0.7'
# legend['ALP_Z_aa_3.GeV_cYY_0.9'] = 'm_{ALP} = 3 GeV, c_{YY} = 0.9'

# legend['ALP_Z_aa_5.GeV_cYY_0.1'] = 'm_{ALP} = 5 GeV, c_{YY} = 0.1'
# legend['ALP_Z_aa_5.GeV_cYY_0.3'] = 'm_{ALP} = 5 GeV, c_{YY} = 0.3'
# legend['ALP_Z_aa_5.GeV_cYY_0.5'] = 'm_{ALP} = 5 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_5.GeV_cYY_0.7'] = 'm_{ALP} = 5 GeV, c_{YY} = 0.7'
# legend['ALP_Z_aa_5.GeV_cYY_0.9'] = 'm_{ALP} = 5 GeV, c_{YY} = 0.9'

# legend['ALP_Z_aa_0.5GeV_cYY_0.5'] = 'm_{ALP} = 0.5 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_0.7GeV_cYY_0.5'] = 'm_{ALP} = 0.7 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_1.GeV_cYY_0.5'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_3.GeV_cYY_0.5'] = 'm_{ALP} = 3 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_5.GeV_cYY_0.5'] = 'm_{ALP} = 5 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_7.GeV_cYY_0.5'] = 'm_{ALP} = 7 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_10.GeV_cYY_0.5'] = 'm_{ALP} = 10 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_15.GeV_cYY_0.5'] = 'm_{ALP} = 15 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_20.GeV_cYY_0.5'] = 'm_{ALP} = 20 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_25.GeV_cYY_0.5'] = 'm_{ALP} = 25 GeV, c_{YY} = 0.5'
# legend['ALP_Z_aa_30.GeV_cYY_0.5'] = 'm_{ALP} = 30 GeV, c_{YY} = 0.5'

# legend['ee_Z_ALPga_gagaga'] = 'm_{ALP} = 1 GeV, c_{YY} = 0.5'

# legend['p8_ee_Zee_ecm91'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ee'
# legend['ee_gaga_1million'] = 'e^{+}e^{-} #rightarrow YY'
# legend['test1'] = 'e^{+}e^{-} #rightarrow YY'
# legend['test4'] = 'e^{+}e^{-} #rightarrow YYY'
# legend['ee_gammagamma'] = 'e^{+}e^{-} #rightarrow YY (spring2021)'
# legend['ee_gaga_test'] = 'e^{+}e^{-} #rightarrow YY'
# legend['ee_aa'] = 'e^{+}e^{-} #rightarrow #gamma#gamma'
# legend['ee_aaa'] = 'e^{+}e^{-} #rightarrow #gamma#gamma#gamma'
# legend['ee_aaaa'] = 'e^{+}e^{-} #rightarrow #gamma#gamma#gamma#gamma'
