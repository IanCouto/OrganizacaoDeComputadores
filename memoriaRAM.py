import dicionario

memoria = []
pc = 31


class memoriaRAM:

    def __init__(self, entrada, dicionario):
        self.memoria = []
        self.pc = 31
        i = 0
        for pos in dicionario.dicRegistradores:
            self.memoria.insert(i, pos)
            i += 1

        for txt in entrada:
            txt = txt.removesuffix("\n")
            self.memoria.insert(i, txt)
            i += 1

        j = 0
        while j < 256:
            i += 1
            j += 1
            self.memoria.insert(i, j)

    def set(self, posicao, valor):
        self.memoria[posicao] = valor

    def get(self, posicao):
        return self.memoria[posicao]

    def size(self):
        return len(self.memoria)

    def getPC(self):
        self.pc += 1
        aux = self.memoria[self.pc]
        if(len(str(aux)) == len('00000001010100000100100000100000')):
            return aux
        else:
            self.pc -= 1
            print('Instruções Finalizadas!')
            return -1

    def getRegistradores(self):
        return self.memoria[0:32]
