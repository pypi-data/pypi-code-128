# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Linux x86 (64-bit) (January 29, 2022)
# Date: Fri 8 Apr 2022 19:16:51


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_9})

V_2 = Vertex(name = 'V_2',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_11,(0,0):C.GC_11,(2,2):C.GC_11})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_6})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_19})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_13})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV5 ],
             couplings = {(0,0):C.GC_20})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_15})

V_9 = Vertex(name = 'V_9',
             particles = [ P.e__plus__, P.e__minus__, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_3})

V_10 = Vertex(name = 'V_10',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_12 = Vertex(name = 'V_12',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_13 = Vertex(name = 'V_13',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_14 = Vertex(name = 'V_14',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_15 = Vertex(name = 'V_15',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_16 = Vertex(name = 'V_16',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_17 = Vertex(name = 'V_17',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_18 = Vertex(name = 'V_18',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_10})

V_19 = Vertex(name = 'V_19',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_10})

V_20 = Vertex(name = 'V_20',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_10})

V_21 = Vertex(name = 'V_21',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_10})

V_22 = Vertex(name = 'V_22',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_10})

V_23 = Vertex(name = 'V_23',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_10})

V_24 = Vertex(name = 'V_24',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_17})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_17})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_17})

V_27 = Vertex(name = 'V_27',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_17})

V_28 = Vertex(name = 'V_28',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_17})

V_29 = Vertex(name = 'V_29',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_17})

V_30 = Vertex(name = 'V_30',
              particles = [ P.e__plus__, P.v1, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_332})

V_31 = Vertex(name = 'V_31',
              particles = [ P.e__plus__, P.v2, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_333})

V_32 = Vertex(name = 'V_32',
              particles = [ P.e__plus__, P.v3, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_334})

V_33 = Vertex(name = 'V_33',
              particles = [ P.mu__plus__, P.v1, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_335})

V_34 = Vertex(name = 'V_34',
              particles = [ P.mu__plus__, P.v2, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_336})

V_35 = Vertex(name = 'V_35',
              particles = [ P.mu__plus__, P.v3, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_337})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ta__plus__, P.v1, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_338})

V_37 = Vertex(name = 'V_37',
              particles = [ P.ta__plus__, P.v2, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_344})

V_38 = Vertex(name = 'V_38',
              particles = [ P.ta__plus__, P.v3, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_350})

V_39 = Vertex(name = 'V_39',
              particles = [ P.v1, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_21})

V_40 = Vertex(name = 'V_40',
              particles = [ P.v2, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_22})

V_41 = Vertex(name = 'V_41',
              particles = [ P.v3, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_23})

V_42 = Vertex(name = 'V_42',
              particles = [ P.v1, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_24})

V_43 = Vertex(name = 'V_43',
              particles = [ P.v2, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_25})

V_44 = Vertex(name = 'V_44',
              particles = [ P.v3, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_26})

V_45 = Vertex(name = 'V_45',
              particles = [ P.v1, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_27})

V_46 = Vertex(name = 'V_46',
              particles = [ P.v2, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_28})

V_47 = Vertex(name = 'V_47',
              particles = [ P.v3, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_29})

V_48 = Vertex(name = 'V_48',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_31})

V_49 = Vertex(name = 'V_49',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_31})

V_50 = Vertex(name = 'V_50',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_31})

V_51 = Vertex(name = 'V_51',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_30})

V_52 = Vertex(name = 'V_52',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_30})

V_53 = Vertex(name = 'V_53',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_30})

V_54 = Vertex(name = 'V_54',
              particles = [ P.v1, P.v1, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_341})

V_55 = Vertex(name = 'V_55',
              particles = [ P.v2, P.v1, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_342,(0,1):C.GC_347})

V_56 = Vertex(name = 'V_56',
              particles = [ P.v2, P.v2, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_348})

V_57 = Vertex(name = 'V_57',
              particles = [ P.v3, P.v1, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_343,(0,1):C.GC_353})

V_58 = Vertex(name = 'V_58',
              particles = [ P.v3, P.v2, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_349,(0,1):C.GC_354})

V_59 = Vertex(name = 'V_59',
              particles = [ P.v3, P.v3, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_355})

V_60 = Vertex(name = 'V_60',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_32})

V_61 = Vertex(name = 'V_61',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_32})

V_62 = Vertex(name = 'V_62',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_32})

V_63 = Vertex(name = 'V_63',
              particles = [ P.D0, P.D0, P.D0, P.D0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_56})

V_64 = Vertex(name = 'V_64',
              particles = [ P.D0, P.D0, P.D__minus____minus__, P.D__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_46})

V_65 = Vertex(name = 'V_65',
              particles = [ P.D__minus____minus__, P.D__minus____minus__, P.D__plus____plus__, P.D__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_12})

V_66 = Vertex(name = 'V_66',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_55})

V_67 = Vertex(name = 'V_67',
              particles = [ P.D0, P.D0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_57})

V_68 = Vertex(name = 'V_68',
              particles = [ P.D__minus____minus__, P.D__plus____plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_45})

V_69 = Vertex(name = 'V_69',
              particles = [ P.D0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_47})

V_70 = Vertex(name = 'V_70',
              particles = [ P.D0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_77})

V_71 = Vertex(name = 'V_71',
              particles = [ P.D0, P.D0, P.D0, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_52})

V_72 = Vertex(name = 'V_72',
              particles = [ P.D0, P.D__minus____minus__, P.D__plus____plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_43})

