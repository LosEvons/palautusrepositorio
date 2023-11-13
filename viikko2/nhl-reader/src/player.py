import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.penalties = dict['penalties']
        self.games = dict['games']
    
    def __str__(self):
        return f"{self.name:<20} {self.team:>10} {self.goals:>3} + {self.assists:>3} = {self.goals + self.assists:>3}"

class PlayerReader:
    def __init__(self, url):
        self.url = url    

    def get_players(self):
        response = requests.get(self.url).json()
    
        for player_dict in response:
            yield Player(player_dict)

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nat: str):
        return list(player for player in self.reader.get_players() if player.nationality == nat)
        