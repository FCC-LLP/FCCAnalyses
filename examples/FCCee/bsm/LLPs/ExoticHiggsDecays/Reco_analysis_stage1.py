import ROOT

testfile="/afs/cern.ch/work/u/uvandevo/exoticHiggs_scalar_ms20GeV_sine-5.root"
#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5':{},
        # 'exoticHiggs_scalar_ms20GeV_sine-6':{},
        # 'exoticHiggs_scalar_ms20GeV_sine-7':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-5':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-6':{},
        # 'exoticHiggs_scalar_ms60GeV_sine-7':{},
}

#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
#prodTag     = "FCCee/spring2021/IDEA/"

#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events
inputDir = "/afs/cern.ch/work/u/uvandevo"
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/output_MadgraphPythiaDelphes/"


#Optional: output directory, default is local dir
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/Reco_output_stage1/"
#outputDirEos = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/Reco_output_stage1/"
outputDir = "Reco_output_stage1/"

#Optional: ncpus, default is 4
nCPUS       = 4

#Optional running on HTCondor, default is False
runBatch    = False
#runBatch    = True

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
#compGroup = "group_u_FCC.local_gen"

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

            # find secondary tracks
            .Define("SecondaryTracks",   "VertexFitterSimple::get_NonPrimaryTracks( EFlowTrack_1,  RecoedPrimaryTracks )")
            .Define("n_SecondaryTracks",  "ReconstructedParticle2Track::getTK_n( SecondaryTracks )" )

            # find secondary vertex
            .Define("SecondaryVertexObject",   "VertexFitterSimple::VertexFitter_Tk ( 2, SecondaryTracks) ")
            .Define("SecondaryVertex",   "VertexingUtils::get_VertexData( SecondaryVertexObject )")

            # which of the tracks are primary according to the reco algprithm (boolean)
            .Define("IsPrimary_based_on_reco",  "VertexFitterSimple::IsPrimary_forTracks( EFlowTrack_1,  RecoedPrimaryTracks )")

            # finding SVs in the event (two interfaces)
	        .Define("SV_evt1", "VertexFinderLCFIPlus::get_SV_event(ReconstructedParticles, EFlowTrack_1, PrimaryVertexObject, IsPrimary_based_on_reco, true, 9., 40., 5.)")

            # number of SVs in the event
            .Define("SV_evt1_n","VertexingUtils::get_n_SV(SV_evt1)")

            # all SV vertices
            .Define('SVs', 'VertexingUtils::get_VertexData(SV_evt1)')

            # get the invariant mass of every vertex
            .Define('invMass_SVs', 'VertexingUtils::get_invM(SV_evt1)')

            # get the position of every vertex
            .Define("SV_evt1_position", "VertexingUtils::get_position_SV( SV_evt1 )")

            .Define('SVs_x', 'myUtils::get_Vertex_x(SV_evt1)')
            .Define('SVs_y', 'myUtils::get_Vertex_y(SV_evt1)')
            .Define('SVs_z', 'myUtils::get_Vertex_z(SV_evt1)')

            # get the decay radius of all the secondary vertices
            .Define("Reco_SVs_Lxy","VertexingUtils::get_dxy_SV(SV_evt1, PrimaryVertexObject)")
            .Define("Reco_SVs_Lxyz","VertexingUtils::get_d3d_SV(SV_evt1, PrimaryVertexObject)")

            # get number of tracks from every vertex
            .Define('n_trks_SVs', 'VertexingUtils::get_VertexNtrk(SV_evt1)')
            
            # select tracks with pT > 1 GeV
            .Define('sel_tracks_pt', 'VertexingUtils::sel_pt_tracks(1)(EFlowTrack_1)')
            .Define("SV_evt_seltracks_pt", "VertexFinderLCFIPlus::get_SV_event(sel_tracks_pt, PrimaryVertexObject, true, 9., 20., 5.)")
            .Define("SV_evt_seltracks_pt_n", "VertexingUtils::get_n_SV(SV_evt_seltracks_pt)")
            .Define('invMass_SVs_seltracks_pt', 'VertexingUtils::get_invM(SV_evt_seltracks_pt)')
            .Define('n_trks_SVs_seltracks_pt', 'VertexingUtils::get_VertexNtrk(SV_evt_seltracks_pt)')

            # get the decay radius of all the secondary vertices from sel pt tracks
            .Define("Reco_SVs_seltracks_Lxy","VertexingUtils::get_dxy_SV(SV_evt_seltracks_pt, PrimaryVertexObject)")
            .Define("Reco_SVs_seltracks_Lxyz","VertexingUtils::get_d3d_SV(SV_evt_seltracks_pt, PrimaryVertexObject)")

            # merge vertices with position within 10*error-of-position, get the tracks from the merged vertices and refit, SV_evt_selTracks_pt
            .Define('merged_SVs_pt', 'VertexingUtils::mergeVertices(SV_evt_seltracks_pt)')
            .Define("merged_SVs_pt_n", "VertexingUtils::get_n_SV(merged_SVs_pt)")
            .Define('n_trks_merged_SVs_pt', 'VertexingUtils::get_VertexNtrk(merged_SVs_pt)')
            .Define('invMass_merged_SVs_pt', 'VertexingUtils::get_invM(merged_SVs_pt)')

            # get the decay radius of all the secondary vertices from merged vertices from sel pt tracks
            .Define("Reco_SVs_merged_pt_Lxy","VertexingUtils::get_dxy_SV(merged_SVs_pt, PrimaryVertexObject)")
            .Define("Reco_SVs_merged_pt_Lxyz","VertexingUtils::get_d3d_SV(merged_SVs_pt, PrimaryVertexObject)")

            # select tracks with |d0 |> 2 mm
            .Define('sel_tracks', 'VertexingUtils::sel_d0_tracks(2)(sel_tracks_pt)')
            .Define("SV_evt_seltracks", "VertexFinderLCFIPlus::get_SV_event(sel_tracks, PrimaryVertexObject, true, 9., 20., 5.)")
            .Define('n_sel_trks_SVs', 'VertexingUtils::get_n_SV(SV_evt_seltracks)')

            # merge vertices with position within 10*error-of-position, get the tracks from the merged vertices and refit
            .Define('merged_SVs', 'VertexingUtils::mergeVertices(SV_evt_seltracks)')
            .Define("merged_SVs_n", "VertexingUtils::get_n_SV(merged_SVs)")
            .Define('n_trks_merged_SVs', 'VertexingUtils::get_VertexNtrk(merged_SVs)')
            .Define('invMass_merged_SVs', 'VertexingUtils::get_invM(merged_SVs)')

            # get the decay radius of all the secondary vertices from sel pt + d0 and merged vertices
            .Define("Reco_SVs_merged_Lxy","VertexingUtils::get_dxy_SV(merged_SVs, PrimaryVertexObject)")
            .Define("Reco_SVs_merged_Lxyz","VertexingUtils::get_d3d_SV(merged_SVs, PrimaryVertexObject)")

            # Reconstructed electrons and muons

            # Electrons
            .Alias('Electron0', 'Electron#0.index')
            .Define('RecoElectrons',  'ReconstructedParticle::get(Electron0, ReconstructedParticles)') 
            .Define('n_RecoElectrons',  'ReconstructedParticle::get_n(RecoElectrons)') #count how many electrons are in the event in total

            .Define("RecoElectron_e", "ReconstructedParticle::get_e(RecoElectrons)")
            .Define("RecoElectron_p", "ReconstructedParticle::get_p(RecoElectrons)")
            .Define("RecoElectron_pt", "ReconstructedParticle::get_pt(RecoElectrons)")
            .Define("RecoElectron_px", "ReconstructedParticle::get_px(RecoElectrons)")
            .Define("RecoElectron_py", "ReconstructedParticle::get_py(RecoElectrons)")
            .Define("RecoElectron_pz", "ReconstructedParticle::get_pz(RecoElectrons)")
            .Define("RecoElectron_charge",  "ReconstructedParticle::get_charge(RecoElectrons)")

            .Define("Reco_ee_energy", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_e.at(0) + RecoElectron_e.at(1)); else return float(-1.);")
            .Define("Reco_ee_px", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_px.at(0) + RecoElectron_px.at(1)); else return float(-1.);")
            .Define("Reco_ee_py", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_py.at(0) + RecoElectron_py.at(1)); else return float(-1.);")
            .Define("Reco_ee_pz", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return (RecoElectron_pz.at(0) + RecoElectron_pz.at(1)); else return float(-1.);")
            .Define("Reco_ee_invMass", "if ((n_RecoElectrons>1) && (RecoElectron_charge.at(0) != RecoElectron_charge.at(1))) return sqrt(Reco_ee_energy*Reco_ee_energy - Reco_ee_px*Reco_ee_px - Reco_ee_py*Reco_ee_py - Reco_ee_pz*Reco_ee_pz ); else return float(-1.);")


            # Muons
            .Alias('Muon0', 'Muon#0.index')
            .Define('RecoMuons',  'ReconstructedParticle::get(Muon0, ReconstructedParticles)')
            .Define('n_RecoMuons',  'ReconstructedParticle::get_n(RecoMuons)') #count how many muons are in the event in total

            .Define("RecoMuon_e",      "ReconstructedParticle::get_e(RecoMuons)")
            .Define("RecoMuon_p",      "ReconstructedParticle::get_p(RecoMuons)")
            .Define("RecoMuon_pt",      "ReconstructedParticle::get_pt(RecoMuons)")
            .Define("RecoMuon_px",      "ReconstructedParticle::get_px(RecoMuons)")
            .Define("RecoMuon_py",      "ReconstructedParticle::get_py(RecoMuons)")
            .Define("RecoMuon_pz",      "ReconstructedParticle::get_pz(RecoMuons)")
            .Define("RecoMuon_charge",  "ReconstructedParticle::get_charge(RecoMuons)")

            .Define("Reco_mumu_energy", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_e.at(0) + RecoMuon_e.at(1)); else return float(-1.);")
            .Define("Reco_mumu_px", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_px.at(0) + RecoMuon_px.at(1)); else return float(-1.);")
            .Define("Reco_mumu_py", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_py.at(0) + RecoMuon_py.at(1)); else return float(-1.);")
            .Define("Reco_mumu_pz", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return (RecoMuon_pz.at(0) + RecoMuon_pz.at(1)); else return float(-1.);")
            .Define("Reco_mumu_invMass", "if ((n_RecoMuons>1) && (RecoMuon_charge.at(0) != RecoMuon_charge.at(1))) return sqrt(Reco_mumu_energy*Reco_mumu_energy - Reco_mumu_px*Reco_mumu_px - Reco_mumu_py*Reco_mumu_py - Reco_mumu_pz*Reco_mumu_pz ); else return float(-1.);")


            # Jet study

            # define the RP px, py, pz and e
            .Define("RP_px",          "ReconstructedParticle::get_px(ReconstructedParticles)")
            .Define("RP_py",          "ReconstructedParticle::get_py(ReconstructedParticles)")
            .Define("RP_pz",          "ReconstructedParticle::get_pz(ReconstructedParticles)")
            .Define("RP_e",           "ReconstructedParticle::get_e(ReconstructedParticles)")
            .Define("RP_m",           "ReconstructedParticle::get_mass(ReconstructedParticles)")
            .Define("RP_q",           "ReconstructedParticle::get_charge(ReconstructedParticles)")

            # build pseudo jets with the RP, using the interface that takes px,py,pz,e 
            .Define("pseudo_jets",    "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")

            # run jet clustering with all reconstructed particles, Durham jet-algorithm
            # ee_kt_algorithm 2: exclusive clustering, exactly njets = 4, 1: sorted by E, 0: recombination scheme E
            .Define("FCCAnalysesJets_ee_kt", "JetClustering::clustering_ee_kt(2, 4, 1, 0)(pseudo_jets)")
            #get the jets out of the struct
            .Define("jets_ee_kt",           "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_kt)")
            #get the jets constituents out of the struct
            .Define("jetconstituents_ee_kt","JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_kt)")

            #get some variables
            .Define("jets_ee_kt_e",        "JetClusteringUtils::get_e(jets_ee_kt)")
            .Define("jets_ee_kt_px",        "JetClusteringUtils::get_px(jets_ee_kt)")
            .Define("jets_ee_kt_py",        "JetClusteringUtils::get_py(jets_ee_kt)")
            .Define("jets_ee_kt_pz",        "JetClusteringUtils::get_pz(jets_ee_kt)")
            .Define("jets_ee_kt_m",        "JetClusteringUtils::get_m(jets_ee_kt)")

        )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            "n_tracks",
            "n_RecoedPrimaryTracks",
            "n_SecondaryTracks",
            # "SV_evt1_n",
            # 'invMass_SVs',
            # "Reco_SVs_Lxy",
            # "Reco_SVs_Lxyz",
            # 'n_trks_SVs',
            # "SV_evt_seltracks_pt_n",
            # 'invMass_SVs_seltracks_pt',
            # 'n_trks_SVs_seltracks_pt',
            # 'n_sel_trks_SVs',
            "merged_SVs_n",
            # "merged_SVs_pt_n",
            # 'n_trks_merged_SVs_pt',
            'n_trks_merged_SVs',
            'invMass_merged_SVs',
            # 'invMass_merged_SVs_pt',
            # "Reco_SVs_seltracks_Lxy",
            # "Reco_SVs_seltracks_Lxyz",
            # "Reco_SVs_merged_pt_Lxy",
            # "Reco_SVs_merged_pt_Lxyz",
            "Reco_SVs_merged_Lxy",
            "Reco_SVs_merged_Lxyz",
            'n_RecoElectrons',
            "Reco_ee_invMass",
            'n_RecoMuons',
            "Reco_mumu_invMass",
            # "jets_ee_kt_e",
            # "jets_ee_kt_px",
            # "jets_ee_kt_py",
            # "jets_ee_kt_pz",
            "jets_ee_kt_m"
        ]
        return branchList