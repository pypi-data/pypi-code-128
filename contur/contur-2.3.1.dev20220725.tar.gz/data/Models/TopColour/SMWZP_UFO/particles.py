# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Fri 11 Dec 2020 18:33:57


from __future__ import division
from .object_library import all_particles, Particle
from . import parameters as Param

from . import propagators as Prop

A = Particle(pdg_code = 22,
             name = 'A',
             antiname = 'A',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = '\\gamma',
             antitexname = '\\gamma',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Zp = Particle(pdg_code = 9000001,
              name = 'Zp',
              antiname = 'Zp',
              spin = 3,
              color = 1,
              mass = Param.MZp,
              width = Param.WZp,
              texname = 'Z\'',
              antitexname = 'Z\'',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W^+',
                     antitexname = 'W^-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

Wp__plus__ = Particle(pdg_code = 9000002,
                      name = 'Wp+',
                      antiname = 'Wp-',
                      spin = 3,
                      color = 1,
                      mass = Param.MWp,
                      width = Param.WWp,
                      texname = 'W\'^+',
                      antitexname = 'W\'^-',
                      charge = 1,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0)

Wp__minus__ = Wp__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000003,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'u_{\\gamma}',
               antitexname = '\\bar{u}_{\\gamma}',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000004,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'u_Z',
               antitexname = '\\bar{u}_Z',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000005,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'u_{W^+}',
                antitexname = '\\bar{u}_{W^+}',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000006,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'u_{W^-}',
                antitexname = '\\bar{u}_{W^-}',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'u_{G-}',
               antitexname = '\\bar{u}_{G}',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

nu_e = Particle(pdg_code = 12,
                name = 'nu_e',
                antiname = 'nu_e~',
                spin = 2,
                color = 1,
                mass = Param.ZERO,
                width = Param.ZERO,
                texname = '\\nu_e',
                antitexname = '\\bar{\\nu}_e',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 1,
                Y = 0)

nu_e__tilde__ = nu_e.anti()

nu_mu = Particle(pdg_code = 14,
                 name = 'nu_mu',
                 antiname = 'nu_mu~',
                 spin = 2,
                 color = 1,
                 mass = Param.ZERO,
                 width = Param.ZERO,
                 texname = '\\nu_\\mu',
                 antitexname = '\\bar{\\nu}_\\mu',
                 charge = 0,
                 GhostNumber = 0,
                 LeptonNumber = 1,
                 Y = 0)

nu_mu__tilde__ = nu_mu.anti()

nu_tau = Particle(pdg_code = 16,
                  name = 'nu_tau',
                  antiname = 'nu_tau~',
                  spin = 2,
                  color = 1,
                  mass = Param.ZERO,
                  width = Param.ZERO,
                  texname = '\\nu_\\tau',
                  antitexname = '\\bar{\\nu}_\\tau',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 1,
                  Y = 0)

nu_tau__tilde__ = nu_tau.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ME,
                      width = Param.ZERO,
                      texname = 'e^-',
                      antitexname = 'e^+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MM,
                       width = Param.WM,
                       texname = '\\mu^-',
                       antitexname = '\\mu^+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

tau__minus__ = Particle(pdg_code = 15,
                        name = 'tau-',
                        antiname = 'tau+',
                        spin = 2,
                        color = 1,
                        mass = Param.MTA,
                        width = Param.WTA,
                        texname = '\\tau^-',
                        antitexname = '\\tau^+',
                        charge = -1,
                        GhostNumber = 0,
                        LeptonNumber = 1,
                        Y = 0)

tau__plus__ = tau__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = '\\bar{u}',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.WC,
             texname = 'c',
             antitexname = '\\bar{c}',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = '\\bar{t}',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = '\\bar{d}',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = '\\bar{s}',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.WB,
             texname = 'b',
             antitexname = '\\bar{b}',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.ZERO,
              texname = 'G_0',
              antitexname = 'G_0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.ZERO,
                     texname = 'G^+',
                     antitexname = 'G^{-}',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Gp0 = Particle(pdg_code = 9000007,
               name = 'Gp0',
               antiname = 'Gp0',
               spin = 1,
               color = 1,
               mass = Param.MZp,
               width = Param.WZp,
               texname = 'G\'_0',
               antitexname = 'G\'_0',
               goldstone = True,
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

Gp__plus__ = Particle(pdg_code = 9000008,
                      name = 'Gp+',
                      antiname = 'Gp-',
                      spin = 1,
                      color = 1,
                      mass = Param.MWp,
                      width = Param.WWp,
                      texname = 'G\'^+',
                      antitexname = 'G\'^{-}',
                      goldstone = True,
                      charge = 1,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0)

Gp__minus__ = Gp__plus__.anti()

