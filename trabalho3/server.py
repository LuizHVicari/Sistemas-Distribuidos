from concurrent import futures

import grpc
import protocol_pb2
import protocol_pb2_grpc

from battleship import BattleShip

game = BattleShip()
game.read_matrix()

class Target(protocol_pb2_grpc.TargetServicer):
   def SendBomb(self, request, context):
      print(f"Recebeu request:\n {str(request)}")
      x = int(request.x)
      y = int(request.y)

      print(f'Coordenadas do lance: x={x}, y={y}')
      game.target(x, y)
      return protocol_pb2.TargetResponse(message = '{0} {1}'.format(request.x, request.y), board=str(game.board))


def server():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
   protocol_pb2_grpc.add_TargetServicer_to_server(Target(), server)
   server.add_insecure_port('[::]:50051')
   print('Starting')
   server.start()
   server.wait_for_termination()

server()