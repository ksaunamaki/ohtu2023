import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)

        if player.nationality == "FIN":
            players.append(player)

    print(f"Players from FIN\n")

    for player in sorted(players, key=lambda player: player.total, reverse=True):
        print(player)

if __name__ == "__main__":
    main()
