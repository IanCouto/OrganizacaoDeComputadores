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

    def traduzirComando(self, comando):
        opcode = comando[0:6] 
        if opcode == '000000':
            func = comando[26:32]
        else:
            func = comando[0:6]
        rs = comando[6:11]
        rt = comando[11:16]
        rd = comando[16:21]
        sa = comando[21:26]
        immediate = comando[16:32]
        alvo = comando[6:32]
        if opcode == '000000' and func in self.dicComandosR:
            if func == '001000':
                return self.dicComandosR[func] + " " + self.dicRegistradores[rs]
            elif func == '000000':
                return self.dicComandosR[func] + " " + self.dicRegistradores[rt] + " " + self.dicRegistradores[rd] + " " + hex(int(sa))
            else:  
                return self.dicComandosR[func] + " " + self.dicRegistradores[rs] + " " + self.dicRegistradores[rt] + " " + self.dicRegistradores[rd]
        elif func in self.dicComandosIJ:
            if func == '001000':
                return self.dicComandosIJ[func] + " " + self.dicRegistradores[rs] + " " + self.dicRegistradores[rt] + " " + str(int(immediate, 10))
            elif func == '100011' or func == '101011':
                return self.dicComandosIJ[func] + " " + self.dicRegistradores[rs] + " " + str(int(immediate,10)) + "(" + self.dicRegistradores[rt] + ")"
            elif func == '000010' or func == '000011':
                return self.dicComandosIJ[func] + " " + hex(int(alvo))
            else:
                return self.dicComandosIJ[func] + " " + self.dicRegistradores[rs] + " " + self.dicRegistradores[rt] + " " + self.dicRegistradores[rd]

    def executaComando(self, comando, memoria):
        opcode = comando[0:6] 
        if opcode == '000000':
            func = comando[26:32]
        else:
            func = comando[0:6]
        rs = comando[6:11]
        rt = comando[11:16]
        rd = comando[16:21]
        sa = comando[21:26]
        immediate = comando[16:32]
        alvo = comando[6:32]
        if opcode == '000000' and func in self.dicComandosR:
            if func == '100000':
                self.add(rs, rt, rd)
            elif func == '100010':
                self.sub(rs, rt, rd)
            elif func == '011000':
                self.mult(rs, rt, rd)
            elif func == '011010':
                self.div(rs, rt, rd)
            elif func == '100100':
                self.myAnd(rs, rt, rd)
            elif func == '100101':
                self.myOr(rs, rt, rd)
            elif func == '101010':
                self.slt(rs, rt,  rd)
            elif func == '000000':
                self.sll(rt, rd, sa)
            elif func == '001000':
                self.jr(rs, memoria)
        elif func in self.dicComandosIJ:
            if func == '001000':
                self.addi(rs, rt, immediate)
            elif func == '100011':
                self.lw(rs, rt, immediate)
            elif func == '101011':
                self.sw(rs, rt, immediate)
            elif func == '000100':
                self.beq(rs, rt, rd, memoria)
            elif func == '000101':
                self.bne(rs, rt, rd, memoria)
            elif func == '000010':
                self.j(alvo, memoria)
            elif func == '000011':
                self.jal(alvo, memoria)


