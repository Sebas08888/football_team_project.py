class League:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)
        print(f"Equipo {team.name} agregado a la liga {self.name}")

    def show_classification(self):
        print(f"\n===== Clasificación de la Liga: {self.name} =====")
        for i, team in enumerate(self.teams, 1):
            print(f"{i}. {team.name} — Jugadores: {len(team.players)}")