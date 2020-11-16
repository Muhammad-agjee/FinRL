import pathlib

#import finrl

import pandas as pd
import datetime
import os
#pd.options.display.max_rows = 10
#pd.options.display.max_columns = 10


#PACKAGE_ROOT = pathlib.Path(finrl.__file__).resolve().parent
#PACKAGE_ROOT = pathlib.Path().resolve().parent

#TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
#DATASET_DIR = PACKAGE_ROOT / "data"

# data
TRAINING_DATA_FILE = "data/ETF_SPY_2009_2020.csv"
TURBULENCE_DATA = "data/dow30_turbulence_index.csv"
TESTING_DATA_FILE = "test.csv"

#now = datetime.datetime.now()
#TRAINED_MODEL_DIR = f"trained_models/{now}"
DATA_SAVE_DIR = f"datasets"
TRAINED_MODEL_DIR = f"trained_models"
RESULTS_DIR = f"results"
#os.makedirs(TRAINED_MODEL_DIR)


## time_fmt = '%Y-%m-%d'
START_DATE = "2009-01-01"
END_DATE = "2020-09-30"

START_TRADE_DATE = "2019-01-01"

## dataset default columns
DEFAULT_DATA_COLUMNS = ['date','tic','close']

## stockstats technical indicator column names
## check https://pypi.org/project/stockstats/ for different names
TECHNICAL_INDICATORS_LIST = ['macd', 'rsi_30', 'cci_30', 'dx_30']


## Model Parameters
A2C_PARAMS = {'n_steps':5, 
			  'ent_coef':0.01, 
			  'learning_rate':0.0007,
			  'verbose':0,
			  'timesteps':20000}
PPO_PARAMS = {'n_steps':128, 
			  'ent_coef':0.01, 
			  'learning_rate':0.00025,   
			  'nminibatches':4,
			  'verbose':0,
			  'timesteps':20000}
DDPG_PARAMS = {'batch_size':128, 
			   'buffer_size':50000,
			   'verbose':0,
			   'timesteps':20000}

########################################################
############## Stock Ticker Setup starts ##############
SINGLE_TICKER =['AAPL']

# self defined
MULTIPLE_STOCK_TICKER = ['AAPL','MSFT','FB']

# check https://wrds-www.wharton.upenn.edu/ for U.S. index constituents
# Dow 30 constituents at 2019/01
DOW_30_TICKER = ['AAPL','MSFT','JPM','V','RTX','PG','GS','NKE','DIS','AXP',
                  'HD','INTC','WMT','IBM','MRK','UNH','KO','CAT','TRV','JNJ',
                  'CVX','MCD','VZ','CSCO','XOM','BA','MMM','PFE','WBA','DD']

# Nasdaq 100 constituents at 2019/01
NAS_100_TICKER = [
'AMGN','AAPL','AMAT','INTC','PCAR','PAYX','MSFT','ADBE','CSCO','XLNX',
'QCOM','COST','SBUX','FISV','CTXS','INTU','AMZN','EBAY','BIIB','CHKP',
'GILD','NLOK','CMCSA','FAST','ADSK','CTSH','NVDA','GOOGL','ISRG','VRTX',
'HSIC','BIDU','ATVI','ADP','ROST','ORLY','CERN','BKNG','MYL','MU',
'DLTR','ALXN','SIRI','MNST','AVGO','TXN','MDLZ','FB','ADI','WDC',
'REGN','LBTYK','VRSK','NFLX','TSLA','CHTR','MAR','ILMN','LRCX',
'EA','AAL','WBA','KHC','BMRN','JD','SWKS','INCY','PYPL','CDW','FOXA',
'MXIM','TMUS','EXPE','TCOM','ULTA','CSX','NTES','MCHP','CTAS','KLAC',
'HAS','JBHT','IDXX','WYNN','MELI','ALGN','CDNS','WDAY','SNPS','ASML',
'TTWO','PEP','NXPI','XEL','AMD','NTAP','VRSN','LULU','WLTW','UAL'
]       

