#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    long double pi = 0;
    int i;

    #pragma omp paralell for reduction(+: pi)
    for(i = 1; i < 1000000000; i+=4){
           pi += 4.0 / i - 4.0 / (i + 2);
    }

    cout << " Valor de pi:" << setprecision(30) << pi << endl;


    return 0;
}