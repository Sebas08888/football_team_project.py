class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def __str__(self):
        return f"Estadio: {self.name} | Capacidad: {self.capacity} | Ciudad: {self.location}"

