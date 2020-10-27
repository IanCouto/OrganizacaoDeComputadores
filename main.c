#include <stdio.h>
#include <stdlib.h>
#include <string.h>



char **leArquivo()
{
    FILE *filePath;
    char **mat;
    char tam = 1;
    mat = (char**)malloc(sizeof(char) * tam);

    for (int i = 0; i < 16; i++)
    {
        mat[i] = (char*)malloc(sizeof(char) * 4);
    }

    filePath = fopen("input.txt", "r");

    if (filePath == NULL)
    {
        perror("Arquivo de input nao encontrado\n");
        exit(0);
    }

    /*
    
    printf("\n");

    for (int i = 0; mat[i][0] != EOF; i++)
    {
        fgets(mat[i], 5, filePath);
        printf(mat[i]);
    }
    fclose(filePath);
    
    */
    return mat;
}


void menu()
{
    printf("[0]carga do arquivo (fornecer o nome do arquivo)\n");
    printf("[1]entrada do programa via teclado (forma alternativa), evitando a necessidade de leitura do arquivo\n");
    printf("[2]inicio da execucao (passo-a-passo ou direta)\n");
    printf("[3]reset - utilizado para limpar a memoria/registradores\n");
}

int main(int argc, char const *argv[])
{
    menu();
    leArquivo();
    return 0;
}