V_73 = Vertex(name = 'V_73',
              particles = [ P.D0, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_53})

V_74 = Vertex(name = 'V_74',
              particles = [ P.D0, P.D0, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_54})

V_75 = Vertex(name = 'V_75',
              particles = [ P.D0, P.D0, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_80})

V_76 = Vertex(name = 'V_76',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_39})

V_77 = Vertex(name = 'V_77',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_79})

V_78 = Vertex(name = 'V_78',
              particles = [ P.D0, P.D0, P.D0 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_42})

V_79 = Vertex(name = 'V_79',
              particles = [ P.D0, P.D0, P.D0 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_78})

V_80 = Vertex(name = 'V_80',
              particles = [ P.D__minus____minus__, P.D__plus____plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_74})

V_81 = Vertex(name = 'V_81',
              particles = [ P.D0, P.D__minus____minus__, P.D__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_71})

V_82 = Vertex(name = 'V_82',
              particles = [ P.D__minus__, P.D__minus__, P.D__plus__, P.D__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_120})

V_83 = Vertex(name = 'V_83',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_119})

V_84 = Vertex(name = 'V_84',
              particles = [ P.D__minus__, P.D__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_121})

V_85 = Vertex(name = 'V_85',
              particles = [ P.D__minus__, P.D__plus__, P.D__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_117})

V_86 = Vertex(name = 'V_86',
              particles = [ P.D__minus__, P.D__minus__, P.D__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_117})

V_87 = Vertex(name = 'V_87',
              particles = [ P.D__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_118})

V_88 = Vertex(name = 'V_88',
              particles = [ P.D__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_118})

V_89 = Vertex(name = 'V_89',
              particles = [ P.D__plus__, P.D__plus__, P.G__minus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_116})

V_90 = Vertex(name = 'V_90',
              particles = [ P.D__minus__, P.D__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_116})

V_91 = Vertex(name = 'V_91',
              particles = [ P.D0, P.D0, P.D__minus__, P.D__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_151})

V_92 = Vertex(name = 'V_92',
              particles = [ P.D__minus__, P.D__plus__, P.D__minus____minus__, P.D__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_132})

V_93 = Vertex(name = 'V_93',
              particles = [ P.D0, P.D__plus__, P.D__plus__, P.D__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_128})

V_94 = Vertex(name = 'V_94',
              particles = [ P.D0, P.D__minus__, P.D__minus__, P.D__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_128})

V_95 = Vertex(name = 'V_95',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_150})

V_96 = Vertex(name = 'V_96',
              particles = [ P.D0, P.D0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_153})

V_97 = Vertex(name = 'V_97',
              particles = [ P.D__minus____minus__, P.D__plus____plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_130})

V_98 = Vertex(name = 'V_98',
              particles = [ P.D__minus__, P.D__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_152})

V_99 = Vertex(name = 'V_99',
              particles = [ P.D0, P.D__plus__, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_154})

V_100 = Vertex(name = 'V_100',
               particles = [ P.D__minus__, P.D__plus____plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_133})

V_101 = Vertex(name = 'V_101',
               particles = [ P.D0, P.D__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_154})

V_102 = Vertex(name = 'V_102',
               particles = [ P.D__plus__, P.D__minus____minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_133})

V_103 = Vertex(name = 'V_103',
               particles = [ P.D__plus____plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_81})

V_104 = Vertex(name = 'V_104',
               particles = [ P.D__plus____plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_156})

V_105 = Vertex(name = 'V_105',
               particles = [ P.D__minus____minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_81})

V_106 = Vertex(name = 'V_106',
               particles = [ P.D__minus____minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_156})

V_107 = Vertex(name = 'V_107',
               particles = [ P.D__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_134})

V_108 = Vertex(name = 'V_108',
               particles = [ P.D__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_159})

V_109 = Vertex(name = 'V_109',
               particles = [ P.D__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_134})

V_110 = Vertex(name = 'V_110',
               particles = [ P.D__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_159})

V_111 = Vertex(name = 'V_111',
               particles = [ P.D0, P.D__minus__, P.D__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_144})

V_112 = Vertex(name = 'V_112',
               particles = [ P.D__plus__, P.D__plus__, P.D__minus____minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_123})

V_113 = Vertex(name = 'V_113',
               particles = [ P.D__minus__, P.D__minus__, P.D__plus____plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_123})

V_114 = Vertex(name = 'V_114',
               particles = [ P.D0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_146})

V_115 = Vertex(name = 'V_115',
               particles = [ P.D0, P.D0, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_147})

V_116 = Vertex(name = 'V_116',
               particles = [ P.D0, P.D__minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_145})

V_117 = Vertex(name = 'V_117',
               particles = [ P.D0, P.D0, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_147})

V_118 = Vertex(name = 'V_118',
               particles = [ P.D0, P.D__plus__, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_145})

V_119 = Vertex(name = 'V_119',
               particles = [ P.D__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_148})

V_120 = Vertex(name = 'V_120',
               particles = [ P.D__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_148})

V_121 = Vertex(name = 'V_121',
               particles = [ P.D0, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_149})

V_122 = Vertex(name = 'V_122',
               particles = [ P.D0, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_162})

V_123 = Vertex(name = 'V_123',
               particles = [ P.D0, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_149})

V_124 = Vertex(name = 'V_124',
               particles = [ P.D0, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_162})

V_125 = Vertex(name = 'V_125',
               particles = [ P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_160})

V_126 = Vertex(name = 'V_126',
               particles = [ P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_84})

