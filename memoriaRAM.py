class memoriaRAM:
    memoriaRAM = dict()
    
    @staticmethod
    def set(self,posicao, valor):
        number = 435
        #print(number, 'in hex =', hex(number))
        self.memoriaRAM[posicao] = valor