# SP 500 constituents at 2019
SP_500_TICKER =['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN',
		       'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES',
		       'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN',
		       'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMG',
		       'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'AOS',
		       'APA', 'APD', 'APH', 'APTV', 'ARE', 'ARNC', 'ATO', 'ATVI', 'AVB',
		       'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBT',
		       'BBY', 'BDX', 'BEN', 'BF.B', 'BHGE', 'BIIB', 'BK', 'BKNG', 'BLK',
		       'BLL', 'BMY', 'BR', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CAG',
		       'CAH', 'CAT', 'CB', 'CBOE', 'CBRE', 'CBS', 'CCI', 'CCL', 'CDNS',
		       'CE', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI',
		       'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS',
		       'CNC', 'CNP', 'COF', 'COG', 'COO', 'COP', 'COST', 'COTY', 'CPB',
		       'CPRI', 'CPRT', 'CRM', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH',
		       'CTVA', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DD', 'DE', 'DFS',
		       'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCK', 'DISH', 'DLR', 'DLTR',
		       'DOV', 'DOW', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC',
		       'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG',
		       'EQIX', 'EQR', 'ES', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVRG', 'EW',
		       'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FB', 'FBHS',
		       'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLS',
		       'FLT', 'FMC', 'FOXA', 'FRC', 'FRT', 'FTI', 'FTNT', 'FTV', 'GD',
		       'GE', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GOOG', 'GPC', 'GPN',
		       'GPS', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA',
		       'HCP', 'HD', 'HES', 'HFC', 'HIG', 'HII', 'HLT', 'HOG', 'HOLX',
		       'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HSIC', 'HST', 'HSY',
		       'HUM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INFO',
		       'INTC', 'INTU', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'ISRG',
		       'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JEF', 'JKHY', 'JNJ',
		       'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC',
		       'KMB', 'KMI', 'KMX', 'KO', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LDOS',
		       'LEG', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC',
		       'LNT', 'LOW', 'LRCX', 'LUV', 'LW', 'LYB', 'M', 'MA', 'MAA', 'MAC',
		       'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET',
		       'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO',
		       'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB',
		       'MTD', 'MU', 'MXIM', 'MYL', 'NBL', 'NCLH', 'NDAQ', 'NEE', 'NEM',
		       'NFLX', 'NI', 'NKE', 'NKTR', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC',
		       'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'O', 'OI', 'OKE',
		       'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PEG', 'PEP',
		       'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM',
		       'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX',
		       'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG',
		       'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP',
		       'ROST', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCHW', 'SEE', 'SHW', 'SIVB',
		       'SJM', 'SLB', 'SLG', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE',
		       'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC',
		       'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TFX', 'TGT', 'TIF', 'TJX', 'TMO',
		       'TMUS', 'TPR', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TTWO',
		       'TWTR', 'TXN', 'TXT', 'UA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH',
		       'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC',
		       'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ',
		       'WAB', 'WAT', 'WBA', 'WCG', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR',
		       'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYNN', 'XEC',
		       'XEL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION',
		       'ZTS']

# Hang Seng Index constituents at 2019/01
HSI_50_TICKER = ['0011.HK', '0005.HK','0012.HK','0006.HK','0003.HK','0016.HK','0019.HK','0002.HK','0001.HK','0267.HK',
				 '0101.HK','0941.HK','0762.HK','0066.HK','0883.HK','2388.HK','0017.HK','0083.HK','0939.HK','0388.HK',
				 '0386.HK','3988.HK','2628.HK','1398.HK','2318.HK', '3328.HK','0688.HK', '0857.HK','1088.HK','0700.HK',
				 '0836.HK','1109.HK','1044.HK','1299.HK','0151.HK','1928.HK','0027.HK','2319.HK','0823.HK','1113.HK',
				 '1038.HK','2018.HK','0175.HK','0288.HK','1997.HK','2007.HK','2382.HK','1093.HK','1177.HK','2313.HK']

# www.csindex.com.cn, for SSE and CSI adjustments
# SSE 50 Index constituents at 2019
SSE_50_TICKER = ['600000.SS','600036.SS','600104.SS','600030.SS','601628.SS','601166.SS','601318.SS','601328.SS','601088.SS','601857.SS',
				 '601601.SS','601668.SS','601288.SS','601818.SS','601989.SS','601398.SS','600048.SS','600028.SS','600050.SS','600519.SS',
				 '600016.SS','600887.SS','601688.SS','601186.SS','601988.SS','601211.SS','601336.SS','600309.SS','603993.SS','600690.SS',
				 '600276.SS','600703.SS','600585.SS','603259.SS','601888.SS','601138.SS','600196.SS','601766.SS','600340.SS','601390.SS',
				  '601939.SS','601111.SS','600029.SS','600019.SS','601229.SS','601800.SS','600547.SS','601006.SS','601360.SS','600606.SS',
				  '601319.SS','600837.SS','600031.SS','601066.SS','600009.SS','601236.SS','601012.SS','600745.SS','600588.SS',
				  '601658.SS','601816.SS','603160.SS']			 

