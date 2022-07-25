# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Mon 15 Jul 2019 15:02:48



from .object_library import all_parameters, Parameter


from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# custom UFO pimping
UVcut = Parameter(name = 'UVcut',
                  nature = 'external',
                  type = 'real',
                  value = 10000.,
                  texname = '\\text{UVcut}',
                  lhablock = 'UVcut',
                  lhacode = [ 1 ])


# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

gAl1x1 = Parameter(name = 'gAl1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl1x1}',
                   lhablock = 'gAl',
                   lhacode = [ 1, 1 ])

gAl1x2 = Parameter(name = 'gAl1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl1x2}',
                   lhablock = 'gAl',
                   lhacode = [ 1, 2 ])

gAl1x3 = Parameter(name = 'gAl1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl1x3}',
                   lhablock = 'gAl',
                   lhacode = [ 1, 3 ])

gAl2x1 = Parameter(name = 'gAl2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl2x1}',
                   lhablock = 'gAl',
                   lhacode = [ 2, 1 ])

gAl2x2 = Parameter(name = 'gAl2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl2x2}',
                   lhablock = 'gAl',
                   lhacode = [ 2, 2 ])

gAl2x3 = Parameter(name = 'gAl2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl2x3}',
                   lhablock = 'gAl',
                   lhacode = [ 2, 3 ])

gAl3x1 = Parameter(name = 'gAl3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl3x1}',
                   lhablock = 'gAl',
                   lhacode = [ 3, 1 ])

gAl3x2 = Parameter(name = 'gAl3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl3x2}',
                   lhablock = 'gAl',
                   lhacode = [ 3, 2 ])

gAl3x3 = Parameter(name = 'gAl3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gAl3x3}',
                   lhablock = 'gAl',
                   lhacode = [ 3, 3 ])

gVl1x1 = Parameter(name = 'gVl1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl1x1}',
                   lhablock = 'gVl',
                   lhacode = [ 1, 1 ])

gVl1x2 = Parameter(name = 'gVl1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl1x2}',
                   lhablock = 'gVl',
                   lhacode = [ 1, 2 ])

gVl1x3 = Parameter(name = 'gVl1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl1x3}',
                   lhablock = 'gVl',
                   lhacode = [ 1, 3 ])

gVl2x1 = Parameter(name = 'gVl2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl2x1}',
                   lhablock = 'gVl',
                   lhacode = [ 2, 1 ])

gVl2x2 = Parameter(name = 'gVl2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{gVl2x2}',
                   lhablock = 'gVl',
                   lhacode = [ 2, 2 ])

gVl2x3 = Parameter(name = 'gVl2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl2x3}',
                   lhablock = 'gVl',
                   lhacode = [ 2, 3 ])

gVl3x1 = Parameter(name = 'gVl3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl3x1}',
                   lhablock = 'gVl',
                   lhacode = [ 3, 1 ])

gVl3x2 = Parameter(name = 'gVl3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{gVl3x2}',
                   lhablock = 'gVl',
                   lhacode = [ 3, 2 ])

gVl3x3 = Parameter(name = 'gVl3x3',
                   nature = 'external',
                   type = 'real',
                   value = -1.,
                   texname = '\\text{gVl3x3}',
                   lhablock = 'gVl',
                   lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 132.50698,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116639,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 173.3,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

g1p = Parameter(name = 'g1p',
                nature = 'external',
                type = 'real',
                value = 0.2,
                texname = 'g_Z',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

MZp = Parameter(name = 'MZp',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MZp}',
                lhablock = 'MASS',
                lhacode = [ 9000001 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.188,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173.3,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.7,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 9000001 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.35,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00417,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

