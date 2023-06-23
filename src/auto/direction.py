class Compass:
    def __init__(self):
        self.directions = {0: "O", 1: "N", 2: "L", 3: "S"}
        self.current_direction = self.directions[1]

    def get_current_direction(self):
        return self.current_direction
