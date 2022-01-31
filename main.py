import numpy as np
import time
from render import Camera, Renderer
import surface
from material import Lambertian, Metal

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 300
VIEWPORT_WIDTH = 2.0
VIEWPORT_HEIGHT = 1.5
FOCAL_LENGTH = 1.0
ORIGIN = np.array([0., 0., 0.])

def main():
    camera = Camera(IMAGE_WIDTH, IMAGE_HEIGHT, VIEWPORT_WIDTH,
                        VIEWPORT_HEIGHT, FOCAL_LENGTH, ORIGIN)
    renderer = Renderer(camera, 10, 50)

    material = Lambertian(np.array([180, 60, 60]))
    material2 = Lambertian(np.array([40, 125, 40]))
    metal1 = Metal(np.array([200, 200, 200]))
    metal2 = Metal(np.array([200, 160, 40]))

    world = surface.World()
    world.add(surface.Sphere(material, np.array([0., 0., -1.]), 0.5))
    world.add(surface.Sphere(metal1, np.array([-1.0, 0., -1.0]), 0.5))
    world.add(surface.Sphere(metal2, np.array([1.0, 0., -1.0]), 0.5))
    world.add(surface.Sphere(material2, np.array([0., -100.5, -1]), 100))

    initial_time = time.time()
    renderer.render(world)
    print(f'Rendered in {time.time() - initial_time} seconds')
    renderer.save('test1.png')

if __name__ == '__main__':
    main()
