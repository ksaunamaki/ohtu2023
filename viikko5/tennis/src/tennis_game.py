class TennisGame:
    point_statuses = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.game_status = {}
        self.game_status[player1_name] = 0
        self.game_status[player2_name] = 0

    def won_point(self, player_name):
        self.game_status[player_name] += 1

    def _get_player_name(self, player):
        return list(self.game_status.keys())[player]

    def _get_points(self):
        return list(self.game_status.values())
    
    def _get_even_score(self, game_points):
        if game_points[0] < len(self.point_statuses):
            return f"{self.point_statuses[game_points[0]]}-All"

        return "Deuce"
    
    def _get_winning_score(self, leading_player, game_points):
        difference = game_points[leading_player] - game_points[abs(leading_player - 1)]
        player = self._get_player_name(leading_player)

        if difference == 1:
            return f"Advantage {player}"
        
        return f"Win for {player}"
    
    def get_score(self):
        game_points = self._get_points()

        if game_points[0] == game_points[1]:
            return self._get_even_score(game_points)
        
        if game_points[0] >= 4 or game_points[1] >= 4:
            leading_player = 0 if game_points[0] > game_points[1] else 1
            return self._get_winning_score(leading_player, game_points)
        
        return f"{self.point_statuses[game_points[0]]}-{self.point_statuses[game_points[1]]}"
