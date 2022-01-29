import numpy as np
from abc import ABC, abstractmethod
from ray import Ray

class Surface(ABC):
    @abstractmethod
    def hit(self, ray: Ray) -> bool:
        pass

class Sphere(Surface):
    def __init__(self, center: np.ndarray, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, ray: Ray) -> bool:
        oc = ray.origin - self.center
        a = np.dot(ray.direction, ray.direction)
        b = 2 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - (self.radius ** 2)
        disc = b ** 2 - 4 * a * c
        return disc > 0
