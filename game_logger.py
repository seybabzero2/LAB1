import logging

class GameLogger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename="game_res.log", filemode="w")
        self.logger = logging.getLogger('SeaBattle')
    
    def log_shot(self, player, x, y, hit_success, ship_type=None):
        if hit_success:
            self.logger.info(f"Гравець {player} влучив у ({x},{y}) - корабель {ship_type}")
        else:
            self.logger.info(f"Гравець {player} промахнувся у ({x},{y})")
    
    def log_winner(self, winner):
        self.logger.info(f"Гравець {winner} виграв гру!")
    
    def log_error(self, message):
        self.logger.error(f"Помилка: {message}")
