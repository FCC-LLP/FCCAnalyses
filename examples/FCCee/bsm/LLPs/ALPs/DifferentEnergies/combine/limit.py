import ROOT
import subprocess
import argparse
import json
import os

#TODO: add tags for cme and selections, clean up

signal_files = {
    #######################################################
    #               CME: 91.188 GeV (Z pole)              #
    #######################################################
    "zpole": {
        # No selections
        "selNone": {
            "0p1":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_0p1_selNone_histo.root",
            "1p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_1p0_selNone_histo.root",
            "5p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_5p0_selNone_histo.root",
            "10p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_10p0_selNone_histo.root",
            "25p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_25p0_selNone_histo.root",
            "50p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_50p0_selNone_histo.root",
            "60p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_60p0_selNone_histo.root",
            "70p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_70p0_selNone_histo.root",
            "80p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_80p0_selNone_histo.root",
            "90p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_90p0_selNone_histo.root",
        },
        # Selection (3 reconstructed photons)
        "sel": {
            "0p1":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_0p1_sel_histo.root",
            "1p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_1p0_sel_histo.root",
            "5p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_5p0_sel_histo.root",
            "10p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_10p0_sel_histo.root",
            "25p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_25p0_sel_histo.root",
            "50p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_50p0_sel_histo.root",
            "60p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_60p0_sel_histo.root",
            "70p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_70p0_sel_histo.root",
            "80p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_80p0_sel_histo.root",
            "90p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/alp_3photons_cme_91p188_malp_90p0_sel_histo.root",
        },
    },
    #######################################################
    #                  CME: 160 GeV (WW)                  #
    #######################################################
    "ww": {
        # No selections
        "selNone": {
            "0p1":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_0p1_selNone_histo.root",
            "1p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_1p0_selNone_histo.root",
            "5p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_5p0_selNone_histo.root",
            "10p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_10p0_selNone_histo.root",
            "25p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_25p0_selNone_histo.root",
            "50p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_50p0_selNone_histo.root",
            "60p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_60p0_selNone_histo.root",
            "70p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_70p0_selNone_histo.root",
            "80p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_80p0_selNone_histo.root",
            "90p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_90p0_selNone_histo.root",
            "100p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_100p0_selNone_histo.root",
            "120p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_120p0_selNone_histo.root",
            "140p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_140p0_selNone_histo.root",
            "150p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_150p0_selNone_histo.root",
        },
        # Selection (3 reconstructed photons)
        "sel": {
            "0p1":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_0p1_sel_histo.root",
            "1p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_1p0_sel_histo.root",
            "5p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_5p0_sel_histo.root",
            "10p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_10p0_sel_histo.root",
            "25p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_25p0_sel_histo.root",
            "50p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_50p0_sel_histo.root",
            "60p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_60p0_sel_histo.root",
            "70p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_70p0_sel_histo.root",
            "80p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_80p0_sel_histo.root",
            "90p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_90p0_sel_histo.root",
            "100p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_100p0_sel_histo.root",
            "120p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_120p0_sel_histo.root",
            "140p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_140p0_sel_histo.root",
            "150p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/alp_3photons_cme_160_malp_150p0_sel_histo.root",
        },
    },
    #######################################################
    #                  CME: 240 GeV (ZH)                  #
    #######################################################
    "zh": {
        # No selections
        "selNone": {
            "0p1":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_0p1_selNone_histo.root",
            "1p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_1p0_selNone_histo.root",
            "5p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_5p0_selNone_histo.root",
            "10p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_10p0_selNone_histo.root",
            "25p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_25p0_selNone_histo.root",
            "50p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_50p0_selNone_histo.root",
            "60p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_60p0_selNone_histo.root",
            "70p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_70p0_selNone_histo.root",
            "80p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_80p0_selNone_histo.root",
            "90p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_90p0_selNone_histo.root",
            "100p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_100p0_selNone_histo.root",
            "120p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_120p0_selNone_histo.root",
            "140p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_140p0_selNone_histo.root",
            "150p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_150p0_selNone_histo.root",
            "160p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_160p0_selNone_histo.root",
            "180p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_180p0_selNone_histo.root",
            "200p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_200p0_selNone_histo.root",
            "220p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_220p0_selNone_histo.root",
            "230p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_230p0_selNone_histo.root",
        },
        # Selection (3 reconstructed photons)
        "sel": {
            "0p1":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_0p1_sel_histo.root",
            "1p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_1p0_sel_histo.root",
            "5p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_5p0_sel_histo.root",
            "10p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_10p0_sel_histo.root",
            "25p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_25p0_sel_histo.root",
            "50p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_50p0_sel_histo.root",
            "60p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_60p0_sel_histo.root",
            "70p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_70p0_sel_histo.root",
            "80p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_80p0_sel_histo.root",
            "90p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_90p0_sel_histo.root",
            "100p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_100p0_sel_histo.root",
            "120p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_120p0_sel_histo.root",
            "140p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_140p0_sel_histo.root",
            "150p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_150p0_sel_histo.root",
            "160p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_160p0_sel_histo.root",
            "180p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_180p0_sel_histo.root",
            "200p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_200p0_sel_histo.root",
            "220p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_220p0_sel_histo.root",
            "230p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/alp_3photons_cme_240_malp_230p0_sel_histo.root",
        },
    },
    #######################################################
    #                  CME: 365 GeV (tt)                  #
    #######################################################
    "tt": {
        # No selections
        "selNone": {
            "0p1":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_0p1_selNone_histo.root",
            "1p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_1p0_selNone_histo.root",
            "5p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_5p0_selNone_histo.root",
            "10p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_10p0_selNone_histo.root",
            "25p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_25p0_selNone_histo.root",
            "50p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_50p0_selNone_histo.root",
            "60p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_60p0_selNone_histo.root",
            "70p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_70p0_selNone_histo.root",
            "80p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_80p0_selNone_histo.root",
            "90p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_90p0_selNone_histo.root",
            "100p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_100p0_selNone_histo.root",
            "120p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_120p0_selNone_histo.root",
            "140p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_140p0_selNone_histo.root",
            "150p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_150p0_selNone_histo.root",
            "160p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_160p0_selNone_histo.root",
            "180p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_180p0_selNone_histo.root",
            "200p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_200p0_selNone_histo.root",
            "220p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_220p0_selNone_histo.root",
            "230p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_230p0_selNone_histo.root",
            "240p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_240p0_selNone_histo.root",
            "250p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_250p0_selNone_histo.root",
            "300p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_300p0_selNone_histo.root",
            "320p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_320p0_selNone_histo.root",
            "340p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_340p0_selNone_histo.root",
            "350p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_350p0_selNone_histo.root",
            "360p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_360p0_selNone_histo.root",
        },
        # Selection (3 reconstructed photons)
        "sel": {
            "0p1":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_0p1_sel_histo.root",
            "1p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_1p0_sel_histo.root",
            "5p0":   "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_5p0_sel_histo.root",
            "10p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_10p0_sel_histo.root",
            "25p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_25p0_sel_histo.root",
            "50p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_50p0_sel_histo.root",
            "60p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_60p0_sel_histo.root",
            "70p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_70p0_sel_histo.root",
            "80p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_80p0_sel_histo.root",
            "90p0":  "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_90p0_sel_histo.root",
            "100p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_100p0_sel_histo.root",
            "120p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_120p0_sel_histo.root",
            "140p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_140p0_sel_histo.root",
            "150p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_150p0_sel_histo.root",
            "160p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_160p0_sel_histo.root",
            "180p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_180p0_sel_histo.root",
            "200p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_200p0_sel_histo.root",
            "220p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_220p0_sel_histo.root",
            "230p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_230p0_sel_histo.root",
            "240p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_240p0_sel_histo.root",
            "250p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_250p0_sel_histo.root",
            "300p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_300p0_sel_histo.root",
            "320p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_320p0_sel_histo.root",
            "340p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_340p0_sel_histo.root",
            "350p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_350p0_sel_histo.root",
            "360p0": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/alp_3photons_cme_365_malp_360p0_sel_histo.root",
        },
    },
}