# CSI 300 Index constituents at 2019
CSI_300_TICKER = ['600000.SS', '600004.SS', '600009.SS', '600010.SS', '600011.SS', '600015.SS', '600016.SS', '600018.SS', '600019.SS', '600025.SS', 
				 '600027.SS', '600028.SS', '600029.SS', '600030.SS', '600031.SS', '600036.SS', '600038.SS', '600048.SS', '600050.SS', '600061.SS', 
				 '600066.SS', '600068.SS', '600085.SS', '600089.SS', '600104.SS', '600109.SS', '600111.SS', '600115.SS', '600118.SS', '600170.SS', 
				 '600176.SS', '600177.SS', '600183.SS', '600188.SS', '600196.SS', '600208.SS', '600219.SS', '600221.SS', '600233.SS', '600271.SS', 
				 '600276.SS', '600297.SS', '600299.SS', '600309.SS', '600332.SS', '600340.SS', '600346.SS', '600352.SS', '600362.SS', '600369.SS', 
				 '600372.SS', '600383.SS', '600390.SS', '600398.SS', '600406.SS', '600436.SS', '600438.SS', '600482.SS', '600487.SS', '600489.SS', 
				 '600498.SS', '600516.SS', '600519.SS', '600522.SS', '600547.SS', '600570.SS', '600583.SS', '600585.SS', '600588.SS', '600606.SS', 
				 '600637.SS', '600655.SS', '600660.SS', '600674.SS', '600690.SS', '600703.SS', '600705.SS', '600741.SS', '600745.SS', '600760.SS', 
				 '600795.SS', '600809.SS', '600837.SS', '600848.SS', '600867.SS', '600886.SS', '600887.SS', '600893.SS', '600900.SS', '600919.SS', 
				 '600926.SS', '600928.SS', '600958.SS', '600968.SS', '600977.SS', '600989.SS', '600998.SS', '600999.SS', '601006.SS', '601009.SS', 
				 '601012.SS', '601018.SS', '601021.SS', '601066.SS', '601077.SS', '601088.SS', '601100.SS', '601108.SS', '601111.SS', '601117.SS', 
				 '601138.SS', '601155.SS', '601162.SS', '601166.SS', '601169.SS', '601186.SS', '601198.SS', '601211.SS', '601212.SS', '601216.SS', 
				 '601225.SS', '601229.SS', '601231.SS', '601236.SS', '601238.SS', '601288.SS', '601298.SS', '601318.SS', '601319.SS', '601328.SS', 
				 '601336.SS', '601360.SS', '601377.SS', '601390.SS', '601398.SS', '601555.SS', '601577.SS', '601600.SS', '601601.SS', '601607.SS', 
				 '601618.SS', '601628.SS', '601633.SS', '601658.SS', '601668.SS', '601669.SS', '601688.SS', '601698.SS', '601727.SS', '601766.SS', 
				 '601788.SS', '601800.SS', '601808.SS', '601816.SS', '601818.SS', '601828.SS', '601838.SS', '601857.SS', '601877.SS', '601878.SS', 
				 '601881.SS', '601888.SS', '601898.SS', '601899.SS', '601901.SS', '601916.SS', '601919.SS', '601933.SS', '601939.SS', '601985.SS', 
				 '601988.SS', '601989.SS', '601992.SS', '601997.SS', '601998.SS', '603019.SS', '603156.SS', '603160.SS', '603259.SS', '603260.SS', 
				 '603288.SS', '603369.SS', '603501.SS', '603658.SS', '603799.SS', '603833.SS', '603899.SS', '603986.SS', '603993.SS', '000001.SZ', 
				 '000002.SZ', '000063.SZ', '000066.SZ', '000069.SZ', '000100.SZ', '000157.SZ', '000166.SZ', '000333.SZ', '000338.SZ', '000425.SZ', 
				 '000538.SZ', '000568.SZ', '000596.SZ', '000625.SZ', '000627.SZ', '000651.SZ', '000656.SZ', '000661.SZ', '000671.SZ', '000703.SZ', 
				 '000708.SZ', '000709.SZ', '000723.SZ', '000725.SZ', '000728.SZ', '000768.SZ', '000776.SZ', '000783.SZ', '000786.SZ', '000858.SZ', 
				 '000860.SZ', '000876.SZ', '000895.SZ', '000938.SZ', '000961.SZ', '000963.SZ', '000977.SZ', '001979.SZ', '002001.SZ', '002007.SZ', 
				 '002008.SZ', '002024.SZ', '002027.SZ', '002032.SZ', '002044.SZ', '002050.SZ', '002120.SZ', '002129.SZ', '002142.SZ', '002146.SZ', 
				 '002153.SZ', '002157.SZ', '002179.SZ', '002202.SZ', '002230.SZ', '002236.SZ', '002241.SZ', '002252.SZ', '002271.SZ', '002304.SZ', 
				 '002311.SZ', '002352.SZ', '002371.SZ', '002410.SZ', '002415.SZ', '002422.SZ', '002456.SZ', '002460.SZ', '002463.SZ', '002466.SZ', 
				 '002468.SZ', '002475.SZ', '002493.SZ', '002508.SZ', '002555.SZ', '002558.SZ', '002594.SZ', '002601.SZ', '002602.SZ', '002607.SZ', 
				 '002624.SZ', '002673.SZ', '002714.SZ', '002736.SZ', '002739.SZ', '002773.SZ', '002841.SZ', '002916.SZ', '002938.SZ', '002939.SZ', 
				 '002945.SZ', '002958.SZ', '003816.SZ', '300003.SZ', '300014.SZ', '300015.SZ', '300033.SZ', '300059.SZ', '300122.SZ', '300124.SZ', 
				 '300136.SZ', '300142.SZ', '300144.SZ', '300347.SZ', '300408.SZ', '300413.SZ', '300433.SZ', '300498.SZ', '300601.SZ', '300628.SZ',]

############## Stock Ticker Setup ends ##############
########################################################