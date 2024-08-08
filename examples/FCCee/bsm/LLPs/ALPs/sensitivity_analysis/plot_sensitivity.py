import ROOT
import numpy as np
import array
import os
import pandas as pd
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self,ana_text,energy,intLumi,output_dir):
        self.ana_tex = ana_tex
        self.s_tex = "#bf{#it{"+"#sqrt{{s}} = {:.1f} GeV".format(energy)+"}}"
        self.lumi_tex = "#bf{#it{" +"L = {:.0f} ab^{{-1}}".format(intLumi) + "}}"
        self.col_tex = "FCC-ee Simulation (Delphes)"

        if not os.path.exists(output_dir):
                os.mkdir(output_dir)
        self.output_dir = output_dir

    ###   Figure   ###
    def drawFigure(self,mN,Ve,Z,func_text,out_name,histo_name="histo",zrange=[],plot_pred=False):

        #Set bins for the plots
        logBins = 14
        stopBin = 3.38
        # startBin = 0.0000107
        startBin = 0.000000338
        logWidth = []
        for i in range(0,logBins):
            logWidth.append(ROOT.Math.pow(10,ROOT.TMath.Log10(startBin)+((ROOT.TMath.Log10(stopBin)-ROOT.TMath.Log10(startBin))/logBins)*i))
        logArray = array.array('d',logWidth)
        print(logArray)

        # linBins = 10
        # linBins0 = 10
        # linWidth = [0,5,10,20,30,40,50,60,70,80]
        # linWidth0 = np.linspace(0,90,linBins0)
        # linArray = array.array('d', linWidth)
        # linArray0 = array.array('d', linWidth0)

        logBinMass = 8
        stopBinMass = 178
        startBinMass = 0.0178
        logWidthMass = []
        for i in range(0,logBinMass):
            logWidthMass.append(ROOT.Math.pow(10,ROOT.TMath.Log10(startBinMass)+((ROOT.TMath.Log10(stopBinMass)-ROOT.TMath.Log10(startBinMass))/logBinMass)*i))
        logMassArray = array.array('d',logWidthMass)
        print(logMassArray)

        c = ROOT.TCanvas("c_"+histo_name,"canvas title")
        c.cd()
        ROOT.gPad.SetLogx(1)
        ROOT.gPad.SetLogy(1)
        ROOT.gPad.SetLogz(1)
        ROOT.gPad.SetRightMargin(0.2)
        ROOT.gStyle.SetOptStat(0)

        # A base histogram to correctly set the bins
        # h0 = ROOT.TH2F("h0",r";m_{N} [GeV];\left|V_{eN}\right|^{2}", linBins0-1, linArray0, logBins-1, logArray)
        # h0.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        # h0.Draw()

        h = ROOT.TH2F(histo_name,r";m_{a}  [GeV];c_{\gamma\gamma}", logBinMass-1, logMassArray, logBins-1, logArray)
        h.GetZaxis().SetTitle(func_text)
        h.GetZaxis().SetTitleOffset(1.5)
        h.GetXaxis().SetTitleOffset(1.4)
        h.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        for m,v,z in zip(mN,Ve,Z):
            h.Fill(m,v,z)
        if zrange:
            h.SetMinimum(zrange[0])
            h.SetMaximum(zrange[1])
        h.Draw("same COLZ")
        # h.GetXaxis().SetRangeUser(0,31.6)

        ## Print text in figure
        Text = ROOT.TLatex()
        Text.SetNDC()
        Text.SetTextAlign(31)
        Text.SetTextSize(0.04)
        Text.SetTextAlign(12)
        Text.DrawLatex(0.090, 0.92, self.col_tex)
        Text.SetNDC(ROOT.kTRUE)
        Text.SetTextSize(0.04)
        # Text.DrawLatex(0.62, 0.83, func_text)
        Text.DrawLatex(0.48, 0.83, self.s_tex)
        Text.DrawLatex(0.48, 0.78, self.lumi_tex)
        Text.DrawLatex(0.48, 0.73, self.ana_tex)

        # c.Modified()
        # c.Update()

        if (plot_pred):
            x4,y4,x1,y1 = self.get_pred()
            # X = np.power(10,x)
            # Y = np.power(10,y)
            X4 = array.array('d',x4)
            Y4 = array.array('d',y4)
            X1 = array.array('d',x1)
            Y1 = array.array('d',y1)

            c.cd()
            gr4 = ROOT.TGraph(len(X4),X4,Y4)
            gr4.SetLineColor(2)
            gr4.SetLineWidth(2)
            gr4.Draw("same L")
            gr4.GetXaxis().SetRangeUser(0,90)

            gr1 = ROOT.TGraph(len(X1),X1,Y1)
            gr1.SetLineColor(1)
            gr1.SetLineWidth(2)
            gr1.Draw("same L")
            gr1.GetXaxis().SetRangeUser(0,90)

            c.Modified()
            c.Update()

            leg = ROOT.TLegend(0.56,0.13,0.73,0.17)
            leg.SetFillColor(0)
            leg.SetFillStyle(0)
            leg.SetLineColor(0)
            leg.SetShadowColor(10)
            leg.SetTextSize(0.035)
            leg.SetTextFont(42)
            leg.AddEntry(gr1, "Theoretical prediction")
            leg.AddEntry(gr4, "Theoretical prediction")
            leg.Draw()

        leg = ROOT.TLegend(0.14,0.23,0.34,0.37)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetLineColor(1)
        leg.SetShadowColor(0)
        leg.SetTextSize(0.035)
        leg.SetTextFont(42)

        c.Modified()
        c.Update()

        x = array.array('d')
        x.append(0.01)
        # # 3 signal event contour
        # if S:
        #     hS = ROOT.TH2F("hS",r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins-1, linArray, logBins-1, logArray)
        #     hS.GetZaxis().SetTitle(func_text)
        #     hS.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        #     for m,v,s in zip(mN,Ve,S):
        #         hS.Fill(m,v**2,s)
        #     x[0] = 3
        #     hS.SetContour(1,x)
        #     hS.SetLineColor(3)
        #     hS.SetLineWidth(2)
        #     hS.Draw("cont3 C")
            # leg.AddEntry(hS,"3 signal event")
            # Text.SetTextColor(3)
            # Text.DrawLatex(0.67,0.41,"#bf{3 signal event}")

        x[0] = 0.0001
        h1 = h.Clone()
        h1.SetContour(1,x)
        h1.SetLineWidth(3)
        h1.SetLineColor(5)
        # Text.SetTextColor(2)
        # Text.DrawLatex(0.3,0.6,"#bf{s = 0.01}")
        h1.DrawCopy("cont3 C same")
        leg.AddEntry(h1,"s = 0.0001","l")

        x[0] = 0.01
        h2 = h.Clone()
        h2.SetContour(1,x)
        h2.SetLineWidth(3)
        h2.SetLineColor(3)
        # Text.SetTextColor(2)
        # Text.DrawLatex(0.3,0.6,"#bf{s = 0.01}")
        h2.DrawCopy("cont3 C same")
        leg.AddEntry(h2,"s = 0.01","l")

        h22 = h.Clone()
        x[0] = 0.05
        h22.SetContour(1,x)
        h22.SetLineWidth(3)
        h22.SetLineColor(4)
        # Text.SetTextColor(3)
        # Text.DrawLatex(0.3,0.7,"#bf{s = 0.05}")
        h22.DrawCopy("cont3 C same")
        leg.AddEntry(h22,"s = 0.05","l")

        leg.Draw()
        c.Modified()
        c.Update()

        c.SaveAs(os.path.join(self.output_dir, out_name))

    def drawFigureWithNumbers(self,mN,Ve,Z,func_text,out_name,histo_name="histo",zrange=[]):

        #Set bins for the plots
        logBins = 15
        stopBin = 1e-5
        startBin = 1e-12
        logWidth = []
        for i in range(0,logBins):
            logWidth.append(ROOT.Math.pow(10,ROOT.TMath.Log10(startBin)+((ROOT.TMath.Log10(stopBin)-ROOT.TMath.Log10(startBin))/logBins)*i))
        logArray = array.array('d',logWidth)

        linBins = 10
        linBins0 = 10
        linWidth = [0,5,10,20,30,40,50,60,70,80]
        linWidth0 = np.linspace(0,90,linBins0)
        linArray = array.array('d', linWidth)
        linArray0 = array.array('d', linWidth0)

        c = ROOT.TCanvas("c_"+histo_name,"canvas title")
        c.cd()
        # ROOT.gPad.SetLogx(1)
        ROOT.gPad.SetLogy(1)
        ROOT.gPad.SetLogz(1)
        ROOT.gPad.SetRightMargin(0.15)
        ROOT.gStyle.SetOptStat(0)

        # A base histogram to correctly set the bins
        h0 = ROOT.TH2F("h0",r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins0-1, linArray0, logBins-1, logArray)
        h0.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        h0.Draw()

        h = ROOT.TH2F(histo_name,r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins-1, linArray, logBins-1, logArray)
        h.GetZaxis().SetTitle(func_text)
        h.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        for m,v,z in zip(mN,Ve,Z):
            h.Fill(m,v**2,z)
        h.Draw("same COLZ text")
        h.GetXaxis().SetRangeUser(0,90)

        ## Print text in figure
        Text = ROOT.TLatex()
        Text.SetNDC()
        Text.SetTextAlign(31)
        Text.SetTextSize(0.04)
        Text.SetTextAlign(12)
        Text.DrawLatex(0.090, 0.92, self.col_tex)
        Text.SetNDC(ROOT.kTRUE)
        Text.SetTextSize(0.04)
        # Text.DrawLatex(0.62, 0.83, func_text)
        Text.DrawLatex(0.56, 0.83, self.s_tex)
        Text.DrawLatex(0.56, 0.78, self.lumi_tex)
        Text.DrawLatex(0.56, 0.73, self.ana_tex)

        c.Modified()
        c.Update()

        c.SaveAs(os.path.join(self.output_dir, out_name))

    def drawFigureWithLimit(self,mN,Ve,Z,func_text,out_name,S=[],histo_name="histo",zrange=[],plot_pred=False):

        #Set bins for the plots
        logBins = 15
        stopBin = 1e-5
        startBin = 1e-12
        logWidth = []
        for i in range(0,logBins):
            logWidth.append(ROOT.Math.pow(10,ROOT.TMath.Log10(startBin)+((ROOT.TMath.Log10(stopBin)-ROOT.TMath.Log10(startBin))/logBins)*i))
        logArray = array.array('d',logWidth)

        linBins = 11
        linBins0 = 10
        linWidth = [0,5,10,20,30,40,50,60,70,80,90]
        linWidth0 = np.linspace(0,90,linBins0)
        linArray = array.array('d', linWidth)
        linArray0 = array.array('d', linWidth0)

        c = ROOT.TCanvas("c_"+histo_name,"canvas title")
        c.cd()
        # ROOT.gPad.SetLogx(1)
        ROOT.gPad.SetLogy(1)
        ROOT.gPad.SetLogz(1)
        ROOT.gPad.SetRightMargin(0.15)
        ROOT.gStyle.SetOptStat(0)

        # A base histogram to correctly set the bins
        h0 = ROOT.TH2F("h0",r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins0-1, linArray0, logBins-1, logArray)
        h0.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        h0.Draw()

        h = ROOT.TH2F(histo_name,r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins-1, linArray, logBins-1, logArray)
        h.GetZaxis().SetTitle(func_text)
        h.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        for m,v,z in zip(mN,Ve,Z):
            h.Fill(m,v**2,z)
        # h.Draw("same COLZ text")
        # h.DrawCopy("same COLZ")
        h.GetXaxis().SetRangeUser(0,90)

        ## Print text in figure
        Text = ROOT.TLatex()
        Text.SetNDC()
        Text.SetTextAlign(31)
        Text.SetTextSize(0.04)
        Text.SetTextAlign(12)
        Text.DrawLatex(0.090, 0.92, self.col_tex)
        Text.SetNDC(ROOT.kTRUE)
        Text.SetTextSize(0.04)
        # Text.DrawLatex(0.62, 0.83, func_text)
        # Text.DrawLatex(0.56, 0.83, self.s_tex)
        # Text.DrawLatex(0.56, 0.78, self.lumi_tex)
        # Text.DrawLatex(0.56, 0.73, self.ana_tex)

        leg = ROOT.TLegend(0.28,0.73,0.63,0.87)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetLineColor(0)
        leg.SetShadowColor(10)
        leg.SetTextSize(0.035)
        leg.SetTextFont(42)

        c.Modified()
        c.Update()

        if (plot_pred):
            x4,y4,x1,y1 = self.get_pred()
            # X = np.power(10,x)
            # Y = np.power(10,y)
            X4 = array.array('d',x4)
            Y4 = array.array('d',y4)
            X1 = array.array('d',x1)
            Y1 = array.array('d',y1)

            c.cd()
            gr4 = ROOT.TGraph(len(X4),X4,Y4)
            gr4.SetLineColor(3)
            gr4.SetLineWidth(3)
            gr4.Draw("same L")
            gr4.GetXaxis().SetRangeUser(0,90)

            gr1 = ROOT.TGraph(len(X1),X1,Y1)
            gr1.SetLineColor(3)
            gr1.SetLineWidth(3)
            gr1.SetLineStyle(7)
            gr1.Draw("same L")
            gr1.GetXaxis().SetRangeUser(0,90)

            c.Modified()
            c.Update()

            leg.AddEntry(gr1, "Prediction","l")
            leg.AddEntry(gr4, "Prediction","l")
            # leg.Draw()
            # Text.SetTextColor(2)
            # Text.SetTextSize(0.04)
            # Text.DrawLatex(0.67,0.32,"#bf{Prediction}")

        x = array.array('d')
        x.append(0.01)
        # # 3 signal event contour
        # if S:
        #     hS = ROOT.TH2F("hS",r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins-1, linArray, logBins-1, logArray)
        #     hS.GetZaxis().SetTitle(func_text)
        #     hS.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        #     for m,v,s in zip(mN,Ve,S):
        #         hS.Fill(m,v**2,s)
        #     x[0] = 3
        #     hS.SetContour(1,x)
        #     hS.SetLineColor(3)
        #     hS.SetLineWidth(2)
        #     hS.Draw("cont3 C")
            # leg.AddEntry(hS,"3 signal event")
            # Text.SetTextColor(3)
            # Text.DrawLatex(0.67,0.41,"#bf{3 signal event}")

        x[0] = 0.01
        h.SetContour(1,x)
        h.SetLineWidth(3)
        h.SetLineColor(5)
        # Text.SetTextColor(2)
        # Text.DrawLatex(0.3,0.6,"#bf{s = 0.01}")
        # h.DrawCopy("cont3 C same")
        leg.AddEntry(h,"s = 0.01","l")
        h22 = h.Clone()
        x[0] = 0.05
        h22.SetContour(1,x)
        h.SetLineWidth(3)
        h22.SetLineColor(4)
        # Text.SetTextColor(3)
        # Text.DrawLatex(0.3,0.7,"#bf{s = 0.05}")
        # h22.DrawCopy("cont3 C same")
        leg.AddEntry(h22,"s = 0.05","l")

        leg.Draw()
        c.Modified()
        c.Update()

        c.SaveAs(os.path.join(self.output_dir, out_name))

    def drawFigureWithLimitZoom(self,mN,Ve,Z,func_text,out_name,S=[],histo_name="histo",zrange=[],plot_pred=False):

        #Set bins for the plots
        logBins = 10
        stopBin = 2.9e-7
        startBin = 2e-12
        logWidth = []
        for i in range(0,logBins):
            logWidth.append(ROOT.Math.pow(10,ROOT.TMath.Log10(startBin)+((ROOT.TMath.Log10(stopBin)-ROOT.TMath.Log10(startBin))/logBins)*i))
        logArray = array.array('d',logWidth)

        linBins = 9
        linBins0 = 10
        linWidth = [5,10,20,30,40,50,60,70,80]
        linWidth0 = np.linspace(0,80,linBins0)
        linArray = array.array('d', linWidth)
        linArray0 = array.array('d', linWidth0)

        c = ROOT.TCanvas("c_"+histo_name,"canvas title",360,250)
        c.cd()
        # ROOT.gPad.SetLogx(1)
        ROOT.gPad.SetLogy(1)
        ROOT.gPad.SetLogz(1)
        ROOT.gPad.SetRightMargin(0.3)
        ROOT.gStyle.SetOptStat(0)

        # A base histogram to correctly set the bins
        # h0 = ROOT.TH2F("h0",r";m_{N};\left|V_{eN}\right|^{2}", linBins0-1, linArray0, logBins-1, logArray)
        # h0.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        # h0.Draw()

        h = ROOT.TH2F(histo_name,r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins-1, linArray, logBins-1, logArray)
        h.GetZaxis().SetTitle(func_text)
        h.GetZaxis().SetRangeUser(zrange[0],zrange[1])
        for m,v,z in zip(mN,Ve,Z):
            h.Fill(m,v**2,z)
        h.DrawCopy("COLZ")
        h.GetXaxis().SetRangeUser(0,90)

        ## Print text in figure
        Text = ROOT.TLatex()
        Text.SetNDC()
        Text.SetTextAlign(31)
        Text.SetTextSize(0.04)
        Text.SetTextAlign(12)
        Text.DrawLatex(0.090, 0.92, self.col_tex)
        Text.SetNDC(ROOT.kTRUE)
        Text.SetTextSize(0.04)
        # Text.DrawLatex(0.62, 0.83, func_text)
        # Text.DrawLatex(0.47, 0.86, self.s_tex)
        # Text.DrawLatex(0.47, 0.81, self.lumi_tex)
        # Text.DrawLatex(0.47, 0.76, self.ana_tex)

        x = array.array('d')
        x.append(0.01)

        # 3 signal event contour
        if S:
            hS = ROOT.TH2F("hS",r";m_{N}  [GeV];\left|V_{eN}\right|^{2}", linBins-1, linArray, logBins-1, logArray)
            hS.GetZaxis().SetTitle(func_text)
            hS.GetZaxis().SetRangeUser(zrange[0],zrange[1])
            for m,v,s in zip(mN,Ve,S):
                hS.Fill(m,v**2,s)
            x[0] = 1
            hS.SetContour(1,x)
            hS.SetLineColor(2)
            hS.SetLineWidth(2)
            hS.Draw("cont3 same")
            Text.SetTextColor(3)
            # Text.DrawLatex(0.67,0.41,"#bf{3 signal event}")

        x[0] = 0.01
        h.SetContour(1,x)
        h.SetLineWidth(2)
        h.SetLineColor(5)
        Text.SetTextColor(5)
        # Text.DrawLatex(0.3,0.6,"#bf{s = 0.01}")
        h.DrawCopy("cont3 same")
        x[0] = 0.05
        h.SetContour(1,x)
        h.SetLineColor(4)
        Text.SetTextColor(4)
        # Text.DrawLatex(0.3,0.7,"#bf{s = 0.05}")
        h.DrawCopy("cont3 same")
        x[0] = 0.5
        h.SetContour(1,x)
        h.SetLineColor(4)
        # Text.SetTextColor(4)
        # Text.DrawLatex(0.3,0.6,"#bf{s = 0.5}")
        h.DrawCopy("cont3 same")

        if (plot_pred):
            x4,y4,x1,y1 = self.get_pred()
            # X = np.power(10,x)
            # Y = np.power(10,y)
            X4 = array.array('d',x4)
            Y4 = array.array('d',y4)
            X1 = array.array('d',x1)
            Y1 = array.array('d',y1)

            c.cd()
            gr4 = ROOT.TGraph(len(X4),X4,Y4)
            gr4.SetLineColor(3)
            gr4.SetLineWidth(2)
            gr4.Draw("same L")
            gr4.GetXaxis().SetRangeUser(0,90)

            gr1 = ROOT.TGraph(len(X1),X1,Y1)
            gr1.SetLineColor(3)
            gr1.SetLineWidth(2)
            gr1.SetLineStyle(7)
            gr1.Draw("same L")
            gr1.GetXaxis().SetRangeUser(0,90)

            c.Modified()
            c.Update()

            # leg = ROOT.TLegend(0.56,0.13,0.73,0.17)
            # leg.SetFillColor(0)
            # leg.SetFillStyle(0)
            # leg.SetLineColor(0)
            # leg.SetShadowColor(10)
            # leg.SetTextSize(0.035)
            # leg.SetTextFont(42)
            # leg.AddEntry(gr, "Theoretical prediction")
            # leg.Draw()
            Text.SetTextColor(2)
            Text.SetTextSize(0.04)
            # Text.DrawLatex(0.67,0.32,"#bf{Prediction}")

        c.Modified()
        c.Update()

        c.SaveAs(os.path.join(self.output_dir, out_name))


    ###   returns S/sqrt(S+B)   ###
    def func1(self,S,B):
        ret = []
        for s in S:
            if s == 0:
                ret.append(0)
                # print(0)
            else:
                ret.append(s/ROOT.Math.sqrt(s+B))
                # print(s/ROOT.Math.sqrt(s+B))
        return ret

    ###   returns S/sqrt(S+B+DeltaB)   ###
    def func2(self,S,B,DeltaB):
        ret = []
        for s in S:
            if s == 0:
                ret.append(0)
                # print(0)
            else:
                ret.append(s/ROOT.Math.sqrt(s+B+DeltaB))
                # print(s/ROOT.Math.sqrt(s+B+DeltaB))
        return ret

    ###   returns S/sqrt(B+DeltaB)   ###
    def func3(self,S,B,DeltaB):
        ret = []
        for s in S:
            ret.append(s/ROOT.Math.sqrt(B+DeltaB))
        return ret

    ###   returns decay length approximation   ###
    def func_L(self,mN,Ve):
        ret = []
        for m,v in zip(mN,Ve):
            ret.append(25*((1e-6/v)**2)*(np.power((100/m),5)))
        return ret


    ##   Print tabular with all values   ###
    def saveTab(self,mN,Ve,S,Z,name1,Z2,name2):
        f = open("sensitivityTabular.txt","w")
        print('\n\n\n\\begin{table}[H] \n    \\centering \n    \\begin{tabular}{|c|c|c|c|c|} \hline \n        $m_N$ & $|V_{eN}|^2$ & S & $',name1,'$ & $',name2,'$ \\\\ \\hline',file=f)
        for m,v,s,z,z2 in zip(mN,Ve,S,Z,Z2):
            print(f'        {m} & {v**2:.2e} & {s:.3f} & {z:.3f} & {z2:.2e}\\\\', file=f)
        print('        \\hline \n    \\end{tabular} \n    \\caption{Caption} \n    \\label{tab:my_label} \n\\end{table}', file=f)
        f.close()

    def get_pred(self):
        # X: log(mN/GeV)
        # pred_data = pd.read_csv("/afs/cern.ch/user/l/lrygaard/public/FCC_ee_data.csv",header=None, sep=",", names = ["X", "Y"])
        pred_data4 = pd.read_csv("HNLe-FCC-ee-IDEA-4-events.csv",header=None, sep='\t', names = ["X", "Y"])
        pred_data1 = pd.read_csv("HNLe-FCC-ee-IDEA-1-event.csv",header=None, sep='\t', names = ["X", "Y"])
        x4, y4, x1, y1 = [], [], [], []
        for i in range(len(pred_data4.index)):
            x4.append(pred_data4.iloc[i]['X'])
            y4.append(pred_data4.iloc[i]['Y'])

        for i in range(len(pred_data1.index)):
            x1.append(pred_data1.iloc[i]['X'])
            y1.append(pred_data1.iloc[i]['Y'])

        return x4,y4,x1,y1


