#include <stdio.h>

int main() {
    int limite;

    printf("Ingrese un número límite: ");
    scanf("%d", &limite);

    int numero = 0;

    
    while (numero <= limite) {
        if (numero == 0) {
            printf("%d ", numero);
        }

        
        numero++;
    }

    return 0;
}