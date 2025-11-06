# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Fri 3 Nov 2017 09:54:44


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


FF6 = Lorentz(name = 'FF6',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,1)')

FF7 = Lorentz(name = 'FF7',
              spins = [ 2, 2 ],
              structure = 'ProjM(2,1) + ProjP(2,1)')

FF8 = Lorentz(name = 'FF8',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FF9 = Lorentz(name = 'FF9',
              spins = [ 2, 2 ],
              structure = '-(P(-1,1)*Gamma(-1,2,1)) + P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

VV4 = Lorentz(name = 'VV4',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2)')

VV5 = Lorentz(name = 'VV5',
              spins = [ 3, 3 ],
              structure = 'Metric(1,2)')

VV6 = Lorentz(name = 'VV6',
              spins = [ 3, 3 ],
              structure = 'P(-1,2)**2*Metric(1,2)')

VV7 = Lorentz(name = 'VV7',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2) - (3*P(-1,2)**2*Metric(1,2))/2.')

VV8 = Lorentz(name = 'VV8',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2) - P(-1,2)**2*Metric(1,2)')

UUS2 = Lorentz(name = 'UUS2',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV3 = Lorentz(name = 'UUV3',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS2 = Lorentz(name = 'SSS2',
               spins = [ 1, 1, 1 ],
               structure = '1')

SSS3 = Lorentz(name = 'SSS3',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)*P(-1,2)')

SSS4 = Lorentz(name = 'SSS4',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)*P(-1,2) - P(-1,1)*P(-1,3)')

FFS5 = Lorentz(name = 'FFS5',
               spins = [ 2, 2, 1 ],
               structure = 'Gamma5(2,1)')

FFS6 = Lorentz(name = 'FFS6',
               spins = [ 2, 2, 1 ],
               structure = 'Identity(2,1)')

FFS7 = Lorentz(name = 'FFS7',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS8 = Lorentz(name = 'FFS8',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) - ProjP(2,1)')

FFS9 = Lorentz(name = 'FFS9',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS10 = Lorentz(name = 'FFS10',
                spins = [ 2, 2, 1 ],
                structure = 'ProjM(2,1) + ProjP(2,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1) - Gamma(3,2,-1)*ProjM(-1,1) - Gamma(3,2,-1)*ProjP(-1,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1) - (4*Gamma(3,2,-1)*ProjM(-1,1))/13. - (4*Gamma(3,2,-1)*ProjP(-1,1))/13.')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

FFV10 = Lorentz(name = 'FFV10',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV11 = Lorentz(name = 'FFV11',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

VSS3 = Lorentz(name = 'VSS3',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2)')

VSS4 = Lorentz(name = 'VSS4',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = '-4*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1) + 4*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS4 = Lorentz(name = 'VVS4',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV9 = Lorentz(name = 'VVV9',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - 3*P(3,2)*Metric(1,2) - P(3,3)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,2)*Metric(1,3) + 3*P(2,3)*Metric(1,3) + 2*P(1,2)*Metric(2,3) - 2*P(1,3)*Metric(2,3)')

VVV10 = Lorentz(name = 'VVV10',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV11 = Lorentz(name = 'VVV11',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - (11*P(3,2)*Metric(1,2))/17. + (3*P(3,3)*Metric(1,2))/17. - P(2,1)*Metric(1,3) - (3*P(2,2)*Metric(1,3))/17. + (11*P(2,3)*Metric(1,3))/17. + (14*P(1,2)*Metric(2,3))/17. - (14*P(1,3)*Metric(2,3))/17.')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

SSSS3 = Lorentz(name = 'SSSS3',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2)')

VSSS1 = Lorentz(name = 'VSSS1',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVS1 = Lorentz(name = 'VVVS1',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Epsilon(1,2,3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,2)*Metric(3,4)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV14 = Lorentz(name = 'VVVV14',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

