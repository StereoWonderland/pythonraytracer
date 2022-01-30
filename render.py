import numpy as np
from PIL import Image
from ray import Ray, normalise
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
        self.vertical = np.array([0., viewport_height, 0.])
        self.lower_left = (self.origin
                                  - self.horizontal / 2
                                  - self.vertical / 2
                                  - np.array([0., 0., self.focal_length]))

    def render(self, world: World) -> None:
        for i in range(self.image_height):
            print(f'Scanlines remaining: {self.image_width - i}', end='\r')
            for j in range(self.image_width):
                x = j / (self.image_width - 1)
                y = (self.image_height - 1 - i) / (self.image_height - 1)
                ray = Ray(self.origin,
                          self.lower_left
                          + x * self.horizontal
                          + y * self.vertical)
                colour = ray_colour(ray, world)
                self.image[i,j] = colour

    def save(self, file_name: str) -> None:
        img = Image.fromarray(self.image, 'RGB')
        img.save(file_name)

def ray_colour(ray: Ray, world: World) -> np.ndarray:
    time, center = world.hit(ray)
    if time > 0:
        normal = normalise(np.subtract(ray.at_time(time), center))
        return 0.5 * 255 * np.array([normal[0] + 1, normal[1] + 1, normal[2] + 1])
    else:
        t = 0.5 * (ray.unit_direction()[1] + 1)
        return (1 - t) * np.array([255, 255, 255]) + t * np.array([130, 200, 255])
