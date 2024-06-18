from ROOT import TFile, gDirectory, TH1D, TCanvas, TMath

myfile = TFile('ALP_Z_aa_1GeV_cYY_0p5_sel0_histo.root')

mychain = gDirectory.Get('FSGenPhoton_eta')
entries = mychain.GetEntriesFast()

# Setup:
eta_hist = TH1D("eta", "eta histogram", 100, -3, 3)
eta_hist.GetXaxis().SetTitle("Final state gen photons eta")
eta_hist.GetYaxis().SetTitle("events")

for jentry in range(entries):
    ientry = mychain.LoadTree(jentry)
    if ientry < 0:
        break
    nb = mychain.GetEntry(jentry)
    if nb <= 0:
        continue

    # Loop:
    eta = mychain.eta
    eta_hist.Fill(eta)

# Wrap-up:
eta_hist.Draw("e")

kill = input("q to exit: ")
