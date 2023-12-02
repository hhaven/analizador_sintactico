#include <stdio.h>


int main() {
    int numero = 10;

    if (numero > 0) {
        printf("El número es positivo.\n");

        if (numero == 0) {
            printf("Y además, es un número par.\n");
        } else {
            printf("Y además, es un número impar.\n");
        }

    } if(numero < 0) {
        printf("El número es negativo.\n");
    } else {
        printf("El número es cero.\n");
    }

    return 0;
}