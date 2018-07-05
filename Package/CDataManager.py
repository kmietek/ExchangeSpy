import os
import json
import sys
import datetime

class CDataManager:
    __pathToMainDict = "E:\python\ExchangeSpy/"
    __dataSubDir = "data/"

    @staticmethod
    def __createFile__(subdir, filename, extension):
        try:
            __here = CDataManager.__pathToMainDict
            os.path.isdir(__here + subdir)
            __filePath = os.path.join(__here, subdir, filename + extension.value)
            f = open(__filePath, 'w')
            f.close()
        except IOError:
            print("Unexpected error:", sys.exc_info()[0])
        return True

    @staticmethod
    def __writeToJSONFile__(subdir, fileName, data, extension):
        __here = CDataManager.__pathToMainDict
        __filePathNameWExt = __here + subdir + '/' + fileName + extension.value
        if(os.path.exists(__filePathNameWExt)):
            try:
                with open(__filePathNameWExt, 'w') as fp:
                    json.dump(data, fp)
            except IOError:
                print("Unexpected error:", sys.exc_info()[0])
                return False
        else:
            if(CDataManager.__createFile__(subdir, fileName, extension)):

                try:
                    with open(__filePathNameWExt, 'w') as fp:
                            json.dump(data, fp)
                except IOError:
                    print("Unexpected error:", sys.exc_info()[0])
                    return False
        return True

    @staticmethod
    def __saveIntervalCharts__(data, currency, interval, extension):
        __dataToSave = dict()
        __dataToSave["TimeofRefresh"] = str(datetime.datetime.now())
        __breakLoop = 0

        for key, value in data.items():

            if(__breakLoop == interval.value):
                break
            __breakLoop = __breakLoop+1
            __dataToSave[key] = value


        if(CDataManager.__writeToJSONFile__("data",currency+interval.name, __dataToSave, extension)):
            return True
        else:
            print("something went wrong")
            return False

    @staticmethod
    def __getDataFromFile__(currency, interval, extension):
        __filePath = CDataManager.__pathToMainDict + CDataManager.__dataSubDir+ currency+interval.name+ extension.value
        data = dict()
        if(os.path.exists(__filePath)):
            try:

                with open(__filePath, "r") as fp:
                    data = json.loads(fp.read())

            except IOError:
                print(sys.exc_info())

        return data

    @staticmethod
    def __getDataToDrawCharts__(data):
        __data = dict()

        for key in data.keys():
            __data = data[key]
