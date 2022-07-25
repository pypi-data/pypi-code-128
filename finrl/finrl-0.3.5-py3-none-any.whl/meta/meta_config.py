from __future__ import annotations

TRAIN_START_DATE = "2019-01-01"
TRAIN_END_DATE = "2019-12-31"

TEST_START_DATE = "2020-01-01"
TEST_END_DATE = "2020-12-31"

TRADE_START_DATE = "2021-01-01"
TRADE_END_DATE = "2021-07-31"

PATH_OF_DATA = "data"
READ_DATA_FROM_LOCAL = 1  # 0 or 1

INDICATORS = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
]

FAANG_TICKER = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]

# Dow 30 constituents at 2019/01
DOW_30_TICKER = [
    "AAPL",
    "MSFT",
    "JPM",
    "V",
    "RTX",
    "PG",
    "GS",
    "NKE",
    "DIS",
    "AXP",
    "HD",
    "INTC",
    "WMT",
    "IBM",
    "MRK",
    "UNH",
    "KO",
    "CAT",
    "TRV",
    "JNJ",
    "CVX",
    "MCD",
    "VZ",
    "CSCO",
    "XOM",
    "BA",
    "MMM",
    "PFE",
    "WBA",
    "DD",
]

# Nasdaq 100 constituents at 2019/01
NAS_100_TICKER = [
    "AMGN",
    "AAPL",
    "AMAT",
    "INTC",
    "PCAR",
    "PAYX",
    "MSFT",
    "ADBE",
    "CSCO",
    "XLNX",
    "QCOM",
    "COST",
    "SBUX",
    "FISV",
    "CTXS",
    "INTU",
    "AMZN",
    "EBAY",
    "BIIB",
    "CHKP",
    "GILD",
    "NLOK",
    "CMCSA",
    "FAST",
    "ADSK",
    "CTSH",
    "NVDA",
    "GOOGL",
    "ISRG",
    "VRTX",
    "HSIC",
    "BIDU",
    "ATVI",
    "ADP",
    "ROST",
    "ORLY",
    "CERN",
    "BKNG",
    "MYL",
    "MU",
    "DLTR",
    "ALXN",
    "SIRI",
    "MNST",
    "AVGO",
    "TXN",
    "MDLZ",
    "FB",
    "ADI",
    "WDC",
    "REGN",
    "LBTYK",
    "VRSK",
    "NFLX",
    "TSLA",
    "CHTR",
    "MAR",
    "ILMN",
    "LRCX",
    "EA",
    "AAL",
    "WBA",
    "KHC",
    "BMRN",
    "JD",
    "SWKS",
    "INCY",
    "PYPL",
    "CDW",
    "FOXA",
    "MXIM",
    "TMUS",
    "EXPE",
    "TCOM",
    "ULTA",
    "CSX",
    "NTES",
    "MCHP",
    "CTAS",
    "KLAC",
    "HAS",
    "JBHT",
    "IDXX",
    "WYNN",
    "MELI",
    "ALGN",
    "CDNS",
    "WDAY",
    "SNPS",
    "ASML",
    "TTWO",
    "PEP",
    "NXPI",
    "XEL",
    "AMD",
    "NTAP",
    "VRSN",
    "LULU",
    "WLTW",
    "UAL",
]

