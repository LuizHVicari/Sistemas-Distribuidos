import grpc
import protocol_pb2
import protocol_pb2_grpc

from battleship import BattleShip
import numpy as np
import os


game = BattleShip()

def target():
    while True:
        x = input('Informe o X do alvo: ')
        y = input('Informe o y do alvo: ')

        if int(x) >= 0 and int(x) < 10 and int(y) >= 0 and int(y) < 10:
            break
        print('Coordenadas inválidas')  

    return x, y

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = protocol_pb2_grpc.TargetStub(channel)
        while True:
            os.system('clear')
            if game.check_win():
                print('ganhou')
                break
            game.print_board()
            x,y = target()
            response = stub.SendBomb(protocol_pb2.TargetRequest(x=x, y=y))


            board = response.board[1:-1].replace(']', '').replace('[', '')
            board = np.fromstring(board, dtype=int, sep=' ').reshape((10,10))
            game.board = board

run()
