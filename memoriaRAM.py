import dicionario

memoria = []
class memoriaRAM:

    def __init__(self, entrada):
        self.memoria = []
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
