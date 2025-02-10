#Input directory where the files produced at the stage1 level are
# inputDir = "./output_stage1/"
#inputDir = "/eos/user/j/jalimena/FCCeeLLP/"
#inputDir = "./stage1_output/"
# inputDir = "/eos/user/e/ebakhish/stage1_output/masses_different/"
# inputDir = "/eos/user/e/ebakhish/stage1_output/couplings_different/"
# inputDir = "/eos/user/e/ebakhish/stage1_output/background/background_obj_sel_pt_deltaR/"
# inputDir = "/eos/user/e/ebakhish/stage1_output/final_signals/"
inputDir = "/eos/user/e/ebakhish/stage1_output/background/all_bkg/"




#Output directory where the files produced at the final-selection level are
#outputDir = "./final_output/"
# outputDir = "/eos/user/e/ebakhish/final_output/masses_different/"
# outputDir = "/eos/user/e/ebakhish/final_output/couplings_different/"
# outputDir = "/eos/user/e/ebakhish/final_output/background/obj_sel_p_10GeV_deltaR_0p4/"
outputDir = "/eos/user/e/ebakhish/final_output/background/all_bkg/"
# outputDir = "/eos/user/e/ebakhish/final_output/final_signals/"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
# intLumi = 205e6 #pb^-1
intLumi = 205e6*0.49   #pb^-1   #to take into account that the Z-pole run is actually spread over three center-of-mass energies

#Scale event yields by intLumi and cross section (optional)
doScale = True

#Save event yields in a table (optional)
saveTabular = True

processList = {
    #run over the full statistics from stage1

    #backgrounds
    # 'p8_ee_Zee_ecm91':{},
    # 'wzp6_gaga_ee_60_ecm240':{},
    # 'ee_gaga_1million':{},
    # 'test1':{},
    # 'test2':{},
    # 'test4':{},
    # 'ee_gammagamma':{},
    # 'ee_gaga_test':{},
    # 'ee_aa':{},
    # 'ee_aaa':{},
    # 'ee_aaaa':{},
    # 'background_ee_aa':{},    

    #signals

    # 'ALP_Z_aa_0.01.GeV_cYY_0.00006':{},
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



    ####     using my new pythia samples  -E      ####
    # 'ALP_Z_aa_0p5GeV_cYY1p0':{},
    # 'ALP_Z_aa_0p8GeV_cYY1p0':{},
    # 'ALP_Z_aa_1p0GeV_cYY1p0':{},
    # 'ALP_Z_aa_5p0GeV_cYY1p0':{},
    # 'ALP_Z_aa_8p0GeV_cYY1p0':{},

    # 'ALP_Z_aa_0p001GeV_cYY1p0':{},
    # 'ALP_Z_aa_0p01GeV_cYY1p0':{},
    # 'ALP_Z_aa_0p1GeV_cYY1p0':{},
    # 'ALP_Z_aa_0p5GeV_cYY1p0':{},
    # 'ALP_Z_aa_0p8GeV_cYY1p0':{},
    # 'ALP_Z_aa_1p0GeV_cYY1p0':{},
    # 'ALP_Z_aa_3p0GeV_cYY1p0':{},       
    # 'ALP_Z_aa_5p0GeV_cYY1p0':{},

    # 'ALP_Z_aa_10p0GeV_cYY1p0':{},
    # 'ALP_Z_aa_20p0GeV_cYY1p0':{},
    # 'ALP_Z_aa_30p0GeV_cYY1p0':{},




    # 'ALP_Z_aa_1p0GeV_cYY0p001':{},
    # 'ALP_Z_aa_1p0GeV_cYY0p01':{},
    # 'ALP_Z_aa_1p0GeV_cYY0p1':{},
    # 'ALP_Z_aa_1p0GeV_cYY0p4':{},
    # 'ALP_Z_aa_1p0GeV_cYY0p7':{},
    # 'ALP_Z_aa_1p0GeV_cYY1p3':{},
    # 'ALP_Z_aa_1p0GeV_cYY1p6':{},

    # 'ALP_Z_aa_0p1GeV_cYY1p6':{},

    # 'ALP_Z_aa_1p0GeV_cYY1p0':{},

    # 'ALP_Z_aa_3p0GeV_cYY0p4':{},

    # 'ALP_Z_aa_10p0GeV_cYY0p03':{},

    # 'ALP_Z_aa_30p0GeV_cYY0p002':{},
    # 'ALP_Z_aa_30p0GeV_cYY0p0002':{},

    #####Background######
    'background_ee_aa1':{},
    'background_ee_aaa1':{},
    'background_ee_aaaa1':{},
    'background_ee_ee':{},
    'background_ee_eea1':{},
    'background_ee_eeaa1':{},
    'background_ee_eeaaa1':{},

    
 
}

