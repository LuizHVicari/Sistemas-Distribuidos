#include <iostream>
#include <omp.h>

#define SIZE 100000000

using namespace std;

int main(){

    long *a = new long[SIZE];
    long *b = new long[SIZE];
    long *c = new long[SIZE];

    fill_n(a, SIZE, 112233);
    fill_n(b, SIZE, 445566);

    for(long i = 0; i < SIZE; ++i){
        c[i] = a[i] * b[i] + a[i] + b[i];
    }

    delete [] a;
    delete [] b;
    delete [] c;

    return 0;
}