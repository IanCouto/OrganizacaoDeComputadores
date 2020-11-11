class memoriaRAM:
    __memoria = None

    def __init__(self):
        self.__memoria = [256] # private attribute
    
    def set(self, posicao, valor):
        self.__memoria.insert(posicao, valor)

    def get(self,posicao):
        return self.__memoria[posicao]