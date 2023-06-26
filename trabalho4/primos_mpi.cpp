#include <iostream>
#include <cmath>
#include <mpi.h>
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

int main(int argc, char** argv){
    int rank, size, chunk_size, chunk_start, chunk_end, local_count, global_count;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    chunk_size = (MAX_NUM - 1) / size;
    chunk_start = rank * chunk_size + 1;
    chunk_end = (rank == size - 1) ? MAX_NUM : chunk_start + chunk_size - 1;

    auto start = std::chrono::steady_clock::now();

    local_count = 0;
    for(int i = chunk_start; i <= chunk_end; ++i){
        if(is_prime(i)){
            local_count++;
        }
    }
    if(rank != 0) {
        MPI_Send(&local_count, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }


    else{
        int c = 0;
        for(int i = 1; i < size; ++i){
            MPI_Recv(&c, 1, MPI_INT, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE); 
            local_count += c;
        }
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> elapsed_time = end - start;
        cout << "total de primos encontrados: " << local_count << endl << "levou: " << elapsed_time.count() << endl;
    }

    MPI_Finalize();

    return 0;
}
