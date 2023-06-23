class Car:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def brake(self, percentage: int):
        percentage = percentage / 100
        self.speed = self.speed * percentage
        return round(self.speed)

    def accelerate(self, percentage: int):
        percentage = percentage / 100 + 1
        self.speed = self.speed * percentage
        return round(self.speed)


