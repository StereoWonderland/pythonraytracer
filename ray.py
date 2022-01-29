import numpy as np

class Ray:
    def __init__(self, origin: np.ndarray, direction: np.ndarray):
        self.origin = origin
        self.direction = direction

    def at_time(self, time: float) -> np.ndarray:
        return self.origin + time * self.direction

    def unit_direction(self) -> np.ndarray:
        return normalise(self.direction)

def normalise(vector: np.ndarray) -> np.ndarray:
    return np.divide(vector, np.sqrt(np.sum(np.square(vector))))
