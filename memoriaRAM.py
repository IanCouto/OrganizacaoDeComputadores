''' 
    ALUNOS: 
            MATHEUS HENRIQUE RUBIO DE MELO (201876036) SI
            IAN COUTO DE PAULA (201876002) SI
''' 

memoria = []
pc = 31


class memoriaRAM:

    def __init__(self, entrada, dicionario):
        self.memoria = []
        self.pc = 31
        self.quantInstrucoes = 0
        i = 0
        for pos in dicionario.dicionarioRegistradores:
            self.memoria.insert(i, pos)
            i += 1

        for txt in entrada:
            txt = txt.removesuffix("\n")
            self.memoria.insert(i, txt)
            i += 1
            self.quantInstrucoes += 1

        j = 0
        while j <= 128:
            self.memoria.insert(i, j)
            i += 1
            j += 2

    def set(self, posicao, valor):
        self.memoria[posicao] = valor

    def get(self, posicao):
        return self.memoria[posicao]

    def size(self):
        return len(self.memoria)

    def getPC(self):
        aux = self.memoria[self.pc]
        self.pc += 1
        self.pc = int(self.pc)
        if(len(str(aux)) == len('00000000000000000000000000000000')):
            return aux
        else:
            return -1

    def setPC(self, pc):
        self.pc = pc

    def getRegistradores(self):
        return self.memoria[0:32]

    def printMemoriaDeDados(self, saida):
        i = 32 + self.quantInstrucoes
        saida.write('\nMemoria de dados:\n')
        while i < len(self.memoria):
            saida.write(str(hex(i)) + ': ' + str(self.memoria[i]) + '\n')
            i += 1