V_127 = Vertex(name = 'V_127',
               particles = [ P.D__minus__, P.D__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_161})

V_128 = Vertex(name = 'V_128',
               particles = [ P.D__minus__, P.D__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_83})

V_129 = Vertex(name = 'V_129',
               particles = [ P.D__minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_155})

V_130 = Vertex(name = 'V_130',
               particles = [ P.D__minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_82})

V_131 = Vertex(name = 'V_131',
               particles = [ P.D__plus__, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_155})

V_132 = Vertex(name = 'V_132',
               particles = [ P.D__plus__, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_82})

V_133 = Vertex(name = 'V_133',
               particles = [ P.D0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_157})

V_134 = Vertex(name = 'V_134',
               particles = [ P.D0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_86})

V_135 = Vertex(name = 'V_135',
               particles = [ P.D0, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_158})

V_136 = Vertex(name = 'V_136',
               particles = [ P.D0, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_87})

V_137 = Vertex(name = 'V_137',
               particles = [ P.D__plus__, P.D__minus____minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_122})

V_138 = Vertex(name = 'V_138',
               particles = [ P.D__minus__, P.D__minus____minus__, P.D__plus____plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_122})

V_139 = Vertex(name = 'V_139',
               particles = [ P.D__plus____plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_143})

V_140 = Vertex(name = 'V_140',
               particles = [ P.D__minus____minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_143})

V_141 = Vertex(name = 'V_141',
               particles = [ P.D0, P.D__plus____plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_131})

V_142 = Vertex(name = 'V_142',
               particles = [ P.D0, P.D__minus____minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_131})

V_143 = Vertex(name = 'V_143',
               particles = [ P.D__plus__, P.D__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_129})

V_144 = Vertex(name = 'V_144',
               particles = [ P.D__plus__, P.D__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_88})

V_145 = Vertex(name = 'V_145',
               particles = [ P.D__minus__, P.D__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_129})

V_146 = Vertex(name = 'V_146',
               particles = [ P.D__minus__, P.D__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_88})

V_147 = Vertex(name = 'V_147',
               particles = [ P.chi, P.chi, P.chi, P.chi ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_186})

V_148 = Vertex(name = 'V_148',
               particles = [ P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_185})

V_149 = Vertex(name = 'V_149',
               particles = [ P.chi, P.chi, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_187})

V_150 = Vertex(name = 'V_150',
               particles = [ P.chi, P.chi, P.chi, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_183})

V_151 = Vertex(name = 'V_151',
               particles = [ P.chi, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_184})

V_152 = Vertex(name = 'V_152',
               particles = [ P.chi, P.chi, P.D0, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_208})

V_153 = Vertex(name = 'V_153',
               particles = [ P.chi, P.chi, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_196})

V_154 = Vertex(name = 'V_154',
               particles = [ P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_207})

V_155 = Vertex(name = 'V_155',
               particles = [ P.D0, P.D0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_209})

V_156 = Vertex(name = 'V_156',
               particles = [ P.D__minus____minus__, P.D__plus____plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_195})

V_157 = Vertex(name = 'V_157',
               particles = [ P.chi, P.chi, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_210})

V_158 = Vertex(name = 'V_158',
               particles = [ P.D0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_192})

V_159 = Vertex(name = 'V_159',
               particles = [ P.D0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_213})

V_160 = Vertex(name = 'V_160',
               particles = [ P.chi, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_197})

V_161 = Vertex(name = 'V_161',
               particles = [ P.chi, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_212})

V_162 = Vertex(name = 'V_162',
               particles = [ P.chi, P.chi, P.D0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_203})

V_163 = Vertex(name = 'V_163',
               particles = [ P.D0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_204})

V_164 = Vertex(name = 'V_164',
               particles = [ P.chi, P.D0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_206})

V_165 = Vertex(name = 'V_165',
               particles = [ P.chi, P.D0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_211})

V_166 = Vertex(name = 'V_166',
               particles = [ P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_189})

V_167 = Vertex(name = 'V_167',
               particles = [ P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_215})

V_168 = Vertex(name = 'V_168',
               particles = [ P.chi, P.chi, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_216})

V_169 = Vertex(name = 'V_169',
               particles = [ P.chi, P.chi, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_205})

V_170 = Vertex(name = 'V_170',
               particles = [ P.chi, P.chi, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_214})

V_171 = Vertex(name = 'V_171',
               particles = [ P.chi, P.chi, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_198})

V_172 = Vertex(name = 'V_172',
               particles = [ P.chi, P.D0, P.D0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_193})

V_173 = Vertex(name = 'V_173',
               particles = [ P.chi, P.D__minus____minus__, P.D__plus____plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_188})

V_174 = Vertex(name = 'V_174',
               particles = [ P.chi, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_194})

V_175 = Vertex(name = 'V_175',
               particles = [ P.chi, P.D0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_191})

V_176 = Vertex(name = 'V_176',
               particles = [ P.chi, P.chi, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_222})

V_177 = Vertex(name = 'V_177',
               particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_221})

V_178 = Vertex(name = 'V_178',
               particles = [ P.D__minus__, P.D__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_223})

V_179 = Vertex(name = 'V_179',
               particles = [ P.chi, P.chi, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_224})

V_180 = Vertex(name = 'V_180',
               particles = [ P.chi, P.D__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_225})

V_181 = Vertex(name = 'V_181',
               particles = [ P.chi, P.D__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_225})

