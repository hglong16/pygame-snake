class Manager:

    def __init__(self, velocity=1) -> None:
        self.velocity = velocity
        self.alive = True
        self.score = 0
        self.factor = 0.22