if __name__=="__main__":

    ana_tex        = 'e^{+}e^{-} #rightarrow Z #rightarrow #gamma ALP #rightarrow 3#gamma'
    collider       = 'FCC-ee'
    energy         = 91
    intLumi        = 150

    output_dir = "plots_sensitivity/"
    plotting = Plotting(ana_tex,energy,intLumi,output_dir)

    ###   Values   ###
    # B = 0
    # DeltaB = 3.88e+07 + 7.55e+07 + 6.83e+07 + 1.92e+07 + 2.79e+07

    # Background #
    # Ztautau + Zee + Zbb + Zcc + Zuds
    # B = 6.64e+04 + 0 + 1.72e+03 + 0 + 0
    B = 0.00e+00 + 7.16e+06 + 1.39e+03
    DeltaB = 3.84e+04 + 3.94e+06 + 1.72e+03 + 1.23e+03 + 2.79e+03

    B_d0cut = 7.47e+06 + 0 + 1.72e+03 + 0 + 0
    print("DeltaB: ", DeltaB)

    # Signal #
    # mN = [5, 5, 5, 5, 5, 5, 5, 5, 5,
    # 10, 10, 10, 10, 10, 10, 10, 10, 10,
    # 20, 20, 20, 20, 20, 20, 20, 20, 20,
    # 30, 30, 30, 30, 30, 30, 30, 30, 30,
    # 40, 40, 40, 40, 40, 40, 40, 40, 40,
    # 50, 50, 50, 50, 50, 50, 50, 50, 50,
    # 60, 60, 60, 60, 60, 60, 60, 60, 60,
    # 70, 70, 70, 70, 70, 70, 70, 70, 70]
    mN = [0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316, 0.0316,
          0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
          0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316, 0.316,
          1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
          3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16, 3.16,
          10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,
          31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6, 31.6]
    # Ve = [2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6,
    # 2e-4, 1e-4, 5e-5, 3e-5, 2e-5, 1e-5, 6e-6, 3e-6, 2e-6]
    Ve = [0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6,
          0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6,
          0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6,
          0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6,
          0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6,
          0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6,
          0.0000006, 0.0000019, 0.000006, 0.000019, 0.00006, 0.00019, 0.0006, 0.0019, 0.006, 0.019, 0.06, 0.19, 0.6]

    # S =  [2.19e+01, 2.36e+00, 1.04e-01, 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06,
    # 8.92e+02, 1.84e+02, 1.87e+01, 2.09e+00, 4.51e-01, 3.71e-02, 3.37e-03, 2.17e-04, 5.07e-05,
    # 6.56e+02, 2.71e+02, 8.15e+01, 3.12e+01, 1.38e+01, 2.39e+00, 3.31e-01, 2.33e-02, 4.83e-03,
    # 3.38e+01, 8.66e+01, 5.20e+01, 2.50e+01, 1.24e+01, 3.39e+00, 1.24e+00, 1.91e-01, 4.87e-02,
    # 3.43e-02, 3.44e+00, 1.37e+01, 1.21e+01, 7.75e+00, 2.63e+00, 1.04e+00, 2.68e-01, 1.12e-01,
    # 1.00e-06, 1.00e-06, 5.36e-01, 2.20e+00, 2.67e+00, 1.56e+00, 7.29e-01, 2.12e-01, 8.93e-02,
    # 1.00e-06, 1.00e-06, 1.00e-06, 2.00e-02, 2.30e-01, 5.02e-01, 3.52e-01, 1.32e-01, 6.43e-02,
    # 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06, 4.75e-04, 5.80e-01, 7.03e-02, 5.23e-02, 3.12e-02]
    # S = [0.00e+00, 5.45e-08, 9.27e+00, 6.90e+03,
    #      3.07e-03, 4.61e+00, 4.26e+00, 1.08e+04,
    #      3.30e-02, 3.30e+00, 3.12e+02, 9.03e+03]

