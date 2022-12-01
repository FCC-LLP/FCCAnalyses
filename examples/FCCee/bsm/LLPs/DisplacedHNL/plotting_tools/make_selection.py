import ROOT
input_path = "/afs/cern.ch/user/d/dimoulin/FCCAnalyses_new/Analysis/outputs/HNL_Majorana_20GeV_1e-3Ve_jets_n50000/output_finalSel/HNL_Majorana_20GeV_1e-3Ve_jets_n50000_selNone_histo.root"
output_file = "histMajorana_ejj_Select.root"

hist_file = ROOT.TFile.Open(input_path)
#hist_file = ROOT.TFile.Open("../outputs/HNL_Majorana_20GeV_1e-3Ve/HNL_Majorana_20GeV_1e-3Ve_jets_selNone_histo.root")
histSelect = ROOT.TFile.Open(output_file, "RECREATE")

#Object variables
histSelect.WriteObject(hist_file.Get("RecoElectron_pt"), "RecoElectron_pt")
histSelect.WriteObject(hist_file.Get("RecoElectron_phi"), "RecoElectron_phi")
histSelect.WriteObject(hist_file.Get("RecoElectron_theta"), "RecoElectron_theta")
histSelect.WriteObject(hist_file.Get("RecoElectron_e"), "RecoElectron_e")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_e"), "RecoMissingEnergy_e")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_p"), "RecoMissingEnergy_p")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_pt"), "RecoMissingEnergy_pt")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_px"), "RecoMissingEnergy_px")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_py"), "RecoMissingEnergy_py")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_pz"), "RecoMissingEnergy_pz")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_eta"), "RecoMissingEnergy_eta")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_theta"), "RecoMissingEnergy_theta")
histSelect.WriteObject(hist_file.Get("RecoMissingEnergy_phi"), "RecoMissingEnergy_phi")

# Jet variables 
histSelect.WriteObject(hist_file.Get("n_RecoJets"), "n_RecoJets")
histSelect.WriteObject(hist_file.Get("RecoJet_e"), "RecoJet_e")
histSelect.WriteObject(hist_file.Get("RecoJet_p"), "RecoJet_p")
histSelect.WriteObject(hist_file.Get("RecoJet_pt"), "RecoJet_pt")
histSelect.WriteObject(hist_file.Get("RecoJet_pz"), "RecoJet_pz")
histSelect.WriteObject(hist_file.Get("RecoJet_eta"), "RecoJet_eta")
histSelect.WriteObject(hist_file.Get("RecoJet_theta"), "RecoJet_theta")
histSelect.WriteObject(hist_file.Get("RecoJet_phi"), "RecoJet_phi")
histSelect.WriteObject(hist_file.Get("RecoJet_charge"), "RecoJet_charge")
histSelect.WriteObject(hist_file.Get("RecoJetTrack_absD0"), "RecoJetTrack_absD0")
histSelect.WriteObject(hist_file.Get("RecoJetTrack_absZ0"), "RecoJetTrack_absZ0")
histSelect.WriteObject(hist_file.Get("RecoJetTrack_absD0sig"), "RecoJetTrack_absD0sig")
histSelect.WriteObject(hist_file.Get("RecoJetTrack_absZ0sig"), "RecoJetTrack_absZ0sig")
histSelect.WriteObject(hist_file.Get("RecoJetTrack_D0cov"), "RecoJetTrack_D0cov")
histSelect.WriteObject(hist_file.Get("RecoJetTrack_Z0cov"), "RecoJetTrack_Z0cov")
#histSelect.WriteObject(hist_file.Get(""), "")
















