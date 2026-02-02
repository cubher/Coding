#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

float AVERAGE_VAL;
int MINIMUM_VAL;
int MAXIMUM_VAL;
int count;

void* AVG(void *data) {
    int *arr = (int*) data;
    float sum = 0;

    for (int i = 0; i < count; i++) {
        sum += arr[i];
    }

    AVERAGE_VAL = sum / count;
    return NULL;
}

void* MAX(void *data) {
    int *arr = (int*) data;
    int temp = arr[0];

    for (int i = 1; i < count; i++) {
        if (arr[i] > temp) {
            temp = arr[i];
        }
    }

    MAXIMUM_VAL = temp;
    return NULL;
}

void* MIN(void *data) {
    int *arr = (int*) data;
    int temp = arr[0];

    for (int i = 1; i < count; i++) {
        if (arr[i] < temp) {
            temp = arr[i];
        }
    }

    MINIMUM_VAL = temp;
    return NULL;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s num1 num2 num3 ...\n", argv[0]);
        return EXIT_FAILURE;
    }

    count = argc - 1;
    int *numbers = malloc(count * sizeof(int));

    for (int i = 0; i < count; i++) {
        numbers[i] = atoi(argv[i + 1]);
    }

    pthread_t p1, p2, p3;

    pthread_create(&p1, NULL, AVG, numbers);
    pthread_create(&p2, NULL, MAX, numbers);
    pthread_create(&p3, NULL, MIN, numbers);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);

    printf("Average value: %.2f\n", AVERAGE_VAL);
    printf("Minimum value: %d\n", MINIMUM_VAL);
    printf("Maximum value: %d\n", MAXIMUM_VAL);

    free(numbers);
    return EXIT_SUCCESS;
}