# Keeping the bottom left corner weirdness:
    # S = [2.22e-02, 2.19e-01, 2.05e+00, 2.06e+01, 2.17e+02, 0.00e+00, 0.00e+00, 1.46e+00, 1.34e+04, 9.17e+05,
    #      5.95e-02, 5.94e-01, 5.95e+00, 0.00e+00, 0.00e+00, 1.46e-04, 2.08e+02, 2.48e+04, 2.01e+06, 5.39e+07,
    #      1.15e-01, 1.15e+00, 0.00e+00, 2.96e-02, 4.15e+00, 5.59e+02, 4.61e+04, 1.09e+06, 1.15e+07, 1.15e+08,
    #      0.00e+00, 8.87e-04, 6.38e-02, 8.21e+00, 6.35e+02, 1.23e+04, 1.24e+05, 1.23e+06, 1.24e+07, 1.23e+08,
    #      8.72e-04, 9.63e-02, 6.60e+00, 1.21e+02, 1.20e+03, 1.20e+04, 1.21e+05, 1.20e+06, 1.21e+07, 1.20e+08,
    #      5.94e-02, 9.45e-01, 8.92e+00, 8.82e+01, 8.86e+02, 8.85e+03, 8.87e+04, 8.84e+05, 8.83e+06, 8.82e+07,
    #      3.58e-03, 3.57e-02, 3.54e-01, 3.54e+00, 3.54e+01, 3.60e+02, 3.52e+03, 3.52e+04, 3.58e+05, 3.53e+06]

