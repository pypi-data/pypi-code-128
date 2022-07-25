# Copyright (c) 2019 Phase Advanced Sensor Systems, Inc.
from ..device import Device, Reg32, Reg32W


class GPT16x1(Device):
    '''
    Driver for the General-purpose Timer device (GPT) supporting only 16-bit
    counters and one capture/compare register.
    '''
    REGS = [Reg32 ('CR1',    0x000,        [('CEN',         1),
                                            ('UDIS',        1),
                                            ('URS',         1),
                                            ('OPM',         1),
                                            ('',            3),
                                            ('ARPE',        1),
                                            ('CKD',         2),     # tDTS
                                            ('',            1),
                                            ('UIFREMAP',    1),
                                            ('DITHEN',      1),
                                            ]),
            Reg32 ('CR2',    0x004,        [('CCPC',        1),
                                            ('',            1),
                                            ('CCUS',        1),
                                            ('CCDS',        1),
                                            ('',            4),
                                            ('OIS1',        1),
                                            ('OIS1N',       1),
                                            ]),
            Reg32 ('DIER',   0x00C,        [('UIE',         1),
                                            ('CC1IE',       1),
                                            ('',            3),
                                            ('COMIE',       1),
                                            ('',            1),
                                            ('BIE',         1),
                                            ('UDE',         1),
                                            ('CC1DE',       1),
                                            ('',            3),
                                            ('COMDE',       1),
                                            ]),
            Reg32 ('SR',     0x010,        [('UIF',         1),
                                            ('CC1F',        1),
                                            ('',            3),
                                            ('COMIF',       1),
                                            ('',            1),
                                            ('BIF',         1),
                                            ('',            1),
                                            ('CC1OF',       1),
                                            ]),
            Reg32W('EGR',    0x014,        [('UG',          1),
                                            ('CC1G',        1),
                                            ('',            3),
                                            ('COMG',        1),
                                            ('',            1),
                                            ('BG',          1),
                                            ]),
            Reg32 ('CCMR1_I',   0x018,     [('CC1S',        2),
                                            ('IC1PSC',      2),
                                            ('IC1F',        4),
                                            ]),
            Reg32 ('CCMR1_O',   0x018,     [('CC1S',        2),
                                            ('OC1FE',       1),
                                            ('OC1PE',       1),
                                            ('OC1M[2:0]',   3),
                                            ('OC1CE',       1),
                                            ('',            8),
                                            ('OC1M[3]',     1),
                                            ]),
            Reg32 ('CCER',      0x020,     [('CC1E',        1),
                                            ('CC1P',        1),
                                            ('CC1NE',       1),
                                            ('CC1NP',       1),
                                            ]),
            Reg32 ('CNT',       0x024,     [('CNT',         16),
                                            ('',            15),
                                            ('UIFCPY',      1),
                                            ]),
            Reg32 ('PSC',       0x028,     [('PSC',         16),
                                            ]),
            Reg32 ('ARR',       0x02C,     [('ARR',         20),
                                            ]),
            Reg32 ('RCR',       0x030,     [('REP',         8),
                                            ]),
            Reg32 ('CCR1',      0x034,     [('CCR1',        20),
                                            ]),
            Reg32 ('BDTR',      0x044,     [('DTG',         8),
                                            ('LOCK',        2),
                                            ('OSSI',        1),
                                            ('OSSR',        1),
                                            ('BKE',         1),
                                            ('BKP',         1),
                                            ('AOE',         1),
                                            ('MOE',         1),
                                            ('BKF',         4),
                                            ('',            6),
                                            ('BKDSRM',      1),
                                            ('',            1),
                                            ('BKBID',       1),
                                            ]),
            Reg32 ('DTR2',      0x054,     [('DTGF',        8),
                                            ('',            8),
                                            ('DTAE',        1),
                                            ('DTPE',        1),
                                            ]),
            Reg32 ('TISEL',     0x05C,     [('TI1SEL',      4),
                                            ]),
            Reg32 ('AF1',       0x060,     [('BKINE',       1),
                                            ('BKCMP1E',     1),
                                            ('BKCMP2E',     1),
                                            ('BKCMP3E',     1),
                                            ('BKCMP4E',     1),
                                            ('BKCMP5E',     1),
                                            ('BKCMP6E',     1),
                                            ('BKCMP7E',     1),
                                            ('BKCMP8E',     1),
                                            ('BKINP',       1),
                                            ('BKCMP1P',     1),
                                            ('BKCMP2P',     1),
                                            ('BKCMP3P',     1),
                                            ('BKCMP4P',     1),
                                            ]),
            Reg32 ('AF2',       0x064,     [('',            16),
                                            ('OCRSEL',      3),
                                            ]),
            Reg32 ('OR1',       0x068,     [('HSE32EN',     1),
                                            ]),  # Address is a misprint!
            Reg32 ('DCR',       0x3DC,     [('DBA',         5),
                                            ('',            3),
                                            ('DBL',         5),
                                            ]),
            Reg32 ('DMAR',      0x3E0,     [('DMAB',        32),
                                            ]),
            ]

    def __init__(self, target, ap, name, addr, **kwargs):
        super().__init__(target, ap, addr, name, GPT16x1.REGS, **kwargs)
