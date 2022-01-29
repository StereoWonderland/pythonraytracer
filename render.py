import numpy as np
from PIL import Image
from ray import Ray
from surface import World

def ray_colour(ray: Ray, world: World) -> np.ndarray:
    if world.hit(ray):
        return np.array([255, 0, 0])
    else:
        t = 0.5 * (ray.unit_direction()[1])
        return (1 - t) * np.array([255, 255, 255]) + t * np.array([130, 200, 255])
