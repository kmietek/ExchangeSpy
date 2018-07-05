from Package.CDataMiner import CDataMiner
from Package.CDataManager import CDataManager
from Enums.EIntervals import EIntervals
from Enums.EExtensions import EExtensions
import json

__jsonData = CDataMiner.__getJson__("GET","https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=USD&apikey=CCTQ39QSZTBXBDOB")
print(__jsonData)
__jsonDic = json.loads(__jsonData)
__test = __jsonDic["Time Series (Digital Currency Weekly)"]

print(__test)
print("dict test:")
__dict = dict()
__dict["0"] = __jsonDic["Time Series (Digital Currency Weekly)"]["2018-07-03"]
__dict["1"] = __jsonDic["Time Series (Digital Currency Weekly)"]["2018-07-01"]
print(__dict)

CDataManager.__writeToJSONFile__("data","data",__dict, EExtensions.JSON)
CDataManager.__saveIntervalCharts__(__test,"BTC", EIntervals.WEEK, EExtensions.JSON)
print("Test read:")
print(CDataManager.__getDataFromFile__("BTC",EIntervals.WEEK,EExtensions.JSON))
print("Test plot")
print(CDataManager.__getDataToDrawCharts__(CDataManager.__getDataFromFile__("BTC",EIntervals.WEEK,EExtensions.JSON)))