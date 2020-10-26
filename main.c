#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void leArquivo()
{
    FILE *filePath;

    filePath = fopen("input.txt", "r");

    if (filePath == NULL)
    {
        perror("Arquivo de input nao encontrado\n");
        exit(0);
    }

    char caractere;
    while ((caractere = fgetc(filePath)) != EOF)
        printf("%c", caractere);

    fclose(filePath);
}

void menu(){
    printf("[0]carga do arquivo (fornecer o nome do arquivo)\n");
    printf("[1]entrada do programa via teclado (forma alternativa), evitando a necessidade de leitura do arquivo\n");
    printf("[2]inicio da execucao (passo-a-passo ou direta)\n");
    printf("[3]reset - utilizado para limpar a memória/registradores\n");
}

int main(int argc, char const *argv[])
{
    leArquivo();
    return 0;
}