V_182 = Vertex(name = 'V_182',
               particles = [ P.chi, P.D__minus__, P.D__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_217})

V_183 = Vertex(name = 'V_183',
               particles = [ P.chi, P.chi, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_220})

V_184 = Vertex(name = 'V_184',
               particles = [ P.chi, P.chi, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_220})

V_185 = Vertex(name = 'V_185',
               particles = [ P.D__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_219})

V_186 = Vertex(name = 'V_186',
               particles = [ P.D__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_219})

V_187 = Vertex(name = 'V_187',
               particles = [ P.chi, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_218})

V_188 = Vertex(name = 'V_188',
               particles = [ P.chi, P.D__plus__, P.D__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_240})

V_189 = Vertex(name = 'V_189',
               particles = [ P.chi, P.D__minus__, P.D__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_242})

V_190 = Vertex(name = 'V_190',
               particles = [ P.D0, P.D__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_230})

V_191 = Vertex(name = 'V_191',
               particles = [ P.D__minus__, P.D__plus____plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_238})

V_192 = Vertex(name = 'V_192',
               particles = [ P.D0, P.D__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_231})

V_193 = Vertex(name = 'V_193',
               particles = [ P.D__plus__, P.D__minus____minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_239})

V_194 = Vertex(name = 'V_194',
               particles = [ P.chi, P.D__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_231})

V_195 = Vertex(name = 'V_195',
               particles = [ P.chi, P.D__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_230})

V_196 = Vertex(name = 'V_196',
               particles = [ P.D__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_97})

V_197 = Vertex(name = 'V_197',
               particles = [ P.D__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_106})

V_198 = Vertex(name = 'V_198',
               particles = [ P.D__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_98})

V_199 = Vertex(name = 'V_199',
               particles = [ P.D__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_105})

V_200 = Vertex(name = 'V_200',
               particles = [ P.chi, P.D0, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_227})

V_201 = Vertex(name = 'V_201',
               particles = [ P.chi, P.D0, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_226})

V_202 = Vertex(name = 'V_202',
               particles = [ P.D__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_227})

V_203 = Vertex(name = 'V_203',
               particles = [ P.D__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_226})

V_204 = Vertex(name = 'V_204',
               particles = [ P.chi, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_235})

V_205 = Vertex(name = 'V_205',
               particles = [ P.chi, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_102})

V_206 = Vertex(name = 'V_206',
               particles = [ P.chi, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_234})

V_207 = Vertex(name = 'V_207',
               particles = [ P.chi, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_101})

V_208 = Vertex(name = 'V_208',
               particles = [ P.D__plus__, P.D__plus__, P.D__minus____minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_237})

V_209 = Vertex(name = 'V_209',
               particles = [ P.D__minus__, P.D__minus__, P.D__plus____plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_236})

V_210 = Vertex(name = 'V_210',
               particles = [ P.chi, P.D__minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_247})

V_211 = Vertex(name = 'V_211',
               particles = [ P.chi, P.D__plus__, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_246})

V_212 = Vertex(name = 'V_212',
               particles = [ P.D__plus____plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_245})

V_213 = Vertex(name = 'V_213',
               particles = [ P.D__minus____minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_244})

V_214 = Vertex(name = 'V_214',
               particles = [ P.chi, P.D__plus____plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_241})

