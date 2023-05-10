import numpy as np
import colorama
from colorama import Fore
import os


class BattleShip():
    def __init__(self):
        self.board = np.zeros((10, 10)).astype(np.uint8)
        self.carrier_pos = False
        self.battleship_pos = False
        self.destroyer_pos = False
        self.submarine_pos = False
        self.patrol_boat_pos = False
        self.rounds = list()

    def position_carrier(self, ini, end, row, axis):
        if np.abs(ini - end) != 5 or self.carrier_pos:
            return False
        if ini > end:
            ini, end = end, ini
        if axis == 'y':
            if not np.sum(self.board[ini:end, row]):
                self.board[ini:end, row] = 1
            else:
                return False
        elif axis == 'x':
            if not np.sum(self.board[row, ini:end]):
                self.board[row, ini:end] = 1
            else:
                return False
        self.carrier_pos = True
        return True


    def position_battleship(self, ini, end, row, axis):
        if np.abs(ini - end) != 4 or self.battleship_pos:
            return False
        if ini > end:
            ini, end = end, ini
        if axis == 'y':
            if not np.sum(self.board[ini:end, row]):
                self.board[ini:end, row] = 1
            else:
                return False
        elif axis == 'x':
            if not np.sum(self.board[row, ini:end]):
                self.board[row, ini:end] = 1
            else:
                return False
        self.battleship_pos = True
        return True

    
    def position_destroyer(self, ini, end, row, axis):
        if np.abs(ini - end) != 3 or self.destroyer_pos:
            return False
        if ini > end:
            ini, end = end, ini
        if axis == 'y':
            if not np.sum(self.board[ini:end, row]):
                self.board[ini:end, row] = 1
            else:
                return False
        elif axis == 'x':
            if not np.sum(self.board[row, ini:end]):
                self.board[row, ini:end] = 1
            else:
                return False
        self.destroyer_pos = True
        return True


    def position_submarine(self, ini, end, row, axis):
        if np.abs(ini - end) != 3 or self.submarine_pos:
            return False
        if ini > end:
            ini, end = end, ini
        if axis == 'y':
            if not np.sum(self.board[ini:end, row]):
                self.board[ini:end, row] = 1
            else:
                return False
        elif axis == 'x':
            if not np.sum(self.board[row, ini:end]):
                self.board[row, ini:end] = 1
            else:
                return False
        self.submarine_pos = True
        return True

    
    def position_patrol_boat(self, ini, end, row, axis):
        if np.abs(ini - end) != 2 or self.patrol_boat_pos:
            return False
        if ini > end:
            ini, end = end, ini
        if axis == 'y':
            if not np.sum(self.board[ini:end, row]):
                self.board[ini:end, row] = 1
            else:
                return False
        elif axis == 'x':
            if not np.sum(self.board[row, ini:end]):
                self.board[row, ini:end] = 1
            else:
                return False
        self.patrol_boat_pos = True
        return True
    

    def is_valid(self, x, y):
        return not ((x, y) in self.rounds or x > 9 or x < 0 or y < 0 or y > 8)

    
    def target(self, x, y):
        if self.is_valid(x , y):
            self.rounds.append((x, y))
            if self.board[y, x] == 1:
                self.board[y, x] = 2
                print('acertou')
            else:
                self.board[y, x] = 3
                print('errou')
            return True
        return False

    def print_board(self):
        print('   ', end='')
        for n in range(0, 10):
            print(n, end=' ')
        print()
        for i in range(self.board.shape[0]):
            print(str(i).ljust(2), end=' ')
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0 or self.board[i, j] == 1:
                    color = Fore.CYAN
                elif self.board[i, j] == 2:
                    color = Fore.BLACK
                else:
                    color = Fore.RED
                print(color + 'X', end=' ')
            print(Fore.WHITE)

    def print_board_defensor_view(self):
        print('   ', end='')
        for n in range(0, 10):
            print(n, end=' ')
        print()
        for i in range(self.board.shape[0]):
            print(str(i).ljust(2), end=' ')
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0:
                    color = Fore.CYAN
                if self.board[i, j] == 1:
                    color = Fore.YELLOW
                elif self.board[i, j] == 2:
                    color = Fore.BLACK
                else:
                    color = Fore.RED
                print(color + 'X', end=' ')
            print(Fore.WHITE)

    def get_ship(self, name, x):
        try:
            ini, end, row, axis = input(f'Informe o ponto de início, de fim, a coluna/linha e o eixo, separados por vírgula para o {name}, {x} pontos: ').split(',')
            ini = int(ini)
            end = int(end)
            row = int(row)

            return ini, end, row, axis
        except Exception as e:
            if e == KeyboardInterrupt:
                raise(KeyboardInterrupt)
            print('Algo deu errado, tente novamente')
            return self.get_ship(name, x)
        
    def build_board(self):
        while True:
            ini, end, row, axis = self.get_ship('carrier', 5)
            if game.position_carrier(ini, end, row, axis):
                break
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board_defensor_view()

        while True:
            ini, end, row, axis = self.get_ship('battleship', 4)
            if self.position_battleship(ini, end, row, axis):
                break

        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board_defensor_view()

        while True:
            ini, end, row, axis = self.get_ship('destroyer', 3)
            if self.position_destroyer(ini, end, row, axis):
                break

        os.system('cls' if os.name == 'nt' else 'clear')   
        self.print_board_defensor_view()

        while True:
            ini, end, row, axis = self.get_ship('submarine', 3)
            if self.position_submarine(ini, end, row, axis):
                break
        
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board_defensor_view()

        while True:
            ini, end, row, axis = self.get_ship('patrol_boat', 2)
            if self.position_patrol_boat(ini, end, row, axis):
                break
        
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board_defensor_view()

    def check_win(self):
        board = self.board.copy()
        board = np.where(board == 1, board, 0)
        return np.sum(board) == 17


if __name__ == '__main__':

    game = BattleShip()
    game.print_board()

    game.build_board()

    while True:
        x, y = input('Informe o ponto do alvo, com valores separados por vírgula: ').split(',')
        x, y = int(x), int(y)
        os.system('cls' if os.name == 'nt' else 'clear')
        game.target(x, y)

        if game.check_win():
            print('Parabés, você ganhou!!')
            break
        game.print_board()