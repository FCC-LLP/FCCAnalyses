# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Fri 3 Nov 2017 09:54:44


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV10 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_160_37,(0,0,1):C.R2GC_160_38})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV14, L.VVVV6, L.VVVV7, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,1,0):C.R2GC_149_27,(0,1,1):C.R2GC_149_28,(2,1,0):C.R2GC_149_27,(2,1,1):C.R2GC_149_28,(6,1,0):C.R2GC_153_32,(6,1,1):C.R2GC_165_44,(7,1,0):C.R2GC_154_34,(7,1,1):C.R2GC_164_43,(5,1,0):C.R2GC_147_23,(5,1,1):C.R2GC_147_24,(1,1,0):C.R2GC_147_23,(1,1,1):C.R2GC_147_24,(4,1,0):C.R2GC_147_23,(4,1,1):C.R2GC_147_24,(3,1,0):C.R2GC_147_23,(3,1,1):C.R2GC_147_24,(8,1,0):C.R2GC_148_25,(8,1,1):C.R2GC_148_26,(11,0,0):C.R2GC_151_30,(11,0,1):C.R2GC_151_31,(10,0,0):C.R2GC_151_30,(10,0,1):C.R2GC_151_31,(9,0,1):C.R2GC_150_29,(0,2,0):C.R2GC_149_27,(0,2,1):C.R2GC_149_28,(2,2,0):C.R2GC_149_27,(2,2,1):C.R2GC_149_28,(6,2,0):C.R2GC_161_39,(6,2,1):C.R2GC_161_40,(7,2,0):C.R2GC_154_34,(7,2,1):C.R2GC_154_35,(5,2,0):C.R2GC_147_23,(5,2,1):C.R2GC_147_24,(1,2,0):C.R2GC_147_23,(1,2,1):C.R2GC_147_24,(4,2,0):C.R2GC_147_23,(4,2,1):C.R2GC_147_24,(3,2,0):C.R2GC_147_23,(3,2,1):C.R2GC_147_24,(8,2,0):C.R2GC_148_25,(8,2,1):C.R2GC_166_45,(0,3,0):C.R2GC_149_27,(0,3,1):C.R2GC_149_28,(2,3,0):C.R2GC_149_27,(2,3,1):C.R2GC_149_28,(6,3,0):C.R2GC_153_32,(6,3,1):C.R2GC_153_33,(7,3,0):C.R2GC_162_41,(7,3,1):C.R2GC_149_28,(5,3,0):C.R2GC_147_23,(5,3,1):C.R2GC_147_24,(1,3,0):C.R2GC_147_23,(1,3,1):C.R2GC_147_24,(4,3,0):C.R2GC_147_23,(4,3,1):C.R2GC_147_24,(3,3,0):C.R2GC_147_23,(3,3,1):C.R2GC_147_24,(8,3,0):C.R2GC_148_25,(8,3,1):C.R2GC_163_42})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS9 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_176_49})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS7 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_177_50})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_174_47})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS6 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_175_48})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_103_4})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_103_4})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_103_4})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_7})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_108_7})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_7})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_157_36})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_157_36})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_157_36})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_157_36})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_157_36})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_157_36})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,1,0):C.R2GC_105_6,(0,0,0):C.R2GC_101_2})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,1,0):C.R2GC_105_6,(0,0,0):C.R2GC_101_2})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,1,0):C.R2GC_105_6,(0,0,0):C.R2GC_101_2})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_101_2})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_101_2})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_101_2})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_3})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF8 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_3})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF7, L.FF8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_46,(0,1,0):C.R2GC_102_3})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_3})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_102_3})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF8 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_3})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV5, L.VV6, L.VV7 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,1):C.R2GC_93_51,(0,0,2):C.R2GC_94_52,(0,1,0):C.R2GC_123_9})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS4 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_96_53})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV14 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_22})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV14 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_126_14,(0,0,1):C.R2GC_126_15})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV14 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_129_20,(0,0,1):C.R2GC_129_21})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV14 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_124_10,(0,0,1):C.R2GC_124_11})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV14, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,1,0):C.R2GC_128_18,(1,1,1):C.R2GC_128_19,(0,0,0):C.R2GC_127_16,(0,0,1):C.R2GC_127_17})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV14 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_125_12,(0,0,1):C.R2GC_125_13})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_117_8})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_117_8})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_117_8})

V_48 = CTVertex(name = 'V_48',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV10, L.VVV11, L.VVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_160_28,(0,0,3):C.UVGC_160_29,(0,1,1):C.UVGC_131_1,(0,2,2):C.UVGC_132_2})

