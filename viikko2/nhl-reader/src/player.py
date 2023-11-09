import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    @property
    def total(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}{self.team:5}{self.goals} + {self.assists} = {self.total}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = filter(lambda player: player.nationality == nationality, self.reader.get_players())
        
        return sorted(players, key=lambda player: player.total, reverse=True)