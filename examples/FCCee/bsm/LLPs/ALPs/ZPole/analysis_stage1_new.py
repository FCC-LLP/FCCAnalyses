#Mandatory: List of processes
processList = {

        #centrally-produced backgrounds
        # 'p8_ee_Zee_ecm91':{'chunks':100},
        # 'wzp6_gaga_ee_60_ecm240':{'chunks':100},
        # 'ee_gaga_1million':{},
        # 'test1':{},
        # 'test2':{},
        # 'test3':{},
        # 'test4':{},
        # 'ee_gaga_test':{},
        # 'ee_aa':{},
        # 'ee_aaa':{},
        # 'ee_aaaa':{},

        #privately-produced signals

        # 'ALP_Z_aa_0.01.GeV_cYY_0.00006':{},     #10 000 events generated for this paragraph
        # 'ALP_Z_aa_0.01.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_0.01.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_0.0316.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_0.1.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_0.316.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_1.0.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.0000019':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.000006':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_3.16.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.0000006':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.0000019':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.000006':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.0000006':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.0000019':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.000006':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.000019':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.00006':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.00019':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.0006':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.0019':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.006':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.019':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.06':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.19':{},
        # 'ALP_Z_aa_31.6.GeV_cYY_0.6':{},

        # 'ee_Z_ALPga_gagaga':{},

        # 'ALP_Z_aa_1GeV_cYY_0p5':{},

        # 'ALP_Z_aa_0.1GeV_cYY_0.1':{},
        # 'ALP_Z_aa_0.2GeV_cYY_0.1':{},
        # 'ALP_Z_aa_0.135GeV_cYY_0.1':{},
        # 'ALP_Z_aa_0.3GeV_cYY_0.1':{},

        # 'ALP_Z_aa_1.GeV_cYY_0.1':{},
        # 'ALP_Z_aa_1.GeV_cYY_0.3':{},
        # 'ALP_Z_aa_1.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_1.GeV_cYY_0.7':{},
        # 'ALP_Z_aa_1.GeV_cYY_0.9':{},

        # 'ALP_Z_aa_0.5.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_0.5.GeV_cYY_1.2':{},

        # 'ALP_Z_aa_1.GeV_cYY_0.6':{},
        # 'ALP_Z_aa_1.GeV_cYY_0.8':{},
        # 'ALP_Z_aa_1.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_1.GeV_cYY_1.2':{},
        # 'ALP_Z_aa_1.GeV_cYY_1.4':{},

        # 'ALP_Z_aa_0.5.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_1.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_1.5.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_2.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_2.1.GeV_cYY_1.0':{},
        #'ALP_Z_aa_3.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_4.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_5.GeV_cYY_1.0':{},
        # 'ALP_5GeV_1p0_bug_new':{},
        # 'ALP_Z_aa_8.GeV_cYY_1.0':{},

        # 'ALP_Z_aa_0.6.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_0.8.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_1.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_1.2.GeV_cYY_1.0':{},
        # 'ALP_Z_aa_1.4.GeV_cYY_1.0':{},

        # 'ALP_Z_aa_2.GeV_cYY_1.0_take3':{},

        # 'ALP_Z_aa_3.GeV_cYY_0.1':{},
        # 'ALP_Z_aa_3.GeV_cYY_0.3':{},
        # 'ALP_Z_aa_3.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_3.GeV_cYY_0.7':{},
        # 'ALP_Z_aa_3.GeV_cYY_0.9':{},

        # 'ALP_Z_aa_5.GeV_cYY_0.1':{},
        # 'ALP_Z_aa_5.GeV_cYY_0.3':{},
        # 'ALP_Z_aa_5.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_5.GeV_cYY_0.7':{},
        # 'ALP_Z_aa_5.GeV_cYY_0.9':{},

        # 'ALP_Z_aa_0.5GeV_cYY_0.5':{},
        # 'ALP_Z_aa_0.7GeV_cYY_0.5':{},
        # 'ALP_Z_aa_1.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_3.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_5.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_7.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_10.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_15.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_20.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_25.GeV_cYY_0.5':{},
        # 'ALP_Z_aa_30.GeV_cYY_0.5':{},

        #test
        #'p8_ee_Zee_ecm91':{'fraction':0.000001},


 #########  private samples, 1Mio events    ########
        # 'ALP_Z_aa_0p5GeV_cYY1p0':{},
        # 'ALP_Z_aa_0p8GeV_cYY1p0':{},
        # 'ALP_Z_aa_1p0GeV_cYY1p0':{},
        # 'ALP_Z_aa_5p0GeV_cYY1p0':{},
        # 'ALP_Z_aa_8p0GeV_cYY1p0':{},



######################################

        # 'ALP_Z_aa_30p0GeV_cYY1p6': {},
        # 'ALP_Z_aa_10p0GeV_cYY1p6': {},
        # 'ALP_Z_aa_3p0GeV_cYY1p6': {},
        # 'ALP_Z_aa_1p0GeV_cYY1p6': {},
        # 'ALP_Z_aa_0p3GeV_cYY1p6': {},
        # 'ALP_Z_aa_0p1GeV_cYY1p6': {},
        # 'ALP_Z_aa_0p03GeV_cYY1p6': {},
        # 'ALP_Z_aa_0p01GeV_cYY1p6': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p4': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p4': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p4': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p4': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p4': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p4': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p4': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p4': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p1': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p1': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p1': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p1': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p1': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p1': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p1': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p1': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p03': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p03': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p03': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p03': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p03': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p03': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p03': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p03': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p009': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p009': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p009': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p009': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p009': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p009': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p009': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p009': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p002': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p002': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p002': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p002': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p002': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p002': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p002': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p002': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p0007': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p0007': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p0007': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p0007': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p0007': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p0007': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p0007': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p0007': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p0002': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p0002': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p0002': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p0002': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p0002': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p0002': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p0002': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p0002': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p00005': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p00005': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p00005': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p00005': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p00005': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p00005': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p00005': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p00005': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p00001': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p00001': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p00001': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p00001': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p00001': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p00001': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p00001': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p00001': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p000004': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p000004': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p000004': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p000004': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p000004': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p000004': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p000004': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p000004': {},

        # 'ALP_Z_aa_30p0GeV_cYY0p000001': {},
        # 'ALP_Z_aa_10p0GeV_cYY0p000001': {},
        # 'ALP_Z_aa_3p0GeV_cYY0p000001': {},
        # 'ALP_Z_aa_1p0GeV_cYY0p000001': {},
        # 'ALP_Z_aa_0p3GeV_cYY0p000001': {},
        # 'ALP_Z_aa_0p1GeV_cYY0p000001': {},
        # 'ALP_Z_aa_0p03GeV_cYY0p000001': {},
        # 'ALP_Z_aa_0p01GeV_cYY0p000001': {},


#########  backgrounds, 1Mio events    ########
        # 'background_ee_aa1':{},
        # 'background_ee_aaa1':{},
        # 'background_ee_aaaa1':{},
        # 'background_ee_ee':{},
        # 'background_ee_eea1':{},
        # 'background_ee_eeaa1':{},
        # 'background_ee_eeaaa1':{},


}

#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
#prodTag     = "FCCee/winter2023/IDEA/"

#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events
# inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/ALPs_3photons/winter2023/output_MadgraphPythiaDelphes/"
# inputDir = "./root_files_for_input/"
# inputDir = "./"
# inputDir = "/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/wzp6_gaga_ee_60_ecm240/"
#inputDir = "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/ALP_sample_creation/"
inputDir = "/eos/user/e/ebakhish/MG/Pythia_Output/"
# inputDir = "./ALP_sample_creation/"



#Optional: output directory, default is local dir
# outputDir = "./stage1_ee_gaga_1million/"
# outputDir = "./stage1_FSGenALP/"
#outputDir = "/eos/user/j/jalimena/FCCeeLLP/"
outputDir = "./stage1_output/"

#outputDirEos = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/ALPs_3photons/winter2023/output_stage1/"
#outputDirEos = "/eos/user/j/jalimena/FCCeeLLP/"
#eosType = "eosuser"

#Optional: ncpus, default is 4
nCPUS       = 4

#Optional running on HTCondor, default is False
# runBatch    = False
runBatch    = False