# Removing the bottom left corner weirdness:
    S = [0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 1.46e+00, 1.34e+04, 9.17e+05,
         0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 1.46e-04, 2.08e+02, 2.48e+04, 2.01e+06, 5.39e+07,
         0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 2.96e-02, 4.15e+00, 5.59e+02, 4.61e+04, 1.09e+06, 1.15e+07, 1.15e+08,
         0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 8.87e-04, 6.38e-02, 8.21e+00, 6.35e+02, 1.23e+04, 1.24e+05, 1.23e+06, 1.24e+07, 1.23e+08,
         0.00e+00, 0.00e+00, 5.90e-06, 8.72e-04, 9.63e-02, 6.60e+00, 1.21e+02, 1.20e+03, 1.20e+04, 1.21e+05, 1.20e+06, 1.21e+07, 1.20e+08,
         8.56e-08, 1.10e-05, 8.89e-04, 5.94e-02, 9.45e-01, 8.92e+00, 8.82e+01, 8.86e+02, 8.85e+03, 8.87e+04, 8.84e+05, 8.83e+06, 8.82e+07,
         1.81e-07, 1.15e-05, 3.00e-04, 3.58e-03, 3.57e-02, 3.54e-01, 3.54e+00, 3.54e+01, 3.60e+02, 3.52e+03, 3.52e+04, 3.58e+05, 3.53e+06]

    S_d0cut =  [2.19e+01, 2.36e+00, 1.04e-01, 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06,
    8.92e+02, 1.84e+02, 1.87e+01, 2.09e+00, 4.51e-01, 3.71e-02, 3.37e-03, 2.17e-04, 5.07e-05,
    3.48e+00, 2.30e+02, 3.71e+01, 2.10e+01, 1.13e+01, 3.28e+00, 1.22e+00, 1.89e-01, 4.84e-02,
    3.38e+01, 8.66e+01, 5.20e+01, 2.50e+01, 1.24e+01, 3.39e+00, 1.24e+00, 1.91e-01, 4.87e-02,
    3.43e-02, 3.44e+00, 1.37e+01, 1.21e+01, 7.75e+00, 2.63e+00, 1.04e+00, 2.68e-01, 1.12e-01,
    1.00e-06, 1.00e-06, 5.36e-01, 2.20e+00, 2.67e+00, 1.56e+00, 7.29e-01, 2.12e-01, 8.93e-02,
    1.00e-06, 1.00e-06, 1.00e-06, 2.00e-02, 2.30e-01, 5.02e-01, 3.52e-01, 1.32e-01, 6.43e-02,
    1.00e-06, 1.00e-06, 1.00e-06, 1.00e-06, 4.75e-04, 5.80e-01, 7.03e-02, 5.23e-02, 3.12e-02]

    #No selection
    S0 = [2.97e+03, 7.43e+02, 1.86e+02, 6.69e+01, 2.97e+01, 7.43e+00, 2.68e+00, 6.69e-01, 2.97e-01,
    2.53e+03, 6.33e+02, 1.58e+02, 5.70e+01, 2.53e+01, 6.33e+00, 2.28e+00, 5.70e-01, 2.53e-01,
    2.26e+03, 5.65e+02, 1.41e+02, 5.08e+01, 2.26e+01, 5.65e+00, 2.03e+00, 5.08e-01, 2.26e-01,
    2.00e+03, 5.01e+02, 1.25e+02, 4.51e+01, 2.00e+01, 5.01e+00, 1.80e+00, 4.51e-01, 2.00e-01,
    1.71e+03, 4.29e+02, 1.07e+02, 3.86e+01, 1.71e+01, 4.29e+00, 1.54e+00, 3.86e-01, 1.71e-01,
    1.37e+03, 3.42e+02, 8.55e+01, 3.08e+01, 1.37e+01, 3.42e+00, 1.23e+00, 3.08e-01, 1.37e-01,
    9.86e+02, 2.46e+02, 6.16e+01, 2.22e+01, 9.86e+00, 2.46e+00, 8.87e-01, 2.22e-01, 9.86e-02,
    5.94e+02, 1.48e+02, 3.71e+01, 1.34e+01, 5.94e+00, 1.48e+00, 5.35e-01, 1.34e-01, 5.94e-02]

    # 2 reco e
    S1 = [2.42e+01, 2.51e+00, 1.04e-01, 2.67e-03, 1.19e-03, 7.94e-01, 2.82e-01, 7.31e-02, 3.24e-02,
    9.91e+02, 1.98e+02, 2.00e+01, 2.22e+00, 4.86e-01, 3.85e-02, 3.78e-03, 2.39e-04, 5.07e-05,
    1.54e+03, 3.85e+02, 9.63e+01, 3.47e+01, 1.51e+01, 2.58e+00, 3.57e-01, 2.50e-02, 5.23e-03,
    1.54e+03, 3.85e+02, 9.63e+01, 3.47e+01, 1.54e+01, 3.85e+00, 1.38e+00, 2.10e-01, 5.34e-02,
    1.36e+03, 3.39e+02, 8.49e+01, 3.07e+01, 1.36e+01, 3.39e+00, 1.22e+00, 3.00e-01, 1.24e-01,
    1.10e+03, 2.74e+02, 6.87e+01, 2.47e+01, 1.10e+01, 2.75e+00, 9.90e-01, 2.47e-01, 9.92e-02,
    7.88e+02, 1.97e+02, 4.92e+01, 1.78e+01, 7.88e+00, 1.97e+00, 7.11e-01, 1.77e-01, 7.14e-02,
    4.75e+02, 1.19e+02, 2.97e+01, 1.07e+01, 4.75e+00, 1.19e+00, 4.28e-01, 1.07e-01, 4.75e-02]

    # vetoes
    S2 = [2.42e+01, 2.51e+00, 1.04e-01, 2.67e-03, 1.19e-03, 7.88e-01, 2.80e-01, 7.25e-02, 3.21e-02,
    9.81e+02, 1.97e+02, 1.98e+01, 2.20e+00, 4.81e-01, 3.80e-02, 3.78e-03, 2.39e-04, 5.07e-05,
    1.51e+03, 3.78e+02, 9.46e+01, 3.42e+01, 1.48e+01, 2.53e+00, 3.50e-01, 2.47e-02, 5.12e-03,
    1.50e+03, 3.77e+02, 9.42e+01, 3.39e+01, 1.50e+01, 3.76e+00, 1.34e+00, 2.03e-01, 5.18e-02,
    1.32e+03, 3.30e+02, 8.25e+01, 2.98e+01, 1.32e+01, 3.30e+00, 1.19e+00, 2.91e-01, 1.20e-01,
    1.06e+03, 2.66e+02, 6.64e+01, 2.39e+01, 1.06e+01, 2.67e+00, 9.57e-01, 2.39e-01, 9.57e-02,
    7.59e+02, 1.90e+02, 4.74e+01, 1.71e+01, 7.59e+00, 1.90e+00, 6.85e-01, 1.71e-01, 6.89e-02,
    4.56e+02, 1.14e+02, 2.84e+01, 1.02e+01, 4.56e+00, 1.14e+00, 4.11e-01, 1.02e-01, 4.55e-02]

    # missing energy gt 10 GeV
    S3 = [2.23e+01, 2.39e+00, 1.04e-01, 1.34e-03, 5.94e-04, 7.25e-01, 2.59e-01, 6.74e-02, 2.95e-02,
    9.36e+02, 1.88e+02, 1.90e+01, 2.12e+00, 4.56e-01, 3.78e-02, 3.47e-03, 2.39e-04, 5.07e-05,
    1.44e+03, 3.61e+02, 9.02e+01, 3.26e+01, 1.41e+01, 2.41e+00, 3.35e-01, 2.35e-02, 4.89e-03,
    1.42e+03, 3.56e+02, 8.89e+01, 3.20e+01, 1.42e+01, 3.54e+00, 1.27e+00, 1.92e-01, 4.90e-02,
    1.25e+03, 3.12e+02, 7.80e+01, 2.81e+01, 1.25e+01, 3.12e+00, 1.12e+00, 2.75e-01, 1.13e-01,
    1.02e+03, 2.55e+02, 6.39e+01, 2.30e+01, 1.02e+01, 2.56e+00, 9.21e-01, 2.30e-01, 9.06e-02,
    7.40e+02, 1.85e+02, 4.62e+01, 1.67e+01, 7.40e+00, 1.85e+00, 6.68e-01, 1.67e-01, 6.52e-02,
    4.49e+02, 1.12e+02, 2.81e+01, 1.01e+01, 4.49e+00, 1.12e+00, 4.05e-01, 1.01e-01, 4.49e-02]

    # d0 gt 0.5 mm
    S4 =  [2.19e+01, 2.36e+00, 1.04e-01, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00,
    8.92e+02, 1.84e+02, 1.87e+01, 2.09e+00, 4.51e-01, 3.71e-02, 3.37e-03, 2.17e-04, 5.07e-05,
    6.56e+02, 2.71e+02, 8.15e+01, 3.12e+01, 1.38e+01, 2.39e+00, 3.31e-01, 2.33e-02, 4.83e-03,
    3.38e+01, 8.66e+01, 5.20e+01, 2.50e+01, 1.24e+01, 3.39e+00, 1.24e+00, 1.91e-01, 4.87e-02,
    3.43e-02, 3.44e+00, 1.37e+01, 1.21e+01, 7.75e+00, 2.63e+00, 1.04e+00, 2.68e-01, 1.12e-01,
    0.00e+00, 0.00e+00, 5.36e-01, 2.20e+00, 2.67e+00, 1.56e+00, 7.29e-01, 2.12e-01, 8.93e-02,
    0.00e+00, 0.00e+00, 0.00e+00, 2.00e-02, 2.30e-01, 5.02e-01, 3.52e-01, 1.32e-01, 6.43e-02,
    0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 4.75e-04, 5.80e-01, 7.03e-02, 5.23e-02, 3.12e-02]

    #Predictions
    # pred_Ve = [5e-9,5e-10,8e-11,2.5e-11,1.5e-11,2e-11,3e-11,1e-10,6e-10,3e-9,2e-8,4e-7]
    # pred_Ve_array = array.array('d',pred_Ve)
    # pred_m = [1,10,20,30,40,50,60,60,50,40,30,20]
    # pred_m2 = [m+5 for m in pred_m]
    # pred_m_array = array.array('d',pred_m)

    # pred_mm = [0,5,5,15,15,25,25,35,35,45,45,55,55,65,65,55,55,45,45,35,35,25,25,15]
    # pred_Vee = [5e-9,5e-9,5e-10,5e-10,8e-11,8e-11,2.5e-11,2.5e-11,1.5e-11,1.5e-11,2e-11,2e-11,3e-11,3e-11,1e-10,1e-10,6e-10,6e-10,3e-9,3e-9,2e-8,2e-8,4e-7,4e-7,4e-7]
    # pred_mm_array = array.array('d',pred_mm)
    # pred_Vee_array = array.array('d',pred_Vee)

    ## Figure
    func_text1 = "s = #frac{n_{S}}{#sqrt{n_{S}+n_{B}}}"
    out_name = "figureMerlin2.png"
    plotting.drawFigure(mN,Ve,plotting.func1(S,B),func_text1,out_name,"histo1",zrange=[1e-10,1e+5],plot_pred=False)

    # out_name = "figure0lim.pdf"
    # plotting.drawFigureWithLimit(mN,Ve,plotting.func1(S4,B),func_text1,out_name,histo_name="histo11",zrange=[1e-11,10],plot_pred=False)

    ## Figure
    # func_text2 = "s = #frac{S}{#sqrt{S+B+#Delta B}}"
    # out_name = "figure1.pdf"
    # plotting.drawFigure(mN,Ve,plotting.func2(S,B,DeltaB),func_text2,out_name,"histo2",zrange=[1e-11,10],plot_pred=True)

    # out_name = "figure1limzoom.pdf"
    # plotting.drawFigureWithLimitZoom(mN,Ve,plotting.func2(S4,B,DeltaB),func_text2,out_name,histo_name="histo21",zrange=[1e-8,10],plot_pred=True)
    # # plotting.drawFigureWithLimitZoom(mN,Ve,plotting.func2(S4,B,DeltaB),func_text2,out_name,histo_name="histo21",zrange=[1e-8,10],plot_pred=True)

    # out_name = "figure1lim.pdf"
    # plotting.drawFigureWithLimit(mN,Ve,plotting.func2(S4,B,DeltaB),func_text2,out_name,S1,histo_name="histo22",zrange=[1e-8,10],plot_pred=True)

    # out_name = "figure1num.pdf"
    # plotting.drawFigureWithNumbers(mN,Ve,plotting.func2(S4,B,DeltaB),func_text2,out_name,"histo23",zrange=[1e-8,10])


    ## Figure
    # func_text3 = "s = #frac{S}{#sqrt{B+#Delta B}}"
    # out_name = "figureMerlin.pdf"
    # plotting.drawFigure(mN,Ve,plotting.func3(S,B,DeltaB),func_text1,out_name,"histo3",zrange=[1e-10,0.1])

    ## Figure Signal no cuts
    # func_text4 = "S"
    # out_name = "signal_nocut.pdf"
    # plotting.drawFigureWithNumbers(mN,Ve,S0,func_text4,out_name,"histo4",zrange=[1e-5,1e4])

    ## Figure Signal Exactly 2 reco e
    # out_name = "signal_2RecoE.pdf"
    # plotting.drawFigureWithNumbers(mN,Ve,S1,func_text4,out_name,"histo5",zrange=[1e-5,1e4])

    ## Figure Signal Vetoes
    # out_name = "signal_vetoes.pdf"
    # plotting.drawFigureWithNumbers(mN,Ve,S2,func_text4,out_name,"histo6",zrange=[1e-5,1e4])

    ## Figure Signal MissingEnergyGt10
    # out_name = "signal_MissingEnergyGt10.pdf"
    # plotting.drawFigureWithNumbers(mN,Ve,S3,func_text4,out_name,"histo7",zrange=[1e-5,1e4])

    ## Figure Signal absD0Gt0p5
    # out_name = "signal_absD0Gt0p5.pdf"
    # plotting.drawFigureWithNumbers(mN,Ve,S4,func_text4,out_name,"histo8",zrange=[1e-5,1e4])

    # out_name = "signal_absD0Gt0p5_lim.pdf"
    # plotting.drawFigureWithLimit(mN,Ve,S4,func_text4,out_name,S,histo_name="histo81",zrange=[1e-5,1e4],plot_pred=False)

    # Figure decay length
    # out_name = "signal_L.pdf"
    # func_text8 = "L [mm]"
    # plotting.drawFigureWithLimit(mN,Ve,plotting.func_L(mN,Ve),func_text4,out_name,S,histo_name="histo9",zrange=[1e-5,1e4],plot_pred=False)


    ## Table
    # plotting.saveTab(mN,Ve,S,plotting.func1(S,B),func_text1,plotting.func2(S,B,DeltaB),func_text2)
