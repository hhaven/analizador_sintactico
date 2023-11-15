#include <stdio.h>

int sum(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    int y = 10;
    int result;

    result = sum(x, y);

    if (result > 10) {
        printf("El resultado es mayor que 10.\n");
    } else {
        printf("El resultado es 10 o menos.\n");
    }

    for (int i = 0; i < result; i++) {
        printf("%d ", i);
    }

    return 0;
}