background_files = {
    #######################################################
    #               CME: 91.188 GeV (Z pole)              #
    #######################################################
    "zpole": {
        "selNone": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/background_3photons_cme_91p188_selNone_histo.root",
        "sel":     "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zpole_samples/background_3photons_cme_91p188_sel_histo.root"
    },
    #######################################################
    #                  CME: 160 GeV (WW)                  #
    #######################################################
    "ww": {
        "selNone": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/background_3photons_cme_160_selNone_histo.root",
        "sel":     "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/ww_samples/background_3photons_cme_160_sel_histo.root"  
    },
    #######################################################
    #                  CME: 240 GeV (ZH)                  #
    #######################################################
    "zh": {
        "selNone": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/background_3photons_cme_240_selNone_histo.root",
        "sel":     "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/zh_samples/background_3photons_cme_240_sel_histo.root"
    },  
    #######################################################
    #                  CME: 365 GeV (tt)                  #
    #######################################################
    "tt": {
        "selNone": "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/background_3photons_cme_365_selNone_histo.root",
        "sel":     "/eos/experiment/fcc/ee/analyses_storage/BSM/LLPs/ALPs_3photons/different_energies/fccanalyses/final/tt_samples/background_3photons_cme_365_sel_histo.root"
    },
}

hist_name = "Reco_aa_invMass"
json_limits = {}

