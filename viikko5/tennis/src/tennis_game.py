from typing import Optional


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def add_score(self):
        self.score += 1
    
    def get_score(self):
        match self.score:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"
            case _:
                return f"Advantage {self.name}"
            
def compare_scores(player1: Player, player2: Player) -> tuple[Optional[Player], int]:
    if player1.score == player2.score:
        return None, 0
    elif player1.score > player2.score:
        return player1, abs(player1.score - player2.score)
    else:
        return player2, abs(player1.score - player2.score)

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.add_score()
        else:
            self.player2.add_score()

    def get_score(self):
        scores = compare_scores(self.player1, self.player2)
        if scores[0] is None:
            if self.player1.score < 3:
                return f"{self.player1.get_score()}-All"
            else:
                return "Deuce"
        
        elif scores[0] is not None and scores[0].score >= 4:
            if scores[1] >= 2:
                return f"Win for {scores[0].name}"
            elif scores[1] == 1:
                return f"Advantage {scores[0].name}"          
                
        else:
            return f"{self.player1.get_score()}-{self.player2.get_score()}"
