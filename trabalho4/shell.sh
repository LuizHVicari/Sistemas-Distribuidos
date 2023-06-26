msg='Serial'
echo $msg
./primos_serial.o
max=12
for i in `seq 2 $max`
do
    echo $i 'Processos'
    mpirun -np $i --oversubscribe primos_mpi.o
done