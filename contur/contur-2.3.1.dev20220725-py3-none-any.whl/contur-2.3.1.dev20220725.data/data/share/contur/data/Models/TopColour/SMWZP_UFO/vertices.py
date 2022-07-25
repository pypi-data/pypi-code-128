# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Fri 11 Dec 2020 18:33:57


from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G0, P.G0, P.G0, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_51})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_49})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_50})

V_4 = Vertex(name = 'V_4',
             particles = [ P.G0, P.G0, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_49})

V_5 = Vertex(name = 'V_5',
             particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_49})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_51})

V_7 = Vertex(name = 'V_7',
             particles = [ P.G0, P.G0, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_245})

V_8 = Vertex(name = 'V_8',
             particles = [ P.G__minus__, P.G__plus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_245})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_246})

V_10 = Vertex(name = 'V_10',
              particles = [ P.A, P.A, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_11 = Vertex(name = 'V_11',
              particles = [ P.A, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_4})

V_12 = Vertex(name = 'V_12',
              particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_4})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_3})

V_14 = Vertex(name = 'V_14',
              particles = [ P.ghWm, P.ghA__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_52})

V_15 = Vertex(name = 'V_15',
              particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_4})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ghWm, P.ghWm__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_212})

V_17 = Vertex(name = 'V_17',
              particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_213})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghWm, P.ghWm__tilde__, P.A ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_3})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_153})

V_20 = Vertex(name = 'V_20',
              particles = [ P.ghWm, P.ghZ__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_240})

V_21 = Vertex(name = 'V_21',
              particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_152})

V_22 = Vertex(name = 'V_22',
              particles = [ P.ghWp, P.ghA__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_52})

V_23 = Vertex(name = 'V_23',
              particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_3})

V_24 = Vertex(name = 'V_24',
              particles = [ P.ghWp, P.ghWp__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_214})

V_25 = Vertex(name = 'V_25',
              particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_213})

V_26 = Vertex(name = 'V_26',
              particles = [ P.ghWp, P.ghWp__tilde__, P.A ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_4})

V_27 = Vertex(name = 'V_27',
              particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_152})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghWp, P.ghZ__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_240})

V_29 = Vertex(name = 'V_29',
              particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_153})

V_30 = Vertex(name = 'V_30',
              particles = [ P.ghZ, P.ghWm__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_233})

V_31 = Vertex(name = 'V_31',
              particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_152})

V_32 = Vertex(name = 'V_32',
              particles = [ P.ghZ, P.ghWp__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_233})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_153})

V_34 = Vertex(name = 'V_34',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_241})

V_35 = Vertex(name = 'V_35',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_10})

V_36 = Vertex(name = 'V_36',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_37 = Vertex(name = 'V_37',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_38 = Vertex(name = 'V_38',
              particles = [ P.u__tilde__, P.d, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_13,(0,1):C.GC_22})

V_39 = Vertex(name = 'V_39',
              particles = [ P.c__tilde__, P.d, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_14,(0,1):C.GC_23})

V_40 = Vertex(name = 'V_40',
              particles = [ P.t__tilde__, P.d, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_15,(0,1):C.GC_24})

V_41 = Vertex(name = 'V_41',
              particles = [ P.u__tilde__, P.s, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_16,(0,1):C.GC_25})

V_42 = Vertex(name = 'V_42',
              particles = [ P.c__tilde__, P.s, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_17,(0,1):C.GC_26})

V_43 = Vertex(name = 'V_43',
              particles = [ P.t__tilde__, P.s, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_18,(0,1):C.GC_27})

V_44 = Vertex(name = 'V_44',
              particles = [ P.u__tilde__, P.b, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_19,(0,1):C.GC_28})

V_45 = Vertex(name = 'V_45',
              particles = [ P.c__tilde__, P.b, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_20,(0,1):C.GC_29})

V_46 = Vertex(name = 'V_46',
              particles = [ P.t__tilde__, P.b, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_30})

V_47 = Vertex(name = 'V_47',
              particles = [ P.d__tilde__, P.d, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_254})

V_48 = Vertex(name = 'V_48',
              particles = [ P.s__tilde__, P.s, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_262})

V_49 = Vertex(name = 'V_49',
              particles = [ P.b__tilde__, P.b, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_250})

V_50 = Vertex(name = 'V_50',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_255})

V_51 = Vertex(name = 'V_51',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_263})

