'''
Analysis for ALP study: e⁺e⁻ → aγ → γγγ
'''
from argparse import ArgumentParser

#TODO: would be nice to have some sort of cme "tag" to select events rather than commenting/uncommenting blocks of code

# Mandatory: Analysis class where the user defines the operations on the dataframe
class Analysis():
    '''
    Generator-level ALP properties from Delphes + Pythia output.
    '''
    def __init__(self, cmdline_args):
        parser = ArgumentParser(description='Additional analysis arguments', usage='Provided after "--"')
        self.ana_args, _ = parser.parse_known_args(cmdline_args['remaining'])

        # Mandatory: List of datasets used in the analysis
        self.process_list = {
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
        
        # Optional: number of threads to run on, default is 'all available'
        # self.n_threads = 4

        # Optional: batch queue name when running on HTCondor, default is 'longlunch'
        # self.batch_queue = 'longlunch'

        # Optional: computing account when running on CERN's HTCondor, default is 'group_u_FCC.local_gen'
        # self.comp_group = 'group_u_FCC.local_gen'

        # Input/output directories
        # uncomment the input directory you want to use
        self.input_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/pythiadelphes/zpole_samples'
        # self.input_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/pythiadelphes/ww_samples/'
        # self.input_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/pythiadelphes/zh_samples/'
        # self.input_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/pythiadelphes/tt_samples/'
        self.output_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/stage1/zpole_samples'
        # self.output_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/stage1/ww_samples'
        # self.output_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/stage1/zh_samples'
        # self.output_dir = '/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/stage1/tt_samples'

        # Optional HTCondor settings
        # self.run_batch = True
        # self.batch_queue = 'longlunch'
        # self.comp_group = 'group_u_FCC.local_gen'

        # Optional: number of threads
        # self.n_threads = 4

    # Mandatory: analyzers function to define the analysis graph
    def analyzers(self, df):
        '''
        Generator-level particle properties.
        '''
        df = df.Alias("MCRecoAssociations0", "_RecoMCLink_from.index")
        df = df.Alias("MCRecoAssociations1", "_RecoMCLink_to.index")

        df2 = (
            df
            .Alias("Particle1",                                             "_Particle_daughters.index")
            .Define("GenALP_PID",                                           "MCParticle::sel_pdgID(9000005,false)(Particle)")
            .Define("Calorimeterhit_time",                                  "CalorimeterHits.time")
            .Define("All_n_GenALP",                                         "MCParticle::get_n(GenALP_PID)")
            .Define("AllGenALP_mass",                                       "MCParticle::get_mass(GenALP_PID)")
            .Define("AllGenALP_e",                                          "MCParticle::get_e(GenALP_PID)")     
            .Define("AllGenALP_p",                                          "MCParticle::get_p(GenALP_PID)")
            .Define("AllGenALP_pt",                                         "MCParticle::get_pt(GenALP_PID)")   
            .Define("AllGenALP_px",                                         "MCParticle::get_px(GenALP_PID)")
            .Define("AllGenALP_py",                                         "MCParticle::get_py(GenALP_PID)")
            .Define("AllGenALP_pz",                                         "MCParticle::get_pz(GenALP_PID)")
            .Define("AllGenALP_eta",                                        "MCParticle::get_eta(GenALP_PID)")
            .Define("AllGenALP_theta",                                      "MCParticle::get_theta(GenALP_PID)")
            .Define("AllGenALP_phi",                                        "MCParticle::get_phi(GenALP_PID)")
            .Define("AllGenALP_genStatus",                                  "MCParticle::get_genStatus(GenALP_PID)")
            .Define("GenElectron_PID",                                      "MCParticle::sel_pdgID(11,false)(Particle)") 
            .Define("FSGenElectron",                                        "MCParticle::sel_genStatus(1)(GenElectron_PID)") 
            .Define("n_FSGenElectron",                                      "MCParticle::get_n(FSGenElectron)")
            .Define("FSGenElectron_e",                                      "MCParticle::get_e(FSGenElectron)")
            .Define("FSGenElectron_p",                                      "MCParticle::get_p(FSGenElectron)")
            .Define("FSGenElectron_pt",                                     "MCParticle::get_pt(FSGenElectron)")
            .Define("FSGenElectron_pz",                                     "MCParticle::get_pz(FSGenElectron)")
            .Define("FSGenElectron_eta",                                    "MCParticle::get_eta(FSGenElectron)")
            .Define("FSGenElectron_theta",                                  "MCParticle::get_theta(FSGenElectron)")
            .Define("FSGenElectron_phi",                                    "MCParticle::get_phi(FSGenElectron)")
            .Define("GenElectronPositron_PID",                              "MCParticle::sel_pdgID(11,true)(Particle)") 
            .Define("FSGenElectronPositron",                                "MCParticle::sel_genStatus(1)(GenElectronPositron_PID)") 
            .Define("n_FSGenElectronPositron",                              "MCParticle::get_n(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_e",                              "MCParticle::get_e(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_p",                              "MCParticle::get_p(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_pt",                             "MCParticle::get_pt(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_px",                             "MCParticle::get_px(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_py",                             "MCParticle::get_py(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_pz",                             "MCParticle::get_pz(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_eta",                            "MCParticle::get_eta(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_theta",                          "MCParticle::get_theta(FSGenElectronPositron)")
            .Define("FSGenElectronPositron_phi",                            "MCParticle::get_phi(FSGenElectronPositron)")
            .Define("GenPositron_PID",                                      "MCParticle::sel_pdgID(-11,false)(Particle)")
            .Define("FSGenPositron",                                        "MCParticle::sel_genStatus(1)(GenPositron_PID)") 
            .Define("n_FSGenPositron",                                      "MCParticle::get_n(FSGenPositron)")
            .Define("FSGenPositron_e",                                      "MCParticle::get_e(FSGenPositron)")
            .Define("FSGenPositron_p",                                      "MCParticle::get_p(FSGenPositron)")
            .Define("FSGenPositron_pt",                                     "MCParticle::get_pt(FSGenPositron)")
            .Define("FSGenPositron_px",                                     "MCParticle::get_px(FSGenPositron)")
            .Define("FSGenPositron_py",                                     "MCParticle::get_py(FSGenPositron)")
            .Define("FSGenPositron_pz",                                     "MCParticle::get_pz(FSGenPositron)")
            .Define("FSGenPositron_eta",                                    "MCParticle::get_eta(FSGenPositron)")
            .Define("FSGenPositron_theta",                                  "MCParticle::get_theta(FSGenPositron)")
            .Define("FSGenPositron_phi",                                    "MCParticle::get_phi(FSGenPositron)")
            .Define("GenPhoton_PID",                                        "MCParticle::sel_pdgID(22,false)(Particle)")
            .Define("FSGenPhoton",                                          "MCParticle::sel_genStatus(1)(GenPhoton_PID)") 
            .Define("n_FSGenPhoton",                                        "MCParticle::get_n(FSGenPhoton)")
            .Define("FSGenPhoton_e",                                        "MCParticle::get_e(FSGenPhoton)")
            .Define("FSGenPhoton_p",                                        "MCParticle::get_p(FSGenPhoton)")
            .Define("FSGenPhoton_pt",                                       "MCParticle::get_pt(FSGenPhoton)")
            .Define("FSGenPhoton_px",                                       "MCParticle::get_px(FSGenPhoton)")
            .Define("FSGenPhoton_py",                                       "MCParticle::get_py(FSGenPhoton)")
            .Define("FSGenPhoton_pz",                                       "MCParticle::get_pz(FSGenPhoton)")
            .Define("FSGenPhoton_eta",                                      "MCParticle::get_eta(FSGenPhoton)")
            .Define("FSGenPhoton_theta",                                    "MCParticle::get_theta(FSGenPhoton)")
            .Define("FSGenPhoton_phi",                                      "MCParticle::get_phi(FSGenPhoton)")
            .Define("FSGenPhoton_vertex_x",                                 "MCParticle::get_vertex_x(FSGenPhoton)")
            .Define("FSGenPhoton_vertex_y",                                 "MCParticle::get_vertex_y(FSGenPhoton)")
            .Define("FSGenPhoton_vertex_z",                                 "MCParticle::get_vertex_z(FSGenPhoton)")
            .Define("FSGen_Lxy",                                            "return sqrt(FSGenPhoton_vertex_x*FSGenPhoton_vertex_x + FSGenPhoton_vertex_y*FSGenPhoton_vertex_y)")
            .Define("FSGen_Lxyz",                                           "return sqrt(FSGenPhoton_vertex_x*FSGenPhoton_vertex_x + FSGenPhoton_vertex_y*FSGenPhoton_vertex_y + FSGenPhoton_vertex_z*FSGenPhoton_vertex_z)")
            .Define("FSGenPhoton0_e",                                       "if (n_FSGenPhoton >= 1) {return FSGenPhoton_e.at(0);}  else {return (-2.0f); }")
            .Define("FSGenPhoton1_e",                                       "if (n_FSGenPhoton >= 2) {return FSGenPhoton_e.at(1);}  else {return (-2.0f); }")
            .Define("FSGenPhoton2_e",                                       "if (n_FSGenPhoton >= 3) {return FSGenPhoton_e.at(2);}  else {return (-2.0f); }")
            .Define("FSGenPhoton0_p",                                       "if (n_FSGenPhoton >= 1) {return FSGenPhoton_p.at(0);}  else {return (-2.0f); }")
            .Define("FSGenPhoton1_p",                                       "if (n_FSGenPhoton >= 2) {return FSGenPhoton_p.at(1);}  else {return (-2.0f); }")
            .Define("FSGenPhoton2_p",                                       "if (n_FSGenPhoton >= 3) {return FSGenPhoton_p.at(2);}  else {return (-2.0f); }")
            .Define("FSGenPhoton0_pt",                                      "if (n_FSGenPhoton >= 1) {return FSGenPhoton_pt.at(0);} else {return (-2.0f); }")
            .Define("FSGenPhoton1_pt",                                      "if (n_FSGenPhoton >= 2) {return FSGenPhoton_pt.at(1);} else {return (-2.0f); }")
            .Define("FSGenPhoton2_pt",                                      "if (n_FSGenPhoton >= 3) {return FSGenPhoton_pt.at(2);} else {return (-2.0f); }")
            .Define("FSGenPhoton0_px",                                      "if (n_FSGenPhoton >= 1) {return FSGenPhoton_px.at(0);} else {return (-2.0f); }")
            .Define("FSGenPhoton1_px",                                      "if (n_FSGenPhoton >= 2) {return FSGenPhoton_px.at(1);} else {return (-2.0f); }")
            .Define("FSGenPhoton2_px",                                      "if (n_FSGenPhoton >= 3) {return FSGenPhoton_px.at(2);} else {return (-2.0f); }")
            .Define("FSGenPhoton0_py",                                      "if (n_FSGenPhoton >= 1) {return FSGenPhoton_py.at(0);} else {return (-2.0f); }")
            .Define("FSGenPhoton1_py",                                      "if (n_FSGenPhoton >= 2) {return FSGenPhoton_py.at(1);} else {return (-2.0f); }")
            .Define("FSGenPhoton2_py",                                      "if (n_FSGenPhoton >= 3) {return FSGenPhoton_py.at(2);} else {return (-2.0f); }")
            .Define("FSGenPhoton0_pz",                                      "if (n_FSGenPhoton >= 1) {return FSGenPhoton_pz.at(0);} else {return (-2.0f); }")
            .Define("FSGenPhoton1_pz",                                      "if (n_FSGenPhoton >= 2) {return FSGenPhoton_pz.at(1);} else {return (-2.0f); }")
            .Define("FSGenPhoton2_pz",                                      "if (n_FSGenPhoton >= 3) {return FSGenPhoton_pz.at(2);} else {return (-2.0f); }")
            .Define("FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0",     "if (FSGenPhoton0_px > 0) {return FSGenPhoton1_px;} else {return -50.0f;}")
            .Define("FSGenPhoton1_px_if_FSGenPhoton2_px_pos",               "if (FSGenPhoton2_px > 0) {return FSGenPhoton1_px;} else {return -50.0f;}")
            .Define("FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos",               "if (FSGenPhoton2_pz > 0) {return FSGenPhoton1_pz;} else {return -50.0f;}")
            .Define("GenALP_indices",                                       "MCParticle::get_indices(9000005, {22, 22}, true, false, false, true)(Particle, Particle1)")
            .Define("GenALP",                                               "myUtils::selMC_leg(0)(GenALP_indices, Particle)")
            .Define("GenALPPhoton1",                                        "myUtils::selMC_leg(1)(GenALP_indices, Particle)")
            .Define("GenALPPhoton2",                                        "myUtils::selMC_leg(2)(GenALP_indices, Particle)")
            .Define("FSGenALP",                                             "MCParticle::sel_genStatus(1)(GenALP_PID)")
            .Define("n_FSGenALP",                                           "MCParticle::get_n(FSGenALP)")
            .Define("FSGenALP_mass",                                        "MCParticle::get_mass(FSGenALP)")
            .Define("FSGenALP_e",                                           "MCParticle::get_e(FSGenALP)")
            .Define("FSGenALP_p",                                           "MCParticle::get_p(FSGenALP)")
            .Define("FSGenALP_pt",                                          "MCParticle::get_pt(FSGenALP)")
            .Define("FSGenALP_px",                                          "MCParticle::get_px(FSGenALP)")
            .Define("FSGenALP_py",                                          "MCParticle::get_py(FSGenALP)")
            .Define("FSGenALP_pz",                                          "MCParticle::get_pz(FSGenALP)")
            .Define("FSGenALP_eta",                                         "MCParticle::get_eta(FSGenALP)")
            .Define("FSGenALP_theta",                                       "MCParticle::get_theta(FSGenALP)")
            .Define("FSGenALP_phi",                                         "MCParticle::get_phi(FSGenALP)")
            .Define("FSGenALP_genStatus",                                   "MCParticle::get_genStatus(FSGenALP)")
            .Define("GenALP_mass",                                          "MCParticle::get_mass(GenALP)")
            .Define("GenALP_e",                                             "MCParticle::get_e(GenALP)")
            .Define("GenALP_p",                                             "MCParticle::get_p(GenALP)")
            .Define("GenALP_pt",                                            "MCParticle::get_pt(GenALP)")
            .Define("GenALP_px",                                            "MCParticle::get_px(GenALP)")
            .Define("GenALP_py",                                            "MCParticle::get_py(GenALP)")
            .Define("GenALP_pz",                                            "MCParticle::get_pz(GenALP)")
            .Define("GenALP_eta",                                           "MCParticle::get_eta(GenALP)")
            .Define("GenALP_theta",                                         "MCParticle::get_theta(GenALP)")
            .Define("GenALP_phi",                                           "MCParticle::get_phi(GenALP)")
            .Define("GenALP_genStatus",                                     "MCParticle::get_genStatus(GenALP)")
            .Define("GenALP_beta",                                          "return GenALP_p / GenALP_e")
            .Define("GenALP_px_if_FSGenPhoton0_px_greaterthan_0",           "if (FSGenPhoton0_px > 0) {return GenALP_px[0];} else {return -50.0f;}")
            .Define("FSGenPhoton1_px_if_GenALP_px_neg",                     "if (GenALP_px[0] < 0) {return FSGenPhoton1_px;} else {return -50.0f;}")
            .Define("FSGenPhoton2_px_if_GenALP_px_neg",                     "if (GenALP_px[0] < 0) {return FSGenPhoton2_px;} else {return -50.0f;}")
            .Define("n_GenALP",                                             "MCParticle::get_n(GenALP)")
            .Define("GenALP_time",                                          "MCParticle::get_time(GenALP)")        
            .Define("GenALP_pdg",                                           "MCParticle::get_pdg(GenALP)")
            .Define("GenALP_endPoint_x",                                    "MCParticle::get_endPoint_x")
            .Define("n_GenALPPhoton1",                                      "MCParticle::get_n(GenALPPhoton1)")
            .Define("n_GenALPPhoton2",                                      "MCParticle::get_n(GenALPPhoton2)")
            .Define("GenALPPhoton1_e",                                      "MCParticle::get_e(GenALPPhoton1)")
            .Define("GenALPPhoton2_e",                                      "MCParticle::get_e(GenALPPhoton2)")
            .Define("GenALPPhoton1_p",                                      "MCParticle::get_p(GenALPPhoton1)")
            .Define("GenALPPhoton2_p",                                      "MCParticle::get_p(GenALPPhoton2)")
            .Define("GenALPPhoton1_pt",                                     "MCParticle::get_pt(GenALPPhoton1)")
            .Define("GenALPPhoton2_pt",                                     "MCParticle::get_pt(GenALPPhoton2)")
            .Define("GenALPPhoton1_px",                                     "MCParticle::get_px(GenALPPhoton1)")
            .Define("GenALPPhoton2_px",                                     "MCParticle::get_px(GenALPPhoton2)")
            .Define("GenALPPhoton1_py",                                     "MCParticle::get_py(GenALPPhoton1)")
            .Define("GenALPPhoton2_py",                                     "MCParticle::get_py(GenALPPhoton2)")
            .Define("GenALPPhoton1_pz",                                     "MCParticle::get_pz(GenALPPhoton1)")
            .Define("GenALPPhoton2_pz",                                     "MCParticle::get_pz(GenALPPhoton2)")
            .Define("GenALPPhoton1_eta",                                    "MCParticle::get_eta(GenALPPhoton1)")
            .Define("GenALPPhoton2_eta",                                    "MCParticle::get_eta(GenALPPhoton2)")
            .Define("GenALPPhoton1_theta",                                  "MCParticle::get_theta(GenALPPhoton1)")
            .Define("GenALPPhoton2_theta",                                  "MCParticle::get_theta(GenALPPhoton2)")
            .Define("GenALPPhoton1_phi",                                    "MCParticle::get_phi(GenALPPhoton1)")
            .Define("GenALPPhoton2_phi",                                    "MCParticle::get_phi(GenALPPhoton2)")
            .Define("GenALPPhoton1_genStatus",                              "MCParticle::get_genStatus(GenALPPhoton1)")
            .Define("GenALPPhoton2_genStatus",                              "MCParticle::get_genStatus(GenALPPhoton2)")
            .Define("GenALPPhotons_deltaEta",                               "return abs(GenALPPhoton1_eta - GenALPPhoton2_eta)")
            .Define("GenALPPhotons_deltaPhi",                               "return abs(GenALPPhoton1_phi - GenALPPhoton2_phi)")
            .Define("GenALPPhotons_deltaR",                                 "return sqrt(GenALPPhotons_deltaEta*GenALPPhotons_deltaEta + GenALPPhotons_deltaPhi*GenALPPhotons_deltaPhi)")
            .Define("FSGenPhotons_delta_r",                                 "MCParticle::get_delta_r(FSGenPhoton)")
            .Define("FSGenPhotons_min_delta_r",                             "MCParticle::get_min_delta_r(FSGenPhoton)")
            .Define("GenALPPhoton1_time",                                   "MCParticle::get_time(GenALPPhoton1)")
            .Define("GenALPPhoton2_time",                                   "MCParticle::get_time(GenALPPhoton2)")
            .Define("GenALPPhoton1_vertex_x",                               "MCParticle::get_vertex_x(GenALPPhoton1)")
            .Define("GenALPPhoton1_vertex_y",                               "MCParticle::get_vertex_y(GenALPPhoton1)")
            .Define("GenALPPhoton1_vertex_z",                               "MCParticle::get_vertex_z(GenALPPhoton1)")
            .Define("GenALP_Lxy",                                           "return sqrt(GenALPPhoton1_vertex_x*GenALPPhoton1_vertex_x + GenALPPhoton1_vertex_y*GenALPPhoton1_vertex_y)")
            .Define("GenALP_Lxyz",                                          "return sqrt(GenALPPhoton1_vertex_x*GenALPPhoton1_vertex_x + GenALPPhoton1_vertex_y*GenALPPhoton1_vertex_y + GenALPPhoton1_vertex_z*GenALPPhoton1_vertex_z)")
            .Define("GenALP_lifetime_xy",                                   "return (GenALP_Lxy * GenALP_mass / (GenALP_pt * 3E8 * 1000))" )
            .Define("GenALP_lifetime_xyz",                                  "return (GenALP_Lxyz * GenALP_mass / (GenALP_p  * 3E8 * 1000))" )
            .Define("GenALP_observed_lifetime_xyz",                         "return ((GenALP_p / GenALP_mass) * GenALP_lifetime_xyz)")
            .Define("GenALPPhoton1_time_minus_GenALP_time",                 "return (GenALPPhoton1_time - GenALP_time)")
            .Define("GenALP_vertex_x",                                      "MCParticle::get_vertex_x(GenALP_PID)")
            .Define("GenALP_vertex_y",                                      "MCParticle::get_vertex_y(GenALP_PID)")
            .Define("GenALP_vertex_z",                                      "MCParticle::get_vertex_z(GenALP_PID)")
            .Define("GenALP_aa_energy",                                     "return (GenALPPhoton1_e  + GenALPPhoton2_e)")
            .Define("GenALP_aa_px",                                         "return (GenALPPhoton1_px + GenALPPhoton2_px)")
            .Define("GenALP_aa_py",                                         "return (GenALPPhoton1_py + GenALPPhoton2_py)")
            .Define("GenALP_aa_pz",                                         "return (GenALPPhoton1_pz + GenALPPhoton2_pz)")
            .Define("GenALP_aa_invMass",                                    "return sqrt(GenALP_aa_energy*GenALP_aa_energy - GenALP_aa_px*GenALP_aa_px - GenALP_aa_py*GenALP_aa_py - GenALP_aa_pz*GenALP_aa_pz )")
            .Define("MC_PrimaryVertex",                                     "MCParticle::get_EventPrimaryVertex(21)(Particle)")
            .Define("n_RecoTracks",                                         "ReconstructedParticle2Track::getTK_n(_EFlowTrack_trackStates)")
            .Define("RecoALPParticles",                                     "ReconstructedParticle2MC::selRP_matched_to_list(GenALP_indices, MCRecoAssociations0,MCRecoAssociations1,ReconstructedParticles,Particle)")
            .Define("RecoALPTracks",                                        "ReconstructedParticle2Track::getRP2TRK(RecoALPParticles, _EFlowTrack_trackStates)")
            .Define("n_RecoALPTracks",                                      "ReconstructedParticle2Track::getTK_n(RecoALPTracks)")
            .Define("RecoALPDecayVertexObject",                             "VertexFitterSimple::VertexFitter_Tk(2, RecoALPTracks)") 
            .Define("RecoALPDecayVertex",                                   "VertexingUtils::get_VertexData(RecoALPDecayVertexObject)")
            .Define("RecoALPL_xyz",                                         "return sqrt(RecoALPDecayVertex.position.x*RecoALPDecayVertex.position.x + RecoALPDecayVertex.position.y*RecoALPDecayVertex.position.y + RecoALPDecayVertex.position.z*RecoALPDecayVertex.position.z)")
            .Define("RecoALPPhoton1",                                       "myUtils::selRP_leg(0)(RecoALPParticles)")
            .Define("RecoALPPhoton2",                                       "myUtils::selRP_leg(1)(RecoALPParticles)")
            .Define("RecoALPPhoton1_e",                                     "ReconstructedParticle::get_e(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_e",                                     "ReconstructedParticle::get_e(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_p",                                     "ReconstructedParticle::get_p(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_p",                                     "ReconstructedParticle::get_p(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_pt",                                    "ReconstructedParticle::get_pt(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_pt",                                    "ReconstructedParticle::get_pt(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_px",                                    "ReconstructedParticle::get_px(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_px",                                    "ReconstructedParticle::get_px(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_py",                                    "ReconstructedParticle::get_py(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_py",                                    "ReconstructedParticle::get_py(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_pz",                                    "ReconstructedParticle::get_pz(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_pz",                                    "ReconstructedParticle::get_pz(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_eta",                                   "ReconstructedParticle::get_eta(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_eta",                                   "ReconstructedParticle::get_eta(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_theta",                                 "ReconstructedParticle::get_theta(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_theta",                                 "ReconstructedParticle::get_theta(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_phi",                                   "ReconstructedParticle::get_phi(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_phi",                                   "ReconstructedParticle::get_phi(RecoALPPhoton2)")
            .Define("RecoALPPhoton1_charge",                                "ReconstructedParticle::get_charge(RecoALPPhoton1)")
            .Define("RecoALPPhoton2_charge",                                "ReconstructedParticle::get_charge(RecoALPPhoton2)")
            .Define("RecoALPPhotons_deltaEta",                              "return abs(RecoALPPhoton1_eta - RecoALPPhoton2_eta)")
            .Define("RecoALPPhotons_deltaPhi",                              "return RecoALPPhoton1_phi - RecoALPPhoton2_phi")
            .Define("RecoALPPhotons_deltaR",                                "if (RecoALPPhoton1.size() > 0 && RecoALPPhoton2.size() > 0) { "
                                                                            "return ReconstructedParticle::get_delta_r(RecoALPPhoton1.at(0), RecoALPPhoton2.at(0)); "
                                                                            "} else { return -2.0f; }")   
            .Define("n_RecoALPPhoton1",                                     "ReconstructedParticle::get_n(RecoALPPhoton1)")
            .Define("n_RecoALPPhoton2",                                     "ReconstructedParticle::get_n(RecoALPPhoton2)")
            .Define("RecoALP_aa_energy",                                    "return (RecoALPPhoton1_e  + RecoALPPhoton2_e)")
            .Define("RecoALP_aa_px",                                        "return (RecoALPPhoton1_px + RecoALPPhoton2_px)")
            .Define("RecoALP_aa_py",                                        "return (RecoALPPhoton1_py + RecoALPPhoton2_py)")
            .Define("RecoALP_aa_pz",                                        "return (RecoALPPhoton1_pz + RecoALPPhoton2_pz)")
            .Define("RecoALP_aa_invMass",                                   "return sqrt(RecoALP_aa_energy*RecoALP_aa_energy - RecoALP_aa_px*RecoALP_aa_px - RecoALP_aa_py*RecoALP_aa_py - RecoALP_aa_pz*RecoALP_aa_pz )")
            .Define("RecoALP_aa_p",                                         "return sqrt(RecoALP_aa_px*RecoALP_aa_px + RecoALP_aa_py*RecoALP_aa_py + RecoALP_aa_pz*RecoALP_aa_pz)")
            .Define("GenMinusRecoALPPhoton1_e",                             "GenALPPhoton1_e-RecoALPPhoton1_e")
            .Define("GenMinusRecoALPPhoton2_e",                             "GenALPPhoton2_e-RecoALPPhoton2_e")
            .Define("GenMinusRecoALPPhoton1_p",                             "GenALPPhoton1_p-RecoALPPhoton1_p")
            .Define("GenMinusRecoALPPhoton2_p",                             "GenALPPhoton2_p-RecoALPPhoton2_p")
            .Define("GenMinusRecoALPPhoton1_pt",                            "GenALPPhoton1_pt-RecoALPPhoton1_pt")
            .Define("GenMinusRecoALPPhoton2_pt",                            "GenALPPhoton2_pt-RecoALPPhoton2_pt")
            .Define("GenMinusRecoALPPhoton1_px",                            "GenALPPhoton1_px-RecoALPPhoton1_px")
            .Define("GenMinusRecoALPPhoton2_px",                            "GenALPPhoton2_px-RecoALPPhoton2_px")
            .Define("GenMinusRecoALPPhoton1_py",                            "GenALPPhoton1_py-RecoALPPhoton1_py")
            .Define("GenMinusRecoALPPhoton2_py",                            "GenALPPhoton2_py-RecoALPPhoton2_py")
            .Define("GenMinusRecoALPPhoton1_pz",                            "GenALPPhoton1_pz-RecoALPPhoton1_pz")
            .Define("GenMinusRecoALPPhoton2_pz",                            "GenALPPhoton2_pz-RecoALPPhoton2_pz")
            .Define("GenMinusRecoALPPhoton1_eta",                           "GenALPPhoton1_eta-RecoALPPhoton1_eta")
            .Define("GenMinusRecoALPPhoton2_eta",                           "GenALPPhoton2_eta-RecoALPPhoton2_eta")
            .Define("GenMinusRecoALPPhoton1_theta",                         "GenALPPhoton1_theta-RecoALPPhoton1_theta")
            .Define("GenMinusRecoALPPhoton2_theta",                         "GenALPPhoton2_theta-RecoALPPhoton2_theta")
            .Define("GenMinusRecoALPPhoton1_phi",                           "GenALPPhoton1_phi-RecoALPPhoton1_phi")
            .Define("GenMinusRecoALPPhoton2_phi",                           "GenALPPhoton2_phi-RecoALPPhoton2_phi")
            .Define("GenMinusRecoALP_DecayVertex_x",                        "GenALPPhoton1_vertex_x-RecoALPDecayVertex.position.x")
            .Define("GenMinusRecoALP_DecayVertex_y",                        "GenALPPhoton1_vertex_y-RecoALPDecayVertex.position.y")
            .Define("GenMinusRecoALP_DecayVertex_z",                        "GenALPPhoton1_vertex_z-RecoALPDecayVertex.position.z")
            .Define("n_RecoJets",                                           "ReconstructedParticle::get_n(Jet)")
            .Alias("Photon0",                                               "Photon_objIdx.index")
            .Define("RecoPhotons",                                          "ReconstructedParticle::get(Photon0, ReconstructedParticles)")
            .Define("n_RecoPhotons",                                        "ReconstructedParticle::get_n(RecoPhotons)") 
            .Alias("Electron0",                                             "Electron_objIdx.index")
            .Define("RecoElectrons",                                        "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
            .Define("n_RecoElectrons",                                      "ReconstructedParticle::get_n(RecoElectrons)") 
            .Alias("Muon0",                                                 "Muon_objIdx.index")
            .Define("RecoMuons",                                            "ReconstructedParticle::get(Muon0,ReconstructedParticles)")
            .Define("n_RecoMuons",                                          "ReconstructedParticle::get_n(RecoMuons)") 
            .Define("RecoElectron_e",                                       "ReconstructedParticle::get_e(RecoElectrons)")
            .Define("RecoElectron_p",                                       "ReconstructedParticle::get_p(RecoElectrons)")
            .Define("RecoElectron_pt",                                      "ReconstructedParticle::get_pt(RecoElectrons)")
            .Define("RecoElectron_pz",                                      "ReconstructedParticle::get_pz(RecoElectrons)")
            .Define("RecoElectron_eta",                                     "ReconstructedParticle::get_eta(RecoElectrons)") 
            .Define("RecoElectron_theta",                                   "ReconstructedParticle::get_theta(RecoElectrons)")
            .Define("RecoElectron_phi",                                     "ReconstructedParticle::get_phi(RecoElectrons)") 
            .Define("RecoPhoton_e",                                         "ReconstructedParticle::get_e(RecoPhotons)")
            .Define("RecoPhoton_p",                                         "ReconstructedParticle::get_p(RecoPhotons)")
            .Define("RecoPhoton_pt",                                        "ReconstructedParticle::get_pt(RecoPhotons)")
            .Define("RecoPhoton_px",                                        "ReconstructedParticle::get_px(RecoPhotons)")
            .Define("RecoPhoton_py",                                        "ReconstructedParticle::get_py(RecoPhotons)")
            .Define("RecoPhoton_pz",                                        "ReconstructedParticle::get_pz(RecoPhotons)")
            .Define("RecoPhoton_eta",                                       "ReconstructedParticle::get_eta(RecoPhotons)") 
            .Define("RecoPhoton_theta",                                     "ReconstructedParticle::get_theta(RecoPhotons)")
            .Define("RecoPhoton_phi",                                       "ReconstructedParticle::get_phi(RecoPhotons)") 
            .Define("RecoPhoton_charge",                                    "ReconstructedParticle::get_charge(RecoPhotons)")
            .Define("RecoPhotons_delta_eta",                                "ReconstructedParticle::get_delta_eta(RecoPhotons)")
            .Define("RecoPhotons_delta_phi",                                "ReconstructedParticle::get_delta_phi(RecoPhotons)")
            .Define("RecoPhotons_delta_r",                                  "ReconstructedParticle::get_delta_r(RecoPhotons)")
            .Define("RecoPhotons_min_delta_r",                              "ReconstructedParticle::get_min_delta_r(RecoPhotons)")
            .Define("RecoPhoton0_e",                                        "if (n_RecoPhotons >= 1) {return RecoPhoton_e.at(0);}  else {return (-2.0f); }")
            .Define("RecoPhoton1_e",                                        "if (n_RecoPhotons >= 2) {return RecoPhoton_e.at(1);}  else {return (-2.0f); }")
            .Define("RecoPhoton2_e",                                        "if (n_RecoPhotons >= 3) {return RecoPhoton_e.at(2);}  else {return (-2.0f); }")
            .Define("RecoPhoton0_p",                                        "if (n_RecoPhotons >= 1) {return RecoPhoton_p.at(0);}  else {return (-2.0f); }")
            .Define("RecoPhoton1_p",                                        "if (n_RecoPhotons >= 2) {return RecoPhoton_p.at(1);}  else {return (-2.0f); }")
            .Define("RecoPhoton2_p",                                        "if (n_RecoPhotons >= 3) {return RecoPhoton_p.at(2);}  else {return (-2.0f); }")
            .Define("RecoPhoton0_pt",                                       "if (n_RecoPhotons >= 1) {return RecoPhoton_pt.at(0);} else {return (-2.0f); }")
            .Define("RecoPhoton1_pt",                                       "if (n_RecoPhotons >= 2) {return RecoPhoton_pt.at(1);} else {return (-2.0f); }")
            .Define("RecoPhoton2_pt",                                       "if (n_RecoPhotons >= 3) {return RecoPhoton_pt.at(2);} else {return (-2.0f); }")
            .Define("RecoPhoton0_px",                                       "if (n_RecoPhotons >= 1) {return RecoPhoton_px.at(0);} else {return (-2.0f); }")
            .Define("RecoPhoton1_px",                                       "if (n_RecoPhotons >= 2) {return RecoPhoton_px.at(1);} else {return (-2.0f); }")
            .Define("RecoPhoton2_px",                                       "if (n_RecoPhotons >= 3) {return RecoPhoton_px.at(2);} else {return (-2.0f); }")
            .Define("RecoPhoton0_py",                                       "if (n_RecoPhotons >= 1) {return RecoPhoton_py.at(0);} else {return (-2.0f); }")
            .Define("RecoPhoton1_py",                                       "if (n_RecoPhotons >= 2) {return RecoPhoton_py.at(1);} else {return (-2.0f); }")
            .Define("RecoPhoton2_py",                                       "if (n_RecoPhotons >= 3) {return RecoPhoton_py.at(2);} else {return (-2.0f); }")
            .Define("RecoPhoton0_pz",                                       "if (n_RecoPhotons >= 1) {return RecoPhoton_pz.at(0);} else {return (-2.0f); }")
            .Define("RecoPhoton1_pz",                                       "if (n_RecoPhotons >= 2) {return RecoPhoton_pz.at(1);} else {return (-2.0f); }")
            .Define("RecoPhoton2_pz",                                       "if (n_RecoPhotons >= 3) {return RecoPhoton_pz.at(2);} else {return (-2.0f); }")
            .Define("Reco_aa_energy",                                       "return (RecoPhoton1_e  + RecoPhoton2_e)")
            .Define("Reco_aa_px",                                           "return (RecoPhoton1_px + RecoPhoton2_px)")
            .Define("Reco_aa_py",                                           "return (RecoPhoton1_py + RecoPhoton2_py)")
            .Define("Reco_aa_pz",                                           "return (RecoPhoton1_pz + RecoPhoton2_pz)")
            .Define("Reco_aa_invMass",                                      "if (Reco_aa_energy != -4.0f && Reco_aa_px != -4.0f && Reco_aa_py != -4.0f && Reco_aa_pz != -4.0f) { return sqrt(Reco_aa_energy*Reco_aa_energy - Reco_aa_px*Reco_aa_px - Reco_aa_py*Reco_aa_py - Reco_aa_pz*Reco_aa_pz); } else { return -2.0f; }")
            .Define("Reco_aa_p",                                            "if (Reco_aa_px != -4.0f && Reco_aa_py != -4.0f && Reco_aa_pz != -4.0f) { return sqrt(Reco_aa_px*Reco_aa_px + Reco_aa_py*Reco_aa_py + Reco_aa_pz*Reco_aa_pz); } else { return -2.0f; }")
            .Define("RecoPhoton1_px_if_RecoPhoton2_px_pos",                 "if (RecoPhoton2_px > 0) {return RecoPhoton1_px;} else {return -50.0f;}")
            .Define("RecoPhoton1_pz_if_RecoPhoton2_pz_pos",                 "if (RecoPhoton2_pz > 0) {return RecoPhoton1_pz;} else {return -50.0f;}")
            .Define("RecoALPPhotons_delta_R3",                              "if (n_RecoPhotons == 3) {return RecoPhotons_delta_r.at(2);} else {return (-2.0f); }")
            .Define("RecoMuon_e",                                           "ReconstructedParticle::get_e(RecoMuons)")
            .Define("RecoMuon_p",                                           "ReconstructedParticle::get_p(RecoMuons)")
            .Define("RecoMuon_pt",                                          "ReconstructedParticle::get_pt(RecoMuons)")
            .Define("RecoMuon_px",                                          "ReconstructedParticle::get_px(RecoMuons)")
            .Define("RecoMuon_py",                                          "ReconstructedParticle::get_py(RecoMuons)")
            .Define("RecoMuon_pz",                                          "ReconstructedParticle::get_pz(RecoMuons)")
            .Define("RecoMuon_eta",                                         "ReconstructedParticle::get_eta(RecoMuons)")
            .Define("RecoMuon_theta",                                       "ReconstructedParticle::get_theta(RecoMuons)")
            .Define("RecoMuon_phi",                                         "ReconstructedParticle::get_phi(RecoMuons)")
            .Define("RecoMuon_charge",                                      "ReconstructedParticle::get_charge(RecoMuons)")
        )

        return df2

    # Mandatory: output function
    def output(self):
        '''
        Output branches to be saved in the final ROOT file.
        '''
        branch_list = [
            "Calorimeterhit_time",
            "All_n_GenALP",
            "AllGenALP_mass",
            "AllGenALP_e",
            "AllGenALP_p",
            "AllGenALP_pt",
            "AllGenALP_px",
            "AllGenALP_py",
            "AllGenALP_pz",
            "AllGenALP_eta",
            "AllGenALP_theta",
            "AllGenALP_phi",
            "AllGenALP_genStatus",
            "n_FSGenElectron",
            "FSGenElectron_e",
            "FSGenElectron_p",
            "FSGenElectron_pt",
            "FSGenElectron_pz",
            "FSGenElectron_eta",
            "FSGenElectron_theta",
            "FSGenElectron_phi",
            "FSGenPhoton_vertex_x",
            "FSGenPhoton_vertex_y",
            "FSGenPhoton_vertex_z",
            "n_FSGenElectronPositron",
            "FSGenElectronPositron_e",
            "FSGenElectronPositron_p",
            "FSGenElectronPositron_pt",
            "FSGenElectronPositron_px",
            "FSGenElectronPositron_py",
            "FSGenElectronPositron_pz",
            "FSGenElectronPositron_eta",
            "FSGenElectronPositron_theta",
            "FSGenElectronPositron_phi",
            "FSGen_Lxy",
            "FSGen_Lxyz",
            "n_FSGenPhoton",
            "FSGenPhoton_e",
            "FSGenPhoton_p",
            "FSGenPhoton_pt",
            "FSGenPhoton_px",
            "FSGenPhoton_py",
            "FSGenPhoton_pz",
            "FSGenPhoton_eta",
            "FSGenPhoton_theta",
            "FSGenPhoton_phi",
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
            "GenALP_vertex_x",
            "GenALP_vertex_y",
            "GenALP_vertex_z",
            "GenALP_aa_invMass",
            "GenALP_mass",
            "GenALP_e",
            "GenALP_p",
            "GenALP_pt",
            "GenALP_pz",
            "GenALP_eta",
            "GenALP_theta",
            "GenALP_phi",
            "GenALP_genStatus",
            "GenALP_beta",
            "GenALP_px_if_FSGenPhoton0_px_greaterthan_0",
            "FSGenPhoton1_px_if_GenALP_px_neg",
            "FSGenPhoton2_px_if_GenALP_px_neg",
            "GenALPPhotons_deltaEta",
            "GenALPPhotons_deltaPhi",
            "GenALPPhotons_deltaR",
            "FSGenPhotons_delta_r",
            "FSGenPhotons_min_delta_r",
            "GenALPPhoton1_time",
            "GenALPPhoton2_time",
            "GenALP_observed_lifetime_xyz",
            "GenALPPhoton1_time_minus_GenALP_time",
            "n_GenALP",
            "GenALP_time",
            "GenALP_pdg",
            "n_FSGenALP",
            "FSGenALP_mass",
            "FSGenALP_p",
            "FSGenALP_pt",
            "FSGenALP_pz",
            "FSGenALP_eta",
            "FSGenALP_theta",
            "FSGenALP_phi",
            "FSGenALP_genStatus",
            "n_GenALPPhoton1",
            "n_GenALPPhoton2",
            "GenALPPhoton1_e",
            "GenALPPhoton2_e",
            "GenALPPhoton1_p",
            "GenALPPhoton2_p",
            "GenALPPhoton1_pt",
            "GenALPPhoton2_pt",
            "GenALPPhoton1_px",
            "GenALPPhoton2_px",
            "GenALPPhoton1_py",
            "GenALPPhoton2_py",
            "GenALPPhoton1_pz",
            "GenALPPhoton2_pz",
            "GenALPPhoton1_eta",
            "GenALPPhoton2_eta",
            "GenALPPhoton1_theta",
            "GenALPPhoton2_theta",
            "GenALPPhoton1_phi",
            "GenALPPhoton2_phi",
            "GenALPPhoton1_genStatus",
            "GenALPPhoton2_genStatus",
            "GenALPPhoton1_vertex_x",
            "GenALPPhoton1_vertex_y",
            "GenALPPhoton1_vertex_z",
            "GenALP_Lxy",
            "GenALP_Lxyz",
            "GenALP_lifetime_xy",
            "GenALP_lifetime_xyz",
            "MC_PrimaryVertex",
            "n_RecoTracks",
            "RecoALPParticles",
            "RecoALPTracks",
            "n_RecoALPTracks",
            "RecoALPDecayVertexObject",
            "RecoALPDecayVertex",
            "RecoALPL_xyz",
            "RecoALPPhoton1_e",
            "RecoALPPhoton2_e",
            "RecoALPPhoton1_p",
            "RecoALPPhoton2_p",
            "RecoALPPhoton1_pt",
            "RecoALPPhoton2_pt",
            "RecoALPPhoton1_px",
            "RecoALPPhoton2_px",
            "RecoALPPhoton1_py",
            "RecoALPPhoton2_py",
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
            "n_RecoALPPhoton1",
            "n_RecoALPPhoton2",
            "RecoALPPhotons_deltaEta",
            "RecoALPPhotons_deltaPhi",
            "RecoALPPhotons_deltaR",
            "RecoALP_aa_invMass",
            "RecoALP_aa_p",
            "RecoALP_aa_energy",
            "Reco_aa_invMass",
            "Reco_aa_p",
            "GenMinusRecoALPPhoton1_e",
            "GenMinusRecoALPPhoton2_e",
            "GenMinusRecoALP_DecayVertex_x",
            "GenMinusRecoALP_DecayVertex_y",
            "GenMinusRecoALP_DecayVertex_z",
            "n_RecoJets",
            "n_RecoPhotons",
            "n_RecoElectrons",
            "n_RecoMuons",
            "RecoPhoton_e",
            "RecoPhoton_p",
            "RecoPhoton_pt",
            "RecoPhoton_px",
            "RecoPhoton_py",
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
            "RecoPhoton1_px_if_RecoPhoton2_px_pos",
            "RecoPhoton1_pz_if_RecoPhoton2_pz_pos",
            "RecoALPPhotons_delta_R3",
            "RecoElectron_e",
            "RecoElectron_p",
            "RecoElectron_pt",
            "RecoElectron_pz",
            "RecoElectron_eta",
            "RecoElectron_theta",
            "RecoElectron_phi",
        ]
        return branch_list
