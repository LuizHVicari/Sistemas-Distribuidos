#include <omp.h>
#include <iostream>

using namespace std;

int main(){
    omp_set_num_threads(5);
    #pragma omp parallel
    {
        cout << "Hello World!" << endl;
    }
}