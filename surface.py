import numpy as np
from abc import ABC, abstractmethod
from typing import NamedTuple
from ray import Ray, normalise

class HitData(NamedTuple):
    time: float
    point: np.ndarray
    normal: np.ndarray

class Surface(ABC):
    def __init__(self, center: np.ndarray):
        self.center = center

    @abstractmethod
    def hit(self, ray: Ray) -> float:
        pass

class Sphere(Surface):
    def __init__(self, center: np.ndarray, radius: float):
        super().__init__(center)
        self.radius = radius

    def hit(self, ray: Ray) -> float:
        oc = ray.origin - self.center
        a = np.dot(ray.direction, ray.direction)
        b = 2 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - (self.radius ** 2)
        disc = b ** 2 - 4 * a * c
        if disc < 0:
            return -1
        else:
            return (-b - np.sqrt(disc)) / 2 * a

class World():
    def __init__(self):
        self.surface_list = []

    def add(self, surface: Surface) -> None:
        self.surface_list.append(surface)

    def hit(self, ray: Ray) -> HitData:
        for surf in self.surface_list:
            if surf.hit(ray) > 0:
                time = surf.hit(ray)
                point = ray.at_time(time)
                normal = normalise(np.subtract(point, surf.center))
                return HitData(time, point, normal)
        return HitData(0, np.array([0., 0., 0.]), np.array([0., 0., 0.]))
