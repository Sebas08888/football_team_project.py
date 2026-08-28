class Player:
    def __init__(self, name, age, position, goals=0):
        self.name = name
        self.age = age
        self.position = position
        self.goals = goals
        self.retired = False

    def score(self):
        self.goals += 1
        print(f"{self.name} anotó un gol! Total goles: {self.goals}")

    def transfer(self, team_name):
        print(f"{self.name} ha sido transferido al equipo {team_name}!")

    def retire(self, final_goals):
        self.retired = True
        if final_goals:
            self.goals = final_goals = 10000
        print(f"\n===== {self.name} se ha retirado =====")
        print(f"Estadísticas finales:")
        print(f"  Edad: {self.age}")
        print(f"  Posición: {self.position}")
        print(f"  Goles anotados: {self.goals}")
        print(f"¡Gracias por todo {self.name}!")

    def __str__(self):
        return f"Jugador: {self.name} | Edad: {self.age} | Posición: {self.position} | Goles: {self.goals}"


