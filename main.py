from dicionario import dicionario
from memoriaRAM import memoriaRAM
import os


def __init__(self):
    self.tipoDeEntrada = ''
    self.entrada = ''
    dicionario.__init__

def entradaPorArquivo():
    global entrada
    aux = ''
    print('Digite o caminho do arquivo de entrada:')
    #caminhoDoArquivo = input()
    entrada = open('input.txt', 'r')


def entradaPorTeclado():
    global entrada
    aux = ''
    print('Digite a entrada e para finaliza-la, digite 2:')
    while aux != '2':
        aux = input()
        if aux == '2':
            break
        if tratarEntrada(aux):
            entrada += aux
            entrada += "\n"
        else:
            entrada = ""
            print('Entrada alternativa indesejada: ' + aux)
            break


def tratarEntrada(str):
    if len(str) != 32:
        return False
    for char in str:
        if char not in {'0', '1'}:
            return False
    return True


def menu():
    
    print('Digite | Para')
    print('   0   | Sair')
    print('   1   | Leitura de comando por arquivo')
    print('   2   | Leitura de comandos via teclado')
    global tipoDeEntrada
    tipoDeEntrada = input()
    if tipoDeEntrada == '1':
        entradaPorArquivo()
        menu2()
    elif tipoDeEntrada == '2':
        entradaPorTeclado()
        menu2()


def menu2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('   1   | Execução completa')
    print('   2   | Execução por linha')
    print('   3   | Reset')
    tipoDeEntrada = input()
    if tipoDeEntrada == '1':
        print('Execução completa')
    elif tipoDeEntrada == '2':
        print('Execução por linha')
    elif tipoDeEntrada == '3':
        print('reset')
        menu()
    elif tipoDeEntrada not in {'1', '2', '3'}:
        print('Entrada indesejada')
        menu2()

if __name__ == "__main__":
    entradaPorArquivo()
    dicionario = dicionario()
    memoria = memoriaRAM(entrada, dicionario)
    i = 0
    while i < memoriaRAM.size(memoria):
        print('pos ' + str(i) + ': ' +str(memoria.get(i)))
        i += 1
    aux = memoria.getPC()
    while aux != -1:
        print(dicionario.traduzirComando(aux))
        for registrador in dicionario.memoriaRegistradores:
            print(dicionario.dicRegistradores[registrador], '=', dicionario.memoriaRegistradores[registrador])
        aux = memoria.getPC()
    #memoria.getRegistradores()