V_52 = Vertex(name = 'V_52',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_251})

V_53 = Vertex(name = 'V_53',
              particles = [ P.nu_e__tilde__, P.e__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_256})

V_54 = Vertex(name = 'V_54',
              particles = [ P.nu_mu__tilde__, P.mu__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_259})

V_55 = Vertex(name = 'V_55',
              particles = [ P.nu_tau__tilde__, P.tau__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_266})

V_56 = Vertex(name = 'V_56',
              particles = [ P.e__plus__, P.e__minus__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_257})

V_57 = Vertex(name = 'V_57',
              particles = [ P.mu__plus__, P.mu__minus__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_260})

V_58 = Vertex(name = 'V_58',
              particles = [ P.tau__plus__, P.tau__minus__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_267})

V_59 = Vertex(name = 'V_59',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_258})

V_60 = Vertex(name = 'V_60',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_261})

V_61 = Vertex(name = 'V_61',
              particles = [ P.tau__plus__, P.tau__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_268})

V_62 = Vertex(name = 'V_62',
              particles = [ P.d__tilde__, P.u, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_31,(0,1):C.GC_40})

V_63 = Vertex(name = 'V_63',
              particles = [ P.s__tilde__, P.u, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_32,(0,1):C.GC_41})

V_64 = Vertex(name = 'V_64',
              particles = [ P.b__tilde__, P.u, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_42})

V_65 = Vertex(name = 'V_65',
              particles = [ P.d__tilde__, P.c, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_43})

V_66 = Vertex(name = 'V_66',
              particles = [ P.s__tilde__, P.c, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_44})

V_67 = Vertex(name = 'V_67',
              particles = [ P.b__tilde__, P.c, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_36,(0,1):C.GC_45})

V_68 = Vertex(name = 'V_68',
              particles = [ P.d__tilde__, P.t, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_46})

V_69 = Vertex(name = 'V_69',
              particles = [ P.s__tilde__, P.t, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_47})

V_70 = Vertex(name = 'V_70',
              particles = [ P.b__tilde__, P.t, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_48})

V_71 = Vertex(name = 'V_71',
              particles = [ P.u__tilde__, P.u, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_270})

V_72 = Vertex(name = 'V_72',
              particles = [ P.c__tilde__, P.c, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_253})

V_73 = Vertex(name = 'V_73',
              particles = [ P.t__tilde__, P.t, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_265})

V_74 = Vertex(name = 'V_74',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_269})

V_75 = Vertex(name = 'V_75',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_252})

V_76 = Vertex(name = 'V_76',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_264})

V_77 = Vertex(name = 'V_77',
              particles = [ P.b__tilde__, P.b, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_90})

V_78 = Vertex(name = 'V_78',
              particles = [ P.b__tilde__, P.d, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_93,(0,1):C.GC_96})

V_79 = Vertex(name = 'V_79',
              particles = [ P.b__tilde__, P.s, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_105,(0,1):C.GC_110})

V_80 = Vertex(name = 'V_80',
              particles = [ P.c__tilde__, P.c, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_91})

V_81 = Vertex(name = 'V_81',
              particles = [ P.c__tilde__, P.t, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_112,(0,1):C.GC_114})

V_82 = Vertex(name = 'V_82',
              particles = [ P.c__tilde__, P.u, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_126,(0,1):C.GC_131})

V_83 = Vertex(name = 'V_83',
              particles = [ P.d__tilde__, P.b, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_95,(0,1):C.GC_92})

V_84 = Vertex(name = 'V_84',
              particles = [ P.d__tilde__, P.d, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_94})

V_85 = Vertex(name = 'V_85',
              particles = [ P.d__tilde__, P.s, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_103,(0,1):C.GC_107})

V_86 = Vertex(name = 'V_86',
              particles = [ P.e__plus__, P.e__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_89})

V_87 = Vertex(name = 'V_87',
              particles = [ P.e__plus__, P.mu__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_98,(0,1):C.GC_100})

V_88 = Vertex(name = 'V_88',
              particles = [ P.e__plus__, P.tau__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_117,(0,1):C.GC_121})