V_215 = Vertex(name = 'V_215',
               particles = [ P.chi, P.D__minus____minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_243})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.a, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_217 = Vertex(name = 'V_217',
               particles = [ P.a, P.a, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_218 = Vertex(name = 'V_218',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_219 = Vertex(name = 'V_219',
               particles = [ P.a, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_220 = Vertex(name = 'V_220',
               particles = [ P.a, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_5})

V_221 = Vertex(name = 'V_221',
               particles = [ P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_222 = Vertex(name = 'V_222',
               particles = [ P.a, P.W__minus__, P.D0, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_180})

V_223 = Vertex(name = 'V_223',
               particles = [ P.a, P.W__minus__, P.D__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_224 = Vertex(name = 'V_224',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_179})

V_225 = Vertex(name = 'V_225',
               particles = [ P.a, P.W__minus__, P.D0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_226 = Vertex(name = 'V_226',
               particles = [ P.a, P.W__minus__, P.D__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_172})

V_227 = Vertex(name = 'V_227',
               particles = [ P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_95})

V_228 = Vertex(name = 'V_228',
               particles = [ P.a, P.W__minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_94})

V_229 = Vertex(name = 'V_229',
               particles = [ P.a, P.W__minus__, P.chi, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_230 = Vertex(name = 'V_230',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_114})

V_231 = Vertex(name = 'V_231',
               particles = [ P.a, P.W__minus__, P.D__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_108})

V_232 = Vertex(name = 'V_232',
               particles = [ P.W__minus__, P.chi, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_110})

V_233 = Vertex(name = 'V_233',
               particles = [ P.W__minus__, P.D0, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_177})

V_234 = Vertex(name = 'V_234',
               particles = [ P.W__minus__, P.D0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_167})

V_235 = Vertex(name = 'V_235',
               particles = [ P.W__minus__, P.D__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_90})

V_236 = Vertex(name = 'V_236',
               particles = [ P.W__minus__, P.D__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_169})

V_237 = Vertex(name = 'V_237',
               particles = [ P.W__minus__, P.D__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_107})

V_238 = Vertex(name = 'V_238',
               particles = [ P.W__minus__, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_92})

V_239 = Vertex(name = 'V_239',
               particles = [ P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_113})

V_240 = Vertex(name = 'V_240',
               particles = [ P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_176})

V_241 = Vertex(name = 'V_241',
               particles = [ P.W__minus__, P.W__minus__, P.D0, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_242 = Vertex(name = 'V_242',
               particles = [ P.W__minus__, P.W__minus__, P.D__plus____plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_243 = Vertex(name = 'V_243',
               particles = [ P.W__minus__, P.W__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_70})

V_244 = Vertex(name = 'V_244',
               particles = [ P.W__minus__, P.W__minus__, P.chi, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_100})

V_245 = Vertex(name = 'V_245',
               particles = [ P.W__minus__, P.W__minus__, P.D__plus____plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_104})

V_246 = Vertex(name = 'V_246',
               particles = [ P.a, P.W__plus__, P.D0, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_180})

V_247 = Vertex(name = 'V_247',
               particles = [ P.a, P.W__plus__, P.D__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_248 = Vertex(name = 'V_248',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_179})

V_249 = Vertex(name = 'V_249',
               particles = [ P.a, P.W__plus__, P.D0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_250 = Vertex(name = 'V_250',
               particles = [ P.a, P.W__plus__, P.D__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_172})

V_251 = Vertex(name = 'V_251',
               particles = [ P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_95})

V_252 = Vertex(name = 'V_252',
               particles = [ P.a, P.W__plus__, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_94})

V_253 = Vertex(name = 'V_253',
               particles = [ P.a, P.W__plus__, P.chi, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_112})

V_254 = Vertex(name = 'V_254',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_115})

V_255 = Vertex(name = 'V_255',
               particles = [ P.a, P.W__plus__, P.D__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_256 = Vertex(name = 'V_256',
               particles = [ P.W__plus__, P.chi, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_110})

V_257 = Vertex(name = 'V_257',
               particles = [ P.W__plus__, P.D0, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_178})

V_258 = Vertex(name = 'V_258',
               particles = [ P.W__plus__, P.D0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_168})

V_259 = Vertex(name = 'V_259',
               particles = [ P.W__plus__, P.D__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_170})

V_260 = Vertex(name = 'V_260',
               particles = [ P.W__plus__, P.D__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_107})

V_261 = Vertex(name = 'V_261',
               particles = [ P.W__plus__, P.D__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_89})

V_262 = Vertex(name = 'V_262',
               particles = [ P.W__plus__, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_93})

V_263 = Vertex(name = 'V_263',
               particles = [ P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_113})

V_264 = Vertex(name = 'V_264',
               particles = [ P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_175})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__minus__, P.W__plus__, P.D0, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_48})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__minus__, P.W__plus__, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_49})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__minus__, P.W__plus__, P.D0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_269 = Vertex(name = 'V_269',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_75})

V_270 = Vertex(name = 'V_270',
               particles = [ P.W__minus__, P.W__plus__, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_72})

V_271 = Vertex(name = 'V_271',
               particles = [ P.W__minus__, P.W__plus__, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_135})

V_272 = Vertex(name = 'V_272',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_136})

V_273 = Vertex(name = 'V_273',
               particles = [ P.W__minus__, P.W__plus__, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_85})

V_274 = Vertex(name = 'V_274',
               particles = [ P.W__minus__, P.W__plus__, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_85})

V_275 = Vertex(name = 'V_275',
               particles = [ P.W__minus__, P.W__plus__, P.chi, P.chi ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_199})

V_276 = Vertex(name = 'V_276',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_200})

V_277 = Vertex(name = 'V_277',
               particles = [ P.W__minus__, P.W__plus__, P.chi, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_278 = Vertex(name = 'V_278',
               particles = [ P.W__plus__, P.W__plus__, P.D0, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_279 = Vertex(name = 'V_279',
               particles = [ P.W__plus__, P.W__plus__, P.D__minus____minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_280 = Vertex(name = 'V_280',
               particles = [ P.W__plus__, P.W__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_70})

V_281 = Vertex(name = 'V_281',
               particles = [ P.W__plus__, P.W__plus__, P.chi, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_99})

V_282 = Vertex(name = 'V_282',
               particles = [ P.W__plus__, P.W__plus__, P.D__minus____minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_103})

V_283 = Vertex(name = 'V_283',
               particles = [ P.a, P.Z, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_37})

V_284 = Vertex(name = 'V_284',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_140})

V_285 = Vertex(name = 'V_285',
               particles = [ P.a, P.Z, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_139})

V_286 = Vertex(name = 'V_286',
               particles = [ P.a, P.Z, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_287 = Vertex(name = 'V_287',
               particles = [ P.a, P.Z, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_288 = Vertex(name = 'V_288',
               particles = [ P.Z, P.chi, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_233})

V_289 = Vertex(name = 'V_289',
               particles = [ P.Z, P.chi, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_228})

V_290 = Vertex(name = 'V_290',
               particles = [ P.Z, P.D0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_229})

V_291 = Vertex(name = 'V_291',
               particles = [ P.Z, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_137})

V_292 = Vertex(name = 'V_292',
               particles = [ P.Z, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_125})

V_293 = Vertex(name = 'V_293',
               particles = [ P.Z, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_124})

V_294 = Vertex(name = 'V_294',
               particles = [ P.Z, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_36})

V_295 = Vertex(name = 'V_295',
               particles = [ P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_232})

V_296 = Vertex(name = 'V_296',
               particles = [ P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_138})

V_297 = Vertex(name = 'V_297',
               particles = [ P.W__minus__, P.Z, P.D0, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_173})

V_298 = Vertex(name = 'V_298',
               particles = [ P.W__minus__, P.Z, P.D__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_163})

V_299 = Vertex(name = 'V_299',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_174})

V_300 = Vertex(name = 'V_300',
               particles = [ P.W__minus__, P.Z, P.D0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_166})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__minus__, P.Z, P.D__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_164})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_182})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__minus__, P.Z, P.D__plus____plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_165})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__minus__, P.Z, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_181})

V_305 = Vertex(name = 'V_305',
               particles = [ P.W__minus__, P.Z, P.chi, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_253})

V_306 = Vertex(name = 'V_306',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_255})

V_307 = Vertex(name = 'V_307',
               particles = [ P.W__minus__, P.Z, P.D__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_251})

V_308 = Vertex(name = 'V_308',
               particles = [ P.W__minus__, P.Z, P.chi, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_249})

V_309 = Vertex(name = 'V_309',
               particles = [ P.W__plus__, P.Z, P.D0, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_173})

V_310 = Vertex(name = 'V_310',
               particles = [ P.W__plus__, P.Z, P.D__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_163})

V_311 = Vertex(name = 'V_311',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_174})

V_312 = Vertex(name = 'V_312',
               particles = [ P.W__plus__, P.Z, P.D0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_166})

V_313 = Vertex(name = 'V_313',
               particles = [ P.W__plus__, P.Z, P.D__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_164})

V_314 = Vertex(name = 'V_314',
               particles = [ P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_182})

V_315 = Vertex(name = 'V_315',
               particles = [ P.W__plus__, P.Z, P.D__minus____minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_165})

V_316 = Vertex(name = 'V_316',
               particles = [ P.W__plus__, P.Z, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_181})

V_317 = Vertex(name = 'V_317',
               particles = [ P.W__plus__, P.Z, P.chi, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_252})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_254})

V_319 = Vertex(name = 'V_319',
               particles = [ P.W__plus__, P.Z, P.D__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_250})

V_320 = Vertex(name = 'V_320',
               particles = [ P.W__plus__, P.Z, P.chi, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_248})

V_321 = Vertex(name = 'V_321',
               particles = [ P.Z, P.Z, P.D0, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_50})

V_322 = Vertex(name = 'V_322',
               particles = [ P.Z, P.Z, P.D__minus____minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_38})

V_323 = Vertex(name = 'V_323',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_51})

V_324 = Vertex(name = 'V_324',
               particles = [ P.Z, P.Z, P.D0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_325 = Vertex(name = 'V_325',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_76})

V_326 = Vertex(name = 'V_326',
               particles = [ P.Z, P.Z, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_73})

V_327 = Vertex(name = 'V_327',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_142})

V_328 = Vertex(name = 'V_328',
               particles = [ P.Z, P.Z, P.D__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_141})

V_329 = Vertex(name = 'V_329',
               particles = [ P.Z, P.Z, P.D__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_127})

V_330 = Vertex(name = 'V_330',
               particles = [ P.Z, P.Z, P.D__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_127})

V_331 = Vertex(name = 'V_331',
               particles = [ P.Z, P.Z, P.chi, P.chi ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_201})

V_332 = Vertex(name = 'V_332',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_202})

V_333 = Vertex(name = 'V_333',
               particles = [ P.Z, P.Z, P.chi, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_190})

V_334 = Vertex(name = 'V_334',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_314,(0,1):C.GC_258})

V_335 = Vertex(name = 'V_335',
               particles = [ P.b__tilde__, P.t, P.D__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_315,(0,1):C.GC_259})

V_336 = Vertex(name = 'V_336',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_312,(0,1):C.GC_312})

V_337 = Vertex(name = 'V_337',
               particles = [ P.t__tilde__, P.t, P.D0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_313,(0,1):C.GC_313})

V_338 = Vertex(name = 'V_338',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_317,(0,1):C.GC_316})

V_339 = Vertex(name = 'V_339',
               particles = [ P.t__tilde__, P.t, P.chi ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_318,(0,1):C.GC_319})

V_340 = Vertex(name = 'V_340',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_258,(0,1):C.GC_314})

V_341 = Vertex(name = 'V_341',
               particles = [ P.t__tilde__, P.b, P.D__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_259,(0,1):C.GC_315})

V_342 = Vertex(name = 'V_342',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_256,(0,1):C.GC_256})

V_343 = Vertex(name = 'V_343',
               particles = [ P.b__tilde__, P.b, P.D0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_257,(0,1):C.GC_257})

V_344 = Vertex(name = 'V_344',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_260,(0,1):C.GC_261})

