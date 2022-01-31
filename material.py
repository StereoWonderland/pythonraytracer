import numpy as np
from abc import ABC, abstractmethod
from ray import normalise

class Material(ABC):
    def __init__(self, colour: np.ndarray):
        self.colour = colour

    @abstractmethod
    def scatter(self, colour):
        pass

class Lambertian(Material):
    def __init__(self, colour: np.ndarray):
        super().__init__(colour)

    def scatter(self, point, normal):
        target = point + normal + random_unit_vector()
        return target

def random_point_in_unit_ball() -> np.ndarray:
    random_point = np.random.uniform(-1, 1, (3,))
    if np.sum(np.square(random_point)) <= 1:
        return random_point
    else:
        return random_point_in_unit_ball()

def random_unit_vector() -> np.ndarray:
    return normalise(random_point_in_unit_ball())