V_89 = Vertex(name = 'V_89',
              particles = [ P.mu__plus__, P.e__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_99,(0,1):C.GC_97})

V_90 = Vertex(name = 'V_90',
              particles = [ P.mu__plus__, P.mu__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_101})

V_91 = Vertex(name = 'V_91',
              particles = [ P.mu__plus__, P.tau__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_119,(0,1):C.GC_123})

V_92 = Vertex(name = 'V_92',
              particles = [ P.s__tilde__, P.b, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_109,(0,1):C.GC_104})

V_93 = Vertex(name = 'V_93',
              particles = [ P.s__tilde__, P.d, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_106,(0,1):C.GC_102})

V_94 = Vertex(name = 'V_94',
              particles = [ P.s__tilde__, P.s, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_108})

V_95 = Vertex(name = 'V_95',
              particles = [ P.tau__plus__, P.e__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_120,(0,1):C.GC_116})

V_96 = Vertex(name = 'V_96',
              particles = [ P.tau__plus__, P.mu__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_122,(0,1):C.GC_118})

V_97 = Vertex(name = 'V_97',
              particles = [ P.tau__plus__, P.tau__minus__, P.Gp0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_124})

V_98 = Vertex(name = 'V_98',
              particles = [ P.t__tilde__, P.c, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_113,(0,1):C.GC_111})

V_99 = Vertex(name = 'V_99',
              particles = [ P.t__tilde__, P.t, P.Gp0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_115})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.u, P.Gp0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_128,(0,1):C.GC_133})

V_101 = Vertex(name = 'V_101',
               particles = [ P.u__tilde__, P.c, P.Gp0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_125})

V_102 = Vertex(name = 'V_102',
               particles = [ P.u__tilde__, P.t, P.Gp0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_127})

V_103 = Vertex(name = 'V_103',
               particles = [ P.u__tilde__, P.u, P.Gp0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_129})

V_104 = Vertex(name = 'V_104',
               particles = [ P.c__tilde__, P.b, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_72,(0,1):C.GC_71})

V_105 = Vertex(name = 'V_105',
               particles = [ P.c__tilde__, P.d, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_73,(0,1):C.GC_74})

V_106 = Vertex(name = 'V_106',
               particles = [ P.c__tilde__, P.s, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_75,(0,1):C.GC_76})

V_107 = Vertex(name = 'V_107',
               particles = [ P.t__tilde__, P.b, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_82,(0,1):C.GC_79})

V_108 = Vertex(name = 'V_108',
               particles = [ P.t__tilde__, P.d, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_80,(0,1):C.GC_77})

V_109 = Vertex(name = 'V_109',
               particles = [ P.t__tilde__, P.s, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_81,(0,1):C.GC_78})

V_110 = Vertex(name = 'V_110',
               particles = [ P.u__tilde__, P.b, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_88,(0,1):C.GC_85})

V_111 = Vertex(name = 'V_111',
               particles = [ P.u__tilde__, P.d, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_86,(0,1):C.GC_83})

V_112 = Vertex(name = 'V_112',
               particles = [ P.u__tilde__, P.s, P.Gp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_87,(0,1):C.GC_84})

V_113 = Vertex(name = 'V_113',
               particles = [ P.nu_e__tilde__, P.e__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_218})

V_114 = Vertex(name = 'V_114',
               particles = [ P.nu_e__tilde__, P.mu__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_224})

V_115 = Vertex(name = 'V_115',
               particles = [ P.nu_e__tilde__, P.tau__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_227,(0,1):C.GC_230})

V_116 = Vertex(name = 'V_116',
               particles = [ P.nu_mu__tilde__, P.e__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_219})

V_117 = Vertex(name = 'V_117',
               particles = [ P.nu_mu__tilde__, P.mu__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_225})

V_118 = Vertex(name = 'V_118',
               particles = [ P.nu_mu__tilde__, P.tau__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_228,(0,1):C.GC_231})

V_119 = Vertex(name = 'V_119',
               particles = [ P.nu_tau__tilde__, P.e__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_220})

V_120 = Vertex(name = 'V_120',
               particles = [ P.nu_tau__tilde__, P.mu__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_223,(0,1):C.GC_226})

V_121 = Vertex(name = 'V_121',
               particles = [ P.nu_tau__tilde__, P.tau__minus__, P.Gp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_229,(0,1):C.GC_232})

