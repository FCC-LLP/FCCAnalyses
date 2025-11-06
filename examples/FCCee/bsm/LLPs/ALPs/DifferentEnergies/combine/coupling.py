import json
import ROOT
from array import array

# copy cross sections from combine.py
cross_sections = {
    "0p1":   0.02013, 
    "1p0":   0.02013, 
    "5p0":   0.02012, 
    "10p0":  0.02009,
    "25p0":  0.01985, 
    "50p0":  0.01902, 
    "60p0":  0.01855, 
    "70p0":  0.01799,
    "80p0":  0.01737, 
    "90p0":  0.01668,
    "100p0": 0.01589,
    "120p0": 0.01371,
    "140p0": 0.01129,
    "150p0": 0.01015,
    "160p0": 0.009066,
    "180p0": 0.007104,
    "200p0": 0.00537,
    "220p0": 0.003888,
    "230p0": 0.003245,
    "240p0": 0.002667,
    "250p0": 0.002152,
    "300p0": 0.0004664,
    "320p0": 0.0001667,
    "340p0": 0.000008181,
    "350p0": 0.00003077,
    "360p0": 0.000006897
}

additional_scale = 1e-4

with open("tt_sel_limits.json") as f:
    data = json.load(f)

xvals = sorted(data.keys(), key=lambda k: float(k.replace("p", ".")))

xvals_float = [float(x.replace("p", ".")) for x in xvals]
xvals_array = array('d', xvals_float)

def sigma_to_coupling(sig):
    # return (sig / 3.1860) ** (1.0 / 1.8866)
    # return (sig / 2.163e-02) ** 0.5

# Build arrays using the correct float conversion
obs_y = array('d', [sigma_to_coupling(data[x]["obs"]   * cross_sections[x] * additional_scale) for x in xvals])
exp_y = array('d', [sigma_to_coupling(data[x]["exp0"]  * cross_sections[x] * additional_scale) for x in xvals])
exp_m1 = array('d', [sigma_to_coupling(data[x]["exp-1"]* cross_sections[x] * additional_scale) for x in xvals])
exp_p1 = array('d', [sigma_to_coupling(data[x]["exp+1"]* cross_sections[x] * additional_scale) for x in xvals])
exp_m2 = array('d', [sigma_to_coupling(data[x]["exp-2"]* cross_sections[x] * additional_scale) for x in xvals])
exp_p2 = array('d', [sigma_to_coupling(data[x]["exp+2"]* cross_sections[x] * additional_scale) for x in xvals])

n = len(xvals)
gr_obs = ROOT.TGraph(n, xvals_array, obs_y)
gr_exp = ROOT.TGraph(n, xvals_array, exp_y)

# 1σ band
gr_1sigma = ROOT.TGraph(2*n)
for i in range(n):
    gr_1sigma.SetPoint(i, xvals_float[i], exp_p1[i])
    gr_1sigma.SetPoint(2*n - i - 1, xvals_float[i], exp_m1[i])
gr_1sigma.SetFillColor(ROOT.kGreen)
gr_1sigma.SetLineColor(ROOT.kGreen)

# 2σ band
gr_2sigma = ROOT.TGraph(2*n)
for i in range(n):
    gr_2sigma.SetPoint(i, xvals_float[i], exp_p2[i])
    gr_2sigma.SetPoint(2*n - i - 1, xvals_float[i], exp_m2[i])
gr_2sigma.SetFillColor(ROOT.kYellow)
gr_2sigma.SetLineColor(ROOT.kYellow)

c = ROOT.TCanvas("c", "Brazil plot", 800, 600)
gr_2sigma.SetTitle("ALP Limit Plot;Mass [GeV];95% CL Limit on Coupling g")
gr_2sigma.Draw("AF")
gr_2sigma.GetXaxis().SetLimits(0.1, 220)
# gr_2sigma.GetYaxis().SetRangeUser(1e-6, 2e-3) 
gr_1sigma.Draw("F")
gr_exp.SetLineStyle(2)
gr_exp.SetLineColor(ROOT.kBlack)
gr_exp.Draw("L")
gr_obs.SetMarkerStyle(20)
gr_obs.SetMarkerColor(ROOT.kBlack)
gr_obs.Draw("P")

c.SetLogx()
c.SetLogy()

legend = ROOT.TLegend(0.55, 0.20, 0.88, 0.40)
legend.SetBorderSize(0)
legend.SetFillStyle(0)
legend.SetTextSize(0.035)

legend.AddEntry(gr_obs, "Observed", "p")
legend.AddEntry(gr_exp, "Expected", "l")
legend.AddEntry(gr_1sigma, "Expected (68%)", "f")
legend.AddEntry(gr_2sigma, "Expected (95%)", "f")

legend.Draw()

# exclusion limits to be used in final plot
print("\nMass vs Coupling (Observed Exclusion Line):")
print(f"{'Mass [GeV]':>10} | {'Observed g (Exclusion)':>20}")
print("-"*32)
for i in range(n):
    print(f"{xvals_float[i]:10.2f} | {obs_y[i]:20.4e}")

c.Draw()
# change name of plot
c.SaveAs("brazil_plot_coupling.png")