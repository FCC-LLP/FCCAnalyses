import json
import ROOT
from array import array
import argparse

parser = argparse.ArgumentParser(description="Make Brazil plot for different CMEs and selections")
parser.add_argument("--cme", required=True, choices=["zpole", "ww", "zh", "tt"], help="Center-of-mass energy")
parser.add_argument("--sel", required=True, choices=["selNone", "sel"], help="Selection type")
args = parser.parse_args()

cme = args.cme
sel = args.sel

green_hex = "#5CC93B"
yellow_hex = "#F7CE46"

green_color = ROOT.TColor.GetColor(green_hex)
yellow_color = ROOT.TColor.GetColor(yellow_hex)

cross_sections_map = {
    "zpole": {
        "0p1":  2.471, 
        "1p0":  2.471, 
        "5p0":  2.448, 
        "10p0": 2.382,
        "25p0": 1.954, 
        "50p0": 0.8451, 
        "60p0": 0.4505, 
        "70p0": 0.1712,
        "80p0": 0.03019, 
        "90p0": 0.00004286
    },
    "ww": {
        "0p1":   0.02176, 
        "1p0":   0.02175, 
        "5p0":   0.02169, 
        "10p0":  0.0215,
        "25p0":  0.0202, 
        "50p0":  0.01598, 
        "60p0":  0.01381, 
        "70p0":  0.0115,
        "80p0":  0.009178, 
        "90p0":  0.00695,
        "100p0": 0.00491,
        "120p0": 0.001749,
        "140p0": 0.0002533,
        "150p0": 0.00003391
    },
    "zh": {
        "0p1":   0.02048, 
        "1p0":   0.02047, 
        "5p0":   0.02045, 
        "10p0":  0.02037,
        "25p0":  0.01982, 
        "50p0":  0.01792, 
        "60p0":  0.01687, 
        "70p0":  0.01568,
        "80p0":  0.01438, 
        "90p0":  0.01299,
        "100p0": 0.01153,
        "120p0": 0.008291,
        "140p0": 0.005316,
        "150p0": 0.004067,
        "160p0": 0.002998,
        "180p0": 0.001396,
        "200p0": 0.0004547,
        "220p0": 0.00006242,
        "230p0": 0.000008181
    },
    "tt": {
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
}

cross_sections = cross_sections_map[cme]
additional_scale = 1e-4

json_path = f"{cme}_{sel}_limits.json"
with open(json_path) as f:
    data = json.load(f)

xvals = sorted(data.keys(), key=lambda k: float(k.replace("p", ".")))
xvals_array = array('d', [float(x.replace("p", ".")) for x in xvals])

obs_y = array('d', [data[x]["obs"] * cross_sections[x] * additional_scale for x in xvals])
exp_y = array('d', [data[x]["exp0"] * cross_sections[x] * additional_scale for x in xvals])
exp_m1 = array('d', [data[x]["exp-1"] * cross_sections[x] * additional_scale for x in xvals])
exp_p1 = array('d', [data[x]["exp+1"] * cross_sections[x] * additional_scale for x in xvals])
exp_m2 = array('d', [data[x]["exp-2"] * cross_sections[x] * additional_scale for x in xvals])
exp_p2 = array('d', [data[x]["exp+2"] * cross_sections[x] * additional_scale for x in xvals])

n = len(xvals)
gr_obs = ROOT.TGraph(n, xvals_array, obs_y)
gr_exp = ROOT.TGraph(n, xvals_array, exp_y)

# 1σ band
gr_1sigma = ROOT.TGraph(2*n)
for i in range(n):
    gr_1sigma.SetPoint(i, xvals_array[i], exp_p1[i])
    gr_1sigma.SetPoint(2*n - i - 1, xvals_array[i], exp_m1[i])
gr_1sigma.SetFillColor(green_color)
gr_1sigma.SetLineColor(green_color)

# 2σ band
gr_2sigma = ROOT.TGraph(2*n)
for i in range(n):
    gr_2sigma.SetPoint(i, xvals_array[i], exp_p2[i])
    gr_2sigma.SetPoint(2*n - i - 1, xvals_array[i], exp_m2[i])
gr_2sigma.SetFillColor(yellow_color)
gr_2sigma.SetLineColor(yellow_color)

c = ROOT.TCanvas("c", "Brazil plot", 1200, 900)
gr_2sigma.SetTitle(f"ALP Limit Plot ({cme}, {sel});Mass [GeV];95% CL Limit on #sigma [pb]")
gr_2sigma.Draw("AF")
gr_2sigma.GetXaxis().SetLimits(0.1, 220)
gr_2sigma.GetYaxis().SetRangeUser(1e-6, 2e-3) 
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

c.Draw()
c.SaveAs(f"brazil_plot_{cme}_{sel}.png")