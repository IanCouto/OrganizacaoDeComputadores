import os
from os import pipe

tipoDeEntrada = ''
entrada = ''

def entradaPorArquivo():
    entrada = ''
    aux = ''
    print('digite o caminho do arquivo de entrada:')
    caminhoDoArquivo = input()
    entrada = open(caminhoDoArquivo, 'r')
    return entrada

def entradaPorTeclado():
    entrada = ''
    aux = ''
    print('digite a entrada e para finaliza-la, digite 2:')
    while aux != '2':
        aux = input()
        if aux == '2':
                break
        if tratarEntrada(aux):
            entrada += aux
            entrada += "\n"
        else:
            entrada = ""
            print('entrada alternativa indesejada: ' + aux)
            break
    return entrada

def tratarEntrada(str):
    for char in str:
        if char not in {'0', '1'}:
            return False
    return True

def menu(tipoDeEntrada):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Digite | Para')
    print('   0   | Sair')
    print('   1   | Leitura de comando por arquivo')
    print('   2   | Leitura de comandos via teclado')
    tipoDeEntrada = input()
    if tipoDeEntrada == '1':
        return entradaPorArquivo()
    elif tipoDeEntrada == '2':
        return entradaPorTeclado()
    elif tipoDeEntrada not in {'0', '1', '2'}:
        print('Entrada indesejada')
    
def menu2():
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


while tipoDeEntrada != '0':
    tipoDeEntrada = 50
    entrada = menu(tipoDeEntrada)
    print(tipoDeEntrada)
    menu2()

