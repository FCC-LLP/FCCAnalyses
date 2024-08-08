import ROOT

testFile = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/exoticHiggsSamplesCLD/exoticHiggs_scalar_ms20GeV_sine-5_H.root"

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5_H':{},
        'exoticHiggs_scalar_ms20GeV_sine-6_H':{},
        'exoticHiggs_scalar_ms20GeV_sine-7_H':{},
        'exoticHiggs_scalar_ms60GeV_sine-5_H':{},
        'exoticHiggs_scalar_ms60GeV_sine-6_H':{},
        'exoticHiggs_scalar_ms60GeV_sine-7_H':{},

        # #centrally produced backgrounds
        #'p8_ee_ZZ_ecm240':{'fraction':0.005, 'chunks':5},   
        #'p8_ee_WW_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_ccH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_qqH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_bbH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_ssH_HWW_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_ssH_Hbb_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_qqH_Hbb_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_bbH_Hbb_ecm240':{'fraction':0.005, 'chunks':5},   
        #'wzp6_ee_ccH_Hbb_ecm240':{'fraction':0.005, 'chunks':5}   

}

#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
#prodTag     = "FCCee/winter2023/IDEA/"

#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events
#inputDir = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ExoticHiggsDecays/MC_generation"
inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/exoticHiggsSamplesCLD"

#Optional: output directory, default is local dir
outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/exoticHiggsSamplesCLD/Reco_output_stage1_H/"

#Optional: ncpus, default is 4
nCPUS       = 8

#Optional running on HTCondor, default is False
#runBatch    = False
runBatch    = True

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "workday"
batchQueue = "testmatch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

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
            .Define("RecoedPrimaryTracks",  "VertexFitterSimple::get_PrimaryTracks( EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0.)")
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
            .Define("DV_evt_seltracks", "VertexFinderLCFIPlus::get_SV_event(sel_tracks, EFlowTrack_1, PrimaryVertexObject, true, 9., 40., 5.)")
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
            .Define('merged_DVs', 'VertexingUtils::mergeVertices(DV_evt_seltracks, EFlowTrack_1)')
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

            # Number of DVs with distance and invariant mass selection applied
            .Define("filter_n_DVs_seltracks", "filter_n_DVs(Reco_seltracks_DVs_Lxyz, invMass_seltracks_DVs)")
            .Define("filter_n_DVs_merge", "filter_n_DVs(Reco_DVs_merged_Lxyz, invMass_merged_DVs)")

            ##### Remove particles associated with DVs, then run N = 2 exclusive jet clustering

            # get particle indices from dv tracks
            #get_recoindTRK
            #DV_evt_seltracks
            .Define("rp_indices_DVs_trks", "VertexingUtils::get_VerticesRecoParticlesInd(DV_evt_seltracks, ReconstructedParticles)")
            .Define("rp_DVs", "ReconstructedParticle::get(rp_indices_DVs_trks, ReconstructedParticles)")
            .Define("nondv_recoparticles",  "ReconstructedParticle::remove( ReconstructedParticles,  rp_DVs )")

            #define the RP px, py, pz and e
            .Define("RP_px",          "ReconstructedParticle::get_px(nondv_recoparticles)")
            .Define("RP_py",          "ReconstructedParticle::get_py(nondv_recoparticles)")
            .Define("RP_pz",          "ReconstructedParticle::get_pz(nondv_recoparticles)")
            .Define("RP_e",           "ReconstructedParticle::get_e(nondv_recoparticles)")
            .Define("RP_m",           "ReconstructedParticle::get_mass(nondv_recoparticles)")
            .Define("RP_q",           "ReconstructedParticle::get_charge(nondv_recoparticles)")

            #build pseudo jets with the RP, using the interface that takes px,py,pz,m for better
            #handling of rounding errors
            .Define("pseudo_jets",    "JetClusteringUtils::set_pseudoJets_xyzm(RP_px, RP_py, RP_pz, RP_m)")

            #run jet clustering with all reconstructed particles. kt_algorithm, R=0.5, exclusive clustering, exactly 2 jets, E0-scheme
            .Define("FCCAnalysesJets_kt", "JetClustering::clustering_kt(0.5, 2, 2, 0, 10)(pseudo_jets)")
            #get the jets out of the struct
            .Define("jets_kt",           "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_kt)")
            #get the jets constituents out of the struct
            .Define("jetconstituents_kt","JetClusteringUtils::get_constituents(FCCAnalysesJets_kt)")
            #get some variables
            .Define("jets_kt_e",        "JetClusteringUtils::get_e(jets_kt)")
            .Define("jets_kt_px",        "JetClusteringUtils::get_px(jets_kt)")
            .Define("jets_kt_py",        "JetClusteringUtils::get_py(jets_kt)")
            .Define("jets_kt_pz",        "JetClusteringUtils::get_pz(jets_kt)")
            .Define("jets_kt_m",        "JetClusteringUtils::get_m(jets_kt)")
            
            .Define("jets_kt_e_sum",        "ReconstructedParticle::get_sum_float(jets_kt_e)")
            .Define("jets_kt_px_sum",        "ReconstructedParticle::get_sum_float(jets_kt_px)")
            .Define("jets_kt_py_sum",        "ReconstructedParticle::get_sum_float(jets_kt_py)")
            .Define("jets_kt_pz_sum",        "ReconstructedParticle::get_sum_float(jets_kt_pz)")
            .Define("jets_kt_m_sum",        "ReconstructedParticle::get_sum_float(jets_kt_m)")

            .Define("jets_kt_e_avg",        "ReconstructedParticle::get_avg_float(jets_kt_e)")
            .Define("jets_kt_px_avg",        "ReconstructedParticle::get_avg_float(jets_kt_px)")
            .Define("jets_kt_py_avg",        "ReconstructedParticle::get_avg_float(jets_kt_py)")
            .Define("jets_kt_pz_avg",        "ReconstructedParticle::get_avg_float(jets_kt_pz)")
            .Define("jets_kt_m_avg",        "ReconstructedParticle::get_avg_float(jets_kt_m)")

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

            "filter_n_DVs_seltracks",
            "filter_n_DVs_merge",

            "jets_kt_e",
            "jets_kt_px",
            "jets_kt_py",
            "jets_kt_pz",
            "jets_kt_m",
            "jetconstituents_kt",

            "jets_kt_e_sum",
            "jets_kt_px_sum",
            "jets_kt_py_sum",
            "jets_kt_pz_sum",
            "jets_kt_m_sum",

            "jets_kt_e_avg",
            "jets_kt_px_avg",
            "jets_kt_py_avg",
            "jets_kt_pz_avg",
            "jets_kt_m_avg"
        ]
        return branchList