from FootballTeam import FootballTeam

class ClubTeam(FootballTeam):
    def __init__(self, name, trophies=0):
        super().__init__(name)
        self.trophies = trophies
        self.stadium = None

    def sign_player(self, player):
        self.players.append(player)
        print(f"{player.name} fichado oficialmente por {self.name}!")

    def compare_trophies(self, other_team):
        print(f"\n===== Comparación de Trofeos =====")
        print(f"{self.name}: {self.trophies} trofeos")
        print(f"{other_team.name}: {other_team.trophies} trofeos")
        if self.trophies > other_team.trophies:
            print(f"{self.name} es más exitoso!")
        elif other_team.trophies > self.trophies:
            print(f"{other_team.name} es más exitoso!")
        else:
            print("Ambos equipos tienen los mismos trofeos!")

    def assign_stadium(self, stadium):
        self.stadium = stadium
        print(f"Estadio {stadium.name} asignado a {self.name}!")