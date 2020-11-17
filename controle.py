
class controle:
    
    def __init__(self):
        self.memToReg = 0
        self.aluOP = 0
        self.memWrite = 0
        self.aluSRC = 0
        self.regWrite = 0
        self.bne = 0
        self.regDst = 0
        self.jump = 0
        self.branch = 0
        self.memRead = 0

    def controlVar(self, opcode, func):
            # Tipo R
        if (opcode == '000000'):
            self.memToReg = 0
            self.aluOP = 2
            self.memWrite = 0
            self.aluSRC = 0
            self.regWrite = 1
            self.bne = 0
            self.regDst = 1
            self.branch = 0
            self.memRead = 0
            if (func == '001000'):
                self.jump = 2
            else:
                self.jump = 0

        # Tipo I

        # addi
        elif (opcode == '001000'):
            self.memToReg = 0
            self.aluOP = 0
            self.memWrite = 0
            self.aluSRC = 1
            self.regWrite = 1
            self.bne = 0
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 0

        # lw
        elif (opcode == '100011'):
            self.memToReg = 1
            self.aluOP = 0
            self.memWrite = 0
            self.aluSRC = 1
            self.regWrite = 1
            self.bne = 0
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 1

        # sw
        elif (opcode == '101011'):
            self.memToReg = 0
            self.aluOP = 0
            self.memWrite = 1
            self.aluSRC = 1
            self.regWrite = 0
            self.bne = 0
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 0

        # beq
        elif (opcode == '000100'):
            self.memToReg = 0
            self.aluOP = 1
            self.memWrite = 0
            self.aluSRC = 0
            self.regWrite = 0
            self.bne = 0
            self.regDst = 0
            self.jump = 0
            self.branch = 1
            self.memRead = 0

        # bne
        elif (opcode == '000101'):
            self.memToReg = 0
            self.aluOP = 1
            self.memWrite = 0
            self.aluSRC = 0
            self.regWrite = 0
            self.bne = 1
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 0

        # Tipo J

        # j
        elif (opcode == '000010'):
            self.memToReg = 0
            self.aluOP = 0
            self.memWrite = 0
            self.aluSRC = 0
            self.regWrite = 0
            self.bne = 0
            self.regDst = 0
            self.jump = 1
            self.branch = 0
            self.memRead = 0

        # jal
        elif (opcode == '000011'):
            self.memToReg = 2
            self.aluOP = 0
            self.memWrite = 0
            self.aluSRC = 0
            self.regWrite = 1
            self.bne = 0
            self.regDst = 2
            self.jump = 1
            self.branch = 0
            self.memRead = 0

    def imprimeVar(self, saida):
        saida.write('Variaveis de controle:\n')
        saida.write('memToReg: ' + str(self.memToReg) + '\n')
        saida.write('aluOP: ' + str(self.aluOP) + '\n')
        saida.write('memWrite: ' + str(self.memWrite) + '\n')
        saida.write('aluSRC: ' + str(self.aluSRC) + '\n')
        saida.write('regWrite: ' + str(self.regWrite) + '\n')
        saida.write('bne: ' + str(self.bne) + '\n')
        saida.write('regDst: ' + str(self.regDst) + '\n')
        saida.write('jump: ' + str(self.jump) + '\n')
        saida.write('branch: ' + str(self.branch) + '\n')
        saida.write('memRead: ' + str(self.memRead) + '\n')
