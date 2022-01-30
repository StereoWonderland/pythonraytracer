import numpy as np
from render import Camera, Renderer
import surface

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 300
VIEWPORT_WIDTH = 2.0
VIEWPORT_HEIGHT = 1.5
FOCAL_LENGTH = 1.0
ORIGIN = np.array([0., 0., 0.])

def main():
    camera = Camera(IMAGE_WIDTH, IMAGE_HEIGHT, VIEWPORT_WIDTH,
                        VIEWPORT_HEIGHT, FOCAL_LENGTH, ORIGIN)
    renderer = Renderer(camera)

    world = surface.World()
    world.add(surface.Sphere(np.array([0., 0., -1.]), 0.5))
    world.add(surface.Sphere(np.array([0., -100.5, -1]), 100))

    renderer.render(world)
    renderer.save('test1.png')

if __name__ == '__main__':
    main()
