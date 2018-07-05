from Package.CCurrency import CCurrency


class CArbitrageCurrency(CCurrency):
    ############## Fields ##################
    __exchangeName = ""

    ############# Methods #################
    def __init__(self, nameCurrency, priceCurrency, exchangeName):
        self.__name = nameCurrency
        self.__price = priceCurrency
        self.__exchangeName = exchangeName

    def __setExchangeName__(self, exchangeName):
        self.__exchangeName = exchangeName

    def __getExchangeName__(self):
        return self.__exchangeName