V_122 = Vertex(name = 'V_122',
               particles = [ P.b__tilde__, P.c, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_71,(0,1):C.GC_72})

V_123 = Vertex(name = 'V_123',
               particles = [ P.d__tilde__, P.c, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_74,(0,1):C.GC_73})

V_124 = Vertex(name = 'V_124',
               particles = [ P.s__tilde__, P.c, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_76,(0,1):C.GC_75})

V_125 = Vertex(name = 'V_125',
               particles = [ P.b__tilde__, P.t, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_79,(0,1):C.GC_82})

V_126 = Vertex(name = 'V_126',
               particles = [ P.d__tilde__, P.t, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_77,(0,1):C.GC_80})

V_127 = Vertex(name = 'V_127',
               particles = [ P.s__tilde__, P.t, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_78,(0,1):C.GC_81})

V_128 = Vertex(name = 'V_128',
               particles = [ P.b__tilde__, P.u, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_85,(0,1):C.GC_88})

V_129 = Vertex(name = 'V_129',
               particles = [ P.d__tilde__, P.u, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_86})

V_130 = Vertex(name = 'V_130',
               particles = [ P.s__tilde__, P.u, P.Gp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_87})

V_131 = Vertex(name = 'V_131',
               particles = [ P.e__plus__, P.nu_e, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_218,(0,1):C.GC_215})

V_132 = Vertex(name = 'V_132',
               particles = [ P.mu__plus__, P.nu_e, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_221})

V_133 = Vertex(name = 'V_133',
               particles = [ P.tau__plus__, P.nu_e, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_230,(0,1):C.GC_227})

V_134 = Vertex(name = 'V_134',
               particles = [ P.e__plus__, P.nu_mu, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_216})

V_135 = Vertex(name = 'V_135',
               particles = [ P.mu__plus__, P.nu_mu, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_222})

V_136 = Vertex(name = 'V_136',
               particles = [ P.tau__plus__, P.nu_mu, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_228})

V_137 = Vertex(name = 'V_137',
               particles = [ P.e__plus__, P.nu_tau, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_220,(0,1):C.GC_217})

V_138 = Vertex(name = 'V_138',
               particles = [ P.mu__plus__, P.nu_tau, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_226,(0,1):C.GC_223})

V_139 = Vertex(name = 'V_139',
               particles = [ P.tau__plus__, P.nu_tau, P.Gp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_232,(0,1):C.GC_229})

V_140 = Vertex(name = 'V_140',
               particles = [ P.A, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_156})

V_141 = Vertex(name = 'V_141',
               particles = [ P.A, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_155})

V_142 = Vertex(name = 'V_142',
               particles = [ P.A, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_248})

V_143 = Vertex(name = 'V_143',
               particles = [ P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_139})

V_144 = Vertex(name = 'V_144',
               particles = [ P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_138})

V_145 = Vertex(name = 'V_145',
               particles = [ P.A, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_3})

V_146 = Vertex(name = 'V_146',
               particles = [ P.A, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_154})

V_147 = Vertex(name = 'V_147',
               particles = [ P.A, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_155})

V_148 = Vertex(name = 'V_148',
               particles = [ P.A, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_248})

V_149 = Vertex(name = 'V_149',
               particles = [ P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_139})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_137})

V_151 = Vertex(name = 'V_151',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_134})

V_152 = Vertex(name = 'V_152',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_134})

V_153 = Vertex(name = 'V_153',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_134})

V_154 = Vertex(name = 'V_154',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_247})

V_155 = Vertex(name = 'V_155',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_5})

V_156 = Vertex(name = 'V_156',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_153})

V_157 = Vertex(name = 'V_157',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_135})

V_158 = Vertex(name = 'V_158',
               particles = [ P.e__plus__, P.nu_e, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_256})

V_159 = Vertex(name = 'V_159',
               particles = [ P.mu__plus__, P.nu_mu, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_259})

V_160 = Vertex(name = 'V_160',
               particles = [ P.tau__plus__, P.nu_tau, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_266})

V_161 = Vertex(name = 'V_161',
               particles = [ P.A, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_239})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_236})

V_163 = Vertex(name = 'V_163',
               particles = [ P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_237})

