import ROOT

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5':{},
        'exoticHiggs_scalar_ms20GeV_sine-6':{},
        'exoticHiggs_scalar_ms20GeV_sine-7':{},
        'exoticHiggs_scalar_ms60GeV_sine-5':{},
        'exoticHiggs_scalar_ms60GeV_sine-6':{},
        'exoticHiggs_scalar_ms60GeV_sine-7':{},

        # #centrally produced backgrounds
        # 'p8_ee_ZH_ecm240':{'fraction':0.01},
        # 'p8_ee_ZZ_ecm240':{'fraction':0.01},   
        # 'p8_ee_WW_ecm240':{'fraction':0.01},     
}

#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
#prodTag     = "FCCee/spring2021/IDEA/"


#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events
inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/output_MadgraphPythiaDelphes/"


#Optional: output directory, default is local dir
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/Reco_output_stage1/"
#outputDirEos = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/Reco_output_stage1/"
outputDir = "Reco_output_stage1/"

#Optional: ncpus, default is 4
nCPUS       = 8

#Optional running on HTCondor, default is False
runBatch    = False
#runBatch    = True

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
#compGroup = "group_u_FCC.local_gen"

#USER DEFINED CODE
# For costum displaced vertex selection, apply selection on the DVs with invariant mass higher than 1 GeV and distance from PV to DV less than 2000 mm, but longer than 4 mm
# and count the number of DVs that fulfill this selection
ROOT.gInterpreter.Declare("""
int filter_n_DVs(ROOT::VecOps::RVec<double> distanceDV, ROOT::VecOps::RVec<double> invMassDV) {
    int result = 0;
    for (size_t i = 0; i < invMassDV.size(); ++i) {
        if (invMassDV.at(i) > 1 && distanceDV.at(i) > 4 && distanceDV.at(i) < 2000)
            result += 1;
    }
    return result;
}
""")
#END USER DEFINED CODE

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (
            df

            .Alias("Particle1", "Particle#1.index")
            .Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
            .Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")

            # MC event primary vertex
            .Define("MC_PrimaryVertex",  "FCCAnalyses::MCParticle::get_EventPrimaryVertex(21)( Particle )" )

            # number of tracks
            .Define("n_tracks","ReconstructedParticle2Track::getTK_n(EFlowTrack_1)")

            # Vertex fitting

            # First, reconstruct a vertex from all tracks 
            # Input parameters are 1 = primary vertex, EFlowTrack_1 contains all tracks, bool beamspotconstraint = true, bsc sigma x/y/z
            .Define("VertexObject_allTracks",  "VertexFitterSimple::VertexFitter_Tk ( 1, EFlowTrack_1, true, 4.5, 20e-3, 300)")

            # Select the tracks that are reconstructed  as primaries
            .Define("RecoedPrimaryTracks",  "VertexFitterSimple::get_PrimaryTracks( VertexObject_allTracks, EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0., 0)")
            .Define("n_RecoedPrimaryTracks",  "ReconstructedParticle2Track::getTK_n( RecoedPrimaryTracks )")

            # the final primary vertex :
            .Define("PrimaryVertexObject",   "VertexFitterSimple::VertexFitter_Tk ( 1, RecoedPrimaryTracks, true, 4.5, 20e-3, 300) ")
            .Define("PrimaryVertex",   "VertexingUtils::get_VertexData( PrimaryVertexObject )")

            # Displaced vertex reconstruction
            
            # select tracks with pT > 1 GeV
            .Define('sel_tracks_pt', 'VertexingUtils::sel_pt_tracks(1)(EFlowTrack_1)')
            # select tracks with |d0 |> 2 mm
            .Define('sel_tracks', 'VertexingUtils::sel_d0_tracks(2)(sel_tracks_pt)')
            # find the DVs
            .Define("DV_evt_seltracks", "VertexFinderLCFIPlus::get_SV_event(sel_tracks, PrimaryVertexObject, true, 9., 40., 5.)")
            # number of DVs
            .Define('n_seltracks_DVs', 'VertexingUtils::get_n_SV(DV_evt_seltracks)')
            # number of tracks from the DVs
            .Define('n_trks_seltracks_DVs', 'VertexingUtils::get_VertexNtrk(DV_evt_seltracks)')
            # invariant mass at the DVs (assuming the tracks to be pions)
            .Define('invMass_seltracks_DVs', 'VertexingUtils::get_invM(DV_evt_seltracks)')

            # get the chi2 distributions of the DVs from selected tracks
            .Define("DV_evt_seltracks_chi2",    "VertexingUtils::get_chi2_SV(DV_evt_seltracks)")
            .Define("DV_evt_seltracks_normchi2","VertexingUtils::get_norm_chi2_SV(DV_evt_seltracks)") # DV chi2 (normalised)

            # get the decay radius of all the DVs from selected tracks
            .Define("Reco_seltracks_DVs_Lxy","VertexingUtils::get_dxy_SV(DV_evt_seltracks, PrimaryVertexObject)")
            .Define("Reco_seltracks_DVs_Lxyz","VertexingUtils::get_d3d_SV(DV_evt_seltracks, PrimaryVertexObject)")
            
            # merge vertices with position within 10*error-of-position, get the tracks from the merged vertices and refit
            .Define('merged_DVs', 'VertexingUtils::mergeVertices(DV_evt_seltracks)')
            # number of merged DVs
            .Define("merged_DVs_n", "VertexingUtils::get_n_SV(merged_DVs)")
            # number of tracks from the merged DVs
            .Define('n_trks_merged_DVs', 'VertexingUtils::get_VertexNtrk(merged_DVs)')
            # invariant mass at the merged DVs
            .Define('invMass_merged_DVs', 'VertexingUtils::get_invM(merged_DVs)')

            # get the chi2 distributions of the merged DVs
            .Define("merged_DVs_chi2",    "VertexingUtils::get_chi2_SV(merged_DVs)")
            .Define("merged_DVs_normchi2","VertexingUtils::get_norm_chi2_SV(merged_DVs)") # DV chi2 (normalised)

            # get the decay radius of all the merged DVs
            .Define("Reco_DVs_merged_Lxy","VertexingUtils::get_dxy_SV(merged_DVs, PrimaryVertexObject)")
            .Define("Reco_DVs_merged_Lxyz","VertexingUtils::get_d3d_SV(merged_DVs, PrimaryVertexObject)")

            # Reconstructed electrons and muons

            # Electrons
            .Alias('Electron0', 'Electron#0.index')
            .Define('RecoElectrons',  'ReconstructedParticle::get(Electron0, ReconstructedParticles)') 
            .Define('n_RecoElectrons',  'ReconstructedParticle::get_n(RecoElectrons)') #count how many electrons are in the event in total

            # some kinematics of the reconstructed electrons and positrons
            .Define("RecoElectron_e", "ReconstructedParticle::get_e(RecoElectrons)")
            .Define("RecoElectron_p", "ReconstructedParticle::get_p(RecoElectrons)")
            .Define("RecoElectron_pt", "ReconstructedParticle::get_pt(RecoElectrons)")
            .Define("RecoElectron_px", "ReconstructedParticle::get_px(RecoElectrons)")
            .Define("RecoElectron_py", "ReconstructedParticle::get_py(RecoElectrons)")
            .Define("RecoElectron_pz", "ReconstructedParticle::get_pz(RecoElectrons)")
            .Define("RecoElectron_charge",  "ReconstructedParticle::get_charge(RecoElectrons)")

            # finding the invariant mass of the reconstructed electron and positron pair
            .Define("Reco_ee_energy", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_e.at(0) + RecoElectron_e.at(1)); else return float(-1.);")
            .Define("Reco_ee_px", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_px.at(0) + RecoElectron_px.at(1)); else return float(-1.);")
            .Define("Reco_ee_py", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_py.at(0) + RecoElectron_py.at(1)); else return float(-1.);")
            .Define("Reco_ee_pz", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_pz.at(0) + RecoElectron_pz.at(1)); else return float(-1.);")
            .Define("Reco_ee_invMass", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return sqrt(Reco_ee_energy*Reco_ee_energy - Reco_ee_px*Reco_ee_px - Reco_ee_py*Reco_ee_py - Reco_ee_pz*Reco_ee_pz ); else return float(-1.);")


            # Muons
            .Alias('Muon0', 'Muon#0.index')
            .Define('RecoMuons',  'ReconstructedParticle::get(Muon0, ReconstructedParticles)')
            .Define('n_RecoMuons',  'ReconstructedParticle::get_n(RecoMuons)') #count how many muons are in the event in total

            # some kinematics of the reconstructed muons
            .Define("RecoMuon_e",      "ReconstructedParticle::get_e(RecoMuons)")
            .Define("RecoMuon_p",      "ReconstructedParticle::get_p(RecoMuons)")
            .Define("RecoMuon_pt",      "ReconstructedParticle::get_pt(RecoMuons)")
            .Define("RecoMuon_px",      "ReconstructedParticle::get_px(RecoMuons)")
            .Define("RecoMuon_py",      "ReconstructedParticle::get_py(RecoMuons)")
            .Define("RecoMuon_pz",      "ReconstructedParticle::get_pz(RecoMuons)")
            .Define("RecoMuon_charge",  "ReconstructedParticle::get_charge(RecoMuons)")

            # finding the invariant mass of the reconstructed muon pair
            .Define("Reco_mumu_energy", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_e.at(0) + RecoMuon_e.at(1)); else return float(-1.);")
            .Define("Reco_mumu_px", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_px.at(0) + RecoMuon_px.at(1)); else return float(-1.);")
            .Define("Reco_mumu_py", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_py.at(0) + RecoMuon_py.at(1)); else return float(-1.);")
            .Define("Reco_mumu_pz", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_pz.at(0) + RecoMuon_pz.at(1)); else return float(-1.);")
            .Define("Reco_mumu_invMass", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return sqrt(Reco_mumu_energy*Reco_mumu_energy - Reco_mumu_px*Reco_mumu_px - Reco_mumu_py*Reco_mumu_py - Reco_mumu_pz*Reco_mumu_pz ); else return float(-1.);")

            # Number of DVs with distance and invariant mass selection applied
            .Define("filter_n_DVs_seltracks", "filter_n_DVs(Reco_seltracks_DVs_Lxyz, invMass_seltracks_DVs)")
            .Define("filter_n_DVs_merge", "filter_n_DVs(Reco_DVs_merged_Lxyz, invMass_merged_DVs)")

        )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            "n_tracks",
            "n_RecoedPrimaryTracks",

            'n_seltracks_DVs',
            'n_trks_seltracks_DVs',
            'invMass_seltracks_DVs',
            "DV_evt_seltracks_chi2",
            "DV_evt_seltracks_normchi2",
            "Reco_seltracks_DVs_Lxy",
            "Reco_seltracks_DVs_Lxyz",

            "merged_DVs_n",
            'n_trks_merged_DVs',
            'invMass_merged_DVs',
            "merged_DVs_chi2",
            "merged_DVs_normchi2",
            "Reco_DVs_merged_Lxy",
            "Reco_DVs_merged_Lxyz",

            'n_RecoElectrons',
            "RecoElectron_e",
            "RecoElectron_p",
            "RecoElectron_pt",
            "RecoElectron_px",
            "RecoElectron_py",
            "RecoElectron_pz",
            "RecoElectron_charge",
            "Reco_ee_invMass",
            'n_RecoMuons',
            "RecoMuon_e",
            "RecoMuon_p",
            "RecoMuon_pt",
            "RecoMuon_px",
            "RecoMuon_py",
            "RecoMuon_pz",
            "RecoMuon_charge",
            "Reco_mumu_invMass",

            "filter_n_DVs_seltracks",
            "filter_n_DVs_merge",
        ]
        return branchList