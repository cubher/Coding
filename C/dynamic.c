#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// macro for array max size
#define MAX_SIZE 100

// inline function for swaping two variables
static inline void swap(int *a,int* b)
{
    int temp =*a;
    *a=*b;
    *b=temp;
}

int main(int argc, char const *argv[])
{
    int i,n;
    int list[MAX_SIZE];
    printf("Enter number of elements (max %d): ", MAX_SIZE);
    scanf("%d",&n);
    if(n>MAX_SIZE && n>1)
    {
        fprintf(stderr,"invalid number of elements \n");
        exit(EXIT_FAILURE); 
    }
}
