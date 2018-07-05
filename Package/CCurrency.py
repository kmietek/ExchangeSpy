from Package.CWare import CWare



class CCurrency(CWare):
    ################# Fields ####################

    # Currency name
    __name = ""
    # Currency price
    __price = 0.0

    ############### Methods ###################

    def __init__(self, nameCurrency, priceCurrency):
        self.__name = nameCurrency
        self.__price = priceCurrency


    def __setName__(self, name):
        self.__name = name

    def __setPrice__(self, price):
        self.__price = price

    def __getName__(self):
        return self.__name

    def __getPrice__(self):
        return self.__price