V_164 = Vertex(name = 'V_164',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_9})

V_165 = Vertex(name = 'V_165',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_166 = Vertex(name = 'V_166',
               particles = [ P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_244})

V_167 = Vertex(name = 'V_167',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_168 = Vertex(name = 'V_168',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_169 = Vertex(name = 'V_169',
               particles = [ P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_244})

V_170 = Vertex(name = 'V_170',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_157})

V_171 = Vertex(name = 'V_171',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_243})

V_172 = Vertex(name = 'V_172',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_242})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_243})

V_174 = Vertex(name = 'V_174',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_249})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_136})

V_176 = Vertex(name = 'V_176',
               particles = [ P.d__tilde__, P.u, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_167,(0,1):C.GC_185})

V_177 = Vertex(name = 'V_177',
               particles = [ P.s__tilde__, P.u, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_168,(0,1):C.GC_186})

V_178 = Vertex(name = 'V_178',
               particles = [ P.b__tilde__, P.u, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_169,(0,1):C.GC_187})

V_179 = Vertex(name = 'V_179',
               particles = [ P.d__tilde__, P.c, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_170,(0,1):C.GC_188})

V_180 = Vertex(name = 'V_180',
               particles = [ P.s__tilde__, P.c, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_189})

V_181 = Vertex(name = 'V_181',
               particles = [ P.b__tilde__, P.c, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_172,(0,1):C.GC_190})

V_182 = Vertex(name = 'V_182',
               particles = [ P.d__tilde__, P.t, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_191})

V_183 = Vertex(name = 'V_183',
               particles = [ P.s__tilde__, P.t, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_192})

V_184 = Vertex(name = 'V_184',
               particles = [ P.b__tilde__, P.t, P.Wp__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_175,(0,1):C.GC_193})

V_185 = Vertex(name = 'V_185',
               particles = [ P.e__plus__, P.nu_e, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_158,(0,1):C.GC_176})

V_186 = Vertex(name = 'V_186',
               particles = [ P.mu__plus__, P.nu_e, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_159,(0,1):C.GC_177})

V_187 = Vertex(name = 'V_187',
               particles = [ P.tau__plus__, P.nu_e, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_178})

V_188 = Vertex(name = 'V_188',
               particles = [ P.e__plus__, P.nu_mu, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_179})

V_189 = Vertex(name = 'V_189',
               particles = [ P.mu__plus__, P.nu_mu, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_162,(0,1):C.GC_180})

V_190 = Vertex(name = 'V_190',
               particles = [ P.tau__plus__, P.nu_mu, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_181})

V_191 = Vertex(name = 'V_191',
               particles = [ P.e__plus__, P.nu_tau, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_164,(0,1):C.GC_182})

V_192 = Vertex(name = 'V_192',
               particles = [ P.mu__plus__, P.nu_tau, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_165,(0,1):C.GC_183})

V_193 = Vertex(name = 'V_193',
               particles = [ P.tau__plus__, P.nu_tau, P.Wp__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_166,(0,1):C.GC_184})

V_194 = Vertex(name = 'V_194',
               particles = [ P.d__tilde__, P.d, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_194,(0,1):C.GC_203})

V_195 = Vertex(name = 'V_195',
               particles = [ P.s__tilde__, P.d, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_53,(0,1):C.GC_62})

V_196 = Vertex(name = 'V_196',
               particles = [ P.b__tilde__, P.d, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_54,(0,1):C.GC_63})

V_197 = Vertex(name = 'V_197',
               particles = [ P.d__tilde__, P.s, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_53,(0,1):C.GC_62})

V_198 = Vertex(name = 'V_198',
               particles = [ P.s__tilde__, P.s, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_195,(0,1):C.GC_204})

V_199 = Vertex(name = 'V_199',
               particles = [ P.b__tilde__, P.s, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_55,(0,1):C.GC_64})

V_200 = Vertex(name = 'V_200',
               particles = [ P.d__tilde__, P.b, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_54,(0,1):C.GC_63})

V_201 = Vertex(name = 'V_201',
               particles = [ P.s__tilde__, P.b, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_55,(0,1):C.GC_64})

V_202 = Vertex(name = 'V_202',
               particles = [ P.b__tilde__, P.b, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_196,(0,1):C.GC_205})

