#include <iostream>

using namespace std;

int main()
{    
    #pragma omp parallel for 
    for (long i=0; i <= 10000000000; ++i)
    {

    }

    return 0;
}