class memoriaRAM:
    __memoria = None

    def __init__(self):
        self.__memoria = [] # private attribute
        i = 0
        while i < 256:
            i += 1
            self.__memoria.insert(i, 0)
        
    
    def set(self, posicao, valor):
        self.__memoria[posicao] = valor

    def get(self,posicao):
        return self.__memoria[posicao]

    def size(self):
        return len(self.__memoria)-1