#Optional batch queue name when running on HTCondor, default is workday
batchQueue = "longlunch"
# batchQueue = "espresso"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
        def analysers(df):

                try:
                        df = df.Alias("MCRecoAssociations0", "_MCRecoAssociations_from.index")
                except:
                        df = df.Alias("MCRecoAssociations0", "_RecoMCLink_from.index")

                try:
                        df = df.Alias("MCRecoAssociations1", "_MCRecoAssociations_to.index")
                except:
                        df = df.Alias("MCRecoAssociations1", "_RecoMCLink_to.index")

                df2 = (df

                #Access the various objects and their properties with the following syntax: .Define("<your_variable>", "<accessor_fct (name_object)>")
		#This will create a column in the RDataFrame named <your_variable> and filled with the return value of the <accessor_fct> for the given collection/object
		#Accessor functions are the functions found in the C++ analyzers code that return a certain variable, e.g. <namespace>::get_n(object) returns the number
		#of these objects in the event and <namespace>::get_pt(object) returns the pt of the object. Here you can pick between two namespaces to access either
		#reconstructed (namespace = ReconstructedParticle) or MC-level objects (namespace = MCParticle).
		#For the name of the object, in principle the names of the EDM4HEP collections are used - photons, muons and electrons are an exception, see below

		#OVERVIEW: Accessing different objects and counting them

              # Following code is written specifically for the ALP study
                ####################################################################################################
                .Alias("Particle1", "_Particle_daughters.index")
             #this part of the analysis changed in pythia/delphes,which changes how the output looks
                # .Alias("MCRecoAssociations0", "_MCRecoAssociations_rec.index")
                # .Alias("MCRecoAssociations1", "_MCRecoAssociations_sim.index")
          #####      .Alias("MCRecoAssociations0", "_MCRecoAssociations_from.index") 
          #####      .Alias("MCRecoAssociations1", "_MCRecoAssociations_to.index")
                # .Alias("MCRecoAssociations0", "_RecoMCLink_from.index")  #use this for newly produces samples since trees in pythia output root changed again
                # .Alias("MCRecoAssociations1", "_RecoMCLink_to.index")

                ##### Added branch for MCParticle; finding PID of the MC particle for ALP
                .Define("GenALP_PID", "MCParticle::sel_pdgID(9000005, false)(Particle)")
                .Define("Calorimeterhit_time", "CalorimeterHits.time")


                # .Define("GenALP_decay", "MCParticle::get_list_of_particles_from_decay(0, GenALP_PID, Particle1)")

                .Define("All_n_GenALP", "MCParticle::get_n(GenALP_PID)")

                .Define("AllGenALP_mass", "MCParticle::get_mass(GenALP_PID)") #finding the generator mass of the ALP through separate ALP branch
                .Define("AllGenALP_e", "MCParticle::get_e(GenALP_PID)")     #energy of the ALP
                .Define("AllGenALP_p", "MCParticle::get_p(GenALP_PID)")
                .Define("AllGenALP_pt", "MCParticle::get_pt(GenALP_PID)")    #finding the pt of the ALP thorugh separate ALP branch
                .Define("AllGenALP_px", "MCParticle::get_px(GenALP_PID)")
                .Define("AllGenALP_py", "MCParticle::get_py(GenALP_PID)")
                .Define("AllGenALP_pz", "MCParticle::get_pz(GenALP_PID)")
                .Define("AllGenALP_eta", "MCParticle::get_eta(GenALP_PID)")
                .Define("AllGenALP_theta", "MCParticle::get_theta(GenALP_PID)")
                .Define("AllGenALP_phi", "MCParticle::get_phi(GenALP_PID)")
                .Define("AllGenALP_genStatus", "MCParticle::get_genStatus(GenALP_PID)")

                #all final state gen electrons
                .Define("GenElectron_PID", "MCParticle::sel_pdgID(11, false)(Particle)") #get MCParticle electrons, but not their charge conjugates
                .Define("FSGenElectron", "MCParticle::sel_genStatus(1)(GenElectron_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenElectron", "MCParticle::get_n(FSGenElectron)")
                .Define("FSGenElectron_e", "MCParticle::get_e(FSGenElectron)")
                .Define("FSGenElectron_p", "MCParticle::get_p(FSGenElectron)")
                .Define("FSGenElectron_pt", "MCParticle::get_pt(FSGenElectron)")
                # .Define("FSGenElectron_px", "MCParticle::get_px(FSGenElectron)")
                # .Define("FSGenElectron_py", "MCParticle::get_py(FSGenElectron)")
                .Define("FSGenElectron_pz", "MCParticle::get_pz(FSGenElectron)")
                .Define("FSGenElectron_eta", "MCParticle::get_eta(FSGenElectron)")
                .Define("FSGenElectron_theta", "MCParticle::get_theta(FSGenElectron)")
                .Define("FSGenElectron_phi", "MCParticle::get_phi(FSGenElectron)")

                #all final state gen electrons and positrons
                .Define("GenElectronPositron_PID", "MCParticle::sel_pdgID(11, true)(Particle)") 
                .Define("FSGenElectronPositron", "MCParticle::sel_genStatus(1)(GenElectronPositron_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenElectronPositron", "MCParticle::get_n(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_e", "MCParticle::get_e(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_p", "MCParticle::get_p(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_pt", "MCParticle::get_pt(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_px", "MCParticle::get_px(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_py", "MCParticle::get_py(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_pz", "MCParticle::get_pz(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_eta", "MCParticle::get_eta(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_theta", "MCParticle::get_theta(FSGenElectronPositron)")
                .Define("FSGenElectronPositron_phi", "MCParticle::get_phi(FSGenElectronPositron)")

                #all final state gen positrons
                .Define("GenPositron_PID", "MCParticle::sel_pdgID(-11, false)(Particle)")
                .Define("FSGenPositron", "MCParticle::sel_genStatus(1)(GenPositron_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenPositron", "MCParticle::get_n(FSGenPositron)")
                .Define("FSGenPositron_e", "MCParticle::get_e(FSGenPositron)")
                .Define("FSGenPositron_p", "MCParticle::get_p(FSGenPositron)")
                .Define("FSGenPositron_pt", "MCParticle::get_pt(FSGenPositron)")
                .Define("FSGenPositron_px", "MCParticle::get_px(FSGenPositron)")
                .Define("FSGenPositron_py", "MCParticle::get_py(FSGenPositron)")
                .Define("FSGenPositron_pz", "MCParticle::get_pz(FSGenPositron)")
                .Define("FSGenPositron_eta", "MCParticle::get_eta(FSGenPositron)")
                .Define("FSGenPositron_theta", "MCParticle::get_theta(FSGenPositron)")
                .Define("FSGenPositron_phi", "MCParticle::get_phi(FSGenPositron)")

                # #all final state gen neutrinos
                # .Define("GenNeutrino_PID", "MCParticle::sel_pdgID(12, false)(Particle)")
                # .Define("FSGenNeutrino", "MCParticle::sel_genStatus(1)(GenNeutrino_PID)") #gen status==1 means final state particle (FS)
                # .Define("n_FSGenNeutrino", "MCParticle::get_n(FSGenNeutrino)")
                # .Define("FSGenNeutrino_e", "MCParticle::get_e(FSGenNeutrino)")
                # .Define("FSGenNeutrino_p", "MCParticle::get_p(FSGenNeutrino)")
                # .Define("FSGenNeutrino_pt", "MCParticle::get_pt(FSGenNeutrino)")
                # .Define("FSGenNeutrino_px", "MCParticle::get_px(FSGenNeutrino)")
                # .Define("FSGenNeutrino_py", "MCParticle::get_py(FSGenNeutrino)")
                # .Define("FSGenNeutrino_pz", "MCParticle::get_pz(FSGenNeutrino)")
                # .Define("FSGenNeutrino_eta", "MCParticle::get_eta(FSGenNeutrino)")
                # .Define("FSGenNeutrino_theta", "MCParticle::get_theta(FSGenNeutrino)")
                # .Define("FSGenNeutrino_phi", "MCParticle::get_phi(FSGenNeutrino)")

                # #all final state gen anti-neutrinos
                # .Define("GenAntiNeutrino_PID", "MCParticle::sel_pdgID(-12, false)(Particle)")
                # .Define("FSGenAntiNeutrino", "MCParticle::sel_genStatus(1)(GenAntiNeutrino_PID)") #gen status==1 means final state particle (FS)
                # .Define("n_FSGenAntiNeutrino", "MCParticle::get_n(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_e", "MCParticle::get_e(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_p", "MCParticle::get_p(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_pt", "MCParticle::get_pt(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_px", "MCParticle::get_px(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_py", "MCParticle::get_py(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_pz", "MCParticle::get_pz(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_eta", "MCParticle::get_eta(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_theta", "MCParticle::get_theta(FSGenAntiNeutrino)")
                # .Define("FSGenAntiNeutrino_phi", "MCParticle::get_phi(FSGenAntiNeutrino)")

                #all final state gen photons
                .Define("GenPhoton_PID", "MCParticle::sel_pdgID(22, false)(Particle)")
                .Define("FSGenPhoton", "MCParticle::sel_genStatus(1)(GenPhoton_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenPhoton", "MCParticle::get_n(FSGenPhoton)")
                .Define("FSGenPhoton_e", "MCParticle::get_e(FSGenPhoton)")
                .Define("FSGenPhoton_p", "MCParticle::get_p(FSGenPhoton)")
                .Define("FSGenPhoton_pt", "MCParticle::get_pt(FSGenPhoton)")
                .Define("FSGenPhoton_px", "MCParticle::get_px(FSGenPhoton)")
                .Define("FSGenPhoton_py", "MCParticle::get_py(FSGenPhoton)")
                .Define("FSGenPhoton_pz", "MCParticle::get_pz(FSGenPhoton)")
                .Define("FSGenPhoton_eta", "MCParticle::get_eta(FSGenPhoton)")
                .Define("FSGenPhoton_theta", "MCParticle::get_theta(FSGenPhoton)")
                .Define("FSGenPhoton_phi", "MCParticle::get_phi(FSGenPhoton)")


                # Number of final state electrons and positrons when the number of final state photons is only 2
                # Returns -2 if the number of final state photons != 2, and therefore will be shown as -2 in the plots
                # .Define("n_FSGenElectron_forFS2GenPhotons", "if (n_FSGenPhoton == 2) {return (n_FSGenElectron); } else {return (-2); }")
                # .Define("n_FSGenPositron_forFS2GenPhotons", "if (n_FSGenPhoton == 2) {return (n_FSGenPositron); } else {return (-2); }")

                .Define("FSGenPhoton_vertex_x", "MCParticle::get_vertex_x( FSGenPhoton )")
                .Define("FSGenPhoton_vertex_y", "MCParticle::get_vertex_y( FSGenPhoton )")
                .Define("FSGenPhoton_vertex_z", "MCParticle::get_vertex_z( FSGenPhoton )")

                # Finding the Lxy of the ALP
                # Definition: Lxy = math.sqrt( (branchGenPtcl.At(daut1).X)**2 + (branchGenPtcl.At(daut1).Y)**2 )
                .Define("FSGen_Lxy", "return sqrt(FSGenPhoton_vertex_x*FSGenPhoton_vertex_x + FSGenPhoton_vertex_y*FSGenPhoton_vertex_y)")
                .Define("FSGen_Lxyz", "return sqrt(FSGenPhoton_vertex_x*FSGenPhoton_vertex_x + FSGenPhoton_vertex_y*FSGenPhoton_vertex_y + FSGenPhoton_vertex_z*FSGenPhoton_vertex_z)")

                # Calculating the lifetime of the ALP
                # Definition: t = Lxy * branchGenPtcl.At(i).Mass / (branchGenPtcl.At(i).PT * 1000 * 3E8)
                # .Define("FSGen_lifetime_xy", "return ( FSGen_Lxy.at(0) * AllGenALP_mass / (AllGenALP_pt * 3E8 * 1000))" )
                # .Define("FSGen_lifetime_xyz", "return ( FSGen_Lxy.at(0) * AllGenALP_mass / (AllGenALP_p * 3E8 * 1000))" )

                # Separating the three first final state photons
                # Returns -2 if the number of final state photons != 2, and therefore will be shown as -2 in the plots
                .Define("FSGenPhoton0_e", "if (n_FSGenPhoton >= 1) {return FSGenPhoton_e.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_e", "if (n_FSGenPhoton >= 2) {return FSGenPhoton_e.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_e", "if (n_FSGenPhoton >= 3) {return FSGenPhoton_e.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_p", "if (n_FSGenPhoton >= 1) {return FSGenPhoton_p.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_p", "if (n_FSGenPhoton >= 2) {return FSGenPhoton_p.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_p", "if (n_FSGenPhoton >= 3) {return FSGenPhoton_p.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_pt", "if (n_FSGenPhoton >= 1) {return FSGenPhoton_pt.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_pt", "if (n_FSGenPhoton >= 2) {return FSGenPhoton_pt.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_pt", "if (n_FSGenPhoton >= 3) {return FSGenPhoton_pt.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_px", "if (n_FSGenPhoton >= 1) {return FSGenPhoton_px.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_px", "if (n_FSGenPhoton >= 2) {return FSGenPhoton_px.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_px", "if (n_FSGenPhoton >= 3) {return FSGenPhoton_px.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_py", "if (n_FSGenPhoton >= 1) {return FSGenPhoton_py.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_py", "if (n_FSGenPhoton >= 2) {return FSGenPhoton_py.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_py", "if (n_FSGenPhoton >= 3) {return FSGenPhoton_py.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_pz", "if (n_FSGenPhoton >= 1) {return FSGenPhoton_pz.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_pz", "if (n_FSGenPhoton >= 2) {return FSGenPhoton_pz.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_pz", "if (n_FSGenPhoton >= 3) {return FSGenPhoton_pz.at(2);} else {return (-2.0f); }")

                .Define("FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0", "if (FSGenPhoton0_px > 0) {return FSGenPhoton1_px;} else {return -50.0f;}")
                .Define("FSGenPhoton1_px_if_FSGenPhoton2_px_pos", "if (FSGenPhoton2_px > 0) {return FSGenPhoton1_px;} else {return -50.0f;}")
                .Define("FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos", "if (FSGenPhoton2_pz > 0) {return FSGenPhoton1_pz;} else {return -50.0f;}")

                # aa invariant mass - for all three combinations of the three first FS photons
                # returns -2 for events with only 1 number of photons
                # .Define("FSGen_a0a1_energy", "return (FSGenPhoton0_e + FSGenPhoton1_e)")
                # .Define("FSGen_a0a1_px", "return (FSGenPhoton0_px + FSGenPhoton1_px)")
                # .Define("FSGen_a0a1_py", "return (FSGenPhoton0_py + FSGenPhoton1_py)")
                # .Define("FSGen_a0a1_pz", "return (FSGenPhoton0_pz + FSGenPhoton1_pz)")
                # .Define("FSGen_a0a1_invMass", "if (n_FSGenPhoton > 1) { return sqrt(FSGen_a0a1_energy*FSGen_a0a1_energy - FSGen_a0a1_px*FSGen_a0a1_px - FSGen_a0a1_py*FSGen_a0a1_py - FSGen_a0a1_pz*FSGen_a0a1_pz ); } else {return -2.0f;}")

                # .Define("FSGen_a0a2_energy", "return (FSGenPhoton0_e + FSGenPhoton2_e)")
                # .Define("FSGen_a0a2_px", "return (FSGenPhoton0_px + FSGenPhoton2_px)")
                # .Define("FSGen_a0a2_py", "return (FSGenPhoton0_py + FSGenPhoton2_py)")
                # .Define("FSGen_a0a2_pz", "return (FSGenPhoton0_pz + FSGenPhoton2_pz)")
                # .Define("FSGen_a0a2_invMass", "if (n_FSGenPhoton > 1) { return sqrt(FSGen_a0a2_energy*FSGen_a0a2_energy - FSGen_a0a2_px*FSGen_a0a2_px - FSGen_a0a2_py*FSGen_a0a2_py - FSGen_a0a2_pz*FSGen_a0a2_pz ); } else {return -2.0f;}")

                # .Define("FSGen_a1a2_energy", "return (FSGenPhoton1_e + FSGenPhoton2_e)")
                # .Define("FSGen_a1a2_px", "return (FSGenPhoton1_px + FSGenPhoton2_px)")
                # .Define("FSGen_a1a2_py", "return (FSGenPhoton1_py + FSGenPhoton2_py)")
                # .Define("FSGen_a1a2_pz", "return (FSGenPhoton1_pz + FSGenPhoton2_pz)")
                # .Define("FSGen_a1a2_invMass", "if (n_FSGenPhoton > 1) { return sqrt(FSGen_a1a2_energy*FSGen_a1a2_energy - FSGen_a1a2_px*FSGen_a1a2_px - FSGen_a1a2_py*FSGen_a1a2_py - FSGen_a1a2_pz*FSGen_a1a2_pz ); } else {return -2.0f;}")

                # aaa invariant mass
                # Returns -2 for events with only 1 or 2 number of photons
                # .Define("FSGen_aaa_energy", "return (FSGenPhoton0_e + FSGenPhoton1_e + FSGenPhoton2_e)")
                # .Define("FSGen_aaa_px", "return (FSGenPhoton0_px + FSGenPhoton1_px + FSGenPhoton2_px)")
                # .Define("FSGen_aaa_py", "return (FSGenPhoton0_py + FSGenPhoton1_py + FSGenPhoton2_py)")
                # .Define("FSGen_aaa_pz", "return (FSGenPhoton0_pz + FSGenPhoton1_pz + FSGenPhoton2_pz)")
                # .Define("FSGen_aaa_invMass", "if (n_FSGenPhoton > 2) { return sqrt(FSGen_aaa_energy*FSGen_aaa_energy - FSGen_aaa_px*FSGen_aaa_px - FSGen_aaa_py*FSGen_aaa_py - FSGen_aaa_pz*FSGen_aaa_pz ); } else {return -2.0f;}")

                # Defining a vector containing the ALP and its daughters in order written
                # Name of vector is ALP_indices
                .Define("GenALP_indices", "MCParticle::get_indices(9000005, {22, 22}, true, false, false, true)(Particle, Particle1)")

                # Defining the individual particles from the vector
                .Define("GenALP", "myUtils::selMC_leg(0)(GenALP_indices, Particle)")
                .Define("GenALPPhoton1", "myUtils::selMC_leg(1)(GenALP_indices, Particle)")
                .Define("GenALPPhoton2", "myUtils::selMC_leg(2)(GenALP_indices, Particle)")

                # Defining final state ALPs to get rid of duplicates
                .Define("FSGenALP", "MCParticle::sel_genStatus(1)(GenALP_PID)")

                .Define("n_FSGenALP", "MCParticle::get_n( FSGenALP )")

                # Kinematics of final state ALP (attempt Merlin) (ALP defined with PID, FS Pythia status)
                .Define("FSGenALP_mass", "MCParticle::get_mass( FSGenALP )")
                .Define("FSGenALP_e", "MCParticle::get_e( FSGenALP )")
                .Define("FSGenALP_p", "MCParticle::get_p( FSGenALP )")
                .Define("FSGenALP_pt", "MCParticle::get_pt( FSGenALP )")
                .Define("FSGenALP_px", "MCParticle::get_px( FSGenALP )")
                .Define("FSGenALP_py", "MCParticle::get_py( FSGenALP )")
                .Define("FSGenALP_pz", "MCParticle::get_pz( FSGenALP )")
                .Define("FSGenALP_eta", "MCParticle::get_eta( FSGenALP )")
                .Define("FSGenALP_theta", "MCParticle::get_theta( FSGenALP )")
                .Define("FSGenALP_phi", "MCParticle::get_phi( FSGenALP )")
                .Define("FSGenALP_genStatus", "MCParticle::get_genStatus( FSGenALP )")

                # Kinematics of the mother particle ALP (defined with 2 daughter photons)
                .Define("GenALP_mass", "MCParticle::get_mass( GenALP )")
                .Define("GenALP_e", "MCParticle::get_e( GenALP )")
                .Define("GenALP_p", "MCParticle::get_p( GenALP )")
                .Define("GenALP_pt", "MCParticle::get_pt( GenALP )")
                .Define("GenALP_px", "MCParticle::get_px( GenALP )")
                .Define("GenALP_py", "MCParticle::get_py( GenALP )")
                .Define("GenALP_pz", "MCParticle::get_pz( GenALP )")
                .Define("GenALP_eta", "MCParticle::get_eta( GenALP )")
                .Define("GenALP_theta", "MCParticle::get_theta( GenALP )")
                .Define("GenALP_phi", "MCParticle::get_phi( GenALP )")
                .Define("GenALP_genStatus", "MCParticle::get_genStatus( GenALP )")

                .Define("GenALP_beta", "return GenALP_p / GenALP_e")

                .Define("GenALP_px_if_FSGenPhoton0_px_greaterthan_0", "if (FSGenPhoton0_px > 0) {return GenALP_px[0];} else {return -50.0f;}")
                .Define("FSGenPhoton1_px_if_GenALP_px_neg", "if (GenALP_px[0] < 0) {return FSGenPhoton1_px;} else {return -50.0f;}")
                .Define("FSGenPhoton2_px_if_GenALP_px_neg", "if (GenALP_px[0] < 0) {return FSGenPhoton2_px;} else {return -50.0f;}")

                .Define("n_GenALP", "MCParticle::get_n( GenALP )")
                .Define("GenALP_time", "MCParticle::get_time( GenALP )")        #time at which ALP decays from Z
                .Define("GenALP_pdg", "MCParticle::get_pdg( GenALP )")
                .Define("GenALP_endPoint_x", "MCParticle::get_endPoint_x")

                # .Define("GenALP_deltaR", "return sqrt(GenALP_eta*GenALP_eta + GenALP_phi*GenALP_phi)")

                # Finding the kinematics of each of these daughters
                .Define("n_GenALPPhoton1", "MCParticle::get_n( GenALPPhoton1 )")
                .Define("n_GenALPPhoton2", "MCParticle::get_n( GenALPPhoton2 )")

                .Define("GenALPPhoton1_e", "MCParticle::get_e( GenALPPhoton1 )")
                .Define("GenALPPhoton2_e", "MCParticle::get_e( GenALPPhoton2 )")
                .Define("GenALPPhoton1_p", "MCParticle::get_p( GenALPPhoton1 )")
                .Define("GenALPPhoton2_p", "MCParticle::get_p( GenALPPhoton2 )")
                .Define("GenALPPhoton1_pt", "MCParticle::get_pt( GenALPPhoton1 )")
                .Define("GenALPPhoton2_pt", "MCParticle::get_pt( GenALPPhoton2 )")
                .Define("GenALPPhoton1_px", "MCParticle::get_px( GenALPPhoton1 )")
                .Define("GenALPPhoton2_px", "MCParticle::get_px( GenALPPhoton2 )")
                .Define("GenALPPhoton1_py", "MCParticle::get_py( GenALPPhoton1 )")
                .Define("GenALPPhoton2_py", "MCParticle::get_py( GenALPPhoton2 )")
                .Define("GenALPPhoton1_pz", "MCParticle::get_pz( GenALPPhoton1 )")
                .Define("GenALPPhoton2_pz", "MCParticle::get_pz( GenALPPhoton2 )")
                .Define("GenALPPhoton1_eta", "MCParticle::get_eta( GenALPPhoton1 )")
                .Define("GenALPPhoton2_eta", "MCParticle::get_eta( GenALPPhoton2 )")
                .Define("GenALPPhoton1_theta", "MCParticle::get_theta( GenALPPhoton1 )")
                .Define("GenALPPhoton2_theta", "MCParticle::get_theta( GenALPPhoton2 )")
                .Define("GenALPPhoton1_phi", "MCParticle::get_phi( GenALPPhoton1 )")
                .Define("GenALPPhoton2_phi", "MCParticle::get_phi( GenALPPhoton2 )")
                .Define("GenALPPhoton1_genStatus", "MCParticle::get_genStatus( GenALPPhoton1 )")
                .Define("GenALPPhoton2_genStatus", "MCParticle::get_genStatus( GenALPPhoton2 )")

                .Define("GenALPPhotons_deltaEta", "return abs(GenALPPhoton1_eta - GenALPPhoton2_eta)")
                .Define("GenALPPhotons_deltaPhi", "return abs(GenALPPhoton1_phi - GenALPPhoton2_phi)")
                .Define("GenALPPhotons_deltaR", "return sqrt(GenALPPhotons_deltaEta*GenALPPhotons_deltaEta + GenALPPhotons_deltaPhi*GenALPPhotons_deltaPhi)")

                # .Define("GenALPPhotons_deltaR_2", "MCParticle::get_ALP_delta_r(GenALPPhoton1, GenALPPhoton2)")
                .Define("FSGenPhotons_delta_r", "MCParticle::get_delta_r(FSGenPhoton)")
                .Define("FSGenPhotons_min_delta_r", "MCParticle::get_min_delta_r(FSGenPhoton)")

                .Define("GenALPPhoton1_time", "MCParticle::get_time( GenALPPhoton1 )")
                .Define("GenALPPhoton2_time", "MCParticle::get_time( GenALPPhoton2 )")

                # .Define("GenALPPhoton1_deltaR", "return sqrt(GenALPPhoton1_eta*GenALPPhoton1_eta + GenALPPhoton1_phi*GenALPPhoton1_phi)")
                # .Define("GenALPPhoton2_deltaR", "return sqrt(GenALPPhoton2_eta*GenALPPhoton2_eta + GenALPPhoton2_phi*GenALPPhoton2_phi)")


                # Finding the production vertex of the daughters (checking GenALPPhoton1 here)
                .Define("GenALPPhoton1_vertex_x", "MCParticle::get_vertex_x( GenALPPhoton1 )")
                .Define("GenALPPhoton1_vertex_y", "MCParticle::get_vertex_y( GenALPPhoton1 )")
                .Define("GenALPPhoton1_vertex_z", "MCParticle::get_vertex_z( GenALPPhoton1 )")

                # Finding the Lxy of the ALP
                # Definition: Lxy = math.sqrt( (branchGenPtcl.At(daut1).X)**2 + (branchGenPtcl.At(daut1).Y)**2 )
                .Define("GenALP_Lxy", "return sqrt(GenALPPhoton1_vertex_x*GenALPPhoton1_vertex_x + GenALPPhoton1_vertex_y*GenALPPhoton1_vertex_y)")
                # Finding the Lxyz of the ALP
                .Define("GenALP_Lxyz", "return sqrt(GenALPPhoton1_vertex_x*GenALPPhoton1_vertex_x + GenALPPhoton1_vertex_y*GenALPPhoton1_vertex_y + GenALPPhoton1_vertex_z*GenALPPhoton1_vertex_z)")

                # Calculating the lifetime of the ALP
                # Definition: t = Lxy * branchGenPtcl.At(i).Mass / (branchGenPtcl.At(i).PT * 1000 * 3E8)
                .Define("GenALP_lifetime_xy", "return ( GenALP_Lxy * GenALP_mass / (GenALP_pt * 3E8 * 1000))" )
                .Define("GenALP_lifetime_xyz", "return ( GenALP_Lxyz * GenALP_mass / (GenALP_p * 3E8 * 1000))" )

                .Define("GenALP_observed_lifetime_xyz", "return ((GenALP_p / GenALP_mass) * GenALP_lifetime_xyz)")

                .Define("GenALPPhoton1_time_minus_GenALP_time", "return (GenALPPhoton1_time - GenALP_time)")

                # Finding the production vertex of the ALP which should be at (0,0,0)
                .Define("GenALP_vertex_x", "MCParticle::get_vertex_x(GenALP_PID)")
                .Define("GenALP_vertex_y", "MCParticle::get_vertex_y(GenALP_PID)")
                .Define("GenALP_vertex_z", "MCParticle::get_vertex_z(GenALP_PID)")

                # aa invariant mass
                .Define("GenALP_aa_energy", "return (GenALPPhoton1_e + GenALPPhoton2_e)")
                .Define("GenALP_aa_px", "return (GenALPPhoton1_px + GenALPPhoton2_px)")
                .Define("GenALP_aa_py", "return (GenALPPhoton1_py + GenALPPhoton2_py)")
                .Define("GenALP_aa_pz", "return (GenALPPhoton1_pz + GenALPPhoton2_pz)")
                .Define("GenALP_aa_invMass", "return sqrt(GenALP_aa_energy*GenALP_aa_energy - GenALP_aa_px*GenALP_aa_px - GenALP_aa_py*GenALP_aa_py - GenALP_aa_pz*GenALP_aa_pz )")

                # Vertexing studies
                # Finding the vertex of the mother particle ALP using decicated Bs method
                #.Define("GenALPMCDecayVertex",   "BsMCDecayVertex( GenALP_indices, Particle )")

                # MC event primary vertex
                .Define("MC_PrimaryVertex",  "MCParticle::get_EventPrimaryVertex(21)( Particle )" )
                .Define("n_RecoTracks","ReconstructedParticle2Track::getTK_n(_EFlowTrack_trackStates)")

                # Reconstructed particles
                # Returns the RecoParticles associated with the ALP decay products
                .Define("RecoALPParticles",  "ReconstructedParticle2MC::selRP_matched_to_list( GenALP_indices, MCRecoAssociations0,MCRecoAssociations1,ReconstructedParticles,Particle)")
                # Reconstructing the tracks from the ALP
                .Define("RecoALPTracks",   "ReconstructedParticle2Track::getRP2TRK( RecoALPParticles, _EFlowTrack_trackStates)")

                # Number of tracks in this RecoALPTracks collection ( = the #tracks used to reconstruct the ALP reco decay vertex)
                .Define("n_RecoALPTracks", "ReconstructedParticle2Track::getTK_n( RecoALPTracks )")

                # Now we reconstruct the ALP reco decay vertex using the reco'ed tracks
                # First the full object, of type Vertexing::FCCAnalysesVertex
                .Define("RecoALPDecayVertexObject",   "VertexFitterSimple::VertexFitter_Tk( 2, RecoALPTracks)" ) #tk=track

                # from which we extract the edm4hep::VertexData object, which contains the vertex position in mm
                .Define("RecoALPDecayVertex",  "VertexingUtils::get_VertexData( RecoALPDecayVertexObject )")

                .Define("RecoALPL_xyz", "return sqrt(RecoALPDecayVertex.position.x*RecoALPDecayVertex.position.x + RecoALPDecayVertex.position.y*RecoALPDecayVertex.position.y + RecoALPDecayVertex.position.z*RecoALPDecayVertex.position.z)")

                # We may want to look at the reco'ed ALPs legs: in the RecoALPParticles vector,
                # the first particle (vector[0]) is the e-, etc :
                .Define("RecoALPPhoton1",   "myUtils::selRP_leg(0)( RecoALPParticles )")
                .Define("RecoALPPhoton2",   "myUtils::selRP_leg(1)( RecoALPParticles )")

                # reconstruced electron, positron values
                .Define("RecoALPPhoton1_e",  "ReconstructedParticle::get_e( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_e",  "ReconstructedParticle::get_e( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_p",  "ReconstructedParticle::get_p( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_p",  "ReconstructedParticle::get_p( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_pt",  "ReconstructedParticle::get_pt( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_pt",  "ReconstructedParticle::get_pt( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_px",  "ReconstructedParticle::get_px( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_px",  "ReconstructedParticle::get_px( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_py",  "ReconstructedParticle::get_py( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_py",  "ReconstructedParticle::get_py( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_pz",  "ReconstructedParticle::get_pz( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_pz",  "ReconstructedParticle::get_pz( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_eta",  "ReconstructedParticle::get_eta( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_eta",  "ReconstructedParticle::get_eta( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_theta",  "ReconstructedParticle::get_theta( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_theta",  "ReconstructedParticle::get_theta( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_phi",  "ReconstructedParticle::get_phi( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_phi",  "ReconstructedParticle::get_phi( RecoALPPhoton2 )")
                .Define("RecoALPPhoton1_charge",  "ReconstructedParticle::get_charge( RecoALPPhoton1 )")
                .Define("RecoALPPhoton2_charge",  "ReconstructedParticle::get_charge( RecoALPPhoton2 )")

                .Define("RecoALPPhotons_deltaEta", "return abs(RecoALPPhoton1_eta - RecoALPPhoton2_eta)")
                .Define("RecoALPPhotons_deltaPhi", "return RecoALPPhoton1_phi - RecoALPPhoton2_phi")
                # .Define("RecoALPPhotons_deltaR", "return sqrt(RecoALPPhotons_deltaEta*RecoALPPhotons_deltaEta  + RecoALPPhotons_deltaPhi*RecoALPPhotons_deltaPhi)")
                # .Define("RecoALPPhotons_deltaR", "ReconstructedParticle::get_delta_r(RecoALPPhoton1.at(0), RecoALPPhoton2.at(0))")
                .Define("RecoALPPhotons_deltaR",
                        "if (RecoALPPhoton1.size() > 0 && RecoALPPhoton2.size() > 0) { "
                        "return ReconstructedParticle::get_delta_r(RecoALPPhoton1.at(0), RecoALPPhoton2.at(0)); "
                        "} else { return -2.0f; }")     #if statement needed otherwise sometimes we have empty containers leading to an out of bounds request

                .Define("n_RecoALPPhoton1", "ReconstructedParticle::get_n( RecoALPPhoton1 )")
                .Define("n_RecoALPPhoton2", "ReconstructedParticle::get_n( RecoALPPhoton2 )")
                # .Define("RecoALPPhoton1_time", "ReconstructedParticle::get_time( RecoALPPhoton1 )")
                # .Define("RecoALPPhoton2_time", "ReconstructedParticle::get_time( RecoALPPhoton2 )")
                # add dxy, dz, dxyz, and uncertainties

                # aa invariant mass of ALP photons (matched to gen level)
                .Define("RecoALP_aa_energy", "return (RecoALPPhoton1_e + RecoALPPhoton2_e)")
                .Define("RecoALP_aa_px", "return (RecoALPPhoton1_px + RecoALPPhoton2_px)")
                .Define("RecoALP_aa_py", "return (RecoALPPhoton1_py + RecoALPPhoton2_py)")
                .Define("RecoALP_aa_pz", "return (RecoALPPhoton1_pz + RecoALPPhoton2_pz)")
                .Define("RecoALP_aa_invMass", "return sqrt(RecoALP_aa_energy*RecoALP_aa_energy - RecoALP_aa_px*RecoALP_aa_px - RecoALP_aa_py*RecoALP_aa_py - RecoALP_aa_pz*RecoALP_aa_pz )")
                .Define("RecoALP_aa_p", "return sqrt(RecoALP_aa_px*RecoALP_aa_px + RecoALP_aa_py*RecoALP_aa_py + RecoALP_aa_pz*RecoALP_aa_pz)")


                #gen-reco
                .Define("GenMinusRecoALPPhoton1_e",   "GenALPPhoton1_e-RecoALPPhoton1_e")
                .Define("GenMinusRecoALPPhoton2_e",   "GenALPPhoton2_e-RecoALPPhoton2_e")
                .Define("GenMinusRecoALPPhoton1_p",   "GenALPPhoton1_p-RecoALPPhoton1_p")
                .Define("GenMinusRecoALPPhoton2_p",   "GenALPPhoton2_p-RecoALPPhoton2_p")
                .Define("GenMinusRecoALPPhoton1_pt",   "GenALPPhoton1_pt-RecoALPPhoton1_pt")
                .Define("GenMinusRecoALPPhoton2_pt",   "GenALPPhoton2_pt-RecoALPPhoton2_pt")
                .Define("GenMinusRecoALPPhoton1_px",   "GenALPPhoton1_px-RecoALPPhoton1_px")
                .Define("GenMinusRecoALPPhoton2_px",   "GenALPPhoton2_px-RecoALPPhoton2_px")
                .Define("GenMinusRecoALPPhoton1_py",   "GenALPPhoton1_py-RecoALPPhoton1_py")
                .Define("GenMinusRecoALPPhoton2_py",   "GenALPPhoton2_py-RecoALPPhoton2_py")
                .Define("GenMinusRecoALPPhoton1_pz",   "GenALPPhoton1_pz-RecoALPPhoton1_pz")
                .Define("GenMinusRecoALPPhoton2_pz",   "GenALPPhoton2_pz-RecoALPPhoton2_pz")
                .Define("GenMinusRecoALPPhoton1_eta",  "GenALPPhoton1_eta-RecoALPPhoton1_eta")
                .Define("GenMinusRecoALPPhoton2_eta",  "GenALPPhoton2_eta-RecoALPPhoton2_eta")
                .Define("GenMinusRecoALPPhoton1_theta",  "GenALPPhoton1_theta-RecoALPPhoton1_theta")
                .Define("GenMinusRecoALPPhoton2_theta",  "GenALPPhoton2_theta-RecoALPPhoton2_theta")
                .Define("GenMinusRecoALPPhoton1_phi",  "GenALPPhoton1_phi-RecoALPPhoton1_phi")
                .Define("GenMinusRecoALPPhoton2_phi",  "GenALPPhoton2_phi-RecoALPPhoton2_phi")

                .Define("GenMinusRecoALP_DecayVertex_x",  "GenALPPhoton1_vertex_x-RecoALPDecayVertex.position.x")
                .Define("GenMinusRecoALP_DecayVertex_y",  "GenALPPhoton1_vertex_y-RecoALPDecayVertex.position.y")
                .Define("GenMinusRecoALP_DecayVertex_z",  "GenALPPhoton1_vertex_z-RecoALPDecayVertex.position.z")


                ####################################################################################################
                # From here the general study begins

                #JETS
                .Define("n_RecoJets", "ReconstructedParticle::get_n(Jet)") #count how many jets are in the event in total

                #PHOTONS
                .Alias("Photon0", "Photon_objIdx.index")
                .Define("RecoPhotons",  "ReconstructedParticle::get(Photon0, ReconstructedParticles)")
                .Define("n_RecoPhotons",  "ReconstructedParticle::get_n(RecoPhotons)") #count how many photons are in the event in total

                #ELECTRONS AND MUONS
                #TODO: ADD EXPLANATION OF THE EXTRA STEPS
                .Alias("Electron0", "Electron_objIdx.index")
                .Define("RecoElectrons",  "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
                .Define("n_RecoElectrons",  "ReconstructedParticle::get_n(RecoElectrons)") #count how many electrons are in the event in total

                .Alias("Muon0", "Muon_objIdx.index")
                .Define("RecoMuons",  "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
                .Define("n_RecoMuons",  "ReconstructedParticle::get_n(RecoMuons)") #count how many muons are in the event in total

                #OBJECT SELECTION: Consider only those objects that have pt > certain threshold
                #.Define("selected_jets", "ReconstructedParticle::sel_pt(0.)(Jet)") #select only jets with a pt > 50 GeV
                #.Define("selected_electrons", "ReconstructedParticle::sel_pt(0.)(electrons)") #select only electrons with a pt > 20 GeV
                # .Define("selected_photons", "ReconstructedParticle::sel_pt(10.0)(photons)") #select only photons with a pt > 10 GeV
                #.Define("selected_muons", "ReconstructedParticle::sel_pt(0.)(muons)")

                #.Define("n_selJets", "ReconstructedParticle::get_n(selected_jets)")
                #.Define("n_selElectrons", "ReconstructedParticle::get_n(selected_electrons)")
                #.Define("n_selPhotons", "ReconstructedParticle::get_n(selected_photons)")
                #.Define("n_selMuons", "ReconstructedParticle::get_n(selected_muons)")

                #SIMPLE VARIABLES: Access the basic kinematic variables of the (selected) jets, works analogously for electrons, muons
                # .Define("RecoJet_e",      "ReconstructedParticle::get_e(Jet)")
                # .Define("RecoJet_p",      "ReconstructedParticle::get_p(Jet)") #momentum p
                # .Define("RecoJet_pt",      "ReconstructedParticle::get_pt(Jet)") #transverse momentum pt
                # .Define("RecoJet_px",      "ReconstructedParticle::get_px(Jet)")
                # .Define("RecoJet_py",      "ReconstructedParticle::get_py(Jet)")
                # .Define("RecoJet_pz",      "ReconstructedParticle::get_pz(Jet)")
                # .Define("RecoJet_eta",     "ReconstructedParticle::get_eta(Jet)") #pseudorapidity eta
                # .Define("RecoJet_theta",   "ReconstructedParticle::get_theta(Jet)")
                # .Define("RecoJet_phi",     "ReconstructedParticle::get_phi(Jet)") #polar angle in the transverse plane phi
                # .Define("RecoJet_charge",  "ReconstructedParticle::get_charge(Jet)")

                .Define("RecoElectron_e",      "ReconstructedParticle::get_e(RecoElectrons)")
                .Define("RecoElectron_p",      "ReconstructedParticle::get_p(RecoElectrons)")
                .Define("RecoElectron_pt",      "ReconstructedParticle::get_pt(RecoElectrons)")
                # .Define("RecoElectron_px",      "ReconstructedParticle::get_px(RecoElectrons)")
                # .Define("RecoElectron_py",      "ReconstructedParticle::get_py(RecoElectrons)")
                .Define("RecoElectron_pz",      "ReconstructedParticle::get_pz(RecoElectrons)")
                .Define("RecoElectron_eta",     "ReconstructedParticle::get_eta(RecoElectrons)") #pseudorapidity eta
                .Define("RecoElectron_theta",   "ReconstructedParticle::get_theta(RecoElectrons)")
                .Define("RecoElectron_phi",     "ReconstructedParticle::get_phi(RecoElectrons)") #polar angle in the transverse plane phi
                # .Define("RecoElectron_charge",  "ReconstructedParticle::get_charge(RecoElectrons)")

                # .Define("RecoElectronPositron_e",      "ReconstructedParticle::get_e(RecoElectronPositrons)")
                # .Define("RecoElectronPositron_p",      "ReconstructedParticle::get_p(RecoElectronPositrons)")
                # .Define("RecoElectronPositron_pt",      "ReconstructedParticle::get_pt(RecoElectronPositrons)")
                # # .Define("RecoElectronPositron_px",      "ReconstructedParticle::get_px(RecoElectronPositrons)")
                # # .Define("RecoElectronPositron_py",      "ReconstructedParticle::get_py(RecoElectronPositrons)")
                # .Define("RecoElectronPositron_pz",      "ReconstructedParticle::get_pz(RecoElectronPositrons)")
                # .Define("RecoElectronPositron_eta",     "ReconstructedParticle::get_eta(RecoElectronPositrons)") #pseudorapidity eta
                # .Define("RecoElectronPositron_theta",   "ReconstructedParticle::get_theta(RecoElectronPositrons)")
                # .Define("RecoElectronPositron_phi",     "ReconstructedParticle::get_phi(RecoElectronPositrons)") #polar angle in the transverse plane phi

                .Define("RecoPhoton_e",      "ReconstructedParticle::get_e(RecoPhotons)")
                .Define("RecoPhoton_p",      "ReconstructedParticle::get_p(RecoPhotons)")
                .Define("RecoPhoton_pt",      "ReconstructedParticle::get_pt(RecoPhotons)")
                .Define("RecoPhoton_px",      "ReconstructedParticle::get_px(RecoPhotons)")
                .Define("RecoPhoton_py",      "ReconstructedParticle::get_py(RecoPhotons)")
                .Define("RecoPhoton_pz",      "ReconstructedParticle::get_pz(RecoPhotons)")
                .Define("RecoPhoton_eta",     "ReconstructedParticle::get_eta(RecoPhotons)") #pseudorapidity eta
                .Define("RecoPhoton_theta",   "ReconstructedParticle::get_theta(RecoPhotons)")
                .Define("RecoPhoton_phi",     "ReconstructedParticle::get_phi(RecoPhotons)") #polar angle in the transverse plane phi
                .Define("RecoPhoton_charge",  "ReconstructedParticle::get_charge(RecoPhotons)")

                .Define("RecoPhotons_delta_eta", "ReconstructedParticle::get_delta_eta(RecoPhotons)")
                .Define("RecoPhotons_delta_phi", "ReconstructedParticle::get_delta_phi(RecoPhotons)")
                .Define("RecoPhotons_delta_r",   "ReconstructedParticle::get_delta_r(RecoPhotons)")

                .Define("RecoPhotons_min_delta_r", "ReconstructedParticle::get_min_delta_r(RecoPhotons)")

                # .Define("RecoPhotons_ALP_delta_r", "ReconstructedParticle::get_ALP_delta_r(RecoALPPhoton1, RecoALPPhoton2)")
                # .Define("RecoPhotons_ALP_delta_phi", "ReconstructedParticle::get_ALP_delta_phi(RecoALPPhoton1, RecoALPPhoton2)")
                # .Define("RecoPhotons_ALP_delta_eta", "ReconstructedParticle::get_ALP_delta_eta(RecoALPPhoton1, RecoALPPhoton2)")

                # .Define("RecoPhoton_y",       "ReconstructedParticle::get_y(RecoPhotons)")
                # .Define("RecoPhoton_time",    "ReconstructedParticle::get_time(RecoPhotons)")

                # .Define("RecoPhoton_reference_point_x", "ReconstructedParticle::get_reference_point_x(RecoPhotons)")

                .Define("RecoPhoton0_e", "if (n_RecoPhotons >= 1) {return RecoPhoton_e.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_e", "if (n_RecoPhotons >= 2) {return RecoPhoton_e.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_e", "if (n_RecoPhotons >= 3) {return RecoPhoton_e.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_p", "if (n_RecoPhotons >= 1) {return RecoPhoton_p.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_p", "if (n_RecoPhotons >= 2) {return RecoPhoton_p.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_p", "if (n_RecoPhotons >= 3) {return RecoPhoton_p.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_pt", "if (n_RecoPhotons >= 1) {return RecoPhoton_pt.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_pt", "if (n_RecoPhotons >= 2) {return RecoPhoton_pt.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_pt", "if (n_RecoPhotons >= 3) {return RecoPhoton_pt.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_px", "if (n_RecoPhotons >= 1) {return RecoPhoton_px.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_px", "if (n_RecoPhotons >= 2) {return RecoPhoton_px.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_px", "if (n_RecoPhotons >= 3) {return RecoPhoton_px.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_py", "if (n_RecoPhotons >= 1) {return RecoPhoton_py.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_py", "if (n_RecoPhotons >= 2) {return RecoPhoton_py.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_py", "if (n_RecoPhotons >= 3) {return RecoPhoton_py.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_pz", "if (n_RecoPhotons >= 1) {return RecoPhoton_pz.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_pz", "if (n_RecoPhotons >= 2) {return RecoPhoton_pz.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_pz", "if (n_RecoPhotons >= 3) {return RecoPhoton_pz.at(2);} else {return (-2.0f); }")
                # .Define("RecoPhoton0_e", "return RecoPhoton_e.at(0)")
                # .Define("RecoPhoton1_e", "return RecoPhoton_e.at(1)")
                # .Define("RecoPhoton2_e", "return RecoPhoton_e.at(2)")
                # .Define("RecoPhoton0_p", "return RecoPhoton_p.at(0)")
                # .Define("RecoPhoton1_p", "return RecoPhoton_p.at(1)")
                # .Define("RecoPhoton2_p", "return RecoPhoton_p.at(2)")
                # .Define("RecoPhoton0_pt", "return RecoPhoton_pt.at(0)")
                # .Define("RecoPhoton1_pt", "return RecoPhoton_pt.at(1)")
                # .Define("RecoPhoton2_pt", "return RecoPhoton_pt.at(2)")
                # .Define("RecoPhoton0_px", "return RecoPhoton_px.at(0)")
                # .Define("RecoPhoton1_px", "return RecoPhoton_px.at(1)")
                # .Define("RecoPhoton2_px", "return RecoPhoton_px.at(2)")
                # .Define("RecoPhoton0_py", "return RecoPhoton_py.at(0)")
                # .Define("RecoPhoton1_py", "return RecoPhoton_py.at(1)")
                # .Define("RecoPhoton2_py", "return RecoPhoton_py.at(2)")
                # .Define("RecoPhoton0_pz", "return RecoPhoton_pz.at(0)")
                # .Define("RecoPhoton1_pz", "return RecoPhoton_pz.at(1)")
                # .Define("RecoPhoton2_pz", "return RecoPhoton_pz.at(2)")

                # invariant mass of diphoton (photon with indices 1 & 2)
                .Define("Reco_aa_energy", "return (RecoPhoton1_e + RecoPhoton2_e)")
                .Define("Reco_aa_px", "return (RecoPhoton1_px + RecoPhoton2_px)")
                .Define("Reco_aa_py", "return (RecoPhoton1_py + RecoPhoton2_py)")
                .Define("Reco_aa_pz", "return (RecoPhoton1_pz + RecoPhoton2_pz)")
                .Define("Reco_aa_invMass", "if (Reco_aa_energy != -4.0f && Reco_aa_px != -4.0f && Reco_aa_py != -4.0f && Reco_aa_pz != -4.0f) { return sqrt(Reco_aa_energy*Reco_aa_energy - Reco_aa_px*Reco_aa_px - Reco_aa_py*Reco_aa_py - Reco_aa_pz*Reco_aa_pz); } else { return -2.0f; }")
                .Define("Reco_aa_p", "if (Reco_aa_px != -4.0f && Reco_aa_py != -4.0f && Reco_aa_pz != -4.0f) { return sqrt(Reco_aa_px*Reco_aa_px + Reco_aa_py*Reco_aa_py + Reco_aa_pz*Reco_aa_pz); } else { return -2.0f; }")


                .Define("RecoPhoton1_px_if_RecoPhoton2_px_pos", "if (RecoPhoton2_px > 0) {return RecoPhoton1_px;} else {return -50.0f;}")
                .Define("RecoPhoton1_pz_if_RecoPhoton2_pz_pos", "if (RecoPhoton2_pz > 0) {return RecoPhoton1_pz;} else {return -50.0f;}")

                .Define("RecoALPPhotons_delta_R3", "if (n_RecoPhotons == 3) {return RecoPhotons_delta_r.at(2);} else {return (-2.0f); }")

                .Define("RecoMuon_e",      "ReconstructedParticle::get_e(RecoMuons)")
                .Define("RecoMuon_p",      "ReconstructedParticle::get_p(RecoMuons)")
                .Define("RecoMuon_pt",      "ReconstructedParticle::get_pt(RecoMuons)")
                .Define("RecoMuon_px",      "ReconstructedParticle::get_px(RecoMuons)")
                .Define("RecoMuon_py",      "ReconstructedParticle::get_py(RecoMuons)")
                .Define("RecoMuon_pz",      "ReconstructedParticle::get_pz(RecoMuons)")
                .Define("RecoMuon_eta",     "ReconstructedParticle::get_eta(RecoMuons)") #pseudorapidity eta
                .Define("RecoMuon_theta",   "ReconstructedParticle::get_theta(RecoMuons)")
                .Define("RecoMuon_phi",     "ReconstructedParticle::get_phi(RecoMuons)") #polar angle in the transverse plane phi
                .Define("RecoMuon_charge",  "ReconstructedParticle::get_charge(RecoMuons)")

                #EVENTWIDE VARIABLES: Access quantities that exist only once per event, such as the missing energy (despite the name, the MissingET collection contains the total missing energy)
                # .Define("RecoMissingEnergy_e", "ReconstructedParticle::get_e(MissingET)")
                # .Define("RecoMissingEnergy_p", "ReconstructedParticle::get_p(MissingET)")
                # .Define("RecoMissingEnergy_pt", "ReconstructedParticle::get_pt(MissingET)")
                # .Define("RecoMissingEnergy_px", "ReconstructedParticle::get_px(MissingET)")
                # .Define("RecoMissingEnergy_py", "ReconstructedParticle::get_py(MissingET)")
                # .Define("RecoMissingEnergy_pz", "ReconstructedParticle::get_pz(MissingET)")
                # .Define("RecoMissingEnergy_eta", "ReconstructedParticle::get_eta(MissingET)")
                # .Define("RecoMissingEnergy_theta", "ReconstructedParticle::get_theta(MissingET)")
                # .Define("RecoMissingEnergy_phi", "ReconstructedParticle::get_phi(MissingET)")

                # .Define("CalorimeterHitsTime", "CalorimeterHits.time")


 ######## OBJECT SELECTION: FSGenPhotons and RecoPhotons with object selection of eta < 2.5 ########
                .Define("FSGenPhoton_obj_sel", "MCParticle::sel_pt(0.0)(FSGenPhoton)") #select only fs gen photons with a pt > 0 GeV
                .Define("FSGenPhoton_obj_sel_eta", "MCParticle::sel_eta(2.5)(FSGenPhoton_obj_sel)") #select only photons with eta<2.5

                .Define("RecoPhotons_obj_sel", "ReconstructedParticle::sel_pt(0.0)(RecoPhotons)") #select only reco photons with a pt > 0 GeV
                .Define("RecoPhotons_obj_sel_eta", "ReconstructedParticle::sel_eta(2.5)(RecoPhotons_obj_sel)") #select only photons with eta<2.5

         #GEN LEVEL
                .Define("FSGenPhoton_eta_obj_sel_eta",     "MCParticle::get_eta(FSGenPhoton_obj_sel_eta)") #pseudorapidity eta
                .Define("FSGenPhoton_theta_obj_sel_eta",   "MCParticle::get_theta(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton_phi_obj_sel_eta",     "MCParticle::get_phi(FSGenPhoton_obj_sel_eta)") #polar angle in the transverse plane phi
                .Define("FSGenPhotons_delta_eta_obj_sel_eta", "MCParticle::get_delta_eta(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhotons_delta_phi_obj_sel_eta", "MCParticle::get_delta_phi(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhotons_delta_r_obj_sel_eta",   "MCParticle::get_delta_r(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhotons_min_delta_r_obj_sel_eta", "MCParticle::get_min_delta_r(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton_pt_obj_sel_eta",      "MCParticle::get_pt(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton_e_obj_sel_eta",      "MCParticle::get_e(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton_p_obj_sel_eta",      "MCParticle::get_p(FSGenPhoton_obj_sel_eta)")
                .Define("n_FSGenPhoton_obj_sel_eta",  "MCParticle::get_n(FSGenPhoton_obj_sel_eta)") #count how many photons are in the event in total

                .Define("FSGenPhoton_pz_obj_sel_eta",      "MCParticle::get_pz(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton_py_obj_sel_eta",      "MCParticle::get_py(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton_px_obj_sel_eta",      "MCParticle::get_px(FSGenPhoton_obj_sel_eta)")
                .Define("FSGenPhoton0_e_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 1) {return FSGenPhoton_e_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_e_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 2) {return FSGenPhoton_e_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_e_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 3) {return FSGenPhoton_e_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_p_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 1) {return FSGenPhoton_p_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_p_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 2) {return FSGenPhoton_p_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_p_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 3) {return FSGenPhoton_p_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_pt_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 1) {return FSGenPhoton_pt_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_pt_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 2) {return FSGenPhoton_pt_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_pt_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 3) {return FSGenPhoton_pt_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_pz_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 1) {return FSGenPhoton_pz_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_pz_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 2) {return FSGenPhoton_pz_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_pz_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 3) {return FSGenPhoton_pz_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_py_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 1) {return FSGenPhoton_py_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_py_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 2) {return FSGenPhoton_py_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_py_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 3) {return FSGenPhoton_py_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("FSGenPhoton0_px_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 1) {return FSGenPhoton_px_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("FSGenPhoton1_px_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 2) {return FSGenPhoton_px_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("FSGenPhoton2_px_obj_sel_eta", "if (n_FSGenPhoton_obj_sel_eta >= 3) {return FSGenPhoton_px_obj_sel_eta.at(2);} else {return (-2.0f); }")

                # invariant mass of photons
                .Define("FSGen_aa_energy_obj_sel_eta", "return (FSGenPhoton1_e_obj_sel_eta + FSGenPhoton2_e_obj_sel_eta)")
                .Define("FSGen_aa_px_obj_sel_eta", "return (FSGenPhoton1_px_obj_sel_eta + FSGenPhoton2_px_obj_sel_eta)")
                .Define("FSGen_aa_py_obj_sel_eta", "return (FSGenPhoton1_py_obj_sel_eta + FSGenPhoton2_py_obj_sel_eta)")
                .Define("FSGen_aa_pz_obj_sel_eta", "return (FSGenPhoton1_pz_obj_sel_eta + FSGenPhoton2_pz_obj_sel_eta)")
                .Define("FSGen_aa_invMass_obj_sel_eta", "if (FSGen_aa_energy_obj_sel_eta != -4.0f && FSGen_aa_px_obj_sel_eta != -4.0f && FSGen_aa_py_obj_sel_eta != -4.0f && FSGen_aa_pz_obj_sel_eta != -4.0f) { return sqrt(FSGen_aa_energy_obj_sel_eta*FSGen_aa_energy_obj_sel_eta - FSGen_aa_px_obj_sel_eta*FSGen_aa_px_obj_sel_eta - FSGen_aa_py_obj_sel_eta*FSGen_aa_py_obj_sel_eta - FSGen_aa_pz_obj_sel_eta*FSGen_aa_pz_obj_sel_eta); } else { return -2.0f; }") #invariant mass of the two photons
                .Define("FSGen_aa_p_obj_sel_eta", "if (FSGen_aa_px_obj_sel_eta != -4.0f && FSGen_aa_py_obj_sel_eta != -4.0f && FSGen_aa_pz_obj_sel_eta != -4.0f) { return sqrt(FSGen_aa_px_obj_sel_eta*FSGen_aa_px_obj_sel_eta + FSGen_aa_py_obj_sel_eta*FSGen_aa_py_obj_sel_eta + FSGen_aa_pz_obj_sel_eta*FSGen_aa_pz_obj_sel_eta); } else { return -2.0f; }")



         #RECO LEVEL
                .Define("RecoPhoton_eta_obj_sel_eta",     "ReconstructedParticle::get_eta(RecoPhotons_obj_sel_eta)") #pseudorapidity eta
                .Define("RecoPhoton_theta_obj_sel_eta",   "ReconstructedParticle::get_theta(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton_phi_obj_sel_eta",     "ReconstructedParticle::get_phi(RecoPhotons_obj_sel_eta)") #polar angle in the transverse plane phi
                .Define("RecoPhotons_delta_eta_obj_sel_eta", "ReconstructedParticle::get_delta_eta(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhotons_delta_phi_obj_sel_eta", "ReconstructedParticle::get_delta_phi(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhotons_delta_r_obj_sel_eta",   "ReconstructedParticle::get_delta_r(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhotons_min_delta_r_obj_sel_eta", "ReconstructedParticle::get_min_delta_r(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton_pt_obj_sel_eta",      "ReconstructedParticle::get_pt(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton_e_obj_sel_eta",      "ReconstructedParticle::get_e(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton_p_obj_sel_eta",      "ReconstructedParticle::get_p(RecoPhotons_obj_sel_eta)")\
                .Define("n_RecoPhotons_obj_sel_eta",  "ReconstructedParticle::get_n(RecoPhotons_obj_sel_eta)") #count how many photons are in the event in total
                .Define("RecoPhoton_charge_obj_sel_eta",  "ReconstructedParticle::get_charge(RecoPhotons_obj_sel_eta)")

                .Define("RecoPhoton_diphoton_delta_r_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) { return ReconstructedParticle::get_diphoton_deltaR(RecoPhotons_obj_sel_eta.at(0), RecoPhotons_obj_sel_eta.at(1), RecoPhotons_obj_sel_eta.at(2)); } else { return (-2.0f); }")

                .Define("RecoPhoton_pz_obj_sel_eta",      "ReconstructedParticle::get_pz(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton_py_obj_sel_eta",      "ReconstructedParticle::get_py(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton_px_obj_sel_eta",      "ReconstructedParticle::get_px(RecoPhotons_obj_sel_eta)")
                .Define("RecoPhoton0_e_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_e_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_e_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return RecoPhoton_e_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_e_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_e_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_p_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_p_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_p_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return RecoPhoton_p_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_p_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_p_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_pt_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_pt_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_pt_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return RecoPhoton_pt_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_pt_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_pt_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_pz_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_pz_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_pz_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return RecoPhoton_pz_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_pz_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_pz_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_py_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_py_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_py_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return RecoPhoton_py_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_py_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_py_obj_sel_eta.at(2);} else {return (-2.0f); }")
                .Define("RecoPhoton0_px_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_px_obj_sel_eta.at(0);} else {return (-2.0f); }")
                .Define("RecoPhoton1_px_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return RecoPhoton_px_obj_sel_eta.at(1);} else {return (-2.0f); }")
                .Define("RecoPhoton2_px_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_px_obj_sel_eta.at(2);} else {return (-2.0f); }")


        # invariant mass of photons calculated with indices photon1&photon2
                .Define("Reco_aa_energy_obj_sel_eta", "return (RecoPhoton1_e_obj_sel_eta + RecoPhoton2_e_obj_sel_eta)")
                .Define("Reco_aa_px_obj_sel_eta", "return (RecoPhoton1_px_obj_sel_eta + RecoPhoton2_px_obj_sel_eta)")
                .Define("Reco_aa_py_obj_sel_eta", "return (RecoPhoton1_py_obj_sel_eta + RecoPhoton2_py_obj_sel_eta)")
                .Define("Reco_aa_pz_obj_sel_eta", "return (RecoPhoton1_pz_obj_sel_eta + RecoPhoton2_pz_obj_sel_eta)")
                .Define("Reco_aa_invMass_obj_sel_eta", "if (Reco_aa_energy_obj_sel_eta != -4.0f && Reco_aa_px_obj_sel_eta != -4.0f && Reco_aa_py_obj_sel_eta != -4.0f && Reco_aa_pz_obj_sel_eta != -4.0f) { return sqrt(Reco_aa_energy_obj_sel_eta*Reco_aa_energy_obj_sel_eta - Reco_aa_px_obj_sel_eta*Reco_aa_px_obj_sel_eta - Reco_aa_py_obj_sel_eta*Reco_aa_py_obj_sel_eta - Reco_aa_pz_obj_sel_eta*Reco_aa_pz_obj_sel_eta); } else { return -2.0f; }")                
                .Define("Reco_aa_p_obj_sel_eta", "if (Reco_aa_px_obj_sel_eta != -4.0f && Reco_aa_py_obj_sel_eta != -4.0f && Reco_aa_pz_obj_sel_eta != -4.0f) { return sqrt(Reco_aa_px_obj_sel_eta*Reco_aa_px_obj_sel_eta + Reco_aa_py_obj_sel_eta*Reco_aa_py_obj_sel_eta + Reco_aa_pz_obj_sel_eta*Reco_aa_pz_obj_sel_eta); } else { return -2.0f; }")

                .Define("Reco_beta_ALP_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) { return Reco_aa_p_obj_sel_eta/Reco_aa_energy_obj_sel_eta; } else { return -2.0f; }")


        # test the new fucntion that picks the photons with mindeltaR
                .Define("RecoPhoton_pidx_min_delta_r_obj_sel_eta",     "ReconstructedParticle::get_pidx_min_delta_r(RecoPhotons_obj_sel_eta)") #photon index of mindeltaR

                # .Define("verify_deltaR", 
                #         "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[0] != -1) { "
                #         "return ReconstructedParticle::get_delta_r(RecoPhotons_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[0]), RecoPhotons_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[1]));"    
                #         "} else { return -2.0f; }")

                .Define("RecoPhoton1_pz_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[0] != -1) { "
                        "return RecoPhoton_pz_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[0]); "
                        "} else { return -2.0f; }")
                .Define("RecoPhoton2_pz_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[1] != -1) { "
                        "return RecoPhoton_pz_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[1]); "
                        "} else { return -2.0f; }")            
                .Define("RecoPhoton1_py_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[0] != -1) { "
                        "return RecoPhoton_py_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[0]); "
                        "} else { return -2.0f; }")
                .Define("RecoPhoton2_py_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[1] != -1) { "
                        "return RecoPhoton_py_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[1]); "
                        "} else { return -2.0f; }")   
                .Define("RecoPhoton1_px_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[0] != -1) { "
                        "return RecoPhoton_px_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[0]); "
                        "} else { return -2.0f; }")
                .Define("RecoPhoton2_px_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[1] != -1) { "
                        "return RecoPhoton_px_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[1]); "
                        "} else { return -2.0f; }")   
                .Define("RecoPhoton1_e_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[0] != -1) { "
                        "return RecoPhoton_e_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[0]); "
                        "} else { return -2.0f; }")
                .Define("RecoPhoton2_e_obj_sel_eta_v2", 
                        "if (RecoPhoton_pidx_min_delta_r_obj_sel_eta.size() > 1 && RecoPhoton_pidx_min_delta_r_obj_sel_eta[1] != -1) { "
                        "return RecoPhoton_e_obj_sel_eta.at(RecoPhoton_pidx_min_delta_r_obj_sel_eta[1]); "
                        "} else { return -2.0f; }")   


                # invariant mass of photons calculated with photons that have the smallest angular separation (mindeltaR)  v2 
                .Define("Reco_aa_energy_obj_sel_eta_v2", "return (RecoPhoton1_e_obj_sel_eta_v2 + RecoPhoton2_e_obj_sel_eta_v2)")
                .Define("Reco_aa_px_obj_sel_eta_v2", "return (RecoPhoton1_px_obj_sel_eta_v2 + RecoPhoton2_px_obj_sel_eta_v2)")
                .Define("Reco_aa_py_obj_sel_eta_v2", "return (RecoPhoton1_py_obj_sel_eta_v2 + RecoPhoton2_py_obj_sel_eta_v2)")
                .Define("Reco_aa_pz_obj_sel_eta_v2", "return (RecoPhoton1_pz_obj_sel_eta_v2 + RecoPhoton2_pz_obj_sel_eta_v2)")
                .Define("Reco_aa_invMass_obj_sel_eta_v2", "if (Reco_aa_energy_obj_sel_eta_v2 != -4.0f && Reco_aa_px_obj_sel_eta_v2 != -4.0f && Reco_aa_py_obj_sel_eta_v2 != -4.0f && Reco_aa_pz_obj_sel_eta_v2 != -4.0f) { return sqrt(Reco_aa_energy_obj_sel_eta_v2*Reco_aa_energy_obj_sel_eta_v2 - Reco_aa_px_obj_sel_eta_v2*Reco_aa_px_obj_sel_eta_v2 - Reco_aa_py_obj_sel_eta_v2*Reco_aa_py_obj_sel_eta_v2 - Reco_aa_pz_obj_sel_eta_v2*Reco_aa_pz_obj_sel_eta_v2); } else { return -2.0f; }")                
                .Define("Reco_aa_p_obj_sel_eta_v2", "if (Reco_aa_px_obj_sel_eta_v2 != -4.0f && Reco_aa_py_obj_sel_eta_v2 != -4.0f && Reco_aa_pz_obj_sel_eta_v2 != -4.0f) { return sqrt(Reco_aa_px_obj_sel_eta_v2*Reco_aa_px_obj_sel_eta_v2 + Reco_aa_py_obj_sel_eta_v2*Reco_aa_py_obj_sel_eta_v2 + Reco_aa_pz_obj_sel_eta_v2*Reco_aa_pz_obj_sel_eta_v2); } else { return -2.0f; }")


        #RECO ALP (MATCHED TO GEN)  with object selection eta ----
                .Define("RecoALPPhoton1_obj_sel", "ReconstructedParticle::sel_pt(0.0)(RecoALPPhoton1)") #select only reco photons with a pt > 0 GeV
                .Define("RecoALPPhoton1_obj_sel_eta", "ReconstructedParticle::sel_eta(2.5)(RecoALPPhoton1_obj_sel)") #select only photons with eta<2.5
                .Define("RecoALPPhoton2_obj_sel", "ReconstructedParticle::sel_pt(0.0)(RecoALPPhoton2)") #select only reco photons with a pt > 0 GeV
                .Define("RecoALPPhoton2_obj_sel_eta", "ReconstructedParticle::sel_eta(2.5)(RecoALPPhoton2_obj_sel)") #select only photons with eta<2.5

                .Define("RecoALPPhoton1_e_obj_sel_eta",  "ReconstructedParticle::get_e( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_e_obj_sel_eta",  "ReconstructedParticle::get_e( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_p_obj_sel_eta",  "ReconstructedParticle::get_p( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_p_obj_sel_eta",  "ReconstructedParticle::get_p( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_pt_obj_sel_eta",  "ReconstructedParticle::get_pt( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_pt_obj_sel_eta",  "ReconstructedParticle::get_pt( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_px_obj_sel_eta",  "ReconstructedParticle::get_px( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_px_obj_sel_eta",  "ReconstructedParticle::get_px( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_py_obj_sel_eta",  "ReconstructedParticle::get_py( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_py_obj_sel_eta",  "ReconstructedParticle::get_py( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_pz_obj_sel_eta",  "ReconstructedParticle::get_pz( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_pz_obj_sel_eta",  "ReconstructedParticle::get_pz( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_eta_obj_sel_eta",  "ReconstructedParticle::get_eta( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_eta_obj_sel_eta",  "ReconstructedParticle::get_eta( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhoton1_phi_obj_sel_eta",  "ReconstructedParticle::get_phi( RecoALPPhoton1_obj_sel_eta )")
                .Define("RecoALPPhoton2_phi_obj_sel_eta",  "ReconstructedParticle::get_phi( RecoALPPhoton2_obj_sel_eta)")
                .Define("RecoALPPhotons_deltaEta_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return abs(RecoALPPhoton1_eta_obj_sel_eta.at(0) - RecoALPPhoton2_eta_obj_sel_eta.at(0)); "
                        "} else { return -2.0f; }")
                .Define("RecoALPPhotons_deltaPhi_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return abs(RecoALPPhoton1_phi_obj_sel_eta.at(0) - RecoALPPhoton2_phi_obj_sel_eta.at(0)); "
                        "} else { return -2.0f; }")
                # .Define("RecoALPPhotons_deltaR_obj_sel_eta",
                #         "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                #         "return sqrt(RecoALPPhotons_deltaEta_obj_sel_eta*RecoALPPhotons_deltaEta_obj_sel_eta  + RecoALPPhotons_deltaPhi_obj_sel_eta*RecoALPPhotons_deltaPhi_obj_sel_eta); "
                #         "} else { return -2.0f; }")
                .Define("RecoALPPhotons_deltaR_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return ReconstructedParticle::get_delta_r(RecoALPPhoton1_obj_sel_eta.at(0), RecoALPPhoton2_obj_sel_eta.at(0)); "
                        "} else { return -2.0f; }") 
                .Define("n_RecoALPPhoton1_obj_sel_eta", "ReconstructedParticle::get_n( RecoALPPhoton1_obj_sel_eta )")
                .Define("n_RecoALPPhoton2_obj_sel_eta", "ReconstructedParticle::get_n( RecoALPPhoton2_obj_sel_eta)")

                # # # aa invariant mass
                .Define("RecoALP_aa_energy_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return (RecoALPPhoton1_e_obj_sel_eta[0] + RecoALPPhoton2_e_obj_sel_eta[0]); "
                        "} else { return -2.0f; }") 
                .Define("RecoALP_aa_px_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return (RecoALPPhoton1_px_obj_sel_eta[0] + RecoALPPhoton2_px_obj_sel_eta[0]); "
                        "} else { return -2.0f; }") 
                .Define("RecoALP_aa_py_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return (RecoALPPhoton1_py_obj_sel_eta[0] + RecoALPPhoton2_py_obj_sel_eta[0]); "
                        "} else { return -2.0f; }") 
                .Define("RecoALP_aa_pz_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0) { "
                        "return (RecoALPPhoton1_pz_obj_sel_eta[0] + RecoALPPhoton2_pz_obj_sel_eta[0]); "
                        "} else { return -2.0f; }") 
                .Define("RecoALP_aa_invMass_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0 && RecoALP_aa_energy_obj_sel_eta != -2.0f && RecoALP_aa_px_obj_sel_eta != -2.0f && RecoALP_aa_py_obj_sel_eta != -2.0f && RecoALP_aa_pz_obj_sel_eta != -2.0f) { "
                        "return sqrt(RecoALP_aa_energy_obj_sel_eta*RecoALP_aa_energy_obj_sel_eta - RecoALP_aa_px_obj_sel_eta*RecoALP_aa_px_obj_sel_eta - RecoALP_aa_py_obj_sel_eta*RecoALP_aa_py_obj_sel_eta - RecoALP_aa_pz_obj_sel_eta*RecoALP_aa_pz_obj_sel_eta ); "
                        "} else { return -2.0f; }") 
                .Define("RecoALP_aa_p_obj_sel_eta",
                        "if (RecoALPPhoton1_obj_sel_eta.size() > 0 && RecoALPPhoton2_obj_sel_eta.size() > 0 && RecoALP_aa_energy_obj_sel_eta != -2.0f && RecoALP_aa_px_obj_sel_eta!= -2.0f && RecoALP_aa_py_obj_sel_eta != -2.0f && RecoALP_aa_pz_obj_sel_eta != -2.0f) { "
                        "return sqrt(RecoALP_aa_px_obj_sel_eta*RecoALP_aa_px_obj_sel_eta + RecoALP_aa_py_obj_sel_eta*RecoALP_aa_py_obj_sel_eta + RecoALP_aa_pz_obj_sel_eta*RecoALP_aa_pz_obj_sel_eta); "
                        "} else { return -2.0f; }") 


##### Calorimeter timing variable attempt - self constructed
                .Define("RecoPhoton_prompt_calorimeter_hit_obj_sel_eta",      "ReconstructedParticle::get_prompt_photon_calorimeter_hits(RecoPhotons_obj_sel_eta)")  #for prompt photon coming from interaction point
                .Define("RecoPhoton0_prompt_calorimeter_hit_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton_prompt_calorimeter_hit_obj_sel_eta.at(0);} else {return std::vector<float>{-2.,0.0,0.0}; }")

                .Define("RecoPhoton0_prompt_calorimeter_hit_x_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton0_prompt_calorimeter_hit_obj_sel_eta[0];} else {return (-9000.0f); }")
                .Define("RecoPhoton0_prompt_calorimeter_hit_y_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton0_prompt_calorimeter_hit_obj_sel_eta[1];} else {return (-9000.0f); }")
                .Define("RecoPhoton0_prompt_calorimeter_hit_z_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return RecoPhoton0_prompt_calorimeter_hit_obj_sel_eta[2];} else {return (-9000.0f); }")

                .Define("RecoPhoton0_prompt_dist_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 1) {return sqrt(RecoPhoton0_prompt_calorimeter_hit_x_obj_sel_eta*RecoPhoton0_prompt_calorimeter_hit_x_obj_sel_eta + RecoPhoton0_prompt_calorimeter_hit_y_obj_sel_eta*RecoPhoton0_prompt_calorimeter_hit_y_obj_sel_eta + RecoPhoton0_prompt_calorimeter_hit_z_obj_sel_eta*RecoPhoton0_prompt_calorimeter_hit_z_obj_sel_eta);} else {return (-9000.0f); }")


        #calculatingn the time of flight for prompt photon
                .Define("RecoPhoton0_time2calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 2) {return static_cast<float>(RecoPhoton0_prompt_dist_calorimeter_obj_sel_eta/(2.997*10e11)); } else {return (-2.0f); }")


        # displaced photon coordinates of hit point
                .Define("RecoPhoton_displaced_calorimeter_hit_obj_sel_eta",      "ReconstructedParticle::get_displaced_photon_calorimeter_hits(RecoPhotons_obj_sel_eta, GenALPPhoton1_vertex_x[0], GenALPPhoton1_vertex_y[0], GenALPPhoton1_vertex_z[0])")
                .Define("RecoPhoton1_displaced_calorimeter_hit_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_displaced_calorimeter_hit_obj_sel_eta.at(1);} else {return std::vector<float>{-2.,0.0,0.0}; }")
                .Define("RecoPhoton2_displaced_calorimeter_hit_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton_displaced_calorimeter_hit_obj_sel_eta.at(2);} else {return std::vector<float>{-2.,0.0,0.0}; }")
#       #coordinates of calormiter hit point 
                .Define("RecoPhoton1_displaced_calorimeter_hit_x_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_displaced_calorimeter_hit_obj_sel_eta[0];} else {return (-9000.0f); }")
                .Define("RecoPhoton1_displaced_calorimeter_hit_y_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_displaced_calorimeter_hit_obj_sel_eta[1];} else {return (-9000.0f); }")
                .Define("RecoPhoton1_displaced_calorimeter_hit_z_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_displaced_calorimeter_hit_obj_sel_eta[2];} else {return (-9000.0f); }")
                .Define("RecoPhoton2_displaced_calorimeter_hit_x_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton2_displaced_calorimeter_hit_obj_sel_eta[0];} else {return (-9000.0f); }")
                .Define("RecoPhoton2_displaced_calorimeter_hit_y_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton2_displaced_calorimeter_hit_obj_sel_eta[1];} else {return (-9000.0f); }")
                .Define("RecoPhoton2_displaced_calorimeter_hit_z_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton2_displaced_calorimeter_hit_obj_sel_eta[2];} else {return (-9000.0f); }")

        #vector between calorihit and alp decay vertex
                .Define("RecoPhoton1_dist_x_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_displaced_calorimeter_hit_x_obj_sel_eta-GenALPPhoton1_vertex_x[0];} else {return (-2.0f); }")
                .Define("RecoPhoton1_dist_y_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_displaced_calorimeter_hit_y_obj_sel_eta-GenALPPhoton1_vertex_y[0];} else {return (-2.0f); }")
                .Define("RecoPhoton1_dist_z_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_displaced_calorimeter_hit_z_obj_sel_eta-GenALPPhoton1_vertex_z[0];} else {return (-2.0f); }")
                .Define("RecoPhoton2_dist_x_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton2_displaced_calorimeter_hit_x_obj_sel_eta-GenALPPhoton1_vertex_x[0];} else {return (-2.0f); }")
                .Define("RecoPhoton2_dist_y_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton2_displaced_calorimeter_hit_y_obj_sel_eta-GenALPPhoton1_vertex_y[0];} else {return (-2.0f); }")
                .Define("RecoPhoton2_dist_z_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton2_displaced_calorimeter_hit_z_obj_sel_eta-GenALPPhoton1_vertex_z[0];} else {return (-2.0f); }")

        #distance between calorihit and alp decay vertex
                .Define("RecoPhoton1_dist_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return sqrt( RecoPhoton1_dist_x_ALP_to_calorimeter_obj_sel_eta*RecoPhoton1_dist_x_ALP_to_calorimeter_obj_sel_eta+ RecoPhoton1_dist_y_ALP_to_calorimeter_obj_sel_eta*RecoPhoton1_dist_y_ALP_to_calorimeter_obj_sel_eta + RecoPhoton1_dist_z_ALP_to_calorimeter_obj_sel_eta*RecoPhoton1_dist_z_ALP_to_calorimeter_obj_sel_eta);} else {return (-2.0f); }")
                .Define("RecoPhoton2_dist_ALP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return sqrt( RecoPhoton2_dist_x_ALP_to_calorimeter_obj_sel_eta*RecoPhoton2_dist_x_ALP_to_calorimeter_obj_sel_eta+ RecoPhoton2_dist_y_ALP_to_calorimeter_obj_sel_eta*RecoPhoton2_dist_y_ALP_to_calorimeter_obj_sel_eta + RecoPhoton2_dist_z_ALP_to_calorimeter_obj_sel_eta*RecoPhoton2_dist_z_ALP_to_calorimeter_obj_sel_eta);} else {return (-2.0f); }")
                #taking the photon from the ALP with the maximum distance to the calorimeter
                .Define("max_dist_ALP_to_calorimeter_obj_sel_eta", "max(RecoPhoton1_dist_ALP_to_calorimeter_obj_sel_eta, RecoPhoton2_dist_ALP_to_calorimeter_obj_sel_eta)" )

        # total path length from interaction point to calorimeter
                .Define("RecoPhoton1_total_dist_IP_to_calorimeter_obj_sel_eta", "if (n_RecoPhotons_obj_sel_eta >= 3) {return max_dist_ALP_to_calorimeter_obj_sel_eta + GenALP_Lxyz[0];} else {return (-2.0f); }")
        
        #  calculatingn the time of flight (assumig speed of light for ALP)
                .Define("RecoPhoton1_time2calorimeter_obj_sel_eta_new", "if (n_RecoPhotons_obj_sel_eta >= 3) {return static_cast<float>(RecoPhoton1_total_dist_IP_to_calorimeter_obj_sel_eta/(2.997*10e11)); } else {return (-2.0f); }")
                .Define("Reco_deltaT_CaloriHit_obj_sel_eta_new", "if (n_RecoPhotons_obj_sel_eta >= 3) {return RecoPhoton1_time2calorimeter_obj_sel_eta_new - RecoPhoton0_time2calorimeter_obj_sel_eta; } else {return (-2.0f); }")

####end of calorimeter timing variable



               )
                return df2

        def output():
                branchList = [
                        # "CalorimeterHitsTime",
                        ######## Monte-Carlo particles #######
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
                        # "FSGenElectron_px",
                        # "FSGenElectron_py",
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
                        # # "n_FSGenElectron_forFS2GenPhotons",
                        # # "n_FSGenPositron_forFS2GenPhotons",
                        "FSGen_Lxy",
                        "FSGen_Lxyz",
                        # "FSGen_lifetime_xy",
                        # "FSGen_lifetime_xyz",
                        # "n_FSGenPositron",
                        # "FSGenPositron_e",
                        # "FSGenPositron_p",
                        # "FSGenPositron_pt",
                        # "FSGenPositron_px",
                        # "FSGenPositron_py",
                        # "FSGenPositron_pz",
                        # "FSGenPositron_eta",
                        # "FSGenPositron_theta",
                        # "FSGenPositron_phi",
                        # "n_FSGenNeutrino",
                        # "FSGenNeutrino_e",
                        # "FSGenNeutrino_p",
                        # "FSGenNeutrino_pt",
                        # "FSGenNeutrino_px",
                        # "FSGenNeutrino_py",
                        # "FSGenNeutrino_pz",
                        # "FSGenNeutrino_eta",
                        # "FSGenNeutrino_theta",
                        # "FSGenNeutrino_phi",
                        # "n_FSGenAntiNeutrino",
                        # "FSGenAntiNeutrino_e",
                        # "FSGenAntiNeutrino_p",
                        # "FSGenAntiNeutrino_pt",
                        # "FSGenAntiNeutrino_px",
                        # "FSGenAntiNeutrino_py",
                        # "FSGenAntiNeutrino_pz",
                        # "FSGenAntiNeutrino_eta",
                        # "FSGenAntiNeutrino_theta",
                        # "FSGenAntiNeutrino_phi",
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

                        # "FSGen_a0a1_invMass",
                        # "FSGen_a0a2_invMass",
                        # "FSGen_a1a2_invMass",
                        # "FSGen_aaa_invMass",
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

                        # "GenALP_deltaR",
                        "GenALPPhotons_deltaEta",
                        "GenALPPhotons_deltaPhi",
                        "GenALPPhotons_deltaR",

                        # "GenALPPhotons_deltaR_2",
                        "FSGenPhotons_delta_r",
                        "FSGenPhotons_min_delta_r",

                        "GenALPPhoton1_time",
                        "GenALPPhoton2_time",

                        "GenALP_observed_lifetime_xyz",

                        "GenALPPhoton1_time_minus_GenALP_time",

                        "n_GenALP",
                        "GenALP_time",
                        "GenALP_pdg",
                        # "GenALP_endPoint_x",

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
                        # "GenALPPhoton1_deltaR",
                        # "GenALPPhoton2_deltaR",

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
                        #"GenALP_decay",
                        "GenALPPhoton1_vertex_x",
                        "GenALPPhoton1_vertex_y",
                        "GenALPPhoton1_vertex_z",
                        "GenALP_Lxy",
                        "GenALP_Lxyz",
                        "GenALP_lifetime_xy",
                        "GenALP_lifetime_xyz",
                        #"GenALPMCDecayVertex",
                        "MC_PrimaryVertex",
                        "n_RecoTracks",
                        ######## Reconstructed particles #######
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
                        # "RecoALPPhoton1_time",
                        # "RecoALPPhoton2_time",
                        "RecoALPPhotons_deltaEta",
                        "RecoALPPhotons_deltaPhi",
                        "RecoALPPhotons_deltaR",
                        # "RecoALPPhotons_deltaR2",

                        "RecoALP_aa_invMass",
                        "RecoALP_aa_p",
                        "RecoALP_aa_energy",
                        "Reco_aa_invMass",
                        "Reco_aa_p",

                        "GenMinusRecoALPPhoton1_e",
                        "GenMinusRecoALPPhoton2_e",
                        # "GenMinusRecoALPPhoton1_p",
                        # "GenMinusRecoALPPhoton2_p",
                        # "GenMinusRecoALPPhoton1_pt",
                        # "GenMinusRecoALPPhoton2_pt",
                        # "GenMinusRecoALPPhoton1_px",
                        # "GenMinusRecoALPPhoton2_px",
                        # "GenMinusRecoALPPhoton1_py",
                        # "GenMinusRecoALPPhoton2_py",
                        # "GenMinusRecoALPPhoton1_pz",
                        # "GenMinusRecoALPPhoton2_pz",
                        # "GenMinusRecoALPPhoton1_eta",
                        # "GenMinusRecoALPPhoton2_eta",
                        # "GenMinusRecoALPPhoton1_theta",
                        # "GenMinusRecoALPPhoton2_theta",
                        # "GenMinusRecoALPPhoton1_phi",
                        # "GenMinusRecoALPPhoton2_phi",
                        "GenMinusRecoALP_DecayVertex_x",
                        "GenMinusRecoALP_DecayVertex_y",
                        "GenMinusRecoALP_DecayVertex_z",
                        "n_RecoJets",
                        "n_RecoPhotons",
                        "n_RecoElectrons",
                        "n_RecoMuons",
                        # "RecoJet_e",
                        # "RecoJet_p",
                        # "RecoJet_pt",
                        # "RecoJet_px",
                        # "RecoJet_py",
                        # "RecoJet_pz",
                        # "RecoJet_eta",
                        # "RecoJet_theta",
                        # "RecoJet_phi",
                        # "RecoJet_charge",
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

                        # "RecoPhotons_ALP_delta_r",
                        # "RecoPhotons_ALP_delta_phi",
                        # "RecoPhotons_ALP_delta_eta",

                        # "RecoPhoton_y",
                        # "RecoPhoton_time",

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

                        "RecoElectron_e",
                        "RecoElectron_p",
                        "RecoElectron_pt",
                        # "RecoElectron_px",
                        # "RecoElectron_py",
                        "RecoElectron_pz",
                        "RecoElectron_eta",
                        "RecoElectron_theta",
                        "RecoElectron_phi",
                        # "RecoElectron_charge",
                        # "RecoMuon_e",
                        # "RecoMuon_p",
                        # "RecoMuon_pt",
                        # "RecoMuon_px",
                        # "RecoMuon_py",
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

                #####  OBJECT SELECTION: FSGenPhotons and RecoPhotons with selection: p_t>10 GeV as threshold #### 
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


                        "RecoPhoton_diphoton_delta_r_obj_sel_eta",
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
                        "Reco_beta_ALP_obj_sel_eta",


                        # "RecoPhoton0_prompt_calorimeter_hit_x_obj_sel_eta",
                        # "RecoPhoton0_prompt_calorimeter_hit_y_obj_sel_eta",
                        # "RecoPhoton0_prompt_calorimeter_hit_z_obj_sel_eta",
                        # "RecoPhoton0_prompt_dist_calorimeter_obj_sel_eta",

                        # "RecoPhoton1_displaced_calorimeter_hit_x_obj_sel_eta",	#newversion
                        # "RecoPhoton1_displaced_calorimeter_hit_y_obj_sel_eta",   #newversion
                        # "RecoPhoton1_displaced_calorimeter_hit_z_obj_sel_eta",   #newversion
                        # "max_dist_ALP_to_calorimeter_obj_sel_eta",
                        # "RecoPhoton1_total_dist_IP_to_calorimeter_obj_sel_eta",  #newversion

                        # "RecoPhoton0_time2calorimeter_obj_sel_eta",
                        # "RecoPhoton1_time2calorimeter_obj_sel_eta_new",                     
                        # "Reco_deltaT_CaloriHit_obj_sel_eta_new",



                        "RecoPhoton_pidx_min_delta_r_obj_sel_eta",
                        "RecoPhoton1_pz_obj_sel_eta_v2",
                        "RecoPhoton2_pz_obj_sel_eta_v2",
                        "Reco_aa_invMass_obj_sel_eta_v2",
                        "Reco_aa_p_obj_sel_eta_v2",

                        # "verify_deltaR",


                #         #RECO ALP (MATCHED TO GEN)
                        "RecoALPPhoton1_e_obj_sel_eta",
                        "RecoALPPhoton2_e_obj_sel_eta",
                        "RecoALPPhoton1_p_obj_sel_eta",
                        "RecoALPPhoton2_p_obj_sel_eta",
                        "RecoALPPhoton1_pt_obj_sel_eta",
                        "RecoALPPhoton2_pt_obj_sel_eta",
                        "RecoALPPhoton1_px_obj_sel_eta",
                        "RecoALPPhoton2_px_obj_sel_eta",
                        "RecoALPPhoton1_py_obj_sel_eta",
                        "RecoALPPhoton2_py_obj_sel_eta",
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
                        "RecoALP_aa_energy_obj_sel_eta",
                        "RecoALP_aa_px_obj_sel_eta",
                        "RecoALP_aa_py_obj_sel_eta",
                        "RecoALP_aa_pz_obj_sel_eta",
                        "RecoALP_aa_invMass_obj_sel_eta",
                        "RecoALP_aa_p_obj_sel_eta",
		]

                return branchList