V_49 = CTVertex(name = 'V_49',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV14, L.VVVV6, L.VVVV7, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,2):C.UVGC_148_12,(0,1,3):C.UVGC_148_11,(2,1,2):C.UVGC_148_12,(2,1,3):C.UVGC_148_11,(6,1,1):C.UVGC_164_39,(6,1,2):C.UVGC_165_43,(6,1,3):C.UVGC_165_44,(6,1,4):C.UVGC_164_42,(7,1,1):C.UVGC_164_39,(7,1,2):C.UVGC_164_40,(7,1,3):C.UVGC_164_41,(7,1,4):C.UVGC_164_42,(5,1,2):C.UVGC_147_9,(5,1,3):C.UVGC_147_10,(1,1,2):C.UVGC_147_9,(1,1,3):C.UVGC_147_10,(4,1,2):C.UVGC_147_9,(4,1,3):C.UVGC_147_10,(3,1,2):C.UVGC_147_9,(3,1,3):C.UVGC_147_10,(8,1,2):C.UVGC_148_11,(8,1,3):C.UVGC_148_12,(11,0,2):C.UVGC_151_15,(11,0,3):C.UVGC_151_16,(10,0,2):C.UVGC_151_15,(10,0,3):C.UVGC_151_16,(9,0,2):C.UVGC_150_13,(9,0,3):C.UVGC_150_14,(0,2,2):C.UVGC_148_12,(0,2,3):C.UVGC_148_11,(2,2,2):C.UVGC_148_12,(2,2,3):C.UVGC_148_11,(6,2,2):C.UVGC_161_30,(6,2,3):C.UVGC_161_31,(6,2,4):C.UVGC_161_32,(7,2,0):C.UVGC_153_21,(7,2,2):C.UVGC_154_23,(7,2,3):C.UVGC_154_24,(5,2,2):C.UVGC_147_9,(5,2,3):C.UVGC_147_10,(1,2,2):C.UVGC_147_9,(1,2,3):C.UVGC_147_10,(4,2,2):C.UVGC_147_9,(4,2,3):C.UVGC_147_10,(3,2,2):C.UVGC_147_9,(3,2,3):C.UVGC_147_10,(8,2,1):C.UVGC_166_45,(8,2,2):C.UVGC_166_46,(8,2,3):C.UVGC_166_47,(8,2,4):C.UVGC_166_48,(0,3,2):C.UVGC_148_12,(0,3,3):C.UVGC_148_11,(2,3,2):C.UVGC_148_12,(2,3,3):C.UVGC_148_11,(6,3,0):C.UVGC_153_21,(6,3,2):C.UVGC_153_22,(6,3,3):C.UVGC_150_13,(7,3,2):C.UVGC_162_33,(7,3,3):C.UVGC_162_34,(7,3,4):C.UVGC_161_32,(5,3,2):C.UVGC_147_9,(5,3,3):C.UVGC_147_10,(1,3,2):C.UVGC_147_9,(1,3,3):C.UVGC_147_10,(4,3,2):C.UVGC_147_9,(4,3,3):C.UVGC_147_10,(3,3,2):C.UVGC_147_9,(3,3,3):C.UVGC_147_10,(8,3,1):C.UVGC_163_35,(8,3,2):C.UVGC_163_36,(8,3,3):C.UVGC_163_37,(8,3,4):C.UVGC_163_38})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS9 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_176_58,(0,0,2):C.UVGC_176_59,(0,0,1):C.UVGC_176_60})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS7 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_177_61,(0,0,2):C.UVGC_177_62,(0,0,1):C.UVGC_177_63})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_174_56})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_175_57})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_135_5})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_135_5})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4, L.FFV9 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_135_5,(0,1,0):C.UVGC_168_50})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_133_3})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_133_3})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_133_3})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV8, L.FFV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_134_4,(0,1,0):C.UVGC_152_17,(0,1,1):C.UVGC_152_18,(0,1,2):C.UVGC_152_19,(0,1,4):C.UVGC_152_20})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV8, L.FFV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_134_4,(0,1,0):C.UVGC_152_17,(0,1,2):C.UVGC_152_18,(0,1,3):C.UVGC_152_19,(0,1,4):C.UVGC_152_20})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_134_4,(0,1,0):C.UVGC_152_17,(0,1,1):C.UVGC_152_18,(0,1,2):C.UVGC_152_19,(0,1,4):C.UVGC_152_20,(0,1,3):C.UVGC_169_51})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV8, L.FFV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_134_4,(0,1,0):C.UVGC_152_17,(0,1,2):C.UVGC_152_18,(0,1,3):C.UVGC_152_19,(0,1,4):C.UVGC_152_20})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV8, L.FFV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_134_4,(0,1,0):C.UVGC_152_17,(0,1,1):C.UVGC_152_18,(0,1,2):C.UVGC_152_19,(0,1,4):C.UVGC_152_20})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV8, L.FFV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_134_4,(0,1,0):C.UVGC_152_17,(0,1,2):C.UVGC_152_18,(0,1,3):C.UVGC_152_19,(0,1,4):C.UVGC_152_20})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_157_25,(0,0,1):C.UVGC_157_26})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_157_25,(0,0,1):C.UVGC_157_26})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_157_25,(0,0,2):C.UVGC_171_53,(0,0,1):C.UVGC_157_26})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_157_25,(0,0,1):C.UVGC_157_26})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_157_25,(0,0,1):C.UVGC_157_26})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_157_25,(0,0,2):C.UVGC_171_53,(0,0,1):C.UVGC_157_26})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,1,0):C.UVGC_172_54,(0,0,0):C.UVGC_173_55})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF9 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_137_6})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF7, L.FF8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_170_52,(0,1,0):C.UVGC_167_49})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF9 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_137_6})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF9 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_137_6})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV4, L.VV8 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_146_7,(0,0,1):C.UVGC_146_8,(0,1,2):C.UVGC_159_27})

