import random
from FootballTeam import FootballTeam

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        goals_team1 = random.randint(0, 5)
        goals_team2 = random.randint(0, 5)
        print(f"\n===== Partido: {self.team1.name} vs {self.team2.name} =====")
        print(f"{self.team1.name} {goals_team1} - {goals_team2} {self.team2.name}")

        if goals_team1 > goals_team2:
            print(f"Ganador: {self.team1.name} 🏆")
        elif goals_team2 > goals_team1:
            print(f"Ganador: {self.team2.name} 🏆")
        else:
            print("Resultado: Empate!")