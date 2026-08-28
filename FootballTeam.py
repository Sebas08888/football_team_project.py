class FootballTeam:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.coach = None

    def add_player(self, player):
        self.players.append(player)
        print(f"{player.name} agregado al equipo {self.name}")

    def hire_coach(self, coach):
        self.coach = coach
        print(f"{coach.name} contratado como entrenador de {self.name}!")

    def show_team(self):
        print(f"\n===== Equipo: {self.name} =====")
        if self.coach:
            print(f"Entrenador: {self.coach.name}")
        print("Jugadores:")
        for player in self.players:
            print(f"  - {player}")