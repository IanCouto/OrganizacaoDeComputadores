#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void leArquivo()
{
    char file_name[25];
    FILE *filePath;

    printf("Digite o nome do arquivo de input:");
    gets(file_name);

    filePath = fopen(file_name, "r");

    if (filePath == NULL)
    {
        perror("Arquivo nao encontrado\n");
        exit(0);
    }

    char caractere;
    while ((caractere = fgetc(filePath)) != EOF)
        printf("%c", caractere);

    fclose(filePath);
}

int main(int argc, char const *argv[])
{
    leArquivo();
    return 0;
}