V_345 = Vertex(name = 'V_345',
               particles = [ P.b__tilde__, P.b, P.chi ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_263,(0,1):C.GC_262})

V_346 = Vertex(name = 'V_346',
               particles = [ P.v1, P.ta__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_322,(0,1):C.GC_375})

V_347 = Vertex(name = 'V_347',
               particles = [ P.v1, P.ta__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_374,(0,0):C.GC_325})

V_348 = Vertex(name = 'V_348',
               particles = [ P.v2, P.ta__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_381})

V_349 = Vertex(name = 'V_349',
               particles = [ P.v2, P.ta__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_380,(0,0):C.GC_326})

V_350 = Vertex(name = 'V_350',
               particles = [ P.v3, P.ta__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_324,(0,1):C.GC_391})

V_351 = Vertex(name = 'V_351',
               particles = [ P.v3, P.ta__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_390,(0,0):C.GC_327})

V_352 = Vertex(name = 'V_352',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_320,(0,1):C.GC_320})

V_353 = Vertex(name = 'V_353',
               particles = [ P.ta__plus__, P.ta__minus__, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_321,(0,1):C.GC_321})

V_354 = Vertex(name = 'V_354',
               particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_328,(0,1):C.GC_329})

V_355 = Vertex(name = 'V_355',
               particles = [ P.ta__plus__, P.ta__minus__, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_331,(0,1):C.GC_330})

