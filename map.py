rom game_logger import GameLogger

class Map:
    def __init__(self, size, counterOfShips):
        self.size = size
        self.globalMap = [['B', 'B', 'A', 'A', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
        self.arrOfHits = []
        self.counterOfShips = counterOfShips
        self.logging = GameLogger()

    def winners(self):
        tempA = 0
        tempB = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.globalMap[i][j] == 'X':
                    tempA += 1
                elif self.globalMap[i][j] == 'Y':
                    tempB += 1
                else:
                    continue

        if tempA == self.counterOfShips:
            print("Player 1 is winner")
            self.logging.log_winner(1)
            return 1
        elif tempB == self.counterOfShips:
            print("Player 2 is winner")
            self.logging.log_winner(2)
            return 2
        return 0
