dicComandosR = dict()
dicComandosIJ = dict()
dicRegistradores = dict()
memoriaRegistradores = dict()


class dicionario:
    def __init__(self):
        self.dicComandosR = {
            '100000': "add",
            '100010': "sub",
            '011000': "mult",
            '011010': "div",
            '100100': "and",
            '100101': "or",
            '101010': "slt",
            '000000': "sll",
            '001000': "jr",
        }

        self.dicComandosIJ = {
            '001000': "addi",
            '100011': "lw",
            '101011': "sw",
            '000100': "beq",
            '000101': "bne",
            '000010': "j",
            '000011': "jal",
        }

        self.dicRegistradores = {
            '00000': "$zero",
            '00001': "$at",
            '00010': "$v0",
            '00011': "$v1",
            '00100': "$a0",
            '00101': "$a1",
            '00110': "$a2",
            '00111': "$a3",
            '01000': "$t0",
            '01001': "$t1",
            '01010': "$t2",
            '01011': "$t3",
            '01100': "$t4",
            '01101': "$t5",
            '01110': "$t6",
            '01111': "$t7",
            '10000': "$s0",
            '10001': "$s1",
            '10010': "$s2",
            '10011': "$s3",
            '10100': "$s4",
            '10101': "$s5",
            '10110': "$s6",
            '10111': "$s7",
            '11000': "$t8",
            '11001': "$t9",
            '11010': "$k0",
            '11011': "$k1",
            '11100': "$gp",
            '11101': "$sp",
            '11110': "$fp",
            '11111': "$ra",
        }

        self.memoriaRegistradores = {
            '00000': 1,
            '00001': 1,
            '00010': 1,
            '00011': 1,
            '00100': 1,
            '00101': 1,
            '00110': 1,
            '00111': 1,
            '01000': 1,
            '01001': 1,
            '01010': 1,
            '01011': 1,
            '01100': 1,
            '01101': 1,
            '01110': 1,
            '01111': 1,
            '10000': 1,
            '10001': 1,
            '10010': 1,
            '10011': 1,
            '10100': 1,
            '10101': 1,
            '10110': 1,
            '10111': 1,
            '11000': 1,
            '11001': 1,
            '11010': 1,
            '11011': 1,
            '11100': 1,
            '11101': 1,
            '11110': 1,
            '11111': 1,
        }

    def traduzirComando(self, str):
        opcode = str[26:32]
        rs = str[21:26]
        rt = str[16:21]
        rd = str[11:16]
        sa = str[6:11]
        func = str[0:6]
        immediate = str[0:16]
        desvio = str[0:26]
        if(func in self.dicComandosR):
            return self.dicComandosR[func] + " " + self.dicRegistradores[rs] + " " + self.dicRegistradores[rt] + " " + self.dicRegistradores[rd]
        elif(func in self.dicComandosIJ):
            return self.dicComandosIJ[func] + " " + self.dicRegistradores[rs] + " " + self.dicRegistradores[rt] + " " + self.dicRegistradores[rd]

    def executaComando(comando, rg1, rg2, rg3):
        if comando in dicComandosR:
            if comando == '100000':
                dicionario.add(rg1, rg2, rg3)
            elif comando == '100010':
                dicionario.sub(rg1, rg2, rg3)
            elif comando == '011000':
                dicionario.mult(rg1, rg2, rg3)
            elif comando == '011010':
                dicionario.div(rg1, rg2, rg3)
            elif comando == '100100':
                dicionario.and(rg1, rg2, rg3)
            elif comando == '100101':
                dicionario.or(rg1, rg2, rg3)
            elif comando == '101010':
                dicionario.slt(rg1, rg2, rg3)
            elif comando == '000000':
                dicionario.sll(rg1, rg2, rg3)
            elif comando == '001000':
                dicionario.jr(rg1)
        elif comando in dicComandosIJ:
            if comando == '001000':
                dicionario.addi(rg1, rg2, rg3)
            elif comando == '100011':
                dicionario.lw(rg1, rg2, rg3)
            elif comando == '101011':
                dicionario.sw(rg1, rg2, rg3)
            elif comando == '000100':
                dicionario.beq(rg1, rg2, rg3)
            elif comando == '000101':
                dicionario.bne(rg1, rg2, rg3)
            elif comando == '000010':
                dicionario.j(rg1, rg2, rg3)
            elif comando == '000011':
                dicionario.jal(rg1, rg2, rg3)

    def add(rg1, rg2, rg3):
        memoriaRegistradores[rg1] = memoriaRegistradores[rg2] + memoriaRegistradores[rg3]
    
    def sub(rg1, rg2, rg3):
        memoriaRegistradores[rg1] = memoriaRegistradores[rg2] - memoriaRegistradores[rg3]

    def mult(rg1, rg2, rg3):
        memoriaRegistradores[rg1] = memoriaRegistradores[rg2] * memoriaRegistradores[rg3]

    def div(rg1, rg2, rg3):
        memoriaRegistradores[rg1] = memoriaRegistradores[rg2] / memoriaRegistradores[rg3]

    def and(rg1, rg2, rg3):
        if memoriaRegistradores[rg2] == 1 & memoriaRegistradores[rg3] == 1:
            memoriaRegistradores[rg1] = 1
        else: 
            memoriaRegistradores[rg1] = 0

    def or(rg1, rg2, rg3):
        if memoriaRegistradores[rg2] == 1 | memoriaRegistradores[rg3] == 1:
            memoriaRegistradores[rg1] = 1
        else: 
            memoriaRegistradores[rg1] = 0
    
    def slt(rg1, rg2, rg3):
        if memoriaRegistradores[rg2] < memoriaRegistradores[rg3]:
            memoriaRegistradores[rg1] = 1
        else: 
            memoriaRegistradores[rg1] = 0
    
    def sll(rg1, rg2, rg3):
        i = 0
        #shift esquerda -> converter valor armazenado no regstrador rg2 para binário, realizar um 
        #shift a esquerda dos numeros de acordo com o rg3 e armazenar no rg1
    
    def jr(rg1):
        #pc pula para o endereço do registrador rg1