V_356 = Vertex(name = 'V_356',
               particles = [ P.v1, P.v1, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_376})

V_357 = Vertex(name = 'V_357',
               particles = [ P.v1, P.v1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_288,(0,1):C.GC_377})

V_358 = Vertex(name = 'V_358',
               particles = [ P.v1, P.v1, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_300,(0,1):C.GC_378})

V_359 = Vertex(name = 'V_359',
               particles = [ P.v1, P.v1, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_306,(0,1):C.GC_379})

V_360 = Vertex(name = 'V_360',
               particles = [ P.v2, P.v1, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_382})

V_361 = Vertex(name = 'V_361',
               particles = [ P.v2, P.v1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_383})

V_362 = Vertex(name = 'V_362',
               particles = [ P.v2, P.v1, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_301,(0,1):C.GC_384})

V_363 = Vertex(name = 'V_363',
               particles = [ P.v2, P.v1, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_307,(0,1):C.GC_385})

V_364 = Vertex(name = 'V_364',
               particles = [ P.v3, P.v1, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_285,(0,1):C.GC_392})

V_365 = Vertex(name = 'V_365',
               particles = [ P.v3, P.v1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_291,(0,1):C.GC_393})

V_366 = Vertex(name = 'V_366',
               particles = [ P.v3, P.v1, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_303,(0,1):C.GC_394})

V_367 = Vertex(name = 'V_367',
               particles = [ P.v3, P.v1, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_309,(0,1):C.GC_395})

V_368 = Vertex(name = 'V_368',
               particles = [ P.v2, P.v2, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_386})

V_369 = Vertex(name = 'V_369',
               particles = [ P.v2, P.v2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_290,(0,1):C.GC_387})

V_370 = Vertex(name = 'V_370',
               particles = [ P.v2, P.v2, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_302,(0,1):C.GC_388})

V_371 = Vertex(name = 'V_371',
               particles = [ P.v2, P.v2, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_308,(0,1):C.GC_389})

V_372 = Vertex(name = 'V_372',
               particles = [ P.v3, P.v2, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_396})

V_373 = Vertex(name = 'V_373',
               particles = [ P.v3, P.v2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_292,(0,1):C.GC_397})

V_374 = Vertex(name = 'V_374',
               particles = [ P.v3, P.v2, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_304,(0,1):C.GC_398})

V_375 = Vertex(name = 'V_375',
               particles = [ P.v3, P.v2, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_310,(0,1):C.GC_399})

V_376 = Vertex(name = 'V_376',
               particles = [ P.v3, P.v3, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_400})

V_377 = Vertex(name = 'V_377',
               particles = [ P.v3, P.v3, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_293,(0,1):C.GC_401})

V_378 = Vertex(name = 'V_378',
               particles = [ P.v3, P.v3, P.chi ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_305,(0,1):C.GC_402})

V_379 = Vertex(name = 'V_379',
               particles = [ P.v3, P.v3, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_311,(0,1):C.GC_403})

V_380 = Vertex(name = 'V_380',
               particles = [ P.e__minus__, P.e__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_356})

V_381 = Vertex(name = 'V_381',
               particles = [ P.mu__minus__, P.e__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_357})

V_382 = Vertex(name = 'V_382',
               particles = [ P.ta__minus__, P.e__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_359})

V_383 = Vertex(name = 'V_383',
               particles = [ P.mu__minus__, P.mu__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_358})

V_384 = Vertex(name = 'V_384',
               particles = [ P.ta__minus__, P.mu__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_366})

V_385 = Vertex(name = 'V_385',
               particles = [ P.ta__minus__, P.ta__minus__, P.D__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_373})

V_386 = Vertex(name = 'V_386',
               particles = [ P.v1, P.e__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_360})

V_387 = Vertex(name = 'V_387',
               particles = [ P.v1, P.e__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_361})

V_388 = Vertex(name = 'V_388',
               particles = [ P.v2, P.e__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_362})

V_389 = Vertex(name = 'V_389',
               particles = [ P.v2, P.e__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_363})

V_390 = Vertex(name = 'V_390',
               particles = [ P.v3, P.e__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_364})

V_391 = Vertex(name = 'V_391',
               particles = [ P.v3, P.e__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_365})

V_392 = Vertex(name = 'V_392',
               particles = [ P.v1, P.mu__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_367})

V_393 = Vertex(name = 'V_393',
               particles = [ P.v1, P.mu__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_368})

V_394 = Vertex(name = 'V_394',
               particles = [ P.v2, P.mu__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_369})

V_395 = Vertex(name = 'V_395',
               particles = [ P.v2, P.mu__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_370})

V_396 = Vertex(name = 'V_396',
               particles = [ P.v3, P.mu__minus__, P.D__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_371})

V_397 = Vertex(name = 'V_397',
               particles = [ P.v3, P.mu__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_372})

V_398 = Vertex(name = 'V_398',
               particles = [ P.e__plus__, P.e__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_264})

