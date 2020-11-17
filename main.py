from dicionario import dicionario
from memoriaRAM import memoriaRAM


tipoDeEntrada = ''
entrada = ''
memoria = None

def entradaPorArquivo():
    global entrada
    aux = ''
    print('Digite o caminho do arquivo de entrada:')
    #caminhoDoArquivo = input()
    entrada = open('input.txt', 'r')


def entradaPorTeclado():
    global entrada
    entrada = []
    aux = ''
    print('Digite a entrada e para finaliza-la, digite 2:')
    while aux != '2':
        aux = str(input())
        if aux == '2':
            break
        if tratarEntrada(aux):
            entrada.append(aux + '\n')
        else:
            entrada = ''
            print('Entrada alternativa indesejada: ' + aux)
            break


def tratarEntrada(str):
    if len(str) != 32:
        return False
    for char in str:
        if char not in {'0', '1'}:
            return False
    return True


def menu(dicionario):
    print('Digite | Para')
    print('   0   | Sair')
    print('   1   | Leitura de comando por arquivo')
    print('   2   | Leitura de comandos via teclado')
    global tipoDeEntrada
    tipoDeEntrada = input()
    if tipoDeEntrada == '1':
        entradaPorArquivo()
        menu2(dicionario)
    elif tipoDeEntrada == '2':
        entradaPorTeclado()
        menu2(dicionario)


def menu2(dicionario):
    print('   1   | Execução completa')
    print('   2   | Execução por linha')
    print('   3   | Reset')
    saida = None
    memoria = memoriaRAM(entrada, dicionario)
    tipoDeEntrada = input()
    i = 0
    aux = memoria.getPC()
    saida = None
    if tipoDeEntrada == '1':
        print('Execução completa')
        aux = memoria.getPC()
        saida = open('output.txt', 'w')
        while aux != -1:
            saida.write('====================================\n')
            print('====================================')
            print(dicionario.traduzirComando(aux))
            dicionario.executaComando(aux, memoria, saida)
            saida.write('\ncomando: ' + dicionario.traduzirComando(aux) + '\n')
            saida.write('pc = ' + aux + '\n')
            print('pc = ' + aux)
            print('registradores: ')
            saida.write('\nregistradores:\n')
            for registrador in dicionario.memoriaRegistradores: 
                string = str(dicionario.dicRegistradores[registrador]) + ' = ' + str(dicionario.memoriaRegistradores[registrador])
                saida.write(str(string) + '\n')
                print(str(string))
                saida.flush()
            aux = memoria.getPC()
            memoria.printMemoriaDeDados(saida)
        saida.close()
        print('Instruções Finalizadas!')

    elif tipoDeEntrada == '2':
        print('Execução por linha')
        aux2 = 0 
        aux = memoria.getPC()
        saida = open('output.txt', 'w')
        while aux != -1:
            saida.write('====================================\n')
            print('====================================')
            dicionario.executaComando(aux, memoria, saida)
            print(dicionario.traduzirComando(aux))
            saida.write('\ncomando: ' + dicionario.traduzirComando(aux) + '\n')
            saida.write('pc = ' + aux + '\n')
            print('pc = ' + aux)
            print('registradores: ')
            saida.write('\nregistradores:\n')
            for registrador in dicionario.memoriaRegistradores: 
                string = str(dicionario.dicRegistradores[registrador]) + ' = ' + str(dicionario.memoriaRegistradores[registrador])
                saida.write(str(string) + '\n')
                print(str(string))
            
            print('pressione enter para seguir para o proximo comando...')
            saida.flush()
            aux = memoria.getPC()
            aux2 = input()
            memoria.printMemoriaDeDados(saida)
            if aux2 == '-1' or aux == '-1':
                break
        saida.close()
        print('Instruções Finalizadas!')

    elif tipoDeEntrada == '3':
        print('reset')
        menu(dicionario)
    elif tipoDeEntrada not in {'1', '2', '3'}:
        print('Entrada indesejada')
        menu2()

if __name__ == "__main__":
    dicionario = dicionario()
    menu(dicionario)
    