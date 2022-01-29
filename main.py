import numpy as np
from render import Renderer
import surface

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 300
VIEWPORT_WIDTH = 2.0
VIEWPORT_HEIGHT = 1.5
FOCAL_LENGTH = 1.0
ORIGIN = np.array([0., 0., 0.])

def main():
    renderer = Renderer(IMAGE_WIDTH, IMAGE_HEIGHT, VIEWPORT_WIDTH,
                        VIEWPORT_HEIGHT, FOCAL_LENGTH, ORIGIN)

    world = surface.World()
    world.add(surface.Sphere(np.array([0., 0., -1.]), 0.5))

    renderer.render(world)
    renderer.save('test1.png')

if __name__ == '__main__':
    main()
