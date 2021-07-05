#include <stdio.h>
#include <string.h>

//Utiliza duas variáveis para atravessar a String de uma extremidade a outra,
//trocando o caractere de uma das pontas pelo da outra extremidade.
//Os últimos termos da String 'in' são salvos nas primeiras posições da String auxiliar 'out'.
//*Note que duas strings se fazem necessárias*

void reverseString(char *in, char *out) {
  int i, j;
  int N = strlen(in);
  for (i = 0, j = N - 1; j >= 0; ++i, --j) {
    out[i] = in[j];
  }
  out[N] = '\0';
}

//Atravessa a String de uma extremidade a outra,
//trocando o caractere de uma das pontas pelo da outra extremidade até chegar ao meio da String;
//de forma que os caracteres em sua String são invertidos.
//*Note que apenas uma string se faz necessária*

void reverseStringInPlace(char *in) {
  //Comprimento da string    
  int N = strlen(in);
  //Última posição válida(exclui-se a posição reservada para o finalizador '\0')
  int L = N-1;
  //comuta os elementos(char) a partir das pontas(i e L-1) até o meio(N/2)
  for (int i = 0; i < N/2; ++i) {
    char c = in[i];
    in[i] = in[L - i];
    in[L - i] = c;
  }
}

/*
Função Original
void reverseStringInPlace(char *in) {
  int i;
  int N = strlen(in);
  for (i = 0; i < N/2; ++i) {
    char c = in[i];
    in[i] = in[N - i];
    in[N - i] = c;
  }
}
*/

int main(int argc, char **argv) {
  //gera uma String para armazenar as informações desejadas pelos usuários
  char string_in[50];
  //gera uma String auxiliar para a função reverseString()
  char stringReversed[50];
  //ambas as strings contam com um limite de 49 "espaços úteis" para caracteres

  printf("Enter the string to be reversed:\n>>");
  //gets(string_in);
  fgets(string_in, 50, stdin); //fgets() é preferível ao gets()
                               //há, no entanto, de se considerar que
                               //o Comprimento da String é variável(podem haver "espaços vazios")    

  reverseString(string_in, stringReversed);
  //imprime a String auxiliar, preenchida com o inverso da Original
  printf("reversed = '%s'\n", stringReversed);

  reverseStringInPlace(string_in);
  //imprime a String Original com os valores das extremidades comutadas
  printf("reversed in place = '%s'\n", string_in);

  return 0;
}

/*
Questões

1. Em situações usuais, o código irá funcionar como esperado?
A função reverseString funcionaria, já a reverseStringInPlace não.
2. Existe alguma situação em que não irá funcionar?
Há problemas com caracteres UTF-8.
3. Caso exista alguma situação em que o código não irá funcionar, quais alterações seriam necessárias para corrigir os problemas?
Uma solução é adicionar a biblioteca locale e definir o idioma
Exemplo:
#include <locale.h>
  setlocale(LC_ALL, "Portuguese");
4. Pensando na legibilidade, facilidade de manutenção por outros desenvolvedores, e extensibilidade, você faria alguma refatoração no código?
Além de comentar o código e utilizar variáveis mais autoexplicativas, creio que o código ficou otimizado.
*/