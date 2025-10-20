from game_map import Map
from game_logger import GameLogger

class MasterClass:
    def __init__(self, winner, move):
        self.winner = winner
        self.move = move
        self.Map1 = Map(10, 2)
        self.logging = GameLogger()

    def fight(self, move, x, y):
        if move == 1:
            if self.Map1.globalMap[y][x] == 'A':
                print("Влучання зареєстровано (A Player)")
                self.Map1.globalMap[y][x] = 'X'
                self.logging.log_shot('A', x, y, True)
            else:
                print("Влучання не зареєстровано (A Player)")
                self.logging.log_shot('A', x, y, False)
        elif move == 2:
            if self.Map1.globalMap[y][x] == 'B':
                print("Влучання зареєстровано (B Player)")
                self.Map1.globalMap[y][x] = 'Y'
                self.logging.log_shot('B', x, y, True)
            else:
                print("Влучання не зареєстровано (B Player)")
                self.logging.log_shot('B', x, y, False)
        
        winner = self.Map1.winners()
        if winner != 0:
            self.winner = winner