###Dictionary for prettier names of processes (optional)
processLabels = {
    #backgrounds
    # 'p8_ee_Zee_ecm91':"Z $\rightarrow$ ee",
    # 'wzp6_gaga_ee_60_ecm240':"YY $\rightarrow$ ee",
    # 'ee_gaga_1million':"$\rightarrow$ #gamma#gamma (mine)",
    # 'test1':"$\rightarrow$ YY",
    # 'test2':"$\rightarrow$ Z $\rightarrow$ ee",
    # 'test4':"$\rightarrow$ YYY",
    # 'ee_gammagamma':"$\rightarrow$ #gamma#gamma (spring2021)",
    # 'ee_gaga_test':"$\rightarrow$ YY",
    # 'ee_aa':"$\rightarrow$ #gamma#gamma",
    # 'ee_aaa':"$\rightarrow$ #gamma#gamma#gamma",
    # 'ee_aaaa':"$\rightarrow$ #gamma#gamma#gamma#gamma",


    'background_ee_aa1':"$\rightarrow$ #gamma#gamma",
    'background_ee_aaa1':"$\rightarrow$ #gamma#gamma#gamma",
    'background_ee_aaaa1':"$\rightarrow$ #gamma#gamma#gamma#gamma",
    'background_ee_ee':"$\rightarrow$ ee",
    'background_ee_eea1':"$\rightarrow$ ee#gamma",
    'background_ee_eeaa1':"$\rightarrow$ ee#gamma#gamma",
    'background_ee_eeaaa1':"$\rightarrow$ ee#gamma#gamma#gamma",

    #signals


    'ALP_Z_aa_0p1GeV_cYY1p6':"$m_ALP =$ 0.1 GeV, $c_{YY} = 1.6$",

    'ALP_Z_aa_1p0GeV_cYY1p0':"$m_ALP =$ 1.0 GeV, $c_{YY} = 1.0$",

    'ALP_Z_aa_3p0GeV_cYY0p4':"$m_ALP =$ 3.0 GeV, $c_{YY} = 0.4$",

    'ALP_Z_aa_10p0GeV_cYY0p03':"$m_ALP =$ 10.0 GeV, $c_{YY} = 0.03$",

    'ALP_Z_aa_30p0GeV_cYY0p002':"$m_ALP =$ 30.0 GeV, $c_{YY} = 0.002$",

    'ALP_Z_aa_30p0GeV_cYY0p0002':"$m_ALP =$ 30.0 GeV, $c_{YY} = 0.0002$",



    # 'ALP_Z_aa_0.01.GeV_cYY_0.00006':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.0006':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.0019':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.006':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.019':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.06':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.19':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_0.01.GeV_cYY_0.6':"$m_ALP =$ 0.01 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.000019':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.00006':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.00019':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.0006':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.0019':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.006':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.019':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.06':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.19':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_0.0316.GeV_cYY_0.6':"$m_ALP =$ 0.0316 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.000019':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.00006':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.00019':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.0006':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.0019':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.006':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.019':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.06':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.19':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_0.1.GeV_cYY_0.6':"$m_ALP =$ 0.1 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.000019':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.00006':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.00019':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.0006':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.0019':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.006':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.019':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.06':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.19':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_0.316.GeV_cYY_0.6':"$m_ALP =$ 0.316 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.000019':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.00006':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.00019':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.0006':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.0019':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.006':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.019':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.06':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.19':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_1.0.GeV_cYY_0.6':"$m_ALP =$ 1.0 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.0000019':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.0000019$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.000006':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.000006$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.000019':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.00006':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.00019':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.0006':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.0019':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.006':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.019':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.06':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.19':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_3.16.GeV_cYY_0.6':"$m_ALP =$ 3.16 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_10.GeV_cYY_0.0000006':"$m_ALP =$ 10 GeV, $c_{YY} = 0.0000006$",
    # 'ALP_Z_aa_10.GeV_cYY_0.0000019':"$m_ALP =$ 10 GeV, $c_{YY} = 0.0000019$",
    # 'ALP_Z_aa_10.GeV_cYY_0.000006':"$m_ALP =$ 10 GeV, $c_{YY} = 0.000006$",
    # 'ALP_Z_aa_10.GeV_cYY_0.000019':"$m_ALP =$ 10 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_10.GeV_cYY_0.00006':"$m_ALP =$ 10 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_10.GeV_cYY_0.00019':"$m_ALP =$ 10 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_10.GeV_cYY_0.0006':"$m_ALP =$ 10 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_10.GeV_cYY_0.0019':"$m_ALP =$ 10 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_10.GeV_cYY_0.006':"$m_ALP =$ 10 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_10.GeV_cYY_0.019':"$m_ALP =$ 10 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_10.GeV_cYY_0.06':"$m_ALP =$ 10 GeV, $c_{YY} = 0.06$",
    # 'ALP_Z_aa_10.GeV_cYY_0.19':"$m_ALP =$ 10 GeV, $c_{YY} = 0.19$",
    # 'ALP_Z_aa_10.GeV_cYY_0.6':"$m_ALP =$ 10 GeV, $c_{YY} = 0.6$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.0000006':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.0000006$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.0000019':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.0000019$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.000006':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.000006$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.000019':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.000019$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.00006':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.00006$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.00019':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.00019$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.0006':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.0006$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.0019':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.0019$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.006':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.006$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.019':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.019$",
    # 'ALP_Z_aa_31.6.GeV_cYY_0.06':"$m_ALP =$ 31.6 GeV, $c_{YY} = 0.06$",



    # 'ALP_Z_aa_0p5GeV_cYY1p0': "$m_ALP =$ 0.5 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_0p8GeV_cYY1p0': "$m_ALP =$ 0.8 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_1p0GeV_cYY1p0': "$m_ALP =$ 1 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_5p0GeV_cYY1p0': "$m_ALP =$ 5 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_8p0GeV_cYY1p0': "$m_ALP =$ 8 GeV, $c_{YY} = 1$",

    # 'ALP_Z_aa_0p001GeV_cYY1p0': "$m_ALP =$ 0.001 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_0p01GeV_cYY1p0': "$m_ALP =$ 0.01 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_0p1GeV_cYY1p0': "$m_ALP =$ 0.1 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_0p5GeV_cYY1p0': "$m_ALP =$ 0.5 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_0p8GeV_cYY1p0': "$m_ALP =$ 0.8 GeV, $c_{YY} = 1$",    
    # 'ALP_Z_aa_1p0GeV_cYY1p0': "$m_ALP =$ 1.00 GeV, $c_{YY} = 1$",
    # # 'ALP_Z_aa_2p0GeV_cYY1p0': "$m_ALP =$ 2.00 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_3p0GeV_cYY1p0': "$m_ALP =$ 3.00 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_5p0GeV_cYY1p0': "$m_ALP =$ 5.00 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_10p0GeV_cYY1p0': "$m_ALP =$ 10.00 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_20p0GeV_cYY1p0': "$m_ALP =$ 20.00 GeV, $c_{YY} = 1$",
    # 'ALP_Z_aa_30p0GeV_cYY1p0': "$m_ALP =$ 30.00 GeV, $c_{YY} = 1$",


    # 'ALP_Z_aa_1p0GeV_cYY0p001': "$m_ALP =$ 1.00 GeV, $c_{YY} = 0.001$",
    # 'ALP_Z_aa_1p0GeV_cYY0p01': "$m_ALP =$ 1.00 GeV, $c_{YY} = 0.01$",
    # 'ALP_Z_aa_1p0GeV_cYY0p1': "$m_ALP =$ 1.00 GeV, $c_{YY} = 0.1$",
    # 'ALP_Z_aa_1p0GeV_cYY0p4': "$m_ALP =$ 1.00 GeV, $c_{YY} = 0.4$",
    # 'ALP_Z_aa_1p0GeV_cYY0p7': "$m_ALP =$ 1.00 GeV, $c_{YY} = 0.7$",
    # 'ALP_Z_aa_1p0GeV_cYY1p3': "$m_ALP =$ 1.00 GeV, $c_{YY} = 1.3$",
    # 'ALP_Z_aa_1p0GeV_cYY1p6': "$m_ALP =$ 1.00 GeV, $c_{YY} = 1.6$",

}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_spring2021_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    # "p8_ee_Zee_ecm91": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ee_gaga_1million": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 57.319, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "test1": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 57.348, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "test2": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 2087.700, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "test4": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 0.461, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ee_gammagamma": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 45.454, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ee_gaga_test": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 4.563, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ee_aa": {"numberOfEvents": 1000000, "sumOfWeights": 100000, "crossSection": 57.3, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "background_ee_aa": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 57.32, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "background_ee_aaa": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.4624, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "background_ee_aaaa": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.001119, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "background_ee_ee": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 4500, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "background_ee_eea": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 29.76, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "background_ee_eeaa": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.09864, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "background_ee_eeaaa": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.000111, "kfactor": 1.0, "matchingEfficiency": 1.0},

    "background_ee_aa1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 67.25 , "kfactor": 1.0, "matchingEfficiency": 1.0},
    "background_ee_aaa1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.995 , "kfactor": 1.0, "matchingEfficiency": 1.0},
    "background_ee_aaaa1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.06271, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "background_ee_ee": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 4500, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "background_ee_eea1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 118.4 , "kfactor": 1.0, "matchingEfficiency": 1.0},
    "background_ee_eeaa1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 1.993 , "kfactor": 1.0, "matchingEfficiency": 1.0},
    "background_ee_eeaaa1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02369, "kfactor": 1.0, "matchingEfficiency": 1.0},




    'ALP_Z_aa_0p1GeV_cYY1p6':{"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 7.014 , "kfactor": 1.0, "matchingEfficiency": 1.0},

    'ALP_Z_aa_1p0GeV_cYY1p0':{"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.739 , "kfactor": 1.0, "matchingEfficiency": 1.0},

    'ALP_Z_aa_3p0GeV_cYY0p4':{"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.437 , "kfactor": 1.0, "matchingEfficiency": 1.0},

    'ALP_Z_aa_10p0GeV_cYY0p03':{"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.002378  , "kfactor": 1.0, "matchingEfficiency": 1.0},

    'ALP_Z_aa_30p0GeV_cYY0p002':{"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 7.772e-06  , "kfactor": 1.0, "matchingEfficiency": 1.0},
    'ALP_Z_aa_30p0GeV_cYY0p0002':{"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 7.772e-08 , "kfactor": 1.0, "matchingEfficiency": 1.0},



    # "ALP_Z_aa_0.01.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.01.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.01.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.01.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.01.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.0316.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.1.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.316.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.0.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.0000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.000006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3.16.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.0000006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.0000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.000006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.0000006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.0000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.000006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.000019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.00006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.00019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.0006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.0019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.006": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.019": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.06": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.19": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_31.6.GeV_cYY_0.6": {"numberOfEvents": 10000, "sumOfWeights": 10000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "ee_Z_ALPga_gagaga": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.6847, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "ALP_Z_aa_1GeV_cYY_0p5": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "ALP_Z_aa_0.1GeV_cYY_0.1": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.2GeV_cYY_0.1": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.135GeV_cYY_0.1": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.3GeV_cYY_0.1": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "ALP_Z_aa_1.GeV_cYY_0.1": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.GeV_cYY_0.3": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.GeV_cYY_0.5": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.GeV_cYY_0.7": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.GeV_cYY_0.9": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.744e-05, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "ALP_Z_aa_0.5.GeV_cYY_0.6": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.986, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0.5.GeV_cYY_1.2": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.94, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # for 0.6 below, cross section is actually 0.98597
    # "ALP_Z_aa_1.GeV_cYY_0.6": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.GeV_cYY_0.8": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #  "ALP_Z_aa_1.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_1.GeV_cYY_1.2": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_1.GeV_cYY_1.4": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},

    #  "ALP_Z_aa_0.5.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_1.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_1.5.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_2.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.73, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_3.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # # "ALP_Z_aa_4.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #  "ALP_Z_aa_5.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.709, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #  "ALP_Z_aa_8.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.671, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # # "ALP_Z_aa_0.6.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #  "ALP_Z_aa_0.8.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.2.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1.4.GeV_cYY_1.0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 0.027, "kfactor": 1.0, "matchingEfficiency": 1.0},


####     using my new pythia samples        ####

    # "ALP_Z_aa_0p5GeV_cYY1p0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0p8GeV_cYY1p0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY1p0": {"numberOfEvents": 100, "sumOfWeights": 100, "crossSection": 2.733, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_5p0GeV_cYY1p0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.709, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_8p0GeV_cYY1p0": {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.671, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # "ALP_Z_aa_0p001GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 1.407, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0p01GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.74, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0p1GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.74, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0p5GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.74, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_0p8GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.74, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.739, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # # "ALP_Z_aa_2p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.736, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_3p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.731, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_5p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.715, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_10p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.642, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_20p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.363, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_30p0GeV_cYY1p0": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 1.943, "kfactor": 1.0, "matchingEfficiency": 1.0},


    # "ALP_Z_aa_1p0GeV_cYY0p001": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 2.739e-06, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY0p01": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.0002739, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY0p1": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.02739, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY0p4": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 0.4382, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY0p7": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 1.342, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY1p3": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 4.629, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # "ALP_Z_aa_1p0GeV_cYY1p6": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 7.011, "kfactor": 1.0, "matchingEfficiency": 1.0},


}

#Number of CPUs to use
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "selNone": "n_RecoTracks > -1",
    # "sel1": "n_RecoPhotons == 3",
    # "sel2": "RecoPhotons_delta_r[0] < 0.5 || RecoPhotons_delta_r[0] > 4.5",
    # "sel1+2": "n_RecoPhotons == 3 && (RecoPhotons_delta_r[0] < 0.5 || RecoPhotons_delta_r[0] > 4.5)",
    # "sel0": "RecoPhotons_min_delta_r[0] < 0.5 || RecoPhotons_min_delta_r[0] > 3 && RecoPhotons_min_delta_r[0] < 3.3",
    # "sel0": "RecoPhotons_min_delta_r[0] < 0.2",
    # "sel0": "RecoPhotons_min_delta_r[0] < 0.5 || RecoPhotons_min_delta_r[0] > 3 && RecoPhotons_min_delta_r[0] < 3.3",
    # "sel1": "GenALP_mass.size() > 0 && n_RecoElectrons > 1",
    # "seltest": "n_RecoPhotons == 3 && (RecoPhoton1_px > 0 && RecoPhoton2_px > 0 || RecoPhoton1_px < 0 && RecoPhoton2_px < 0) && RecoPhotons_min_delta_r[0] < 1.0",
    # "seldeltaR": "n_RecoPhotons == 3 && RecoPhotons_min_delta_r[0] < 1.0",
    # "selp": "n_RecoPhotons == 3 && RecoPhoton0_p > 44",
    # "selall": "n_RecoPhotons == 3 && RecoPhotons_min_delta_r[0] < 1.0 && RecoPhoton0_p > 44",



    ### E ###
    # "preselection": "FSGenPhotons_min_delta_r[0] > 0.4 && RecoPhotons_min_delta_r[0] > 0.4",

}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    "selNone": "Before selection",
    # "sel1": "Exactly 3 Reconstructed Photons",
    # "sel2": "Reco Photons #DeltaR < 0.5 or > 4.5",
    # "sel1+2": "Exactly 3 Reconstruced Photons and Reco Photons #DeltaR < 0.5 or > 4.5",
    # "sel0": "RecoPhotons_min_delta_r close to 0 and pi",
    # "sel0": "Good GEN ALP mass",
    # "sel1": "Good GEN ALP mass and 2 reco electrons",
    # "seltest": "3 reco photons, second and third photons have the same direction px, and min #DeltaR < 1",
    # "seldeltaR": "3 reco photons and reco photons min #DeltaR < 1",
    # "selp": "3 reco photons and RecoPhoton0 momentum > 44",
    # "selall": "all selections",
    # "selbkg": "FSGenPhotons_min_delta_r > 0.4",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    #gen variables
    "All_n_GenALP":                    {"name":"All_n_GenALP",                   "title":"Total number of gen ALPs",                   "bin":5,"xmin":-0.5 ,"xmax":4.5},

    "n_FSGenALP":                      {"name":"n_FSGenALP",                     "title":"Total number of FS gen ALPs",                "bin":5,"xmin":-0.5 ,"xmax":4.5},

    "AllGenALP_mass":                  {"name":"AllGenALP_mass",                 "title":"All gen ALP mass [GeV]",                       "bin":100,"xmin":0 ,"xmax":10},
    "AllGenALP_e":                     {"name":"AllGenALP_e",                    "title":"All gen ALP energy [GeV]",                     "bin":100,"xmin":0 ,"xmax":100},
    "AllGenALP_p":                     {"name":"AllGenALP_p",                    "title":"All gen ALP p [GeV]",                          "bin":100,"xmin":0 ,"xmax":50},
    "AllGenALP_pt":                    {"name":"AllGenALP_pt",                   "title":"All gen ALP p_{T} [GeV]",                      "bin":100,"xmin":0 ,"xmax":50},
    "AllGenALP_pz":                    {"name":"AllGenALP_pz",                   "title":"All gen ALP p_{z} [GeV]",                      "bin":100,"xmin":0 ,"xmax":50},
    "AllGenALP_eta":                   {"name":"AllGenALP_eta",                  "title":"All gen ALP #eta",                             "bin":60, "xmin":-3,"xmax":3},
    "AllGenALP_theta":                 {"name":"AllGenALP_theta",                "title":"All gen ALP #theta",                           "bin":64, "xmin":0,"xmax":3.2},
    "AllGenALP_phi":                   {"name":"AllGenALP_phi",                  "title":"All gen ALP #phi",                             "bin":64, "xmin":-3.2,"xmax":3.2},

    "n_FSGenElectron":                 {"name":"n_FSGenElectron",                "title":"Number of final state gen electrons",        "bin":7,"xmin":-0.5 ,"xmax":6.5},
    # "n_FSGenPositron":                 {"name":"n_FSGenPositron",                "title":"Number of final state gen positrons",        "bin":5,"xmin":-0.5 ,"xmax":4.5},
    # "n_FSGenNeutrino":                 {"name":"n_FSGenNeutrino",                "title":"Number of final state gen neutrinos",        "bin":5,"xmin":-0.5 ,"xmax":4.5},
    # "n_FSGenAntiNeutrino":             {"name":"n_FSGenAntiNeutrino",            "title":"Number of final state gen anti-neutrinos",   "bin":5,"xmin":-0.5 ,"xmax":4.5},
    "n_FSGenPhoton":                   {"name":"n_FSGenPhoton",                  "title":"Number of final state gen photons",          "bin":9,"xmin":-0.5 ,"xmax":8.5},

    # # "n_FSGenElectron_forFS2GenPhotons":                 {"name":"n_FSGenElectron_forFS2GenPhotons",                "title":"Number of final state gen electrons for events with 2 FS photons",        "bin":7,"xmin":-2.5 ,"xmax":4.5},
    # # "n_FSGenPositron_forFS2GenPhotons":                 {"name":"n_FSGenPositron_forFS2GenPhotons",                "title":"Number of final state gen positrons for events with 2 FS photons",        "bin":7,"xmin":-2.5 ,"xmax":4.5},

    "FSGenElectron_e":                 {"name":"FSGenElectron_e",                "title":"Final state gen electrons energy [GeV]",     "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectron_p":                 {"name":"FSGenElectron_p",                "title":"Final state gen electrons p [GeV]",          "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectron_pt":                {"name":"FSGenElectron_pt",               "title":"Final state gen electrons p_{T} [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectron_pz":                {"name":"FSGenElectron_pz",               "title":"Final state gen electrons p_{z} [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectron_eta":               {"name":"FSGenElectron_eta",              "title":"Final state gen electrons #eta",             "bin":60, "xmin":-3,"xmax":3},
    "FSGenElectron_theta":             {"name":"FSGenElectron_theta",            "title":"Final state gen electrons #theta",           "bin":64, "xmin":0,"xmax":3.2},
    "FSGenElectron_phi":               {"name":"FSGenElectron_phi",              "title":"Final state gen electrons #phi",             "bin":64, "xmin":-3.2,"xmax":3.2},

    "FSGenElectronPositron_e":                 {"name":"FSGenElectronPositron_e",                "title":"Final state gen e energy [GeV]",     "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectronPositron_p":                 {"name":"FSGenElectronPositron_p",                "title":"Final state gen e p [GeV]",          "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectronPositron_pt":                {"name":"FSGenElectronPositron_pt",               "title":"Final state gen e p_{T} [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectronPositron_pz":                {"name":"FSGenElectronPositron_pz",               "title":"Final state gen e p_{z} [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectronPositron_py":                {"name":"FSGenElectronPositron_py",               "title":"Final state gen e p_{y} [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectronPositron_px":                {"name":"FSGenElectronPositron_px",               "title":"Final state gen e p_{x} [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "FSGenElectronPositron_eta":               {"name":"FSGenElectronPositron_eta",              "title":"Final state gen e #eta",             "bin":60, "xmin":-3,"xmax":3},
    "FSGenElectronPositron_theta":             {"name":"FSGenElectronPositron_theta",            "title":"Final state gen e #theta",           "bin":64, "xmin":0,"xmax":3.2},
    "FSGenElectronPositron_phi":               {"name":"FSGenElectronPositron_phi",              "title":"Final state gen e #phi",             "bin":64, "xmin":-3.2,"xmax":3.2},

    # "FSGenPositron_e":                 {"name":"FSGenPositron_e",                "title":"Final state gen positrons energy [GeV]",     "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenPositron_p":                 {"name":"FSGenPositron_p",                "title":"Final state gen positrons p [GeV]",          "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenPositron_pt":                {"name":"FSGenPositron_pt",               "title":"Final state gen positrons p_{T} [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenPositron_pz":                {"name":"FSGenPositron_pz",               "title":"Final state gen positrons p_{z} [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenPositron_eta":               {"name":"FSGenPositron_eta",              "title":"Final state gen positrons #eta",             "bin":60, "xmin":-3,"xmax":3},
    # "FSGenPositron_theta":             {"name":"FSGenPositron_theta",            "title":"Final state gen positrons #theta",           "bin":64, "xmin":0,"xmax":3.2},
    # "FSGenPositron_phi":               {"name":"FSGenPositron_phi",              "title":"Final state gen positrons #phi",             "bin":64, "xmin":-3.2,"xmax":3.2},

    # "FSGenNeutrino_e":                 {"name":"FSGenNeutrino_e",                "title":"Final state gen neutrino energy [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenNeutrino_p":                 {"name":"FSGenNeutrino_p",                "title":"Final state gen neutrino p [GeV]",           "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenNeutrino_pt":                {"name":"FSGenNeutrino_pt",               "title":"Final state gen neutrino p_{T} [GeV]",       "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenNeutrino_pz":                {"name":"FSGenNeutrino_pz",               "title":"Final state gen neutrino p_{z} [GeV]",       "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenNeutrino_eta":               {"name":"FSGenNeutrino_eta",              "title":"Final state gen neutrinos #eta",             "bin":60, "xmin":-3,"xmax":3},
    # "FSGenNeutrino_theta":             {"name":"FSGenNeutrino_theta",            "title":"Final state gen neutrinos #theta",           "bin":64, "xmin":0,"xmax":3.2},
    # "FSGenNeutrino_phi":               {"name":"FSGenNeutrino_phi",              "title":"Final state gen neutrinos #phi",             "bin":64, "xmin":-3.2,"xmax":3.2},

    # "FSGenAntiNeutrino_e":             {"name":"FSGenAntiNeutrino_e",            "title":"Final state gen anti-neutrino energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenAntiNeutrino_p":             {"name":"FSGenAntiNeutrino_p",            "title":"Final state gen anti-neutrino p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenAntiNeutrino_pt":            {"name":"FSGenAntiNeutrino_pt",           "title":"Final state gen anti-neutrino p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenAntiNeutrino_pz":            {"name":"FSGenAntiNeutrino_pz",           "title":"Final state gen anti-neutrino p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    # "FSGenAntiNeutrino_eta":           {"name":"FSGenAntiNeutrino_eta",          "title":"Final state gen anti-neutrinos #eta",        "bin":60, "xmin":-3,"xmax":3},
    # "FSGenAntiNeutrino_theta":         {"name":"FSGenAntiNeutrino_theta",        "title":"Final state gen anti-neutrinos #theta",      "bin":64, "xmin":0,"xmax":3.2},
    # "FSGenAntiNeutrino_phi":           {"name":"FSGenAntiNeutrino_phi",          "title":"Final state gen anti-neutrinos #phi",        "bin":64, "xmin":-3.2,"xmax":3.2},
    "FSGenALP_p":                      {"name":"FSGenALP_p",                     "title":"Final state gen ALP p [GeV]",               "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_e":                   {"name":"FSGenPhoton_e",                  "title":"Final state gen photons energy [GeV]",       "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_p":                   {"name":"FSGenPhoton_p",                  "title":"Final state gen photons p [GeV]",            "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_pt":                  {"name":"FSGenPhoton_pt",                 "title":"Final state gen photons p_{T} [GeV]",        "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_pz":                  {"name":"FSGenPhoton_pz",                 "title":"Final state gen photons p_{z} [GeV]",        "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_eta":                 {"name":"FSGenPhoton_eta",                "title":"Final state gen photons #eta",               "bin":60, "xmin":-3,"xmax":3},
    "FSGenPhoton_theta":               {"name":"FSGenPhoton_theta",              "title":"Final state gen photons #theta",             "bin":64, "xmin":0,"xmax":3.2},
    "FSGenPhoton_phi":                 {"name":"FSGenPhoton_phi",                "title":"Final state gen photons #phi",               "bin":64, "xmin":-3.2,"xmax":3.2},

    "FSGenPhoton0_e":                 {"name":"FSGenPhoton0_e",                "title":"Final state gen photon_{0} energy [GeV]",               "bin":100, "xmin":-3.2,"xmax":50},
    "FSGenPhoton1_e":                 {"name":"FSGenPhoton1_e",                "title":"Final state gen photon_{1} energy [GeV]",               "bin":100, "xmin":-3.2,"xmax":50},
    "FSGenPhoton2_e":                 {"name":"FSGenPhoton2_e",                "title":"Final state gen photon_{2} energy [GeV]",               "bin":100, "xmin":-3.2,"xmax":50},
    "FSGenPhoton0_p":                   {"name":"FSGenPhoton0_p",                  "title":"Final state gen photon_{0} p [GeV]",            "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_p":                   {"name":"FSGenPhoton1_p",                  "title":"Final state gen photon_{1} p [GeV]",            "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_p":                   {"name":"FSGenPhoton2_p",                  "title":"Final state gen photon_{2} p [GeV]",            "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_pt":                  {"name":"FSGenPhoton0_pt",                 "title":"Final state gen photon_{0} p_{T} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_pt":                  {"name":"FSGenPhoton1_pt",                 "title":"Final state gen photon_{1} p_{T} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_pt":                  {"name":"FSGenPhoton2_pt",                 "title":"Final state gen photon_{2} p_{T} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_px":                  {"name":"FSGenPhoton0_px",                 "title":"Final state gen photon_{0} p_{x} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_px":                  {"name":"FSGenPhoton1_px",                 "title":"Final state gen photon_{1} p_{x} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_px":                  {"name":"FSGenPhoton2_px",                 "title":"Final state gen photon_{2} p_{x} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_py":                  {"name":"FSGenPhoton0_py",                 "title":"Final state gen photon_{0} p_{y} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_py":                  {"name":"FSGenPhoton1_py",                 "title":"Final state gen photon_{1} p_{y} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_py":                  {"name":"FSGenPhoton2_py",                 "title":"Final state gen photon_{2} p_{y} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_pz":                  {"name":"FSGenPhoton0_pz",                 "title":"Final state gen photon_{0} p_{z} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_pz":                  {"name":"FSGenPhoton1_pz",                 "title":"Final state gen photon_{1} p_{z} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_pz":                  {"name":"FSGenPhoton2_pz",                 "title":"Final state gen photon_{2} p_{z} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},

    "FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0": {"name": "FSGenPhoton1_px_if_FSGenPhoton0_px_greaterthan_0", "title": "FS gen photon_{1} p_{x} if FS gen photon_{0} p_{x} > 0", "bin":100, "xmin":-55, "xmax":50},
    "FSGenPhoton1_px_if_FSGenPhoton2_px_pos": {"name": "FSGenPhoton1_px_if_FSGenPhoton2_px_pos", "title": "FS gen photon_{1} p_{x} if FS gen photon_{2} p_{x} > 0", "bin":100, "xmin":-55, "xmax":50},
    "FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos": {"name": "FSGenPhoton1_pz_if_FSGenPhoton2_pz_pos", "title": "FS gen photon_{1} p_{z} if FS gen photon_{2} p_{z} > 0", "bin":100, "xmin":-55, "xmax":50},

    "FSGenPhoton_vertex_x": {"name":"FSGenPhoton_vertex_x", "title":"Final state gen photon production vertex x [mm]",      "bin":100,"xmin":-1000 ,"xmax":1000},
    "FSGenPhoton_vertex_y": {"name":"FSGenPhoton_vertex_y", "title":"Final state gen photon production vertex y [mm]",      "bin":100,"xmin":-1000 ,"xmax":1000},
    "FSGenPhoton_vertex_z": {"name":"FSGenPhoton_vertex_z", "title":"Final state gen photon production vertex z [mm]",      "bin":100,"xmin":-1000 ,"xmax":1000},

    # "FSGen_lifetime_xy": {"name":"FSGen_lifetime_xy", "title":"Gen ALP (FS eles) #tau_{xy} [s]",        "bin":100,"xmin":0 ,"xmax":1E-10},
    # "FSGen_lifetime_xyz": {"name":"FSGen_lifetime_xyz", "title":"Gen ALP (FS eles) #tau_{xyz} [s]",        "bin":100,"xmin":0 ,"xmax":1E-10},
    # "FSGen_Lxy":      {"name":"FSGen_Lxy",      "title":"Gen ALP (FS eles) L_{xy} [mm]",     "bin":100,"xmin":0 ,"xmax":1000},
    # "FSGen_Lxyz":     {"name":"FSGen_Lxyz",     "title":"Gen ALP (FS eles) L_{xyz} [mm]",    "bin":100,"xmin":0 ,"xmax":1000},

    # # "FSGen_a0a1_invMass":   {"name":"FSGen_a0a1_invMass",   "title":"Gen FS photons m_{01} [GeV]",           "bin":105,"xmin":-5, "xmax":100},
    # # "FSGen_a0a2_invMass":   {"name":"FSGen_a0a2_invMass",   "title":"Gen FS photons m_{02} [GeV]",           "bin":105,"xmin":-5, "xmax":100},
    # # "FSGen_a1a2_invMass":   {"name":"FSGen_a1a2_invMass",   "title":"Gen FS photons m_{12} [GeV]",           "bin":105,"xmin":-5, "xmax":100},
    # # "FSGen_aaa_invMass":   {"name":"FSGen_aaa_invMass",   "title":"Gen FS m_{#gamma #gamma #gamma} [GeV]",           "bin":105,"xmin":-5, "xmax":100},

    "FSGenALP_mass":        {"name":"FSGenALP_mass",   "title":"FS gen ALP mass [GeV]",   "bin":100,"xmin":0 ,"xmax":10},

    "GenALP_mass":     {"name":"GenALP_mass",     "title":"Gen ALP mass [GeV]",      "bin":100,"xmin":0 ,"xmax":10},
    "GenALP_e":        {"name":"GenALP_e",        "title":"Gen ALP energy [GeV]",    "bin":100,"xmin":0 ,"xmax":50},
    "GenALP_p":        {"name":"GenALP_p",        "title":"Gen ALP p [GeV]",         "bin":100,"xmin":0 ,"xmax":50},
    "GenALP_pt":       {"name":"GenALP_pt",       "title":"Gen ALP p_{T} [GeV]",     "bin":100,"xmin":0 ,"xmax":50},
    "GenALP_pz":       {"name":"GenALP_pz",       "title":"Gen ALP p_{z} [GeV]",     "bin":100,"xmin":0 ,"xmax":50},
    "GenALP_eta":      {"name":"GenALP_eta",      "title":"Gen ALP #eta",            "bin":60, "xmin":-3,"xmax":3},
    "GenALP_theta":    {"name":"GenALP_theta",    "title":"Gen ALP #theta",          "bin":64, "xmin":0,"xmax":3.2},
    "GenALP_phi":      {"name":"GenALP_phi",      "title":"Gen ALP #phi",            "bin":64, "xmin":-3.2,"xmax":3.2},
    "GenALP_lifetime_xy": {"name":"GenALP_lifetime_xy", "title":"Gen ALP #tau_{xy} [s]",        "bin":100,"xmin":0 ,"xmax":1E-11},
    "GenALP_lifetime_xyz": {"name":"GenALP_lifetime_xyz", "title":"Gen ALP #tau_{xyz} [s]",        "bin":100,"xmin":0 ,"xmax":1E-11},
    "GenALP_Lxy":      {"name":"GenALP_Lxy",      "title":"Gen ALP L_{xy} [mm]",     "bin":100,"xmin":0 ,"xmax":10},
    "GenALP_Lxyz":     {"name":"GenALP_Lxyz",     "title":"Gen ALP L_{xyz} [mm]",    "bin":100,"xmin":0 ,"xmax":10},
    "GenALP_vertex_x": {"name":"GenALP_vertex_x", "title":"Gen ALP production vertex x [mm]",   "bin":100,"xmin":-1000 ,"xmax":1000},
    "GenALP_vertex_y": {"name":"GenALP_vertex_y", "title":"Gen ALP production vertex y [mm]",   "bin":100,"xmin":-1000 ,"xmax":1000},
    "GenALP_vertex_z": {"name":"GenALP_vertex_z", "title":"Gen ALP production vertex z [mm]",   "bin":100,"xmin":-1000 ,"xmax":1000},

    "GenALP_px_if_FSGenPhoton0_px_greaterthan_0": {"name": "GenALP_px_if_FSGenPhoton0_px_greaterthan_0", "title": "Gen ALP p_{x} if FS gen photon_{0} p_{x} > 0", "bin":100, "xmin":-55, "xmax":50},
    "FSGenPhoton1_px_if_GenALP_px_neg": {"name": "FSGenPhoton1_px_if_GenALP_px_neg", "title": "FS gen photon_{1} p_{x} if gen ALP p_{x} < 0", "bin":100, "xmin":-55, "xmax":50},
    "FSGenPhoton2_px_if_GenALP_px_neg": {"name": "FSGenPhoton2_px_if_GenALP_px_neg", "title": "FS gen photon_{2} p_{x} if gen ALP p_{x} < 0", "bin":100, "xmin":-55, "xmax":50},

    # "GenALP_deltaR":   {"name":"GenALP_deltaR",   "title":"Gen ALP #DeltaR",        "bin":60,"xmin":0,"xmax":5},
    "n_GenALP":        {"name":"n_GenALP",        "title":"Number of gen ALPs",      "bin":5,"xmin":-0.5,"xmax":4.5},
    "n_GenALPPhoton1":  {"name":"n_GenALPPhoton1",  "title":"Number of gen photon_{1}","bin":100,"xmin":-0.5,"xmax":4.5},
    "n_GenALPPhoton2":  {"name":"n_GenALPPhoton2",  "title":"Number of gen photon_{2}","bin":100,"xmin":-0.5,"xmax":4.5},
    "GenALP_time":     {"name":"GenALP_time",       "title":"Gen ALP time [s]",            "bin":100,"xmin":0,"xmax":5E-24},
    "GenALP_pdg":      {"name":"GenALP_pdg",        "title":"Gen ALP pdg",             "bin":100,"xmin":-10,"xmax":10},

    # "GenALPPhoton1_time_minus_GenALP_time": {"name":"GenALPPhoton1_time_minus_GenALP_time", "title":"Gen ALP Photon_{1} time - Gen ALP time", "bin":100,"xmin":0,"xmax":1E-7},

    # "GenALPPhoton1_deltaR":   {"name":"GenALPPhoton1_deltaR",   "title":"Gen photon_{1} #DeltaR",                       "bin":60,"xmin":0, "xmax":5},
    # "GenALPPhoton2_deltaR":   {"name":"GenALPPhoton2_deltaR",   "title":"Gen photon_{2} #DeltaR",                       "bin":60,"xmin":0, "xmax":5},
    "GenALPPhotons_deltaEta": {"name":"GenALPPhotons_deltaEta", "title":"Gen ALP photons #Delta#eta",                   "bin":100, "xmin":0, "xmax":8},
    "GenALPPhotons_deltaPhi": {"name":"GenALPPhotons_deltaPhi", "title":"Gen ALP photons #Delta#phi",                   "bin":100, "xmin":0, "xmax":8},
    "GenALPPhotons_deltaR":   {"name":"GenALPPhotons_deltaR",   "title":"Gen ALP photons #DeltaR",                      "bin":100, "xmin":0, "xmax":8},

    # "GenALPPhotons_deltaR_2": {"name":"GenALPPhotons_deltaR_2", "title":"Gen ALP photons #DeltaR (from ROOT)",          "bin":100, "xmin":0, "xmax":8},
    "FSGenPhotons_delta_r":   {"name":"FSGenPhotons_delta_r",   "title":"Final state gen photons #DeltaR",              "bin":100, "xmin":0, "xmax":7},
    "FSGenPhotons_min_delta_r":   {"name":"FSGenPhotons_min_delta_r",   "title":"Final state gen photons minimum #DeltaR",              "bin":100, "xmin":0, "xmax":7},

    "GenALPPhoton1_e":        {"name":"GenALPPhoton1_e",        "title":"Gen photon_{1} energy [GeV]",                  "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton2_e":        {"name":"GenALPPhoton2_e",        "title":"Gen photon_{2} energy [GeV]",                                "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton1_p":        {"name":"GenALPPhoton1_p",        "title":"Gen photon_{1} p [GeV]",                       "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton2_p":        {"name":"GenALPPhoton2_p",        "title":"Gen photon_{2} p [GeV]",                                     "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton1_pt":       {"name":"GenALPPhoton1_pt",       "title":"Gen photon_{1} p_{T} [GeV]",                   "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton2_pt":       {"name":"GenALPPhoton2_pt",       "title":"Gen photon_{2} p_{T} [GeV]",                                 "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton1_pz":       {"name":"GenALPPhoton1_pz",       "title":"Gen photon_{1} p_{z} [GeV]",                   "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton2_pz":       {"name":"GenALPPhoton2_pz",       "title":"Gen photon_{2} p_{z} [GeV]",                                 "bin":100,"xmin":0 ,"xmax":50},
    "GenALPPhoton1_eta":      {"name":"GenALPPhoton1_eta",      "title":"Gen photon_{1} #eta",                          "bin":60, "xmin":-3,"xmax":3},
    "GenALPPhoton2_eta":      {"name":"GenALPPhoton2_eta",      "title":"Gen photon_{2} #eta",                                        "bin":60, "xmin":-3,"xmax":3},
    "GenALPPhoton1_theta":    {"name":"GenALPPhoton1_theta",    "title":"Gen photon_{1} #theta",                        "bin":64, "xmin":0,"xmax":3.2},
    "GenALPPhoton2_theta":    {"name":"GenALPPhoton2_theta",    "title":"Gen photon_{2} #theta",                                      "bin":64, "xmin":0,"xmax":3.2},
    "GenALPPhoton1_phi":      {"name":"GenALPPhoton1_phi",      "title":"Gen photon_{1} #phi",                          "bin":64, "xmin":-3.2,"xmax":3.2},
    "GenALPPhoton2_phi":      {"name":"GenALPPhoton2_phi",      "title":"Gen photon_{2} #phi",                                        "bin":64, "xmin":-3.2,"xmax":3.2},

    "GenALPPhoton1_time":      {"name":"GenALPPhoton1_time",     "title":"Gen photon_{1} time [s]",                          "bin":100, "xmin":0, "xmax":0.1E-12},
    "GenALPPhoton2_time":      {"name":"GenALPPhoton2_time",     "title":"Gen photon_{2} time [s]",                          "bin":100, "xmin":0, "xmax":250E-14},

    "GenALP_observed_lifetime_xyz": {"name":"GenALP_observed_lifetime_xyz", "title":"Gen ALP #tau_{xyz, lab} [s]", "bin":100, "xmin":0, "xmax":1E-12},

    "GenALPPhoton1_vertex_x": {"name":"GenALPPhoton1_vertex_x", "title":"Gen photon_{1} production vertex x [mm]",      "bin":100,"xmin":-1000 ,"xmax":1000},
    "GenALPPhoton1_vertex_y": {"name":"GenALPPhoton1_vertex_y", "title":"Gen photon_{1} production vertex y [mm]",      "bin":100,"xmin":-1000 ,"xmax":1000},
    "GenALPPhoton1_vertex_z": {"name":"GenALPPhoton1_vertex_z", "title":"Gen photon_{1} production vertex z [mm]",      "bin":100,"xmin":-1000 ,"xmax":1000},

    "GenALP_aa_invMass":   {"name":"GenALP_aa_invMass",   "title":"Gen m_{#gamma#gamma} (from ALP) [GeV]",           "bin":100,"xmin":0, "xmax":10},

    # #reco variables
    "n_RecoTracks":                    {"name":"n_RecoTracks",                   "title":"Total number of reco tracks",           "bin":5,"xmin":-0.5 ,"xmax":4.5},
    "n_RecoALPTracks":                 {"name":"n_RecoALPTracks",                "title":"Number of reco ALP tracks",             "bin":5,"xmin":-0.5 ,"xmax":4.5},
    "RecoALP_DecayVertex_x":           {"name":"RecoALPDecayVertex.position.x",  "title":"Reco ALP decay vertex x [mm]",            "bin":100,"xmin":-1000 ,"xmax":1000},
    "RecoALP_DecayVertex_y":           {"name":"RecoALPDecayVertex.position.y",  "title":"Reco ALP decay vertex y [mm]",            "bin":100,"xmin":-1000 ,"xmax":1000},
    "RecoALP_DecayVertex_z":           {"name":"RecoALPDecayVertex.position.z",  "title":"Reco ALP decay vertex z [mm]",            "bin":100,"xmin":-1000 ,"xmax":1000},
    # "RecoALP_DecayVertex_chi2":        {"name":"RecoALPDecayVertex.chi2",        "title":"Reco ALP decay vertex #chi^{2}",          "bin":100,"xmin":0 ,"xmax":3},
    # "RecoALP_DecayVertex_probability": {"name":"RecoALPDecayVertex.probability", "title":"Reco ALP decay vertex probability",       "bin":100,"xmin":0 ,"xmax":10},

    # "RecoALPL_xyz":            {"name":"RecoALPL_xyz",            "title":"Reco ALP L_{xyz}",                        "bin":100,"xmin":-1,"xmax":10},

    "RecoALPPhoton1_e":        {"name":"RecoALPPhoton1_e",        "title":"Reco photon_{1} (from ALP) energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_e":        {"name":"RecoALPPhoton2_e",        "title":"Reco photon_{2} (from ALP) energy [GeV]",               "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_p":        {"name":"RecoALPPhoton1_p",        "title":"Reco photon_{1} (from ALP) p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_p":        {"name":"RecoALPPhoton2_p",        "title":"Reco photon_{2} (from ALP) p [GeV]",                    "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_pt":       {"name":"RecoALPPhoton1_pt",       "title":"Reco photon_{1} (from ALP) p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_pt":       {"name":"RecoALPPhoton2_pt",       "title":"Reco photon_{2} (from ALP) p_{T} [GeV]",                "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_pz":       {"name":"RecoALPPhoton1_pz",       "title":"Reco photon_{1} (from ALP) p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_pz":       {"name":"RecoALPPhoton2_pz",       "title":"Reco photon_{2} (from ALP) p_{z} [GeV]",                "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_eta":      {"name":"RecoALPPhoton1_eta",      "title":"Reco photon_{1} (from ALP) #eta",         "bin":60, "xmin":-3,"xmax":3},
    "RecoALPPhoton2_eta":      {"name":"RecoALPPhoton2_eta",      "title":"Reco photon_{2} (from ALP) #eta",                       "bin":60, "xmin":-3,"xmax":3},
    "RecoALPPhoton1_theta":    {"name":"RecoALPPhoton1_theta",    "title":"Reco photon_{1} (from ALP) #theta",       "bin":64, "xmin":0,"xmax":3.2},
    "RecoALPPhoton2_theta":    {"name":"RecoALPPhoton2_theta",    "title":"Reco photon_{2} (from ALP) #theta",                     "bin":64, "xmin":0,"xmax":3.2},
    "RecoALPPhoton1_phi":      {"name":"RecoALPPhoton1_phi",      "title":"Reco photon_{1} (from ALP) #phi",         "bin":64, "xmin":-3.2,"xmax":3.2},
    "RecoALPPhoton2_phi":      {"name":"RecoALPPhoton2_phi",      "title":"Reco photon_{2} (from ALP) #phi",                       "bin":64, "xmin":-3.2,"xmax":3.2},
    "RecoALPPhoton1_charge":   {"name":"RecoALPPhoton1_charge",   "title":"Reco photon_{1} (from ALP) charge",       "bin":3, "xmin":-1.5,"xmax":1.5},
    "RecoALPPhoton2_charge":   {"name":"RecoALPPhoton2_charge",   "title":"Reco photon_{2} (from ALP) charge",                     "bin":3, "xmin":-1.5,"xmax":1.5},

    "RecoALPPhotons_deltaEta": {"name":"RecoALPPhotons_deltaEta", "title":"Reco photons (from ALP) #Delta#eta",                   "bin":60, "xmin":-2, "xmax":8},
    "RecoALPPhotons_deltaPhi": {"name":"RecoALPPhotons_deltaPhi", "title":"Reco photons (from ALP) #Delta#phi",                   "bin":60, "xmin":-2, "xmax":8},
    "RecoALPPhotons_deltaR":   {"name":"RecoALPPhotons_deltaR",   "title":"Reco photons (from ALP) #DeltaR",                      "bin":60, "xmin":-3, "xmax":8},
    # "RecoALPPhotons_deltaR2":   {"name":"RecoALPPhotons_deltaR2",   "title":"Reco ALP photons #DeltaR_{2}",                      "bin":60, "xmin":-3, "xmax":8},

    "n_RecoALPPhoton1":        {"name":"n_RecoALPPhoton1",        "title":"Number of reco photon_{1} (from ALP)",    "bin":5, "xmin":-0.5, "xmax":4.5},
    "n_RecoALPPhoton2":        {"name":"n_RecoALPPhoton2",        "title":"Number of reco photon_{2} (from ALP)",    "bin":5, "xmin":-0.5, "xmax":4.5},
    # "RecoALPPhoton1_time":     {"name":"RecoALPPhoton1_time",     "title":"Reco photon_{1} (from ALP) time",         "bin":100, "xmin":0, "xmax":2E-24},
    # "RecoALPPhoton2_time":     {"name":"RecoALPPhoton2_time",     "title":"Reco photon_{2} (from ALP) time",         "bin":100, "xmin":0, "xmax":2E-24},

    
    "Reco_aa_invMass":   {"name":"Reco_aa_invMass",   "title":" Reco photon m_{#gamma#gamma} [GeV]",           "bin":100,"xmin":0, "xmax":100},
    "Reco_aa_p":         {"name":"Reco_aa_p",         "title":"Reco photon p_{#gamma#gamma} [GeV]",           "bin":60,"xmin":0, "xmax":60},

    "RecoALP_aa_invMass":   {"name":"RecoALP_aa_invMass",   "title":"Reco m_{#gamma#gamma} (from ALP) [GeV]",   "bin":100,"xmin":0, "xmax":100},
    "RecoALP_aa_p":   {"name":"RecoALP_aa_p",   "title":"Reco p_{#gamma#gamma} (from ALP) [GeV]",   "bin":60,"xmin":0, "xmax":60},
    "RecoALP_aa_energy": {"name":"RecoALP_aa_energy",   "title":"Reco energy_{#gamma#gamma} (from ALP) [GeV]",   "bin":60,"xmin":0, "xmax":60},

    "n_RecoJets":       {"name":"n_RecoJets",      "title":"Total number of reco jets",         "bin":5,"xmin":-0.5 ,"xmax":4.5},
    "n_RecoPhotons":    {"name":"n_RecoPhotons",   "title":"Total number of reco photons",      "bin":9,"xmin":-0.5 ,"xmax":8.5},
    "n_RecoElectrons":  {"name":"n_RecoElectrons", "title":"Total number of reco electrons",    "bin":7,"xmin":-0.5 ,"xmax":6.5},
    "n_RecoMuons":      {"name":"n_RecoMuons",     "title":"Total number of reco muons",        "bin":5,"xmin":-0.5 ,"xmax":4.5},
    
    # "RecoPhotons": {"name": "RecoPhotons", "title": "Total number of reco photons (all events combined)", "bin":8, "xmin":0, "xmax":8},


    # "RecoJet_e":        {"name":"RecoJet_e",        "title":"Reco jet energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    # "RecoJet_p":        {"name":"RecoJet_p",        "title":"Reco jet p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    # "RecoJet_pt":       {"name":"RecoJet_pt",       "title":"Reco jet p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    # "RecoJet_pz":       {"name":"RecoJet_pz",       "title":"Reco jet p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    # "RecoJet_eta":      {"name":"RecoJet_eta",      "title":"Reco jet #eta",         "bin":60, "xmin":-3,"xmax":3},
    # "RecoJet_theta":    {"name":"RecoJet_theta",    "title":"Reco jet #theta",       "bin":64, "xmin":0,"xmax":3.2},
    # "RecoJet_phi":      {"name":"RecoJet_phi",      "title":"Reco jet #phi",         "bin":64, "xmin":-3.2,"xmax":3.2},
    # "RecoJet_charge":   {"name":"RecoJet_charge",   "title":"Reco jet charge",       "bin":3, "xmin":-1.5,"xmax":1.5},

    "RecoElectron_e":        {"name":"RecoElectron_e",        "title":"Reco electron energy [GeV]", "bin":100,"xmin":0 ,"xmax":90},
    "RecoElectron_p":        {"name":"RecoElectron_p",        "title":"Reco electron p [GeV]",      "bin":100,"xmin":0 ,"xmax":90},
    "RecoElectron_pt":       {"name":"RecoElectron_pt",       "title":"Reco electron p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":90},
    "RecoElectron_pz":       {"name":"RecoElectron_pz",       "title":"Reco electron p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":90},
    "RecoElectron_eta":      {"name":"RecoElectron_eta",      "title":"Reco electron #eta",         "bin":60, "xmin":-3,"xmax":3},
    "RecoElectron_theta":    {"name":"RecoElectron_theta",    "title":"Reco electron #theta",       "bin":64, "xmin":0,"xmax":3.2},
    "RecoElectron_phi":      {"name":"RecoElectron_phi",      "title":"Reco electron #phi",         "bin":64, "xmin":-3.2,"xmax":3.2},
    # "RecoElectron_charge":   {"name":"RecoElectron_charge",   "title":"Reco electron charge",       "bin":3, "xmin":-1.5,"xmax":1.5},

    "RecoPhoton_e":        {"name":"RecoPhoton_e",        "title":"Reco photon energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    "RecoPhoton_p":        {"name":"RecoPhoton_p",        "title":"Reco photon p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    "RecoPhoton_pt":       {"name":"RecoPhoton_pt",       "title":"Reco photon p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoPhoton_pz":       {"name":"RecoPhoton_pz",       "title":"Reco photon p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoPhoton_eta":      {"name":"RecoPhoton_eta",      "title":"Reco photon #eta",         "bin":60, "xmin":-3,"xmax":3},
    "RecoPhoton_theta":    {"name":"RecoPhoton_theta",    "title":"Reco photon #theta",       "bin":64, "xmin":0,"xmax":3.2},
    "RecoPhoton_phi":      {"name":"RecoPhoton_phi",      "title":"Reco photon #phi",         "bin":64, "xmin":-3.2,"xmax":3.2},
    "RecoPhoton_charge":   {"name":"RecoPhoton_charge",   "title":"Charge of reco photons",       "bin":3, "xmin":-1.5,"xmax":1.5},

    # "RecoPhoton_y":        {"name":"RecoPhoton_y",        "title":"Reco photon rapidity",     "bin":100, "xmin":-5, "xmax":5},

    "RecoPhotons_delta_eta":{"name": "RecoPhotons_delta_eta", "title": "Reco photons #Delta#eta", "bin":100, "xmin":0, "xmax":10},
    "RecoPhotons_delta_phi":{"name": "RecoPhotons_delta_phi", "title": "Reco photons #Delta#phi", "bin":100, "xmin":0, "xmax":10},
    "RecoPhotons_delta_r":  {"name": "RecoPhotons_delta_r",   "title": "Reco photons #DeltaR",    "bin":100, "xmin":0, "xmax":7},

    "RecoPhotons_min_delta_r": {"name": "RecoPhotons_min_delta_r", "title": "Reco photons minimum #DeltaR", "bin":100, "xmin":0, "xmax": 7},

    # "RecoPhotons_ALP_delta_r":{"name": "RecoPhotons_ALP_delta_r", "title": "Reco photons #DeltaR (from ALP)", "bin":100, "xmin": 0, "xmax": 0.2},
    # "RecoPhotons_ALP_delta_phi":{"name": "RecoPhotons_ALP_delta_phi", "title": "Reco photons #Delta#phi (from ALP)", "bin":100, "xmin": -4, "xmax": 4},
    # "RecoPhotons_ALP_delta_eta":{"name": "RecoPhotons_ALP_delta_eta", "title": "Reco photons #Delta#eta (from ALP)", "bin":100, "xmin": -4, "xmax": 4},

    # "RecoPhoton_reference_point_x": {"name": "RecoPhoton_reference_point_x", "title": "Reco photons reference point x", "bin": 200, "xmin": -100, "xmax": 100},

    "RecoPhoton0_e":       {"name":"RecoPhoton0_e",     "title":"Reco photon_{0} energy [GeV]",     "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton1_e":       {"name":"RecoPhoton1_e",     "title":"Reco photon_{1} energy [GeV]",     "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton2_e":       {"name":"RecoPhoton2_e",     "title":"Reco photon_{2} energy [GeV]",     "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton0_p":       {"name":"RecoPhoton0_p",     "title":"Reco photon_{0} p [GeV]",          "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton1_p":       {"name":"RecoPhoton1_p",     "title":"Reco photon_{1} p [GeV]",          "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton2_p":       {"name":"RecoPhoton2_p",     "title":"Reco photon_{2} p [GeV]",          "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton0_pt":       {"name":"RecoPhoton0_pt",     "title":"Reco photon_{0} p_{T} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton1_pt":       {"name":"RecoPhoton1_pt",     "title":"Reco photon_{1} p_{T} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton2_pt":       {"name":"RecoPhoton2_pt",     "title":"Reco photon_{2} p_{T} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton0_px":       {"name":"RecoPhoton0_px",     "title":"Reco photon_{0} p_{x} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton1_px":       {"name":"RecoPhoton1_px",     "title":"Reco photon_{1} p_{x} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton2_px":       {"name":"RecoPhoton2_px",     "title":"Reco photon_{2} p_{x} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton0_py":       {"name":"RecoPhoton0_py",     "title":"Reco photon_{0} p_{y} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton1_py":       {"name":"RecoPhoton1_py",     "title":"Reco photon_{1} p_{y} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton2_py":       {"name":"RecoPhoton2_py",     "title":"Reco photon_{2} p_{y} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton0_pz":       {"name":"RecoPhoton0_pz",     "title":"Reco photon_{0} p_{z} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton1_pz":       {"name":"RecoPhoton1_pz",     "title":"Reco photon_{1} p_{z} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},
    "RecoPhoton2_pz":       {"name":"RecoPhoton2_pz",     "title":"Reco photon_{2} p_{z} [GeV]",    "bin":100, "xmin":-3.2, "xmax": 50},

    "RecoPhoton1_px_if_RecoPhoton2_px_pos": {"name": "RecoPhoton1_px_if_RecoPhoton2_px_pos", "title": "Reco photon_{1} p_{x} if reco photon_{2} p_{x} > 0", "bin":100, "xmin":-55, "xmax":50},
    "RecoPhoton1_pz_if_RecoPhoton2_pz_pos": {"name": "RecoPhoton1_pz_if_RecoPhoton2_pz_pos", "title": "Reco photon_{1} p_{z} if reco photon_{2} p_{z} > 0", "bin":100, "xmin":-55, "xmax":50},

    "RecoALPPhotons_delta_R3": {"name":"RecoALPPhotons_delta_R3", "title":"Reco ALP photons #DeltaR_{3}", "bin":60, "xmin":-3, "xmax":8},

    # "RecoMuon_e":        {"name":"RecoMuon_e",        "title":"Reco muon energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMuon_p":        {"name":"RecoMuon_p",        "title":"Reco muon p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMuon_pt":       {"name":"RecoMuon_pt",       "title":"Reco muon p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMuon_pz":       {"name":"RecoMuon_pz",       "title":"Reco muon p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMuon_eta":      {"name":"RecoMuon_eta",      "title":"Reco muon #eta",         "bin":60, "xmin":-3,"xmax":3},
    # "RecoMuon_theta":    {"name":"RecoMuon_theta",    "title":"Reco muon #theta",       "bin":64, "xmin":0,"xmax":3.2},
    # "RecoMuon_phi":      {"name":"RecoMuon_phi",      "title":"Reco muon #phi",         "bin":64, "xmin":-3.2,"xmax":3.2},
    # "RecoMuon_charge":   {"name":"RecoMuon_charge",   "title":"Reco muon charge",       "bin":3, "xmin":-1.5,"xmax":1.5},

    # "RecoMissingEnergy_e":       {"name":"RecoMissingEnergy_e",       "title":"Reco Total Missing Energy [GeV]",    "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMissingEnergy_p":       {"name":"RecoMissingEnergy_p",       "title":"Reco Total Missing p [GeV]",         "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMissingEnergy_pt":      {"name":"RecoMissingEnergy_pt",      "title":"Reco Missing p_{T} [GeV]",           "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMissingEnergy_px":      {"name":"RecoMissingEnergy_px",      "title":"Reco Missing p_{x} [GeV]",           "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMissingEnergy_py":      {"name":"RecoMissingEnergy_py",      "title":"Reco Missing p_{y} [GeV]",           "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMissingEnergy_pz":      {"name":"RecoMissingEnergy_pz",      "title":"Reco Missing p_{z} [GeV]",           "bin":100,"xmin":0 ,"xmax":50},
    # "RecoMissingEnergy_eta":     {"name":"RecoMissingEnergy_eta",     "title":"Reco Missing Energy #eta",           "bin":60,"xmin":-3 ,"xmax":3},
    # "RecoMissingEnergy_theta":   {"name":"RecoMissingEnergy_theta",   "title":"Reco Missing Energy #theta",         "bin":64,"xmin":0 , "xmax":3.2},
    # "RecoMissingEnergy_phi":     {"name":"RecoMissingEnergy_phi",     "title":"Reco Missing Energy #phi",           "bin":64,"xmin":-3.2 ,"xmax":3.2},

    # #gen-reco
    "GenMinusRecoALPPhoton1_e":    {"name":"GenMinusRecoALPPhoton1_e",    "title":"Gen photon_{1} energy - Reco photon_{1} energy [GeV]","bin":100,"xmin":-5 ,"xmax":5},
    "GenMinusRecoALPPhoton2_e":    {"name":"GenMinusRecoALPPhoton2_e",    "title":"Gen photon_{2} energy - Reco photon_{2} energy [GeV]",                            "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton1_p":    {"name":"GenMinusRecoALPPhoton1_p",    "title":"Gen photon_{1} p - Reco photon_{1} p [GeV]",          "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton2_p":    {"name":"GenMinusRecoALPPhoton2_p",    "title":"Gen photon_{2} p - Reco photon_{2} p [GeV]",                                      "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton1_pt":   {"name":"GenMinusRecoALPPhoton1_pt",   "title":"Gen photon_{1} p_{T} - Reco photon_{1} p_{T} [GeV]",  "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton2_pt":   {"name":"GenMinusRecoALPPhoton2_pt",   "title":"Gen photon_{2} p_{T} - Reco photon_{2} p_{T} [GeV]",                              "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton1_pz":   {"name":"GenMinusRecoALPPhoton1_pz",   "title":"Gen photon_{1} p_{z} - Reco photon_{1} p_{z} [GeV]",  "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton2_pz":   {"name":"GenMinusRecoALPPhoton2_pz",   "title":"Gen photon_{2} p_{z} - Reco photon_{2} p_{z} [GeV]",                              "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton1_eta":  {"name":"GenMinusRecoALPPhoton1_eta",  "title":"Gen photon_{1} #eta - Reco photon_{1} #eta",          "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton2_eta":  {"name":"GenMinusRecoALPPhoton2_eta",  "title":"Gen photon_{2} #eta - Reco photon_{2} #eta",                                      "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton1_theta":{"name":"GenMinusRecoALPPhoton1_theta","title":"Gen photon_{1} #theta - Reco photon_{1} #theta",      "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton2_theta":{"name":"GenMinusRecoALPPhoton2_theta","title":"Gen photon_{2} #theta - Reco photon_{2} #theta",                                  "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton1_phi":  {"name":"GenMinusRecoALPPhoton1_phi",  "title":"Gen photon_{1} #phi - Reco photon_{1} #phi",          "bin":100,"xmin":-5 ,"xmax":5},
    # "GenMinusRecoALPPhoton2_phi":  {"name":"GenMinusRecoALPPhoton2_phi",  "title":"Gen photon_{2} #phi - Reco photon_{2} #phi",                                      "bin":100,"xmin":-5 ,"xmax":5},

    "GenMinusRecoALP_DecayVertex_x":  {"name":"GenMinusRecoALP_DecayVertex_x",  "title":"Gen ALP decay vertex x - Reco ALP decay vertex x [mm]",              "bin":100,"xmin":-1000 ,"xmax":1000},
    "GenMinusRecoALP_DecayVertex_y":  {"name":"GenMinusRecoALP_DecayVertex_y",  "title":"Gen ALP decay vertex y - Reco ALP decay vertex y [mm]",              "bin":100,"xmin":-1000 ,"xmax":1000},
    "GenMinusRecoALP_DecayVertex_z":  {"name":"GenMinusRecoALP_DecayVertex_z",  "title":"Gen ALP decay vertex z - Reco ALP decay vertex z [mm]",              "bin":100,"xmin":-1000 ,"xmax":1000},

    # "CalorimeterHitsTime":            {"name":"CalorimeterHitsTime",            "title":"Calorimeter hits time",                                              "bin":100,"xmin":0,"xmax":2E-8}



########  obj selection: pt threshold for photons >10GeV, eta<2.5    #######
    "FSGenPhoton_eta_obj_sel_pt_eta":                 {"name":"FSGenPhoton_eta_obj_sel_pt_eta",                "title":"Final state gen photons #eta",               "bin":60, "xmin":-3,"xmax":3},
    "FSGenPhoton_theta_obj_sel_pt_eta":               {"name":"FSGenPhoton_theta_obj_sel_pt_eta",              "title":"Final state gen photons #theta",             "bin":64, "xmin":0,"xmax":3.2},
    "FSGenPhoton_phi_obj_sel_pt_eta":                 {"name":"FSGenPhoton_phi_obj_sel_pt_eta",                "title":"Final state gen photons #phi",               "bin":64, "xmin":-3.2,"xmax":3.2},
    "FSGenPhotons_delta_eta_obj_sel_pt_eta":{"name": "FSGenPhotons_delta_eta_obj_sel_pt_eta", "title": "Final state gen photons #Delta#eta", "bin":100, "xmin":0, "xmax":10},
    "FSGenPhotons_delta_phi_obj_sel_pt_eta":{"name": "FSGenPhotons_delta_phi_obj_sel_pt_eta", "title": "Final state gen photons #Delta#phi", "bin":100, "xmin":0, "xmax":10},
    "FSGenPhotons_delta_r_obj_sel_pt_eta":  {"name": "FSGenPhotons_delta_r_obj_sel_pt_eta",   "title": "Final state gen photons #DeltaR",    "bin":100, "xmin":0, "xmax":7},
    "FSGenPhotons_min_delta_r_obj_sel_pt_eta": {"name": "FSGenPhotons_min_delta_r_obj_sel_pt_eta", "title": "Final state gen photons minimum #DeltaR", "bin":100, "xmin":0, "xmax": 7},
    "FSGenPhoton_pt_obj_sel_pt_eta":                  {"name":"FSGenPhoton_pt_obj_sel_pt_eta",                 "title":"Final state gen photons p_{T} [GeV]",        "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_e_obj_sel_pt_eta":                   {"name":"FSGenPhoton_e_obj_sel_pt_eta",                  "title":"Final state gen photons energy [GeV]",       "bin":100,"xmin":0 ,"xmax":50},
    "FSGenPhoton_p_obj_sel_pt_eta":                   {"name":"FSGenPhoton_p_obj_sel_pt_eta",                  "title":"Final state gen photons p [GeV]",            "bin":100,"xmin":0 ,"xmax":50},
    "n_FSGenPhoton_obj_sel_pt_eta":                   {"name":"n_FSGenPhoton_obj_sel_pt_eta",                  "title":"Number of final state gen photons",          "bin":9,"xmin":-0.5 ,"xmax":8.5},
    "FSGenPhoton_pz_obj_sel_pt_eta":                  {"name":"FSGenPhoton_pz_obj_sel_pt_eta",                 "title":"Final state gen photons p_{z} [GeV]",        "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_e_obj_sel_pt_eta":                  {"name":"FSGenPhoton0_e_obj_sel_pt_eta",                 "title":"Final state gen photon_{0} energy [GeV]",      "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_e_obj_sel_pt_eta":                  {"name":"FSGenPhoton1_e_obj_sel_pt_eta",                 "title":"Final state gen photon_{1} energy [GeV]",      "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_e_obj_sel_pt_eta":                  {"name":"FSGenPhoton2_e_obj_sel_pt_eta",                 "title":"Final state gen photon_{3} energy [GeV]",      "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_p_obj_sel_pt_eta":                  {"name":"FSGenPhoton0_p_obj_sel_pt_eta",                 "title":"Final state gen photon_{0} p [GeV]",           "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_p_obj_sel_pt_eta":                  {"name":"FSGenPhoton1_p_obj_sel_pt_eta",                 "title":"Final state gen photon_{1} p [GeV]",           "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_p_obj_sel_pt_eta":                  {"name":"FSGenPhoton2_p_obj_sel_pt_eta",                 "title":"Final state gen photon_{3} p [GeV]",           "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_pt_obj_sel_pt_eta":                 {"name":"FSGenPhoton0_pt_obj_sel_pt_eta",                "title":"Final state gen photon_{0} p_{T} [GeV]",       "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_pt_obj_sel_pt_eta":                 {"name":"FSGenPhoton1_pt_obj_sel_pt_eta",                "title":"Final state gen photon_{1} p_{T} [GeV]",       "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_pt_obj_sel_pt_eta":                 {"name":"FSGenPhoton2_pt_obj_sel_pt_eta",                "title":"Final state gen photon_{3} p_{T} [GeV]",       "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton0_pz_obj_sel_pt_eta":                 {"name":"FSGenPhoton0_pz_obj_sel_pt_eta",                "title":"Final state gen photon_{0} p_{z} [GeV]",       "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton1_pz_obj_sel_pt_eta":                 {"name":"FSGenPhoton1_pz_obj_sel_pt_eta",                "title":"Final state gen photon_{1} p_{z} [GeV]",       "bin":100,"xmin":-3.2 ,"xmax":50},
    "FSGenPhoton2_pz_obj_sel_pt_eta":                 {"name":"FSGenPhoton2_pz_obj_sel_pt_eta",                "title":"Final state gen photon_{3} p_{z} [GeV]",       "bin":100,"xmin":-3.2 ,"xmax":50},

    "FSGen_aa_invMass_obj_sel_pt_eta":   {"name":"FSGen_aa_invMass_obj_sel_pt_eta",   "title":" Gen photon m_{#gamma#gamma} [GeV]",           "bin":100,"xmin":0, "xmax":100},
    "FSGen_aa_p_obj_sel_pt_eta":         {"name":"FSGen_aa_p_obj_sel_pt_eta",         "title":" Gen photon p_{#gamma#gamma} [GeV]",           "bin":100,"xmin":0, "xmax":100},


    "RecoPhoton_eta_obj_sel_pt_eta":                 {"name":"RecoPhoton_eta_obj_sel_pt_eta",                "title":"Reco photon #eta",               "bin":60, "xmin":-3,"xmax":3},
    "RecoPhoton_theta_obj_sel_pt_eta":    {"name":"RecoPhoton_theta_obj_sel_pt_eta",    "title":"Reco photon #theta",       "bin":64, "xmin":0,"xmax":3.2},
    "RecoPhoton_phi_obj_sel_pt_eta":    {"name":"RecoPhoton_phi_obj_sel_pt_eta",    "title":"Reco photon #phi",       "bin":64, "xmin":-3.2,"xmax":3.2},
    "RecoPhotons_delta_eta_obj_sel_pt_eta":{"name": "RecoPhotons_delta_eta_obj_sel_pt_eta", "title": "Reco photons #Delta#eta", "bin":100, "xmin":0, "xmax":10},
    "RecoPhotons_delta_phi_obj_sel_pt_eta":{"name": "RecoPhotons_delta_phi_obj_sel_pt_eta", "title": "Reco photons #Delta#phi", "bin":100, "xmin":0, "xmax":10},
    "RecoPhotons_delta_r_obj_sel_pt_eta":  {"name": "RecoPhotons_delta_r_obj_sel_pt_eta",   "title": "Reco photons #DeltaR",    "bin":100, "xmin":0, "xmax":7},
    "RecoPhotons_min_delta_r_obj_sel_pt_eta": {"name": "RecoPhotons_min_delta_r_obj_sel_pt_eta", "title": "Reco photons minimum #DeltaR", "bin":100, "xmin":0, "xmax": 7},
    "RecoPhoton_pt_obj_sel_pt_eta":       {"name":"RecoPhoton_pt_obj_sel_pt_eta",       "title":"Reco photon p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoPhoton_e_obj_sel_pt_eta":        {"name":"RecoPhoton_e_obj_sel_pt_eta",        "title":"Reco photon energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    "RecoPhoton_p_obj_sel_pt_eta":        {"name":"RecoPhoton_p_obj_sel_pt_eta",        "title":"Reco photon p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    "n_RecoPhotons_obj_sel_pt_eta":    {"name":"n_RecoPhotons_obj_sel_pt_eta",   "title":"Total number of reco photons",      "bin":9,"xmin":-0.5 ,"xmax":8.5},
    "RecoPhoton_charge_obj_sel_pt_eta":    {"name":"RecoPhoton_charge_obj_sel_pt_eta",   "title":"Charge of reco photons",     "bin":3, "xmin":-1.5,"xmax":1.5},
    "RecoPhoton_pz_obj_sel_pt_eta":       {"name":"RecoPhoton_pz_obj_sel_pt_eta",       "title":"Reco photon p_{z} [GeV]",  "bin":100,"xmin":-3.2 ,"xmax":50},
    "RecoPhoton0_e_obj_sel_pt_eta":       {"name":"RecoPhoton0_e_obj_sel_pt_eta",       "title":"Reco photon_{0} energy [GeV]", "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton1_e_obj_sel_pt_eta":       {"name":"RecoPhoton1_e_obj_sel_pt_eta",       "title":"Reco photon_{1} energy [GeV]", "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton2_e_obj_sel_pt_eta":       {"name":"RecoPhoton2_e_obj_sel_pt_eta",       "title":"Reco photon_{2} energy [GeV]", "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton0_p_obj_sel_pt_eta":       {"name":"RecoPhoton0_p_obj_sel_pt_eta",       "title":"Reco photon_{0} p [GeV]",      "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton1_p_obj_sel_pt_eta":       {"name":"RecoPhoton1_p_obj_sel_pt_eta",       "title":"Reco photon_{1} p [GeV]",      "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton2_p_obj_sel_pt_eta":       {"name":"RecoPhoton2_p_obj_sel_pt_eta",       "title":"Reco photon_{2} p [GeV]",      "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton0_pt_obj_sel_pt_eta":      {"name":"RecoPhoton0_pt_obj_sel_pt_eta",      "title":"Reco photon_{0} p_{T} [GeV]",  "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton1_pt_obj_sel_pt_eta":      {"name":"RecoPhoton1_pt_obj_sel_pt_eta",      "title":"Reco photon_{1} p_{T} [GeV]",  "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton2_pt_obj_sel_pt_eta":      {"name":"RecoPhoton2_pt_obj_sel_pt_eta",      "title":"Reco photon_{2} p_{T} [GeV]",  "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton0_pz_obj_sel_pt_eta":      {"name":"RecoPhoton0_pz_obj_sel_pt_eta",      "title":"Reco photon_{0} p_{z} [GeV]",  "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton1_pz_obj_sel_pt_eta":      {"name":"RecoPhoton1_pz_obj_sel_pt_eta",      "title":"Reco photon_{1} p_{z} [GeV]",  "bin":100,"xmin":-3.2  ,"xmax":50},
    "RecoPhoton2_pz_obj_sel_pt_eta":      {"name":"RecoPhoton2_pz_obj_sel_pt_eta",      "title":"Reco photon_{2} p_{z} [GeV]",  "bin":100,"xmin":-3.2  ,"xmax":50},

    "Reco_aa_invMass_obj_sel_pt_eta":   {"name":"Reco_aa_invMass_obj_sel_pt_eta",   "title":"Reco photon m_{#gamma#gamma} [GeV]",           "bin":100,"xmin":0, "xmax":100},
    "Reco_aa_p_obj_sel_pt_eta":         {"name":"Reco_aa_p_obj_sel_pt_eta",         "title":"Reco photon p_{#gamma#gamma} [GeV]",          "bin":60,"xmin":0, "xmax":60},

    "RecoPhoton_pidx_min_delta_r_obj_sel_pt_eta": {"name":"RecoPhoton_pidx_min_delta_r_obj_sel_pt_eta",   "title":"Reco photon indices of mindeltaR [GeV]",           "bin":15,"xmin":0, "xmax":15},
    "RecoPhoton1_pz_obj_sel_pt_eta_v2": {"name":"RecoPhoton1_pz_obj_sel_pt_eta_v2",   "title":"Reco photon_{1} p_{z} [GeV]",           "bin":100,"xmin":-3.2, "xmax":50},
    "RecoPhoton2_pz_obj_sel_pt_eta_v2": {"name":"RecoPhoton2_pz_obj_sel_pt_eta_v2",   "title":"Reco photon_{2} p_{z} [GeV]",           "bin":100,"xmin":-3.2, "xmax":50},
    "Reco_aa_invMass_obj_sel_pt_eta_v2":{"name":"Reco_aa_invMass_obj_sel_pt_eta_v2",   "title":"Reco photon m_{#gamma#gamma} [GeV]",           "bin":100,"xmin":0, "xmax":100},
    "Reco_aa_p_obj_sel_pt_eta_v2":{"name":"Reco_aa_p_obj_sel_pt_eta_v2",         "title":"Reco photon p_{#gamma#gamma} [GeV]",           "bin":60,"xmin":0, "xmax":60},


    # "verify_deltaR":  {"name": "verify_deltaR",   "title": "Reco photons #DeltaR",    "bin":100, "xmin":0, "xmax":7},

    # #   alp photons with obj sel
    "RecoALPPhoton1_e_obj_sel_pt_eta":        {"name":"RecoALPPhoton1_e_obj_sel_pt_eta",        "title":"Reco photon_{1} (from ALP) energy [GeV]", "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_e_obj_sel_pt_eta":        {"name":"RecoALPPhoton2_e_obj_sel_pt_eta",        "title":"Reco photon_{2} (from ALP) energy [GeV]",               "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_p_obj_sel_pt_eta":        {"name":"RecoALPPhoton1_p_obj_sel_pt_eta",        "title":"Reco photon_{1} (from ALP) p [GeV]",      "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_p_obj_sel_pt_eta":        {"name":"RecoALPPhoton2_p_obj_sel_pt_eta",        "title":"Reco photon_{2} (from ALP) p [GeV]",                    "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_pt_obj_sel_pt_eta":       {"name":"RecoALPPhoton1_pt_obj_sel_pt_eta",       "title":"Reco photon_{1} (from ALP) p_{T} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_pt_obj_sel_pt_eta":       {"name":"RecoALPPhoton2_pt_obj_sel_pt_eta",       "title":"Reco photon_{2} (from ALP) p_{T} [GeV]",                "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_pz_obj_sel_pt_eta":       {"name":"RecoALPPhoton1_pz_obj_sel_pt_eta",       "title":"Reco photon_{1} (from ALP) p_{z} [GeV]",  "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton2_pz_obj_sel_pt_eta":       {"name":"RecoALPPhoton2_pz_obj_sel_pt_eta",       "title":"Reco photon_{2} (from ALP) p_{z} [GeV]",                "bin":100,"xmin":0 ,"xmax":50},
    "RecoALPPhoton1_eta_obj_sel_pt_eta":      {"name":"RecoALPPhoton1_eta_obj_sel_pt_eta",      "title":"Reco photon_{1} (from ALP) #eta",         "bin":60, "xmin":-3,"xmax":3},
    "RecoALPPhoton2_eta_obj_sel_pt_eta":      {"name":"RecoALPPhoton2_eta_obj_sel_pt_eta",      "title":"Reco photon_{2} (from ALP) #eta",                       "bin":60, "xmin":-3,"xmax":3},
    "RecoALPPhoton1_phi_obj_sel_pt_eta":      {"name":"RecoALPPhoton1_phi_obj_sel_pt_eta",      "title":"Reco photon_{1} (from ALP) #phi",         "bin":64, "xmin":-3.2,"xmax":3.2},
    "RecoALPPhoton2_phi_obj_sel_pt_eta":      {"name":"RecoALPPhoton2_phi_obj_sel_pt_eta",      "title":"Reco photon_{2} (from ALP) #phi",                       "bin":64, "xmin":-3.2,"xmax":3.2},
    "RecoALPPhotons_deltaEta_obj_sel_pt_eta": {"name":"RecoALPPhotons_deltaEta_obj_sel_pt_eta", "title":"Reco ALP photons #Delta#eta",                   "bin":60, "xmin":-2, "xmax":8},
    "RecoALPPhotons_deltaPhi_obj_sel_pt_eta": {"name":"RecoALPPhotons_deltaPhi_obj_sel_pt_eta", "title":"Reco ALP photons #Delta#phi",                   "bin":60, "xmin":-2, "xmax":8},
    "RecoALPPhotons_deltaR_obj_sel_pt_eta":   {"name":"RecoALPPhotons_deltaR_obj_sel_pt_eta",   "title":"Reco ALP photons #DeltaR",                      "bin":60, "xmin":-3, "xmax":8},
    "n_RecoALPPhoton1_obj_sel_pt_eta":        {"name":"n_RecoALPPhoton1_obj_sel_pt_eta",        "title":"Number of reco photon_{1} (from ALP)",    "bin":5, "xmin":-0.5, "xmax":4.5},
    "n_RecoALPPhoton2_obj_sel_pt_eta":        {"name":"n_RecoALPPhoton2_obj_sel_pt_eta",        "title":"Number of reco photon_{2} (from ALP)",    "bin":5, "xmin":-0.5, "xmax":4.5},
    "RecoALP_aa_invMass_obj_sel_pt_eta":      {"name":"RecoALP_aa_invMass_obj_sel_pt_eta",      "title":"Reco m_{#gamma #gamma} (from ALP) [GeV]",           "bin":100,"xmin":0, "xmax":100},
    "RecoALP_aa_p_obj_sel_pt_eta":         {"name":"RecoALP_aa_p_obj_sel_pt_eta",         "title":"Reco photon (from ALP) p_{#gamma#gamma} [GeV]",           "bin":100,"xmin":0, "xmax":100},



}
