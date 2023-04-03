#include <iostream>
#include <omp.h>

#define SIZE 100000000

using namespace std;

int main(){

    long *a = new long[SIZE];
    long *b = new long[SIZE];
    long *c = new long[SIZE];

    #pragma omp parallel for num_threads(16)
    for(long i = 0; i < SIZE; ++i){
        a[i] = i;
        b[i] = i;
        c[i] = a[i] * b[i] + a[i] + b[i];
    }

    delete [] a;
    delete [] b;
    delete [] c;

    return 0;
}