V_203 = Vertex(name = 'V_203',
               particles = [ P.e__plus__, P.e__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_197,(0,1):C.GC_206})

V_204 = Vertex(name = 'V_204',
               particles = [ P.mu__plus__, P.e__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_65})

V_205 = Vertex(name = 'V_205',
               particles = [ P.tau__plus__, P.e__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_66})

V_206 = Vertex(name = 'V_206',
               particles = [ P.e__plus__, P.mu__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_65})

V_207 = Vertex(name = 'V_207',
               particles = [ P.mu__plus__, P.mu__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_198,(0,1):C.GC_207})

V_208 = Vertex(name = 'V_208',
               particles = [ P.tau__plus__, P.mu__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_58,(0,1):C.GC_67})

V_209 = Vertex(name = 'V_209',
               particles = [ P.e__plus__, P.tau__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_66})

V_210 = Vertex(name = 'V_210',
               particles = [ P.mu__plus__, P.tau__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_58,(0,1):C.GC_67})

V_211 = Vertex(name = 'V_211',
               particles = [ P.tau__plus__, P.tau__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_199,(0,1):C.GC_208})

V_212 = Vertex(name = 'V_212',
               particles = [ P.u__tilde__, P.u, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_200,(0,1):C.GC_209})

V_213 = Vertex(name = 'V_213',
               particles = [ P.c__tilde__, P.u, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_59,(0,1):C.GC_68})

V_214 = Vertex(name = 'V_214',
               particles = [ P.t__tilde__, P.u, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_60,(0,1):C.GC_69})

V_215 = Vertex(name = 'V_215',
               particles = [ P.u__tilde__, P.c, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_59,(0,1):C.GC_68})

V_216 = Vertex(name = 'V_216',
               particles = [ P.c__tilde__, P.c, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_201,(0,1):C.GC_210})

V_217 = Vertex(name = 'V_217',
               particles = [ P.t__tilde__, P.c, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_61,(0,1):C.GC_70})

V_218 = Vertex(name = 'V_218',
               particles = [ P.u__tilde__, P.t, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_60,(0,1):C.GC_69})

V_219 = Vertex(name = 'V_219',
               particles = [ P.c__tilde__, P.t, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_61,(0,1):C.GC_70})

V_220 = Vertex(name = 'V_220',
               particles = [ P.t__tilde__, P.t, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_202,(0,1):C.GC_211})

V_221 = Vertex(name = 'V_221',
               particles = [ P.u__tilde__, P.d, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_167,(0,1):C.GC_185})

V_222 = Vertex(name = 'V_222',
               particles = [ P.c__tilde__, P.d, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_170,(0,1):C.GC_188})

V_223 = Vertex(name = 'V_223',
               particles = [ P.t__tilde__, P.d, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_191})

V_224 = Vertex(name = 'V_224',
               particles = [ P.u__tilde__, P.s, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_168,(0,1):C.GC_186})

V_225 = Vertex(name = 'V_225',
               particles = [ P.c__tilde__, P.s, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_189})

V_226 = Vertex(name = 'V_226',
               particles = [ P.t__tilde__, P.s, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_192})

V_227 = Vertex(name = 'V_227',
               particles = [ P.u__tilde__, P.b, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_169,(0,1):C.GC_187})

V_228 = Vertex(name = 'V_228',
               particles = [ P.c__tilde__, P.b, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_172,(0,1):C.GC_190})

V_229 = Vertex(name = 'V_229',
               particles = [ P.t__tilde__, P.b, P.Wp__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_175,(0,1):C.GC_193})

V_230 = Vertex(name = 'V_230',
               particles = [ P.nu_e__tilde__, P.e__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_158,(0,1):C.GC_176})

V_231 = Vertex(name = 'V_231',
               particles = [ P.nu_mu__tilde__, P.e__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_179})

V_232 = Vertex(name = 'V_232',
               particles = [ P.nu_tau__tilde__, P.e__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_164,(0,1):C.GC_182})

V_233 = Vertex(name = 'V_233',
               particles = [ P.nu_e__tilde__, P.mu__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_159,(0,1):C.GC_177})

V_234 = Vertex(name = 'V_234',
               particles = [ P.nu_mu__tilde__, P.mu__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_162,(0,1):C.GC_180})

