import numpy as np
from PIL import Image
from ray import Ray
from surface import World

class Renderer:
    def __init__(self, image_width, image_height, viewport_width,
                 viewport_height, focal_length, origin):
        self.image_width = image_width
        self.image_height = image_height
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.focal_length = focal_length
        self.origin = origin

        self.image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
        self.horizontal = np.array([viewport_width, 0., 0.])
        self.vertical = np.array([0., viewport_width, 0.])
        self.lower_left = (self.origin
                                  - self.horizontal / 2
                                  - self.vertical / 2
                                  - np.array([0., 0., self.focal_length]))

def ray_colour(ray: Ray, world: World) -> np.ndarray:
    if world.hit(ray):
        return np.array([255, 0, 0])
    else:
        t = 0.5 * (ray.unit_direction()[1] + 1)
        return (1 - t) * np.array([255, 255, 255]) + t * np.array([130, 200, 255])