V_399 = Vertex(name = 'V_399',
               particles = [ P.e__plus__, P.v1, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_268})

V_400 = Vertex(name = 'V_400',
               particles = [ P.e__plus__, P.v1, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_271})

V_401 = Vertex(name = 'V_401',
               particles = [ P.e__plus__, P.v2, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_269})

V_402 = Vertex(name = 'V_402',
               particles = [ P.e__plus__, P.v2, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_272})

V_403 = Vertex(name = 'V_403',
               particles = [ P.e__plus__, P.v3, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_270})

V_404 = Vertex(name = 'V_404',
               particles = [ P.e__plus__, P.v3, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_273})

V_405 = Vertex(name = 'V_405',
               particles = [ P.mu__plus__, P.e__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_265})

V_406 = Vertex(name = 'V_406',
               particles = [ P.mu__plus__, P.v1, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_275})

V_407 = Vertex(name = 'V_407',
               particles = [ P.mu__plus__, P.v1, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_278})

V_408 = Vertex(name = 'V_408',
               particles = [ P.mu__plus__, P.v2, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_276})

V_409 = Vertex(name = 'V_409',
               particles = [ P.mu__plus__, P.v2, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_279})

V_410 = Vertex(name = 'V_410',
               particles = [ P.mu__plus__, P.v3, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_277})

V_411 = Vertex(name = 'V_411',
               particles = [ P.mu__plus__, P.v3, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_280})

V_412 = Vertex(name = 'V_412',
               particles = [ P.ta__plus__, P.e__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_267})

V_413 = Vertex(name = 'V_413',
               particles = [ P.ta__plus__, P.v1, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_294,(0,1):C.GC_340})

V_414 = Vertex(name = 'V_414',
               particles = [ P.ta__plus__, P.v1, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_297,(0,1):C.GC_339})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ta__plus__, P.v2, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_295,(0,1):C.GC_346})

V_416 = Vertex(name = 'V_416',
               particles = [ P.ta__plus__, P.v2, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_298,(0,1):C.GC_345})

V_417 = Vertex(name = 'V_417',
               particles = [ P.ta__plus__, P.v3, P.D__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_296,(0,1):C.GC_352})

V_418 = Vertex(name = 'V_418',
               particles = [ P.ta__plus__, P.v3, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_299,(0,1):C.GC_351})

V_419 = Vertex(name = 'V_419',
               particles = [ P.mu__plus__, P.mu__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_266})

V_420 = Vertex(name = 'V_420',
               particles = [ P.ta__plus__, P.mu__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_274})

V_421 = Vertex(name = 'V_421',
               particles = [ P.ta__plus__, P.ta__plus__, P.D__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_281})

V_422 = Vertex(name = 'V_422',
               particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_3})

V_423 = Vertex(name = 'V_423',
               particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_4})

V_424 = Vertex(name = 'V_424',
               particles = [ P.ghWm, P.ghA__tilde__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_62})

V_425 = Vertex(name = 'V_425',
               particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_3})

V_426 = Vertex(name = 'V_426',
               particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_60})

V_427 = Vertex(name = 'V_427',
               particles = [ P.ghWm, P.ghWm__tilde__, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_63})

V_428 = Vertex(name = 'V_428',
               particles = [ P.ghWm, P.ghWm__tilde__, P.chi ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_59})

V_429 = Vertex(name = 'V_429',
               particles = [ P.ghWm, P.ghWm__tilde__, P.a ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_4})

V_430 = Vertex(name = 'V_430',
               particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_19})

V_431 = Vertex(name = 'V_431',
               particles = [ P.ghWm, P.ghZ__tilde__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_66})

V_432 = Vertex(name = 'V_432',
               particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_18})

V_433 = Vertex(name = 'V_433',
               particles = [ P.ghWp, P.ghA__tilde__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_61})

V_434 = Vertex(name = 'V_434',
               particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_4})

V_435 = Vertex(name = 'V_435',
               particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_60})

V_436 = Vertex(name = 'V_436',
               particles = [ P.ghWp, P.ghWp__tilde__, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_63})

V_437 = Vertex(name = 'V_437',
               particles = [ P.ghWp, P.ghWp__tilde__, P.chi ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_58})

V_438 = Vertex(name = 'V_438',
               particles = [ P.ghWp, P.ghWp__tilde__, P.a ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_3})

V_439 = Vertex(name = 'V_439',
               particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_18})

V_440 = Vertex(name = 'V_440',
               particles = [ P.ghWp, P.ghZ__tilde__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_65})

V_441 = Vertex(name = 'V_441',
               particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_19})

V_442 = Vertex(name = 'V_442',
               particles = [ P.ghZ, P.ghWm__tilde__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_67})

V_443 = Vertex(name = 'V_443',
               particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_18})

V_444 = Vertex(name = 'V_444',
               particles = [ P.ghZ, P.ghWp__tilde__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_64})

V_445 = Vertex(name = 'V_445',
               particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_19})

V_446 = Vertex(name = 'V_446',
               particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_68})

V_447 = Vertex(name = 'V_447',
               particles = [ P.ghZ, P.ghZ__tilde__, P.D0 ],
               color = [ '1' ],
               lorentz = [ L.UUS1 ],
               couplings = {(0,0):C.GC_69})

V_448 = Vertex(name = 'V_448',
               particles = [ P.ghG, P.ghG__tilde__, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.UUV1 ],
               couplings = {(0,0):C.GC_9})