V_235 = Vertex(name = 'V_235',
               particles = [ P.nu_tau__tilde__, P.mu__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_165,(0,1):C.GC_183})

V_236 = Vertex(name = 'V_236',
               particles = [ P.nu_e__tilde__, P.tau__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_178})

V_237 = Vertex(name = 'V_237',
               particles = [ P.nu_mu__tilde__, P.tau__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_181})

V_238 = Vertex(name = 'V_238',
               particles = [ P.nu_tau__tilde__, P.tau__minus__, P.Wp__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_166,(0,1):C.GC_184})

V_239 = Vertex(name = 'V_239',
               particles = [ P.e__plus__, P.e__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_240 = Vertex(name = 'V_240',
               particles = [ P.mu__plus__, P.mu__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_241 = Vertex(name = 'V_241',
               particles = [ P.tau__plus__, P.tau__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_242 = Vertex(name = 'V_242',
               particles = [ P.u__tilde__, P.u, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_243 = Vertex(name = 'V_243',
               particles = [ P.c__tilde__, P.c, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_244 = Vertex(name = 'V_244',
               particles = [ P.t__tilde__, P.t, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_245 = Vertex(name = 'V_245',
               particles = [ P.d__tilde__, P.d, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_246 = Vertex(name = 'V_246',
               particles = [ P.s__tilde__, P.s, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_247 = Vertex(name = 'V_247',
               particles = [ P.b__tilde__, P.b, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_248 = Vertex(name = 'V_248',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_249 = Vertex(name = 'V_249',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_250 = Vertex(name = 'V_250',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_251 = Vertex(name = 'V_251',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_252 = Vertex(name = 'V_252',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_253 = Vertex(name = 'V_253',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_254 = Vertex(name = 'V_254',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_141})

V_255 = Vertex(name = 'V_255',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_142})

V_256 = Vertex(name = 'V_256',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_143})

V_257 = Vertex(name = 'V_257',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_144})

V_258 = Vertex(name = 'V_258',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_145})

V_259 = Vertex(name = 'V_259',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_146})

V_260 = Vertex(name = 'V_260',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_147})

V_261 = Vertex(name = 'V_261',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_262 = Vertex(name = 'V_262',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_149})

V_263 = Vertex(name = 'V_263',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_271})

V_264 = Vertex(name = 'V_264',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_274})

V_265 = Vertex(name = 'V_265',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_277})

V_266 = Vertex(name = 'V_266',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_272})

V_267 = Vertex(name = 'V_267',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_275})

V_268 = Vertex(name = 'V_268',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_278})

V_269 = Vertex(name = 'V_269',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_273})

V_270 = Vertex(name = 'V_270',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_276})

V_271 = Vertex(name = 'V_271',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_279})

V_272 = Vertex(name = 'V_272',
               particles = [ P.e__plus__, P.nu_e, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_273 = Vertex(name = 'V_273',
               particles = [ P.mu__plus__, P.nu_mu, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_274 = Vertex(name = 'V_274',
               particles = [ P.tau__plus__, P.nu_tau, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_275 = Vertex(name = 'V_275',
               particles = [ P.nu_e__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_276 = Vertex(name = 'V_276',
               particles = [ P.nu_mu__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_277 = Vertex(name = 'V_277',
               particles = [ P.nu_tau__tilde__, P.tau__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_278 = Vertex(name = 'V_278',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_234})

V_279 = Vertex(name = 'V_279',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_234})

V_280 = Vertex(name = 'V_280',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_234})

V_281 = Vertex(name = 'V_281',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_234})

V_282 = Vertex(name = 'V_282',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_234})

V_283 = Vertex(name = 'V_283',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_234})

V_284 = Vertex(name = 'V_284',
               particles = [ P.nu_e__tilde__, P.nu_e, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_238})

V_285 = Vertex(name = 'V_285',
               particles = [ P.nu_mu__tilde__, P.nu_mu, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_238})

V_286 = Vertex(name = 'V_286',
               particles = [ P.nu_tau__tilde__, P.nu_tau, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_238})

V_287 = Vertex(name = 'V_287',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_235})

V_288 = Vertex(name = 'V_288',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_235})

V_289 = Vertex(name = 'V_289',
               particles = [ P.tau__plus__, P.tau__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_235})

