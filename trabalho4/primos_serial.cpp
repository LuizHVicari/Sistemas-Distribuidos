#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;

#define MAX_NUM 30000000

bool is_prime(int num){
    bool ret = false;
    for(int i = 2; i < sqrt(num); ++i){
        if(num % i == 0){
            break;
        }
        if(i == sqrt(num)){
            ret = true;
        }
    }
    return ret;
}

int main(){
    int tot_primes = 0;
    auto start = std::chrono::steady_clock::now();
    for(long long i = 1; i < MAX_NUM; ++i){
        if(is_prime(i)){
            tot_primes++;
        }
    }
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_time = end - start;
    cout << tot_primes << endl << "levou: " << elapsed_time.count() << endl;
    return 0;
}