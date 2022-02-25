class Conjunto:

    def __init__(self, conjunto):
        self.__conjunto = conjunto
    
    def promedio(self):
        if(len(self.__conjunto) == 2):
            return (self.__conjunto[0] + self.__conjunto[1]) / 2
        if(len(self.__conjunto) == 1):
            return (self.__conjunto[0])
        else:
            return None