parser = argparse.ArgumentParser(description="Create datacards for a given center-of-mass energy and selection")
parser.add_argument("--cme", required=True, help="center-of-mass, e.g., zpole")
parser.add_argument("--sel", required=True, choices=["selNone", "sel"], help="selection")
args = parser.parse_args()

cme = args.cme
sel = args.sel

if cme not in signal_files:
    raise ValueError(f"CME {cme} not found in signal files")
if sel not in signal_files[cme]:
    raise ValueError(f"Selection {sel} not found for CME {cme}")

sig_dict = signal_files[cme][sel]
bkg_file = background_files[cme][sel]

for mass, sig_path in sig_dict.items():
    output_root = f"./{cme}_{sel}_malp_{mass}_datacard.root"
    datacard_path = f"./{cme}_{sel}_malp_{mass}_datacard.txt"

    sig_file = ROOT.TFile(sig_path, "READ")
    bkg_file_root = ROOT.TFile(bkg_file, "READ")
    out_file = ROOT.TFile(output_root, "RECREATE")

    # get histograms
    sig_hist = sig_file.Get(hist_name)
    if not sig_hist:
        sig_file.ls()
        raise RuntimeError(f"Signal histogram '{hist_name}' not found in {sig_path}")
    sig_hist.Scale(1e-4)
    for i in range(1, sig_hist.GetNbinsX() + 1):
        if sig_hist.GetBinContent(i) == 0:
            sig_hist.SetBinError(i, 1.84)

    bkg_hist = bkg_file_root.Get(hist_name)
    if not bkg_hist:
        bkg_file_root.ls()
        raise RuntimeError(f"Background histogram '{hist_name}' not found in {bkg_file}")

    sig_hist.SetName("signal")
    bkg_hist.SetName("background")
    data_hist = bkg_hist.Clone("data_obs")
    integral = data_hist.Integral()

    # write histograms
    out_file.cd()
    sig_hist.Write()
    bkg_hist.Write()
    data_hist.Write()
    out_file.Close()

    # create datacard
    with open(datacard_path, "w") as f:
        f.write("# Datacard for combined histograms\n")
        f.write("imax 1  number of channels\n")
        f.write("jmax 1  number of backgrounds\n")
        f.write("kmax *  number of nuisance parameters\n")
        f.write(f"shapes * * {output_root} $PROCESS $PROCESS_$SYSTEMATIC\n")
        f.write("------------\n")
        f.write("bin bin1\n")
        f.write(f"observation {integral}\n")
        f.write("------------\n")
        f.write("bin bin1 bin1\n")
        f.write("process signal background\n")
        f.write("process 0 1\n")
        f.write(f"rate {sig_hist.Integral()} {bkg_hist.Integral()}\n")
        f.write("------------\n")

    sig_file.Close()
    bkg_file_root.Close()
    out_file.Close()

    # run combine
    combine_cmd = ["combine", "-M", "AsymptoticLimits", datacard_path]
    result = subprocess.run(combine_cmd, capture_output=True, text=True)
    output_text = result.stdout

    # parse limits
    exp0 = exp_m1 = exp_p1 = exp_m2 = exp_p2 = obs = None
    for line in output_text.split("\n"):
        if "Expected 50.0%" in line: exp0 = float(line.split()[-1])
        elif "Expected 16.0%" in line: exp_m1 = float(line.split()[-1])
        elif "Expected 84.0%" in line: exp_p1 = float(line.split()[-1])
        elif "Expected  2.5%" in line: exp_m2 = float(line.split()[-1])
        elif "Expected 97.5%" in line: exp_p2 = float(line.split()[-1])
        elif "Observed Limit:" in line: obs = float(line.split()[-1])

    json_limits[mass] = {
        k: v if v is not None else 0
        for k, v in {
            "exp-2": exp_m2,
            "exp-1": exp_m1,
            "exp0": exp0,
            "exp+1": exp_p1,
            "exp+2": exp_p2,
            "obs": obs
        }.items()
    }

json_path = f"./{cme}_{sel}_limits.json"

with open(json_path, "w") as f:
    json.dump(json_limits, f, indent=2)

print(f"All limits saved to {json_path}")