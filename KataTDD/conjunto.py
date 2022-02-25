class Conjunto:

    def __init__(self, conjunto):
        self.__conjunto = conjunto
    
    def promedio(self):
        if len(self.__conjunto) > 0:
            return sum(self.__conjunto)/len(self.__conjunto)
        else:
            return None