# ---------- COMANDOS TYPE-R ----------
    def add(self, rs, rt, rd):
        self.memoriaRegistradores[rs] = self.memoriaRegistradores[rt] + self.memoriaRegistradores[rd]
    
    def sub(self, rs, rt, rd):
        self.memoriaRegistradores[rs] = self.memoriaRegistradores[rt] - self.memoriaRegistradores[rd]

    def mult(self, rs, rt, rd):
        self.memoriaRegistradores[rs] = self.memoriaRegistradores[rt] * self.memoriaRegistradores[rd]

    def div(self, rs, rt, rd):
        self.memoriaRegistradores[rs] = self.memoriaRegistradores[rt] / self.memoriaRegistradores[rd]

    def myAnd(self, rs, rt, rd):
        if self.memoriaRegistradores[rt] == 1 and self.memoriaRegistradores[rd] == 1:
            self.memoriaRegistradores[rs] = 1
        else: 
            self.memoriaRegistradores[rs] = 0

    def myOr(self, rs, rt, rd):
        if self.memoriaRegistradores[rt] == 1 or self.memoriaRegistradores[rd] == 1:
            self.memoriaRegistradores[rs] = 1
        else: 
            self.memoriaRegistradores[rs] = 0
    
    def slt(self, rs, rt, rd):
        if self.memoriaRegistradores[rt] < self.memoriaRegistradores[rd]:
            self.memoriaRegistradores[rs] = 1
        else: 
            self.memoriaRegistradores[rs] = 0
    
    def sll(self, rs, rt, bits):
        self.memoriaRegistradores[rs] = self.memoriaRegistradores[rt] << int(bits)
        #shift esquerda -> converter valor armazenado no regstrador rt para binário, realizar um 
        #shift a esquerda dos numeros de acordo com o rd e armazenar no rs
    
    def jr(self, rs, memoria):
        memoria.setPC(int(str(int(rs,2)),10))
        #pc pula para o endereço do registrador rs

# ---------- COMANDOS TYPE-IJ ----------

    def addi(self, rs, rt, val):
        self.memoriaRegistradores[rs] = self.memoriaRegistradores[rt] + (int(val,2))

    def lw(self, rs,rt,val):
        pos = '{0:05b}'.format(self.memoriaRegistradores[rt] + int(str(val), 10))
        if pos in self.memoriaRegistradores:
            self.memoriaRegistradores[rs] = self.memoriaRegistradores[pos]
        else:
            print('posição inexistente')
        # Load Word: Esta instrução carrega uma palavra (estrutura de 4 bytes)
        # localizada no endereço representado pela soma do valor
        # armazenado no registrador $r2 mais 4. O resultado é armazenado em $r1.
    def sw(self, rs,rt,val):
        pos = '{0:05b}'.format(self.memoriaRegistradores[rt] + int(str(val), 10))
        if pos in self.memoriaRegistradores:
            self.memoriaRegistradores[pos] = self.memoriaRegistradores[rs]
        else:
            print('posição inexistente')
        # Store Word: Esta instrução carrega uma palavra (estrutura de 4 bytes)
        # localizada no registrador $r1 e armazena no endereço representado 
        # pela soma do valor armazenado no registrador $r2 mais 4.     
    def beq(self, rs, rt, destino, memoria):
        if(self.memoriaRegistradores[rs] == self.memoriaRegistradores[rt]):
            aux = int(str(int(destino,2)),10)
            aux /= 4
            aux += memoria.pc
            aux += 1
            memoria.setPC(aux)
        # Essa função verifica se o valor de um registrador é igual ao outro.
        # Caso verdadeiro muda o valor de PC para o destino informado.
        # Caso falso não faz nada.
    def bne(self, rs, rt, destino, memoria):
        if(self.memoriaRegistradores[rs] != self.memoriaRegistradores[rt]):
            memoria.setPC(int(str(int(destino,2)),10))
        # A função é semelhante a beq.
        # Nessa função o valor de PC só é alterado caso o valor dos registradores forem diferentes.
    def j (self, destino, memoria):
        memoria.setPC(int(str(int(destino,2)),10))
        # Essa função faz com que o programa passe a executar a instrução encontrada no endereço informado.
    
    def jal(self, destino, memoria):
        if int(str(int(destino,2)),10) > 31 and int(str(int(destino,2)),10) < 31 + memoria.quantInstrucoes: 
            memoria.setPC(memoria.pc+3)
            self.memoriaRegistradores['11111'] = memoria.getPC()
            memoria.setPC(int(str(int(destino,2)),10))
        else:
            print('Posicao inexistente')