# SP 500 constituents at 2019
SP_500_TICKER = [
    "A",
    "AAL",
    "AAP",
    "AAPL",
    "ABBV",
    "ABC",
    "ABMD",
    "ABT",
    "ACN",
    "ADBE",
    "ADI",
    "ADM",
    "ADP",
    "ADS",
    "ADSK",
    "AEE",
    "AEP",
    "AES",
    "AFL",
    "AGN",
    "AIG",
    "AIV",
    "AIZ",
    "AJG",
    "AKAM",
    "ALB",
    "ALGN",
    "ALK",
    "ALL",
    "ALLE",
    "ALXN",
    "AMAT",
    "AMCR",
    "AMD",
    "AME",
    "AMG",
    "AMGN",
    "AMP",
    "AMT",
    "AMZN",
    "ANET",
    "ANSS",
    "ANTM",
    "AON",
    "AOS",
    "APA",
    "APD",
    "APH",
    "APTV",
    "ARE",
    "ARNC",
    "ATO",
    "ATVI",
    "AVB",
    "AVGO",
    "AVY",
    "AWK",
    "AXP",
    "AZO",
    "BA",
    "BAC",
    "BAX",
    "BBT",
    "BBY",
    "BDX",
    "BEN",
    "BF.B",
    "BHGE",
    "BIIB",
    "BK",
    "BKNG",
    "BLK",
    "BLL",
    "BMY",
    "BR",
    "BRK.B",
    "BSX",
    "BWA",
    "BXP",
    "C",
    "CAG",
    "CAH",
    "CAT",
    "CB",
    "CBOE",
    "CBRE",
    "CBS",
    "CCI",
    "CCL",
    "CDNS",
    "CE",
    "CELG",
    "CERN",
    "CF",
    "CFG",
    "CHD",
    "CHRW",
    "CHTR",
    "CI",
    "CINF",
    "CL",
    "CLX",
    "CMA",
    "CMCSA",
    "CME",
    "CMG",
    "CMI",
    "CMS",
    "CNC",
    "CNP",
    "COF",
    "COG",
    "COO",
    "COP",
    "COST",
    "COTY",
    "CPB",
    "CPRI",
    "CPRT",
    "CRM",
    "CSCO",
    "CSX",
    "CTAS",
    "CTL",
    "CTSH",
    "CTVA",
    "CTXS",
    "CVS",
    "CVX",
    "CXO",
    "D",
    "DAL",
    "DD",
    "DE",
    "DFS",
    "DG",
    "DGX",
    "DHI",
    "DHR",
    "DIS",
    "DISCK",
    "DISH",
    "DLR",
    "DLTR",
    "DOV",
    "DOW",
    "DRE",
    "DRI",
    "DTE",
    "DUK",
    "DVA",
    "DVN",
    "DXC",
    "EA",
    "EBAY",
    "ECL",
    "ED",
    "EFX",
    "EIX",
    "EL",
    "EMN",
    "EMR",
    "EOG",
    "EQIX",
    "EQR",
    "ES",
    "ESS",
    "ETFC",
    "ETN",
    "ETR",
    "EVRG",
    "EW",
    "EXC",
    "EXPD",
    "EXPE",
    "EXR",
    "F",
    "FANG",
    "FAST",
    "FB",
    "FBHS",
    "FCX",
    "FDX",
    "FE",
    "FFIV",
    "FIS",
    "FISV",
    "FITB",
    "FLIR",
    "FLS",
    "FLT",
    "FMC",
    "FOXA",
    "FRC",
    "FRT",
    "FTI",
    "FTNT",
    "FTV",
    "GD",
    "GE",
    "GILD",
    "GIS",
    "GL",
    "GLW",
    "GM",
    "GOOG",
    "GPC",
    "GPN",
    "GPS",
    "GRMN",
    "GS",
    "GWW",
    "HAL",
    "HAS",
    "HBAN",
    "HBI",
    "HCA",
    "HCP",
    "HD",
    "HES",
    "HFC",
    "HIG",
    "HII",
    "HLT",
    "HOG",
    "HOLX",
    "HON",
    "HP",
    "HPE",
    "HPQ",
    "HRB",
    "HRL",
    "HSIC",
    "HST",
    "HSY",
    "HUM",
    "IBM",
    "ICE",
    "IDXX",
    "IEX",
    "IFF",
    "ILMN",
    "INCY",
    "INFO",
    "INTC",
    "INTU",
    "IP",
    "IPG",
    "IPGP",
    "IQV",
    "IR",
    "IRM",
    "ISRG",
    "IT",
    "ITW",
    "IVZ",
    "JBHT",
    "JCI",
    "JEC",
    "JEF",
    "JKHY",
    "JNJ",
    "JNPR",
    "JPM",
    "JWN",
    "K",
    "KEY",
    "KEYS",
    "KHC",
    "KIM",
    "KLAC",
    "KMB",
    "KMI",
    "KMX",
    "KO",
    "KR",
    "KSS",
    "KSU",
    "L",
    "LB",
    "LDOS",
    "LEG",
    "LEN",
    "LH",
    "LHX",
    "LIN",
    "LKQ",
    "LLY",
    "LMT",
    "LNC",
    "LNT",
    "LOW",
    "LRCX",
    "LUV",
    "LW",
    "LYB",
    "M",
    "MA",
    "MAA",
    "MAC",
    "MAR",
    "MAS",
    "MCD",
    "MCHP",
    "MCK",
    "MCO",
    "MDLZ",
    "MDT",
    "MET",
    "MGM",
    "MHK",
    "MKC",
    "MKTX",
    "MLM",
    "MMC",
    "MMM",
    "MNST",
    "MO",
    "MOS",
    "MPC",
    "MRK",
    "MRO",
    "MS",
    "MSCI",
    "MSFT",
    "MSI",
    "MTB",
    "MTD",
    "MU",
    "MXIM",
    "MYL",
    "NBL",
    "NCLH",
    "NDAQ",
    "NEE",
    "NEM",
    "NFLX",
    "NI",
    "NKE",
    "NKTR",
    "NLSN",
    "NOC",
    "NOV",
    "NRG",
    "NSC",
    "NTAP",
    "NTRS",
    "NUE",
    "NVDA",
    "NWL",
    "NWS",
    "O",
    "OI",
    "OKE",
    "OMC",
    "ORCL",
    "ORLY",
    "OXY",
    "PAYX",
    "PBCT",
    "PCAR",
    "PEG",
    "PEP",
    "PFE",
    "PFG",
    "PG",
    "PGR",
    "PH",
    "PHM",
    "PKG",
    "PKI",
    "PLD",
    "PM",
    "PNC",
    "PNR",
    "PNW",
    "PPG",
    "PPL",
    "PRGO",
    "PRU",
    "PSA",
    "PSX",
    "PVH",
    "PWR",
    "PXD",
    "PYPL",
    "QCOM",
    "QRVO",
    "RCL",
    "RE",
    "REG",
    "REGN",
    "RF",
    "RHI",
    "RJF",
    "RL",
    "RMD",
    "ROK",
    "ROL",
    "ROP",
    "ROST",
    "RSG",
    "RTN",
    "SBAC",
    "SBUX",
    "SCHW",
    "SEE",
    "SHW",
    "SIVB",
    "SJM",
    "SLB",
    "SLG",
    "SNA",
    "SNPS",
    "SO",
    "SPG",
    "SPGI",
    "SRE",
    "STI",
    "STT",
    "STX",
    "STZ",
    "SWK",
    "SWKS",
    "SYF",
    "SYK",
    "SYMC",
    "SYY",
    "T",
    "TAP",
    "TDG",
    "TEL",
    "TFX",
    "TGT",
    "TIF",
    "TJX",
    "TMO",
    "TMUS",
    "TPR",
    "TRIP",
    "TROW",
    "TRV",
    "TSCO",
    "TSN",
    "TSS",
    "TTWO",
    "TWTR",
    "TXN",
    "TXT",
    "UA",
    "UAL",
    "UDR",
    "UHS",
    "ULTA",
    "UNH",
    "UNM",
    "UNP",
    "UPS",
    "URI",
    "USB",
    "UTX",
    "V",
    "VAR",
    "VFC",
    "VIAB",
    "VLO",
    "VMC",
    "VNO",
    "VRSK",
    "VRSN",
    "VRTX",
    "VTR",
    "VZ",
    "WAB",
    "WAT",
    "WBA",
    "WCG",
    "WDC",
    "WEC",
    "WELL",
    "WFC",
    "WHR",
    "WLTW",
    "WM",
    "WMB",
    "WMT",
    "WRK",
    "WU",
    "WY",
    "WYNN",
    "XEC",
    "XEL",
    "XLNX",
    "XOM",
    "XRAY",
    "XRX",
    "XYL",
    "YUM",
    "ZBH",
    "ZION",
    "ZTS",
]
