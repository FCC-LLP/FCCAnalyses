import ROOT

analysesList = ['ExoticHiggsDecays_analysis_code']

testfile="/afs/cern.ch/work/u/uvandevo/exoticHiggs_scalar_ms20GeV_sine-5.root"

#Mandatory: List of processes
processList = {

        #privately-produced signals
        'exoticHiggs_scalar_ms20GeV_sine-5':{},
        'exoticHiggs_scalar_ms20GeV_sine-6':{},
        'exoticHiggs_scalar_ms20GeV_sine-7':{},
        'exoticHiggs_scalar_ms60GeV_sine-5':{},
        'exoticHiggs_scalar_ms60GeV_sine-6':{},
        'exoticHiggs_scalar_ms60GeV_sine-7':{},
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
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/MC_output_stage1/"
#outputDirEos = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/H_SS_4b/MC_output_stage1/"
outputDir = "MC_output_stage1/"

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
            # MC-particles/truth particles

            # select the generated electrons and positrons
            .Define('GenElectrons_PID', 'MCParticle::sel_pdgID(11, true)(Particle)')
            # get the number of generated electrons and positrons
            .Define('n_GenElectrons', 'MCParticle::get_n(GenElectrons_PID)')

            # select the generated muons
            .Define('GenMuons_PID', 'MCParticle::sel_pdgID(13, true)(Particle)')
            # get the number of generated muons
            .Define('n_GenMuons', 'MCParticle::get_n(GenMuons_PID)')

            # select generated Z boson
            .Define('GenZ_PID',  'MCParticle::sel_pdgID(23, false)(Particle)')
            # get the number of Z bosons
            .Define('n_GenZ', 'MCParticle::get_n(GenZ_PID)')

            # select generated Higgs boson
            .Define('GenHiggs_PID',  'MCParticle::sel_pdgID(25, false)(Particle)')
            # get the number of Higgs bosons
            .Define('n_GenHiggs', 'MCParticle::get_n(GenHiggs_PID)')

            # select the generated b b~ quarks
            .Define('Genb_PID', 'MCParticle::sel_pdgID(5, true)(Particle)') # true means charge conjugation = true, i.e pick out both b and b~
            # get the number of generated b b~ quarks
            .Define('n_Genb', 'MCParticle::get_n(Genb_PID)')

            # select generated scalar HS
            .Define('GenHS_PID',  'MCParticle::sel_pdgID(35, false)(Particle)')
            # get the number of scalars
            .Define('n_GenHS', 'MCParticle::get_n(GenHS_PID)')
            .Define("AllGenHS_mass", "MCParticle::get_mass(GenHS_PID)") 
            .Define("AllGenHS_e", "MCParticle::get_e(GenHS_PID)")
            .Define("AllGenHS_p", "MCParticle::get_p(GenHS_PID)")
            .Define("AllGenHS_pt", "MCParticle::get_pt(GenHS_PID)")
            .Define("AllGenHS_px", "MCParticle::get_px(GenHS_PID)")
            .Define("AllGenHS_py", "MCParticle::get_py(GenHS_PID)")
            .Define("AllGenHS_pz", "MCParticle::get_pz(GenHS_PID)")

            .Define("GenHS1_e", "AllGenHS_e.at(0)")
            .Define("GenHS2_e", "AllGenHS_e.at(1)")

            # get the production vertex for the 2 HS in x y z
            .Define('HS_vertex_x', 'MCParticle::get_vertex_x(GenHS_PID)')
            .Define('HS_vertex_y', 'MCParticle::get_vertex_y(GenHS_PID)')
            .Define('HS_vertex_z', 'MCParticle::get_vertex_z(GenHS_PID)')

            # decay length of Higgs
            .Define('decayLengthHiggs', 'return sqrt(HS_vertex_x.at(0)*HS_vertex_x.at(0) + HS_vertex_y.at(0)*HS_vertex_y.at(0) + HS_vertex_z.at(0)*HS_vertex_z.at(0))')
          
            # get the indices of the Higgs and the scalars, sorted in order h hs hs
            .Define('H2HSHS_indices', 'MCParticle::get_indices_ExclusiveDecay(25, {35, 35}, false, false)(Particle, Particle1)')

            # get the indices of the b quarks from related scalar, 1 are from the "first" scalar and 2 from the second one
            .Define('bquarks1_indices', 'MCParticle::get_indices_ExclusiveDecay_MotherByIndex(H2HSHS_indices[1], {5, -5}, false, Particle, Particle1)')
            .Define('bquarks2_indices', 'MCParticle::get_indices_ExclusiveDecay_MotherByIndex(H2HSHS_indices[2], {5, -5}, false, Particle, Particle1)')

            # # get the b quarks, right now only picking the first daughter (hopefully b quark) from the list of decay particles from hs, should update this section maybe
            .Define('bquarks1', 'myUtils::selMC_leg(1) (bquarks1_indices, Particle)')
            .Define('bquarks2', 'myUtils::selMC_leg(1) (bquarks2_indices, Particle)')

            # # get the vertex position for the first group of b quarks
            .Define('b1_vertex_x', 'MCParticle::get_vertex_x(bquarks1)')
            .Define('b1_vertex_y', 'MCParticle::get_vertex_y(bquarks1)')
            .Define('b1_vertex_z', 'MCParticle::get_vertex_z(bquarks1)')

            # # get the vertex position for the second group of b quarks
            .Define('b2_vertex_x', 'MCParticle::get_vertex_x(bquarks2)')
            .Define('b2_vertex_y', 'MCParticle::get_vertex_y(bquarks2)')
            .Define('b2_vertex_z', 'MCParticle::get_vertex_z(bquarks2)')

            # get the decay length of HS 1
            .Define('decayLengthHS1', 'return sqrt((b1_vertex_x - HS_vertex_x.at(0))*(b1_vertex_x - HS_vertex_x.at(0)) + (b1_vertex_y - HS_vertex_y.at(0))*(b1_vertex_y - HS_vertex_y.at(0)) + (b1_vertex_z - HS_vertex_z.at(0))*(b1_vertex_z - HS_vertex_z.at(0)))')

            # get the decay length of HS 2
            .Define('decayLengthHS2', 'return sqrt((b2_vertex_x - HS_vertex_x.at(1))*(b2_vertex_x - HS_vertex_x.at(1)) + (b2_vertex_y - HS_vertex_y.at(1))*(b2_vertex_y - HS_vertex_y.at(1)) + (b2_vertex_z - HS_vertex_z.at(1))*(b2_vertex_z - HS_vertex_z.at(1)))')

            # get decay length of both scalars in a vector for each event
            .Define('decayLengthsHS', 'myUtils::get_both_scalars(decayLengthHS1, decayLengthHS2)')

            # get the transverse decay length of HS 1
            .Define('LxyHS1', 'return sqrt((b1_vertex_x - HS_vertex_x.at(0))*(b1_vertex_x - HS_vertex_x.at(0)) + (b1_vertex_y - HS_vertex_y.at(0))*(b1_vertex_y - HS_vertex_y.at(0)))')

            # get the transverse decay length of HS 2
            .Define('LxyHS2', 'return sqrt((b2_vertex_x - HS_vertex_x.at(1))*(b2_vertex_x - HS_vertex_x.at(1)) + (b2_vertex_y - HS_vertex_y.at(1))*(b2_vertex_y - HS_vertex_y.at(1)))')

            # get the transverse decay length of both scalars in a vector for each event
            .Define('LxyHS', 'ExoticHiggsDecays_analysis_code::get_both_scalars(LxyHS1, LxyHS2)')

            # the proper lifetime of the scalars given in [ns]
            .Define('lifetimeHS1', 'return (decayLengthHS1 * 1E-3 * AllGenHS_mass.at(0)/(3E8 * AllGenHS_e.at(0))*1E9)')
            .Define('lifetimeHS2', 'return (decayLengthHS2 * 1E-3 * AllGenHS_mass.at(1)/(3E8 * AllGenHS_e.at(1))*1E9)')

            # get proper lifetime of both scalars in a vector for each event
            .Define('lifetimeHS', 'myUtils::get_both_scalars(lifetimeHS1, lifetimeHS2)')

            # the lifetime of the scalars in the LAB frame in [ns]
            .Define('lifetimeHS1LAB', 'return (decayLengthHS1 * 1E-3 * 1E9/3E8)')
            .Define('lifetimeHS2LAB', 'return (decayLengthHS2 * 1E-3 * 1E9/3E8)')

            # get lifetime in LAB of both scalars in a vector for each event
            .Define('lifetimeHSLAB', 'myUtils::get_both_scalars(lifetimeHS1LAB, lifetimeHS2LAB)')
        )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            'n_GenElectrons',
            'n_GenMuons',
            'n_GenZ',
            'n_GenHiggs',
            'n_Genb',
            'n_GenHS',
            'AllGenHS_mass',
            'AllGenHS_e',
            'decayLengthsHS',
            'LxyHS',
            'lifetimeHS',
            'lifetimeHSLAB'
        ]
        return branchList
