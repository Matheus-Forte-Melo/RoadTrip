class Compass:
    def __init__(self):
        self.direc = 1
        self.directions = {0: "O", 1: "N", 2: "L", 3: "S"}
        self.current_direction = self.direc

    def get_current_direction(self):
        return self.current_direction

    def turn_right(self):
        self.direc = self.direc + 1
        return self.current_direction
