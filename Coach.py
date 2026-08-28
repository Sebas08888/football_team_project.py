class Coach:
    def __init__(self, name, experience_years):
        self.name = name
        self.experience_years = experience_years

    def give_instructions(self, tactic):
        print(f"Entrenador {self.name} dice: Vamos a jugar {tactic}!")

    def __str__(self):
        return f"Entrenador: {self.name} | Experiencia: {self.experience_years} años"