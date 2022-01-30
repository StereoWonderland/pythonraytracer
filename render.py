import numpy as np
from PIL import Image
from random import random
from ray import Ray
from surface import World

class Camera:
    def __init__(self, image_width, image_height, viewport_width,
                 viewport_height, focal_length, origin):
        self.image_width = image_width
        self.image_height = image_height
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.focal_length = focal_length
        self.origin = origin

        self.horizontal = np.array([viewport_width, 0., 0.])
        self.vertical = np.array([0., viewport_height, 0.])
        self.lower_left = (self.origin
                                  - self.horizontal / 2
                                  - self.vertical / 2
                                  - np.array([0., 0., self.focal_length]))

    def get_ray(self, i, j):
        x = j / (self.image_width - 1)
        y = (self.image_height - 1 - i) / (self.image_height - 1)
        ray = Ray(self.origin,
                  self.lower_left + x * self.horizontal + y * self.vertical)
        return ray

class Renderer:
    def __init__(self, camera: Camera, samples: int = 1):
        self.camera = camera
        self.samples = samples
        self.image = np.zeros((camera.image_height, camera.image_width, 3),
                              dtype=np.uint8)

    def render(self, world: World) -> None:
        for i in range(self.camera.image_height):
            print(f'\x1b[2KScanlines remaining: {self.camera.image_height - i}',
                  end='\r')
            for j in range(self.camera.image_width):
                colour = np.array([0., 0., 0.,])
                for _ in range(self.samples):
                    ray = self.camera.get_ray(i + random(), j + random())
                    colour += ray_colour(ray, world)
                self.image[i,j] = colour / self.samples

    def save(self, file_name: str) -> None:
        img = Image.fromarray(self.image, 'RGB')
        img.save(file_name)

def ray_colour(ray: Ray, world: World) -> np.ndarray:
    hit_data = world.hit(ray)
    if hit_data.time > 0:
        return 0.5 * 255 * np.array([hit_data.normal[0] + 1,
                                     hit_data.normal[1] + 1,
                                     hit_data.normal[2] + 1])
    else:
        t = 0.5 * (ray.unit_direction()[1] + 1)
        return (1 - t) * np.array([255, 255, 255]) + t * np.array([130, 200, 255])
